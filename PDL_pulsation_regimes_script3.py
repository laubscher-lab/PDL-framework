# PDL_pulsation_regimes_script3.py
# ============================================================
# Verification script -- The frustrated regime: does the pulsation
# classification survive C4, and can C4 select the bipartition?
# PDL Framework -- preliminary to a possible document D68
#
# CONTEXT (scripts 1 and 2, all PASSED):
#   - C2-admissible relational states are bipartitions of entities;
#   - switching by a fixed subset S preserves C2 and is involutive;
#   - universal simultaneous inversion (S = V) is the trivial
#     element: a fixed point, excluded by C1;
#   - exhaustive over 234256 pulsation laws (p in {None,1..6}) on
#     n = 4: exactly 28 are C1-compliant, in exactly two families
#     (uniform period 2 with binary phase: 14; degenerate {1,None}:
#     14), zero laws of a third type;
#   - compliant laws = 2(2^n - 2); DISTINCT relational dynamics
#     = 2^(n-1) - 1 = |Coh(K_n)| - 1, matching the D60 orbit
#     decomposition (phase splits 1|3 and 3|1 -> O_4; 2|2 -> O_3).
#
#   ALL OF THIS ASSUMED EXACT BALANCE (eta = 0). The real PDL
#   universe is frustrated: C4 minimises a non-zero residual
#   leakage. If the classification collapses under frustration,
#   scripts 1-2 describe a toy model, not PDL.
#
# CLAIM UNDER TEST (hand-derived, NOT established):
#   (T1) A triangle has 0 or 2 edges in any cut delta(S), never 1
#        or 3. Hence switching multiplies each triangle product by
#        (-1)^0 or (-1)^2 = +1. The SET of violated triangles is
#        pointwise invariant under every switching, not merely its
#        cardinality.
#   (T2) Consequently the entire classification of scripts 1-2 is
#        independent of frustration: it used only the cut structure.
#   (T3) Consequently C4 has NO SELECTIVE POWER over the pulsation:
#        eta is identical for all 2^(n-1) - 1 candidate bipartitions.
#        The pulsation bipartition is UNDETERMINED by C1-C4.
#        [If confirmed, this is a NEGATIVE RESULT to be documented
#         as such, locating precisely where a further axiom is
#         needed.]
#
# GENUINELY OPEN (the only part whose outcome is unknown):
#   Under a cut S, every triangle is either CROSSING (its vertices
#   are split by S; exactly 2 of its edges lie in delta(S)) or
#   INTERNAL (all three vertices on one side; 0 edges in the cut).
#   The split of the VIOLATED triangles between these two classes
#   depends on S and is NOT switching-invariant. It is built
#   entirely from C4, hence admissible as a C5 candidate under the
#   programme's anchoring requirement.
#
#   PART 5 asks: does any extremal principle on this split select a
#   bipartition uniquely, up to the automorphism group of the
#   SIGNED graph? If yes -> serious C5 candidate. If the selection
#   is massively degenerate -> clean negative result, the fifth in
#   the C5 search.
#
# All arithmetic is exact integer arithmetic. No floating point:
# frustration is reported as a COUNT of violated triangles, never
# as a ratio, so that no rounding can enter.
#
# Standard library only: itertools.
#
# PDL verrouillage protocol: execute independently in Google Colab
# and return the full output BEFORE any LaTeX drafting.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from itertools import combinations

print("=" * 68)
print("PDL_pulsation_regimes_script3.py")
print("The frustrated regime: does C4 select the pulsation bipartition?")
print("=" * 68)
print()


# ============================================================
# Machinery (repeated in full; no dependency on scripts 1-2)
# ============================================================

def edges_complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def triangles_complete(n):
    return list(combinations(range(n), 3))


def edge_id_map(edges):
    idx = {e: k for k, e in enumerate(edges)}

    def eid(a, b):
        return idx[(a, b)] if a < b else idx[(b, a)]

    return eid


def violated_set(s, edges, tris):
    """Frozenset of triangles whose sign product is -1."""
    eid = edge_id_map(edges)
    return frozenset(T for T in tris
                     if s[eid(T[0], T[1])] * s[eid(T[0], T[2])]
                     * s[eid(T[1], T[2])] == -1)


def switch(S, s, edges):
    return tuple(-v if ((i in S) != (j in S)) else v
                 for v, (i, j) in zip(s, edges))


def subsets(n):
    return [frozenset(c) for k in range(n + 1)
            for c in combinations(range(n), k)]


def proper_subsets(n):
    return [S for S in subsets(n) if 0 < len(S) < n]


def vertex_induced(x, edges):
    return tuple(x[i] * x[j] for (i, j) in edges)


# ============================================================
# PART 1 -- (T1) the violated-triangle SET is switching-invariant
# ============================================================
print("PART 1 -- (T1) Switching invariance of the violated-triangle set")
print("-" * 68)

for n in range(3, 6):
    edges, tris = edges_complete(n), triangles_complete(n)
    m = len(edges)
    subs = subsets(n)
    ok_set, ok_count, checks = True, True, 0
    cut_parity_ok = True

    # structural check: every triangle has 0 or 2 edges in every cut
    for S in subs:
        for T in tris:
            k = sum(1 for (a, b) in combinations(T, 2)
                    if (a in S) != (b in S))
            if k not in (0, 2):
                cut_parity_ok = False

    for s in itertools.product([1, -1], repeat=m):
        V0 = violated_set(s, edges, tris)
        for S in subs:
            V1 = violated_set(switch(S, s, edges), edges, tris)
            checks += 1
            if V1 != V0:
                ok_set = False
            if len(V1) != len(V0):
                ok_count = False

    print(f"  n = {n}: configs = {2 ** m:6d}, subsets = {len(subs):3d}, "
          f"checks = {checks:8d}")
    print(f"         every triangle has 0 or 2 edges in every cut : "
          f"{cut_parity_ok}")
    print(f"         violated-triangle SET invariant              : {ok_set}")
    print(f"         violated-triangle COUNT invariant            : {ok_count}")
print()
print("  If the SET (not merely the count) is invariant, then C4 is blind")
print("  to the choice of pulsation bipartition. This is (T3).")
print()


# ============================================================
# PART 2 -- (T2) the classification of script 2 under frustration
# ============================================================
print("PART 2 -- (T2) Re-running the pulsation-law classification on a")
print("         FRUSTRATED reference configuration")
print("-" * 68)


def flips_by(t, p, phi):
    if p is None:
        return 0
    return sum(1 for u in range(1, t + 1) if u % p == phi % p)


def parity_set(t, law):
    return frozenset(i for i, (p, phi) in enumerate(law)
                     if flips_by(t, p, phi) % 2 == 1)


def sequence(law, s0, edges, horizon):
    return [switch(parity_set(t, law), s0, edges) for t in range(horizon)]


def exact_period(seq):
    L = len(seq)
    for T in range(1, L // 2 + 1):
        if all(seq[t] == seq[t + T] for t in range(L - T)):
            return T
    return None


n = 4
edges, tris = edges_complete(n), triangles_complete(n)
CHOICES = [(None, 0)] + [(p, phi) for p in range(1, 4) for phi in range(p)]

# reference configurations at several frustration levels
refs = {}
for s in itertools.product([1, -1], repeat=len(edges)):
    v = len(violated_set(s, edges, tris))
    refs.setdefault(v, s)

print(f"  Frustration levels available on K_4 (out of {len(tris)} triangles):"
      f" {sorted(refs)}")
print()
print(f"  {'v(s0)':>6s} {'laws':>8s} {'C1-compliant':>13s} "
      f"{'uniform p=2':>12s} {'{1,None}':>9s} {'other':>6s} "
      f"{'distinct dyn':>13s}")

for v in sorted(refs):
    s0 = refs[v]
    good, unif, degen, dyn = 0, 0, 0, set()
    for law in itertools.product(CHOICES, repeat=n):
        seq = sequence(law, s0, edges, 60)
        if exact_period(seq) == 2 and len(set(seq)) > 1:
            good += 1
            dyn.add(tuple(seq[:2]))
            if all(p == 2 for (p, _) in law):
                unif += 1
            elif all(p in (1, None) for (p, _) in law):
                degen += 1
    other = good - unif - degen
    print(f"  {v:6d} {len(CHOICES) ** n:8d} {good:13d} {unif:12d} "
          f"{degen:9d} {other:6d} {len(dyn):13d}")

print()
print("  Script 2 (balanced, v = 0) gave: 28 compliant, 14 uniform p=2,")
print("  14 degenerate, 0 other, 7 distinct dynamics = 2^(n-1) - 1.")
print("  If every row above matches, the classification is INDEPENDENT")
print("  of frustration and scripts 1-2 are not a toy model.")
print()


# ============================================================
# PART 3 -- (T3) C4 has no selective power: explicit demonstration
# ============================================================
print("PART 3 -- (T3) Does C4 distinguish the candidate bipartitions?")
print("-" * 68)

for n in (4, 5):
    edges, tris = edges_complete(n), triangles_complete(n)
    props = proper_subsets(n)
    worst = 0
    for s in itertools.product([1, -1], repeat=len(edges)):
        vals = {len(violated_set(switch(S, s, edges), edges, tris))
                for S in props}
        worst = max(worst, len(vals))
    print(f"  n = {n}: over all {2 ** len(edges)} configurations, the number of")
    print(f"         DISTINCT frustration counts across the "
          f"{len(props)} candidate")
    print(f"         bipartitions is at most: {worst}")
    print(f"         C4 selective (would need > 1): {worst > 1}")
print()


# ============================================================
# PART 4 -- Switching classes and the C4 ground states
# ============================================================
print("PART 4 -- Switching classes and the C4-minimal (ground) classes")
print("-" * 68)

CLASSES = {}
for n in (4, 5):
    edges, tris = edges_complete(n), triangles_complete(n)
    subs = subsets(n)
    seen, classes = set(), []
    for s in itertools.product([1, -1], repeat=len(edges)):
        if s in seen:
            continue
        orbit = {switch(S, s, edges) for S in subs}
        seen |= orbit
        classes.append((min(orbit), len(orbit),
                        len(violated_set(s, edges, tris))))
    CLASSES[n] = (edges, tris, classes)
    sizes = sorted({c[1] for c in classes})
    spectrum = {}
    for _, _, v in classes:
        spectrum[v] = spectrum.get(v, 0) + 1
    print(f"  n = {n}: {len(classes)} switching classes, "
          f"orbit sizes {sizes} (expected [{2 ** (n - 1)}])")
    print(f"         frustration spectrum (violated triangles -> "
          f"number of classes):")
    for v in sorted(spectrum):
        print(f"           v = {v:2d} : {spectrum[v]:4d} classes")
    nz = [v for v in spectrum if v > 0]
    print(f"         minimal NON-ZERO frustration: v = {min(nz)}")
print()


# ============================================================
# PART 5 -- THE OPEN QUESTION: can the crossing/internal split
#           of the frustration select a bipartition?
# ============================================================
print("PART 5 -- Crossing vs internal frustration: a C5 candidate?")
print("-" * 68)
print("  For a cut S, a triangle is CROSSING if its vertices are split by")
print("  S (exactly 2 of its edges lie in delta(S)), else INTERNAL.")
print("  v_cross(S) = violated triangles that are crossing.")
print("  This depends on S and is NOT switching-invariant.")
print()


def crossing(T, S):
    return len({v in S for v in T}) == 2


def signed_automorphisms(s, n, edges):
    """Permutations of vertices mapping the switching class to itself."""
    eid = edge_id_map(edges)
    subs = subsets(n)
    orbit = {switch(S, s, edges) for S in subs}
    auts = []
    for perm in itertools.permutations(range(n)):
        t = tuple(s[eid(perm[i], perm[j])] for (i, j) in edges)
        if t in orbit:
            auts.append(perm)
    return auts


for n in (4, 5):
    edges, tris, classes = CLASSES[n]
    props = proper_subsets(n)
    print(f"  --- n = {n} ---")
    print(f"  {'v(class)':>9s} {'min v_cross':>12s} {'argmin count':>13s} "
          f"{'|Aut|':>6s} {'orbits of argmin':>17s} {'unique?':>8s}")
    for rep, _, v in sorted(classes, key=lambda c: c[2]):
        if v == 0:
            continue
        Vset = violated_set(rep, edges, tris)
        vc = {S: sum(1 for T in Vset if crossing(T, S)) for S in props}
        mn = min(vc.values())
        arg = [S for S in props if vc[S] == mn]
        auts = signed_automorphisms(rep, n, edges)
        # orbits of the argmin set under the signed automorphism group,
        # working modulo complementation (S and V\S give the same cut)
        canon = lambda S: min(frozenset(S),
                              frozenset(range(n)) - frozenset(S),
                              key=lambda Z: (len(Z), sorted(Z)))
        argc = {canon(S) for S in arg}
        orbits = set()
        for S in argc:
            orb = frozenset(canon(frozenset(p[i] for i in S)) for p in auts)
            orbits.add(orb)
        print(f"  {v:9d} {mn:12d} {len(argc):13d} {len(auts):6d} "
              f"{len(orbits):17d} {str(len(orbits) == 1):>8s}")
    print()

print("  READING THE TABLE:")
print("    'orbits of argmin' = 1  ->  the minimising bipartition is unique")
print("       up to the automorphism group of the SIGNED graph. A genuine")
print("       selection principle, and a serious C5 candidate.")
print("    'orbits of argmin' > 1  ->  the principle leaves an irreducible")
print("       choice. Clean negative result; the fifth in the C5 search.")
print("  The same must then be checked for the MAXIMISING principle and")
print("  for the balanced split |v_cross - v_int| -> min, in script 4.")
print()

print("=" * 68)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 68)
print("  Part 1: whether frustration is pointwise switching-invariant (T1).")
print("  Part 2: whether the pulsation classification survives C4 (T2).")
print("  Part 3: whether C4 can select a bipartition at all (T3).")
print("  Part 4: the frustration spectrum of the switching classes.")
print("  Part 5: whether crossing/internal frustration selects one.")
print()
print("  Parts 1-3 are expected to CONFIRM and to yield a negative result.")
print("  Part 5 is the only genuinely open question. Its outcome is not")
print("  anticipated here and must not be read into the design.")
print("=" * 68)
