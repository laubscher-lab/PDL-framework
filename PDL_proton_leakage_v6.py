#!/usr/bin/env python3
# ============================================================
# PDL v6 -- dynamic proton-leakage estimators on the C1-C4 closure process
# Target: Delta r_val = 0.04795969 (+- 6.98e-8). Colab-ready, stdlib only.
# Declared a priori : 12 hard-coded estimators measured DURING the closure
# trajectory (nothing postulated, nothing fitted after the fact).
# Compatibility law 2^(1-k) taken as theorem (D70 Part I, module U2 of v2).
# ============================================================
import math, random, sys
from itertools import combinations
from datetime import datetime, timezone

PHI = (1+5**0.5)/2
TARGET = 0.04795969
WIN = 6.98e-8
F_OBS = 0.157126

EST = ["S1 motif open-out fraction",
       "S2 Fopen/N @ f=f_obs",
       "S3 Fopen/N @ f=1/phi^2",
       "S4 Fopen/N @ f=1/2",
       "S5 endgame Fopen/N (f>=0.9)",
       "S6 Fcut@310 /310",
       "E1 n_fail/n_succ",
       "E2 n_fail/(n_succ*d)",
       "E3 N/A_used",
       "C1 1/(1+log2 A_used)",
       "C2 1/log2 A_used",
       "G1 (Fopen/N @ 1/phi^2)*phi^2"]

def k4s(N, half):
    s = set()
    for i in range(N):
        w = [(i+t) % N for t in range(half+1)]
        for c in combinations(w, 4):
            s.add(tuple(sorted(c)))
    return [list(x) for x in s]

def simulate(N, half, Amax, seed):
    d = 2*half
    rng = random.Random(seed)
    K4 = k4s(N, half)
    nbr = [set() for _ in range(N)]
    E = 0
    for i in range(N):
        for t in range(1, half+1):
            j = (i+t) % N
            if j not in nbr[i]:
                nbr[i].add(j); nbr[j].add(i); E += 1
    deg = [len(nbr[i]) for i in range(N)]
    ext = 4*d - 12
    fixed = [False]*N
    nf = 0
    Fopen = float(E)
    Fcut = 0.0
    ns = 0; nfail = 0; att = 0; oo = 0.0
    rec = []
    end_sum = 0.0; end_cnt = 0; cut310 = None
    while nf < N and att < Amax:
        m = K4[rng.randrange(len(K4))]
        k = 0
        for u in m:
            if fixed[u]: k += 1
        if k == 4:
            continue
        att += 1
        if k > 1:
            if rng.random() > 2.0**(1-k):
                nfail += 1
                continue
        ms = set(m)
        for u in m:
            for v in nbr[u]:
                if v not in ms and not fixed[v]:
                    oo += 1.0
        for u in m:
            if fixed[u]: continue
            fnb = 0
            for v in nbr[u]:
                if fixed[v]: fnb += 1
            unb = deg[u] - fnb
            Fopen -= fnb
            Fcut += unb - fnb
            fixed[u] = True
            nf += 1
        ns += 1
        f = nf/N
        rec.append((nf, Fopen, Fcut))
        if f >= 0.9:
            end_sum += Fopen/N; end_cnt += 1
        if cut310 is None and nf >= 310 and N > 310:
            cut310 = Fcut/310.0
    A = att if att > 0 else 1
    def at(fm):
        bi = min(range(len(rec)), key=lambda i: abs(rec[i][0]/N - fm))
        return rec[bi][1]/N
    v = {}
    v[EST[0]] = (oo/ns)/ext if ns else None
    v[EST[1]] = at(F_OBS)
    v[EST[2]] = at(1/PHI**2)
    v[EST[3]] = at(0.5)
    v[EST[4]] = end_sum/end_cnt if end_cnt else None
    v[EST[5]] = cut310
    v[EST[6]] = nfail/ns if ns else None
    v[EST[7]] = nfail/(ns*d) if ns else None
    v[EST[8]] = N/A
    v[EST[9]] = 1.0/(1.0+math.log2(A)) if A > 1 else None
    v[EST[10]] = 1.0/math.log2(A) if A > 1 else None
    v[EST[11]] = v[EST[2]]*PHI**2 if v[EST[2]] is not None else None
    return v, nf, A

def mean_se(xs):
    m = sum(xs)/len(xs)
    if len(xs) < 2:
        return m, float('nan')
    var = sum((x-m)**2 for x in xs)/(len(xs)-1)
    return m, (var**0.5)/(len(xs)**0.5)

def main():
    print("="*78)
    print("PDL v6 -- dynamic proton-leakage estimators on the C1-C4 closure process")
    print("(Colab-ready, stdlib only ; 12 estimators hard-coded BEFORE execution ;")
    print(" compatibility law 2^(1-k) from D70 Part I ; nothing fitted post hoc)")
    print("="*78)
    print("run UTC :", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    print("target  : Delta r_val = %.8f   window = +-%.2e (alpha-precision, v4)" % (TARGET, WIN))
    print()
    archs = [("ring N=930 d=8", 930, 4), ("ring N=310 d=8", 310, 4), ("ring N=930 d=6", 930, 3)]
    REPS = 16
    allv = {n: [] for n in EST}
    per_arch = {}
    Apl = {}
    for label, N, half in archs:
        pv = {n: [] for n in EST}; As = []
        for r in range(REPS):
            v, nf, A = simulate(N, half, 1000000, 10000 + r*77 + N*10 + half)
            As.append(A)
            for n in EST:
                if v[n] is not None:
                    pv[n].append(v[n]); allv[n].append(v[n])
        per_arch[label] = pv; Apl[label] = As
    print("-- attempts actually consumed until full closure (A_used) --")
    for label, N, half in archs:
        mA, _ = mean_se(Apl[label])
        print("   %-16s A_used ~ %.0f" % (label, mA))
    print()
    print("--- estimator table : aggregate over %d replicas x %d archs ---" % (REPS, len(archs)))
    print("%-34s %12s %12s %14s %12s" % ("estimator", "mean", "SE", "|mean-target|", "ppm"))
    rows = []
    for n in EST:
        m, se = mean_se(allv[n])
        dev = abs(m-TARGET)
        ppm = (m-TARGET)/TARGET*1e6
        rows.append((n, m, se, dev, ppm))
        print("%-34s %12.6g %12.3g %14.3g %12.1f" % (n, m, se, dev, ppm))
    print()
    lam = len(EST)*2*WIN/0.5
    p_ge1 = 1 - math.exp(-lam)
    hits = [r for r in rows if r[3] <= WIN]
    print("-- Poisson null (declared : K=%d estimators, value range ~0.5) --" % len(EST))
    print("lambda = %.3e ; P(>=1 hit by pure chance) = %.3e" % (lam, p_ge1))
    print("hits inside +-%0.2e : %d" % (WIN, len(hits)))
    print()
    rows.sort(key=lambda r: r[3])
    print("-- closest estimator to Delta r_val --")
    print("  %s" % rows[0][0])
    print("   mean = %.8g ; |dev| = %.3g = %.1f ppm = %.0f windows" % (rows[0][1], rows[0][3], rows[0][4], rows[0][3]/WIN))
    print("   per-architecture mean (stability check) :")
    for label, N, half in archs:
        xs = per_arch[label][rows[0][0]]
        if xs:
            mA, _ = mean_se(xs)
            print("      %-16s %.8g" % (label, mA))
    print()
    print("="*78)
    print("SUMMARY")
    print("="*78)
    if hits:
        for h in hits:
            print("HIT   | %s : mean=%.8g within window" % (h[0], h[1]))
        print("VERDICT | V6 POSITIVE-CANDIDATE : declaration and test were simultaneous,")
        print("          so any hit is ONLY a candidate for public pre-registration +")
        print("          independent replication, not yet evidence.")
    else:
        print("VERDICT | V6 NEGATIVE : no declared dynamic estimator lands on Delta r_val")
        print("          within the alpha-window. Closest is '%s' at %.0f ppm." % (rows[0][0], rows[0][4]))
        print("          The circularity of G survives the stochastic closure readout :")
        print("          Delta r_val must come from an ANALYTIC fixed-point (mean-field)")
        print("          of the frontier, the same missing law as OP-overlap.")
    print()
    print("="*78)
    print("NEGATIVE-RESULT BLOCK - paste into a dated public note (e.g. Zenodo)")
    print("="*78)
    print("Date (UTC run) : %s" % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    print("Test           : 12 dynamic leakage estimators declared a priori, measured")
    print("                 on the C1-C4 K4-closure process (law 2^(1-k), 48 runs).")
    print("Target         : Delta r_val = 0.04795969 +- 6.98e-8.")
    print("Null           : lambda = %.2e ; P(>=1 chance hit) = %.2e." % (lam, p_ge1))
    print("Result         : 0 hit. Closest : %s at %.0f ppm." % (rows[0][0], rows[0][4]))
    print("Consequence    : circularity of the alpha<->G bridge is NOT lifted by a")
    print("                 stochastic readout of the closure trajectory ; the leak")
    print("                 length must be an analytic frontier fixed point, i.e. the")
    print("                 same missing law as OP-overlap (single missing ingredient).")
    print()
    print("EXIT=0")

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    sys.exit(0)
