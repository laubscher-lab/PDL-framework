# PDL_pulsation_regimes_script4.py
# ============================================================
# Verification script -- FALSIFICATION of the crossing-frustration
# selection principle
# PDL Framework -- preliminary to a possible document D68
#
# CONTEXT (scripts 1-3, all PASSED):
#   - the C1-compliant pulsation laws are exactly 2(2^n - 2), in two
#     families (uniform period 2 with binary phase; degenerate
#     {1,None}), giving 2^(n-1) - 1 distinct relational dynamics,
#     in bijection with the non-trivial cuts;
#   - (T1) the SET of violated triangles is pointwise invariant
#     under every switching (verified to n = 5, 32768 checks);
#   - (T2) the classification is independent of frustration
#     (v = 0, 2, 4 on K_4 all give 28 / 14 / 14 / 0 / 7);
#   - (T3) NEGATIVE RESULT: C4 is blind to the pulsation
#     bipartition. Distinct frustration counts across candidate
#     bipartitions: exactly 1, for every configuration, n = 4, 5.
#   - the frustration spectrum is symmetric under v -> C(n,3) - v,
#     i.e. under the global edge inversion s -> -s of D60; C4 breaks
#     this symmetry by selecting the low-frustration end.
#
# SCRIPT 3 PART 5 REPORTED: minimising v_cross(S) selects a unique
#   bipartition up to the automorphism group of the SIGNED graph,
#   for 71 classes out of 71, at both n = 4 and n = 5, with no
#   exception.
#
# THIS SCRIPT TREATS THAT AS SUSPECT, NOT AS A RESULT.
#   A selection principle that never fails anywhere is more often a
#   tautology than a discovery. Three specific concerns:
#     (a) every class tested had a LARGE automorphism group
#         (|Aut| in {4,8,10,12,24,120}); "one orbit" is trivially
#         easy when the group is large;
#     (b) the argmin count frequently equalled v itself, which
#         smells of a combinatorial coincidence;
#     (c) only ONE principle was tested. No contrast, no control.
#
# THE THREE TESTS, in decreasing order of severity:
#
#   CONTROL 0 (null): minimise |S|. This uses NO information about
#     the frustration whatsoever. If it ALSO yields one orbit
#     almost everywhere, then "one orbit" merely measures whether
#     Aut is transitive on vertices, and the whole test of script 3
#     was empty. THIS IS THE DECISIVE CONTROL.
#
#   CONTROL 1 (contrast): MAXIMISE v_cross. If maximising succeeds
#     as often as minimising, uniqueness reflects symmetry, not
#     selection, and neither principle carries information.
#
#   TEST 2 (variant): minimise |v_cross - v_int|, the balanced
#     split. Reported for completeness; NOT to be adopted merely
#     because it happens to work, per the programme's rule against
#     variants of a failed family.
#
#   REGIME TEST 3: all of the above restricted to classes with
#     SMALL |Aut| (<= 2), which exist only from n = 6 upward. This
#     is the only regime in which the test has any bite at all.
#
#   STRUCTURE TEST 4: does minimising v_cross systematically select
#     cuts of size 1 (i.e. O_4-type, the "dynamic orbit" of D60)?
#     Hand calculation on K_4 says yes; verified here for n up to 7,
#     where cut sizes 1, 2, 3 all exist and the answer is not
#     forced.
#
# METHOD NOTE -- canonical representatives:
#   Every switching class of a signed complete graph has exactly one
#   representative with all edges at vertex 0 positive: set x_0 = +1
#   and x_i = s(0,i). Hence classes are enumerated DIRECTLY, without
#   generating orbits: 2^C(n-1,2) of them. n=4:8, n=5:64, n=6:1024,
#   n=7:32768.
#
# All arithmetic is exact integer arithmetic. Frustration is a COUNT
# of violated triangles, never a ratio.
#
# Standard library only: itertools, random.
#
# PDL verrouillage protocol: execute independently in Google Colab
# and return the full output BEFORE any LaTeX drafting.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
import random
from itertools import combinations

print("=" * 70)
print("PDL_pulsation_regimes_script4.py")
print("FALSIFICATION of the crossing-frustration selection principle")
print("=" * 70)
print()


# ============================================================
# Machinery (self-contained)
# ============================================================

def setup(n):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    tris = list(combinations(range(n), 3))
    idx = {e: k for k, e in enumerate(edges)}
    return edges, tris, idx


def eid(idx, a, b):
    return idx[(a, b)] if a < b else idx[(b, a)]


def violated(s, tris, idx):
    return frozenset(T for T in tris
                     if s[eid(idx, T[0], T[1])] * s[eid(idx, T[0], T[2])]
                     * s[eid(idx, T[1], T[2])] == -1)


def canon(s, n, edges, idx):
    """Unique class representative: all edges at vertex 0 positive."""
    x = [1] * n
    for i in range(1, n):
        x[i] = s[eid(idx, 0, i)]
    return tuple(v * x[i] * x[j] for v, (i, j) in zip(s, edges))


def class_representatives(n, edges, idx):
    """Directly enumerate one representative per switching class."""
    free = [k for k, (i, j) in enumerate(edges) if i != 0]
    reps = []
    for bits in itertools.product([1, -1], repeat=len(free)):
        s = [1] * len(edges)
        for k, b in zip(free, bits):
            s[k] = b
        reps.append(tuple(s))
    return reps


def automorphisms(s, n, edges, idx):
    """Vertex permutations preserving the switching class."""
    auts = []
    for perm in itertools.permutations(range(n)):
        t = tuple(s[eid(idx, perm[i], perm[j])] for (i, j) in edges)
        if canon(t, n, edges, idx) == s:
            auts.append(perm)
    return auts


def proper_cuts(n):
    """Cuts modulo complementation: one representative per cut."""
    out = []
    for k in range(1, n // 2 + 1):
        for c in combinations(range(n), k):
            S = frozenset(c)
            if 2 * k == n and 0 not in S:
                continue          # avoid listing S and its complement
            out.append(S)
    return out


def canon_cut(S, n):
    C = frozenset(range(n)) - S
    return min(S, C, key=lambda Z: (len(Z), sorted(Z)))


def crossing(T, S):
    return len({v in S for v in T}) == 2


def n_orbits(argset, auts, n):
    """Number of Aut-orbits among a set of cuts (taken modulo complement)."""
    remaining = {canon_cut(S, n) for S in argset}
    count = 0
    while remaining:
        S = next(iter(remaining))
        orb = {canon_cut(frozenset(p[i] for i in S), n) for p in auts}
        remaining -= orb
        count += 1
    return count


# ============================================================
# The four principles
# ============================================================

def principle_min_cross(Vset, cuts, n):
    sc = {S: sum(1 for T in Vset if crossing(T, S)) for S in cuts}
    m = min(sc.values())
    return [S for S in cuts if sc[S] == m], m


def principle_max_cross(Vset, cuts, n):
    sc = {S: sum(1 for T in Vset if crossing(T, S)) for S in cuts}
    m = max(sc.values())
    return [S for S in cuts if sc[S] == m], m


def principle_balanced(Vset, cuts, n):
    sc = {}
    for S in cuts:
        c = sum(1 for T in Vset if crossing(T, S))
        sc[S] = abs(c - (len(Vset) - c))
    m = min(sc.values())
    return [S for S in cuts if sc[S] == m], m


def principle_null(Vset, cuts, n):
    """CONTROL: minimise |S|. Uses no frustration information at all."""
    m = min(len(S) for S in cuts)
    return [S for S in cuts if len(S) == m], m


PRINCIPLES = [("NULL  min|S|   ", principle_null),
              ("min  v_cross   ", principle_min_cross),
              ("MAX  v_cross   ", principle_max_cross),
              ("bal |vc - vi|  ", principle_balanced)]


# ============================================================
# PART 1 -- The four principles compared, n = 4, 5, 6
# ============================================================
print("PART 1 -- Four principles compared. 'unique' = exactly one Aut-orbit")
print("-" * 70)
print("  A principle only carries information if it does BETTER than the")
print("  NULL control. If NULL also scores ~100%, the test is empty.")
print()

STORE = {}
for n in (4, 5, 6):
    edges, tris, idx = setup(n)
    reps = class_representatives(n, edges, idx)
    cuts = proper_cuts(n)
    rows = []
    for s in reps:
        Vset = violated(s, tris, idx)
        if len(Vset) == 0:
            continue                       # balanced class: no frustration
        auts = automorphisms(s, n, edges, idx)
        rec = {"v": len(Vset), "aut": len(auts)}
        for name, fn in PRINCIPLES:
            arg, val = fn(Vset, cuts, n)
            rec[name] = (n_orbits(arg, auts, n), len(arg), val,
                         sorted({len(canon_cut(S, n)) for S in arg}))
        rows.append(rec)
    STORE[n] = (rows, cuts)

    print(f"  --- n = {n}: {len(rows)} frustrated switching classes "
          f"(of {len(reps)} total) ---")
    print(f"      {'principle':16s} {'unique':>8s} {'/ total':>8s} "
          f"{'% unique':>9s}")
    for name, _ in PRINCIPLES:
        u = sum(1 for r in rows if r[name][0] == 1)
        print(f"      {name:16s} {u:8d} {len(rows):8d} "
              f"{100.0 * u / len(rows):8.1f}%")
    print()


# ============================================================
# PART 2 -- Automorphism spectrum: do we reach small groups?
# ============================================================
print("PART 2 -- Automorphism spectrum of the frustrated classes")
print("-" * 70)
for n in (4, 5, 6):
    rows, _ = STORE[n]
    spec = {}
    for r in rows:
        spec[r["aut"]] = spec.get(r["aut"], 0) + 1
    print(f"  n = {n}: |Aut| -> count : "
          + ", ".join(f"{k}->{spec[k]}" for k in sorted(spec)))
    small = sum(v for k, v in spec.items() if k <= 2)
    print(f"         classes with |Aut| <= 2 : {small} "
          f"({100.0 * small / len(rows):.1f}%)")
print()


# ============================================================
# PART 3 -- THE REGIME THAT MATTERS: small automorphism group
# ============================================================
print("PART 3 -- Restricted to classes with |Aut| <= 2 (the only regime")
print("          in which 'one orbit' is a non-trivial statement)")
print("-" * 70)
for n in (4, 5, 6):
    rows, _ = STORE[n]
    sub = [r for r in rows if r["aut"] <= 2]
    if not sub:
        print(f"  n = {n}: no class with |Aut| <= 2. Test has no bite here.")
        continue
    print(f"  --- n = {n}: {len(sub)} classes with |Aut| <= 2 ---")
    print(f"      {'principle':16s} {'unique':>8s} {'/ total':>8s} "
          f"{'% unique':>9s} {'mean |argmin|':>14s}")
    for name, _ in PRINCIPLES:
        u = sum(1 for r in sub if r[name][0] == 1)
        mean = sum(r[name][1] for r in sub) / len(sub)
        print(f"      {name:16s} {u:8d} {len(sub):8d} "
              f"{100.0 * u / len(sub):8.1f}% {mean:14.2f}")
    print()


# ============================================================
# PART 4 -- Does min v_cross select cuts of size 1 (O_4-type)?
# ============================================================
print("PART 4 -- Cut-size profile of the selected bipartitions")
print("-" * 70)
print("  Hand calculation on K_4 predicts min v_cross always selects")
print("  cuts of size 1 (O_4-type, the 'dynamic orbit' of D60). For")
print("  n >= 6 cut sizes 1, 2, 3 all exist and nothing forces this.")
print()
for n in (4, 5, 6):
    rows, _ = STORE[n]
    for name in ("min  v_cross   ", "MAX  v_cross   "):
        prof = {}
        for r in rows:
            key = tuple(r[name][3])
            prof[key] = prof.get(key, 0) + 1
        print(f"  n = {n}, {name.strip()}: selected cut sizes -> count")
        for k in sorted(prof, key=str):
            print(f"      sizes {str(list(k)):12s} : {prof[k]:5d} classes")
    print()


# ============================================================
# PART 5 -- n = 7 by random sampling
# ============================================================
print("PART 5 -- n = 7, random sample of switching classes")
print("-" * 70)
n = 7
edges, tris, idx = setup(n)
cuts = proper_cuts(n)
free = [k for k, (i, j) in enumerate(edges) if i != 0]
random.seed(20260810)
NSAMP = 150

rows7 = []
while len(rows7) < NSAMP:
    s = [1] * len(edges)
    for k in free:
        s[k] = random.choice([1, -1])
    s = tuple(s)
    Vset = violated(s, tris, idx)
    if len(Vset) == 0:
        continue
    auts = automorphisms(s, n, edges, idx)
    rec = {"v": len(Vset), "aut": len(auts)}
    for name, fn in PRINCIPLES:
        arg, val = fn(Vset, cuts, n)
        rec[name] = (n_orbits(arg, auts, n), len(arg), val,
                     sorted({len(canon_cut(S, n)) for S in arg}))
    rows7.append(rec)

spec = {}
for r in rows7:
    spec[r["aut"]] = spec.get(r["aut"], 0) + 1
print(f"  sampled classes: {len(rows7)}")
print(f"  |Aut| -> count : "
      + ", ".join(f"{k}->{spec[k]}" for k in sorted(spec)))
print()
print(f"  {'principle':16s} {'unique':>8s} {'/ total':>8s} {'% unique':>9s} "
      f"{'mean |argmin|':>14s}")
for name, _ in PRINCIPLES:
    u = sum(1 for r in rows7 if r[name][0] == 1)
    mean = sum(r[name][1] for r in rows7) / len(rows7)
    print(f"  {name:16s} {u:8d} {len(rows7):8d} {100.0 * u / len(rows7):8.1f}% "
          f"{mean:14.2f}")
print()
sub = [r for r in rows7 if r["aut"] <= 2]
if sub:
    print(f"  Restricted to |Aut| <= 2 ({len(sub)} classes):")
    for name, _ in PRINCIPLES:
        u = sum(1 for r in sub if r[name][0] == 1)
        print(f"    {name:16s} {u:5d} / {len(sub):5d}  "
              f"({100.0 * u / len(sub):.1f}%)")
print()
print("  Cut sizes selected by min v_cross at n = 7:")
prof = {}
for r in rows7:
    key = tuple(r["min  v_cross   "][3])
    prof[key] = prof.get(key, 0) + 1
for k in sorted(prof, key=str):
    print(f"    sizes {str(list(k)):12s} : {prof[k]:5d} classes")
print()

print("=" * 70)
print("HOW TO READ THIS SCRIPT")
print("=" * 70)
print("  If NULL scores as high as 'min v_cross', script 3 Part 5 measured")
print("  the symmetry of K_n and nothing else: the C5 candidate is DEAD,")
print("  and this is the fifth clean negative result of the C5 search.")
print()
print("  If MAX scores as high as 'min', uniqueness carries no direction:")
print("  the principle has no content even if it is not vacuous.")
print()
print("  The candidate survives only if, on the |Aut| <= 2 classes,")
print("  'min v_cross' is unique substantially more often than BOTH")
print("  controls. Anything less is not a selection principle.")
print("=" * 70)
