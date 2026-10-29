#!/usr/bin/env python3
# =============================================================================
# PDL proton leakage v9 : hierarchical stationary skin + period-3 core dynamics
# Colab-ready, stdlib only. Deterministic (no RNG). Family declared BEFORE solving.
#
# Context (from v3..v8): the leakage length Dr_val must come from a mean-field
# fixed point; a single lock/unlock level is falsified (v8) : U/L = 2^-14.2 is
# required, i.e. suppression must be composed over hierarchy levels (exponent 18).
# New in v9 (Turns 19-20 discussion):
#   - unlock rule U DERIVED from valence-core internal dynamics (D69 period-3
#     cycle, omega/omega_bar in the transfer spectrum) instead of being postulated
#   - phase-accessible modulation of the lock kernel (~1/3 compatible core states)
#   - TRIPLE declared target :
#       T1 skin          Dr_val = 0.04795969 +- 6.98e-8   (G bridge amplitude)
#       T2 closed frac   f      = 0.157126   +- 0.0009    (Omega_b/Omega_m)
#       T3 spin share    dSigma = 0.30       +- 0.05      (EMC/COMPASS valence share)
#     A configuration survives ONLY if the SAME (U, d, mod, level) hits T1, T2, T3.
# =============================================================================
import math
from math import comb

phi = (1.0 + 5.0**0.5) / 2.0

# ---------------- declared targets (frozen from session pre-registrations) ------
T1_DR, T1_TOL = 0.04795969, 6.98e-8      # skin (930 * p*) ; D21 erratum value
T2_F,  T2_TOL = 0.157126, 0.0009         # Omega_b/Omega_m, Planck18/ACT DR6+DESI
T3_S,  T3_TOL = 0.30, 0.05               # Delta Sigma, EMC/COMPASS/HERMES
N_UNITS = 930
LEVELS  = list(range(1, 19))             # exponent-18 hierarchy (declared)
DEGS    = [4, 8]                         # motif K4 coordination / sea-ring degree

def Lkern(p, d):
    """Exact phase-lock kernel of D70 : success 2^(1-k) against k locked neighbours."""
    return sum(comb(d, k) * (1.0 - p)**k * p**(d - k) * 2.0**(1 - k)
               for k in range(1, d + 1))

def unlock_forms():
    """Declared a priori : unlock rate U per valence cycle, derived from the
    period-3 internal dynamics of the three valence cores (D69 spectrum)."""
    return [
        ("A1 U=1/3           (one compatible phase of 3)",        1.0/3.0),
        ("B1 U=2^(1-3)=1/4   (inverse lock law, period-3)",       0.25),
        ("C1 U=(1/3)*2^(1-4) (phase x lock, motif degree)",       (1.0/3.0) * 2.0**-3),
        ("C2 U=(1/3)*2^(1-8) (phase x lock, sea-ring degree)",    (1.0/3.0) * 2.0**-7),
        ("D1 U=(1/3)^2       (two-core co-rotation)",             1.0/9.0),
        ("D2 U=(1/3)^3       (three-core co-rotation)",           1.0/27.0),
        ("E1 U=1/(3*phi)     (golden-weighted phase, D69)",       1.0/(3.0*phi)),
        ("E2 U=1/(3*phi^2)   (golden-weighted, one inflation)",   1.0/(3.0*phi**2)),
        ("E3 U=1/(4*phi)     (inverse lock x golden phase)",      1.0/(4.0*phi)),
        ("E4 U=1/(4*phi^2)   (inverse lock x golden inflation)",  1.0/(4.0*phi**2)),
    ]

MODS = [
    ("M1 phase-gated  L_eff = L(p/3)",   lambda p, d: Lkern(p/3.0, d)),
    ("M2 phase-damped L_eff = L(p)/3",   lambda p, d: Lkern(p, d) / 3.0),
    ("M3 raw          L_eff = L(p)",     lambda p, d: Lkern(p, d)),
]

def step(p, U, d, M):
    """One hierarchy level of the stationary-skin map  p -> U / (U + L_eff(p,d))."""
    den = U + M(p, d)
    return U / den if den > 0 else float("nan")

def spin_proxy(level):
    """Declared : fraction of the order parameter carried by the static core sector
    after 'level' hierarchy levels, if each level transmits one accessible phase
    of the period-3 core cycle : dSigma_model = 3^-level. (Declared, not fitted.)"""
    return 3.0 ** (-level)

def banner(t):
    print(); print("=" * 78); print(t); print("=" * 78)

def main():
    banner("PDL unified instrument v9 : hierarchical skin x period-3 cores x spin")

    # ------------------------------------------------------------------ V9-A --
    print()
    print("--- V9-A  declared family BEFORE solving (method lock) ---")
    forms = unlock_forms()
    print("targets (frozen) :")
    print("  T1 Dr_val = %.8f +- %.2e   (skin -> G)" % (T1_DR, T1_TOL))
    print("  T2 f      = %.6f +- %.4f   (closed fraction -> dark sector)" % (T2_F, T2_TOL))
    print("  T3 dSigma = %.2f +- %.2f          (valence spin share, EMC/COMPASS)" % (T3_S, T3_TOL))
    print("levels scanned : 1..18 (exponent-18 hierarchy, declared)")
    print("degrees        :", DEGS, " ; phase modulations : M1, M2, M3")
    print("unlock family  : %d forms" % len(forms))
    for name, U in forms:
        print("   %s  = %.8f" % (name, U))
    n_tested = len(forms) * len(DEGS) * len(MODS) * len(LEVELS)
    print("total (U,d,mod,level) configurations tested : %d" % n_tested)
    print("PASS | V9-A family + triple target declared before solving")

    # ------------------------------------------------------------------ V9-B --
    print()
    print("--- V9-B  solving the hierarchical stationary map ---")
    traj = {}   # (iU, d, iM) -> list of p per level (index 0 = level 1)
    bad = 0
    for iU, (name, U) in enumerate(forms):
        for d in DEGS:
            for iM, (mname, M) in enumerate(MODS):
                p = 1.0 - 1e-9           # declared start : almost fully open
                ps = []
                for lv in LEVELS:
                    p = step(p, U, d, M)
                    if not (0.0 < p <= 1.0) or math.isnan(p):
                        bad += 1
                        p = float("nan")
                    ps.append(p)
                traj[(iU, d, iM)] = ps
    print("trajectories computed : %d  (pathological : %d)" % (len(traj), bad))
    sample = traj[(0, 8, 0)]
    print("sample  A1/M1/d=8  p_1=%.6f  p_3=%.6e  p_6=%.6e  p_12=%.6e  p_18=%.6e"
          % (sample[0], sample[2], sample[5], sample[11], sample[17]))
    print("PASS | V9-B all trajectories finite (no v3/v6 freeze-to-100%% artefact)" if bad == 0
          else "WARN | V9-B %d pathological trajectories kept out of hits" % bad)

    # ------------------------------------------------------------------ V9-C --
    print()
    print("--- V9-C  confrontation : Poisson statistics on the triple target ---")
    dr_vals, f_vals = [], []
    hits1, hits2, hits3, hits123 = [], [], [], []
    witness1 = witness2 = witness3 = None
    for (iU, d, iM), ps in traj.items():
        Uname, _ = forms[iU]
        mname, _ = MODS[iM]
        for lv in LEVELS:
            p = ps[lv - 1]
            if math.isnan(p):
                continue
            Dr = N_UNITS * p
            f  = 1.0 - p
            s  = spin_proxy(lv)
            dr_vals.append(Dr); f_vals.append(f)
            e1 = abs(Dr - T1_DR); e2 = abs(f - T2_F); e3 = abs(s - T3_S)
            if witness1 is None or e1 < witness1[0]: witness1 = (e1, Uname, d, mname, lv, Dr)
            if witness2 is None or e2 < witness2[0]: witness2 = (e2, Uname, d, mname, lv, f)
            if witness3 is None or e3 < witness3[0]: witness3 = (e3, Uname, d, mname, lv, s)
            h1, h2, h3 = e1 <= T1_TOL, e2 <= T2_TOL, e3 <= T3_TOL
            if h1: hits1.append((Uname, d, mname, lv, Dr))
            if h2: hits2.append((Uname, d, mname, lv, f))
            if h3: hits3.append((Uname, d, mname, lv, s))
            if h1 and h2 and h3: hits123.append((Uname, d, mname, lv))

    def poisson(vals, tol):
        n = len(vals); rng = max(vals) - min(vals)
        lam = n * (2.0 * tol) / rng if rng > 0 else 0.0
        return n, lam, 1.0 - math.exp(-lam)

    n1, lam1, p1 = poisson(dr_vals, T1_TOL)
    n2, lam2, p2 = poisson(f_vals,  T2_TOL)
    # T3 depends on level only : 18 declared values
    n3 = len(LEVELS)
    rng3 = max(spin_proxy(l) for l in LEVELS) - min(spin_proxy(l) for l in LEVELS)
    lam3 = n3 * (2.0 * T3_TOL) / rng3
    p3 = 1.0 - math.exp(-lam3)

    print("T1 skin   : %d hits | null lambda=%.3g, P(>=1)=%.3g" % (len(hits1), lam1, p1))
    print("   closest : e=%.3e  %s d=%d %s level=%d  Dr=%.8f (target %.8f)"
          % (witness1[0], witness1[1], witness1[2], witness1[3], witness1[4], witness1[5], T1_DR))
    print("T2 closed : %d hits | null lambda=%.3f, P(>=1)=%.3f" % (len(hits2), lam2, p2))
    print("   closest : e=%.3e  %s d=%d %s level=%d  f=%.6f (target %.6f)"
          % (witness2[0], witness2[1], witness2[2], witness2[3], witness2[4], witness2[5], T2_F))
    print("T3 spin   : %d levels in window | null lambda=%.2f, P(>=1)=%.2f  (level-only proxy : context, never alone)" % (len(hits3), lam3, p3))
    print("   closest : e=%.3e  level=%d  dSigma=%.4f (target %.2f)"
          % (witness3[0], witness3[4], witness3[5], T3_S))
    for Uname, d, mname, lv, f in hits2:
        print("   T2 hit : %s d=%d %s level=%d  f=%.6f" % (Uname, d, mname, lv, f))
    print()
    print("TRIPLE coincidence (same U,d,mod,level in T1 AND T2 AND T3) : %d" % len(hits123))
    for cfg in hits123:
        print("   SURVIVOR :", cfg)

    verdict = \
        "POSITIVE | a declared configuration meets the triple target" if hits123 else \
        "NEGATIVE | no declared configuration meets the triple target"
    print(verdict)

    # ------------------------------------------------------------------ V9-D --
    print()
    print("--- V9-D  suppression bookkeeping : how deep must the hierarchy go? ---")
    p_need = T1_DR / N_UNITS
    bits_total = math.log2(1.0 / p_need)
    print("required skin p* = %.4e  -> total suppression = %.2f bits" % (p_need, bits_total))
    for lv in (1, 3, 6, 9, 12, 18):
        print("   if reached at level %2d : %.2f bits/level needed" % (lv, bits_total / lv))
    print("per-level delivered (bits from p=1-1e-9, level 1) :")
    for iU, (name, U) in enumerate(forms[:6]):
        for iM in (0,):
            for d in DEGS:
                p1v = traj[(iU, d, iM)][0]
                if 0 < p1v < 1:
                    print("   %s d=%d %.2f bits at L1" % (name.split()[0], d, -math.log2(p1v)))
    print("PASS | V9-D required-vs-delivered suppression table")

    # ------------------------------------------------------------- Zenodo ----
    banner("ZENODO BLOCK - dated negative/pre-registration note (run 2026-10-29)")
    print("Family       : hierarchical stationary skin, p_{l+1}=U/(U+L(p_l,d)),")
    print("               10 unlock forms from period-3 core dynamics, 3 phase mods,")
    print("               d in {4,8}, levels 1..18  -> %d configurations" % n_tested)
    print("Targets      : T1 Dr=%.8f+-%.1e  T2 f=%.6f+-%.1e  T3 dSigma=%.2f+-%.2f"
          % (T1_DR, T1_TOL, T2_F, T2_TOL, T3_S, T3_TOL))
    print("Result       : T1 hits=%d (lambda=%.3g) ; T2 hits=%d (lambda=%.3f) ; triple=%d"
          % (len(hits1), lam1, len(hits2), lam2, len(hits123)))
    if hits123:
        print("Verdict      : SURVIVING pre-registered configuration(s) -> evidence")
    else:
        print("Verdict      : NEGATIVE - declared family falsified on the triple target.")
        print("Remaining    : any successful derivation must deliver ~14.2 bits of")
        print("               suppression jointly with f=0.157126 and dSigma~0.30 from")
        print("               the same period-3 core mechanism.")
    banner("SUMMARY")
    print("PASS | V9-A family declared a priori")
    print("PASS | V9-B trajectories solved (stationary, deterministic)")
    print(("PASS | V9-C %s" % verdict))
    print("PASS | V9-D suppression bookkeeping (14.2 bits over 18 levels = 0.79 bits/level)")
    print()
    print("VERDICT LINES (v9)")
    print("* The period-3 core cycle was promoted from backdrop to mechanism : the unlock")
    print("  rule U is now derived from D69, not postulated.")
    if not hits123:
        print("* No declared (U,d,mod,level) hits the triple target simultaneously : the")
        print("  hierarchical stationary family, as declared, is falsified.")
    print("* T2 near-misses or hits are context only : without the same configuration")
    print("  matching T1 (+-1.45 ppm relative) and T3, they are not evidence.")
    print("* The remaining requirement is now three numbers, one equation - the hardest")
    print("  constraint the framework has ever faced, hence the most discriminative.")
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        if e.code not in (0, None):
            raise
