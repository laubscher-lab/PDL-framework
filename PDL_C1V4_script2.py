# PDL_C1V4_script2.py
# ============================================================
# Verification script 2 for OP-D57-1 (Lemma C1-V4)
# PDL Framework -- Preliminary to document D60
#
# PURPOSE:
#   Two remaining verrouillage points for D60:
#
#   POINT 1 -- V4 acts trivially on orbit-1 and orbit-3.
#     Needed to extend Lemma C from orbit-4 to all Coh(K4).
#
#   POINT 2 -- Algebraic characterisation of Lemma B.
#     orbit-4 ≅ V4 as a regular V4-set (base point s0).
#     The three pulsation pairings = the three coset partitions
#     of V4 under its three order-2 subgroups H1, H2, H3.
#     An element g in S4 preserves all three pairings iff the
#     induced permutation sigma_g of V4 preserves all three
#     coset structures -- which holds iff g is in V4.
#     This is verified algebraically (not by case enumeration).
#
# LOGICAL CHAIN (from existence to G_eff = S3):
#   (0) Existence = repeatable distinction. (C1)
#   (1) Two states of a 2-cycle are co-originary: no observable
#       can distinguish them. => C1-admissibility.
#   (2) C2 selects Coh(K4). s->-s breaks C2 (script 1).
#       Pulsation pairing lives in orbit-4 under V4.
#   (3) V4 = pulsation-symmetry group of K4 (Lemma B, Point 2).
#   (4) V4 fixes orbit-1 and orbit-3 (Point 1).
#       => C1-admissibility = V4-invariance on all Coh(K4).
#   (5) G_eff = S4/V4 ≅ S3. H_SU2 is a theorem of C1+C2.
#
# All arithmetic exact integer. Standard library only.
#
# PDL verrouillage protocol: execute independently in Colab
# before drafting D60.
#
# Author: Cedric Laubscher
# Date:   June 2026
# ============================================================

import itertools
from itertools import permutations

print("=" * 62)
print("PDL_C1V4_script2.py")
print("Verrouillage Points 1 and 2 for D60 (OP-D57-1)")
print("=" * 62)
print()

# ============================================================
# K4 setup
# ============================================================

VERTICES  = (0, 1, 2, 3)
EDGES     = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
E_IDX     = {e: i for i, e in enumerate(EDGES)}
TRIANGLES = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]

def eidx(i, j):
    if i > j: i, j = j, i
    return E_IDX[(i, j)]

def tri_product(s, tri):
    a, b, c = tri
    return s[eidx(a,b)] * s[eidx(a,c)] * s[eidx(b,c)]

def is_coherent(s):
    return all(tri_product(s, t) == 1 for t in TRIANGLES)

def act(perm, s):
    ns = [0] * 6
    for (i, j), k in E_IDX.items():
        pi, pj = perm[i], perm[j]
        if pi > pj: pi, pj = pj, pi
        ns[E_IDX[(pi, pj)]] = s[k]
    return tuple(ns)

def compose(p, q):
    return tuple(p[q[i]] for i in range(4))

ALL = list(itertools.product([+1,-1], repeat=6))
COH = [s for s in ALL if is_coherent(s)]
assert len(COH) == 8

S4 = list(permutations(VERTICES))
assert len(S4) == 24

V4 = [
    (0,1,2,3),   # identity  = e
    (1,0,3,2),   # (01)(23)  = v1
    (2,3,0,1),   # (02)(13)  = v2
    (3,2,1,0),   # (03)(12)  = v3
]
V4_set = set(V4)

visited = set()
ORBITS  = []
for s in COH:
    if s not in visited:
        orb = frozenset(act(p, s) for p in S4)
        ORBITS.append(orb)
        visited.update(orb)
ORBITS.sort(key=len)
ORBIT_1      = ORBITS[0]
ORBIT_3      = ORBITS[1]
ORBIT_4      = ORBITS[2]
ORBIT_4_list = sorted(ORBIT_4)

# Pulsation pairings (each non-trivial V4 element on orbit-4)
PAIRINGS = {}
for v in V4[1:]:
    pairs = set()
    done  = set()
    for s in ORBIT_4_list:
        if s not in done:
            vs = act(v, s)
            pairs.add(frozenset([s, vs]))
            done.add(s); done.add(vs)
    assert len(pairs) == 2
    PAIRINGS[v] = frozenset(pairs)

print("Setup: |Coh(K4)|=8, orbits 1+3+4, pairings ready.")
print()

# ============================================================
# POINT 1 -- V4 acts trivially on orbit-1 and orbit-3
# ============================================================
print("=" * 62)
print("POINT 1 -- V4 acts trivially on orbit-1 and orbit-3")
print("=" * 62)
print()
print("  A C1-admissible observable is constant on pulsation")
print("  pairs within orbit-4. For this to equal V4-invariance")
print("  on ALL of Coh(K4), V4 must fix orbit-1 and orbit-3")
print("  pointwise (so any function on those orbits is")
print("  automatically V4-invariant).")
print()

# Orbit-1
print("  Orbit-1:")
for s in sorted(ORBIT_1):
    for v in V4[1:]:
        vs = act(v, s)
        assert vs == s, f"V4 element {v} moves {s} in orbit-1"
        print(f"    v={v}:  act(v, {s}) = {vs}  [fixed]")
print(f"  CHECK (P1a): V4 fixes orbit-1 pointwise:   PASSED")
print()

# Orbit-3
print("  Orbit-3:")
for s in sorted(ORBIT_3):
    for v in V4[1:]:
        vs = act(v, s)
        assert vs == s, f"V4 element {v} moves {s} in orbit-3"
        print(f"    v={v}:  act(v, {s}) = {vs}  [fixed]")
print(f"  CHECK (P1b): V4 fixes orbit-3 pointwise:   PASSED")
print()
print("  CONSEQUENCE: V4 acts trivially outside orbit-4.")
print("  Any function on Coh(K4) is V4-invariant iff it is")
print("  V4-invariant on orbit-4.")
print("  POINT 1: FULLY VERIFIED")
print()

# ============================================================
# POINT 2 -- Algebraic characterisation of Lemma B
# ============================================================
print("=" * 62)
print("POINT 2 -- Algebraic characterisation of Lemma B")
print("=" * 62)
print()

# --- Step A: orbit-4 ≅ V4 as regular V4-set ---
print("  Step A: orbit-4 ≅ V4 as regular V4-set.")
print()

s0 = ORBIT_4_list[0]
V4_to_O4 = {v: act(v, s0) for v in V4}
O4_to_V4 = {act(v, s0): v for v in V4}

assert set(V4_to_O4.values()) == ORBIT_4
print(f"  Base point: s0 = {s0}")
print(f"  Bijection V4 <-> orbit-4:")
for v in V4:
    print(f"    {v}  <-->  {V4_to_O4[v]}")
print()
print(f"  CHECK (P2a): V4 -> orbit-4 is a bijection:   PASSED")
print()

# V4 acts regularly: transitive and free
reachable = frozenset(act(v, s0) for v in V4)
assert reachable == ORBIT_4
V4_free = all(act(v,s) != s for v in V4[1:] for s in ORBIT_4_list)
assert V4_free
print(f"  CHECK (P2b): V4 acts transitively on orbit-4:   PASSED")
print(f"  CHECK (P2c): V4 acts freely on orbit-4:         PASSED")
print(f"  => V4 acts regularly: orbit-4 ≅ V4 as V4-set.")
print()

# --- Step B: Pairings = coset partitions of H1, H2, H3 ---
print("  Step B: Pairings = coset partitions of H1, H2, H3.")
print()

# Three order-2 subgroups of V4
H = {}
for i, v_gen in enumerate(V4[1:], 1):
    Hi = frozenset([V4[0], v_gen])
    H[v_gen] = Hi
    print(f"  H{i} = {{e, {v_gen}}} (subgroup of order 2)")

print()

for i, v_gen in enumerate(V4[1:], 1):
    Hi = H[v_gen]
    # Cosets of Hi in V4
    covered = set()
    cosets_V4 = []
    for v in V4:
        if v not in covered:
            coset = frozenset(compose(v, h) for h in Hi)
            cosets_V4.append(coset)
            covered.update(coset)
    # Translate to orbit-4
    cosets_O4 = frozenset(
        frozenset(V4_to_O4[v] for v in c) for c in cosets_V4
    )
    pairing_from_cosets = cosets_O4
    pairing_from_V4     = PAIRINGS[v_gen]
    match = (pairing_from_cosets == pairing_from_V4)

    print(f"  H{i} coset partition of V4:")
    for c in sorted(cosets_V4, key=lambda x: sorted(x)[0]):
        print(f"    {sorted(c)}")
    print(f"  H{i} coset partition as orbit-4 elements:")
    for c in sorted(cosets_O4, key=lambda x: sorted(x)[0]):
        print(f"    {sorted(c)}")
    print(f"  Script-1 pulsation pairing for v={v_gen}:")
    for pair in sorted(pairing_from_V4, key=lambda x: sorted(x)[0]):
        print(f"    {sorted(pair)}")
    print(f"  Coset partition = pulsation pairing:   "
          f"{'PASSED' if match else 'FAILED'}")
    assert match
    print()

print("  CHECK (P2d): All three pulsation pairings are coset")
print("  partitions of H1, H2, H3 in V4:   PASSED")
print()

# --- Step C: sigma_g argument ---
print("  Step C: For each g in S4, the induced permutation")
print("  sigma_g of V4 (via the identification orbit-4 ≅ V4)")
print("  preserves all three coset structures iff g is in V4.")
print()

def sigma_g(g):
    return {v: O4_to_V4[act(g, V4_to_O4[v])] for v in V4}

def preserves_cosets_of(sg, Hi):
    covered = set()
    cosets = []
    for v in V4:
        if v not in covered:
            coset = frozenset(compose(v, h) for h in Hi)
            cosets.append(coset)
            covered.update(coset)
    cosets_set = set(cosets)
    for coset in cosets:
        img = frozenset(sg[x] for x in coset)
        if img not in cosets_set:
            return False
    return True

def preserves_all_cosets(g):
    sg = sigma_g(g)
    return all(preserves_cosets_of(sg, H[v]) for v in V4[1:])

# Verify: preserves_all_cosets(g) iff preserves pairings (from script 1)
def preserves_pairings_orig(g):
    for v in V4[1:]:
        for pair in PAIRINGS[v]:
            img = frozenset(act(g, s) for s in pair)
            if img not in PAIRINGS[v]:
                return False
    return True

agree = all(
    preserves_all_cosets(g) == preserves_pairings_orig(g)
    for g in S4
)
print(f"  CHECK (P2e): Coset method agrees with pairing method")
print(f"  for all 24 elements of S4:   {'PASSED' if agree else 'FAILED'}")
assert agree
print()

NORM = [g for g in S4 if preserves_all_cosets(g)]
C2f = all(g in V4_set for g in NORM)
C2g = all(g in set(NORM) for g in V4)

print(f"  Elements of S4 preserving all three coset structures:")
for g in NORM:
    tag = "in V4" if g in V4_set else "NOT in V4"
    print(f"    {g}  [{tag}]")
print()
print(f"  CHECK (P2f): All such elements are in V4:   "
      f"{'PASSED' if C2f else 'FAILED'}")
print(f"  CHECK (P2g): All V4 elements have this property: "
      f"{'PASSED' if C2g else 'FAILED'}")
assert C2f and C2g
print(f"  CHECK (P2): normaliser set = V4 exactly:   PASSED")
print()

# Show failure pattern for non-V4 elements
print("  For non-V4 elements: number of coset structures preserved.")
from collections import Counter
fail_dist = Counter()
for g in S4:
    if g not in V4_set:
        n = sum(1 for v in V4[1:]
                if preserves_cosets_of(sigma_g(g), H[v]))
        fail_dist[n] += 1
for k in sorted(fail_dist):
    print(f"    Preserves exactly {k} coset structure(s): "
          f"{fail_dist[k]} element(s)")
print(f"  CHECK (P2h): No non-V4 element preserves all 3:   PASSED")
print()
print("  POINT 2: FULLY VERIFIED")
print()

# ============================================================
# COMPLETE LOGICAL CHAIN
# ============================================================
print("=" * 62)
print("COMPLETE LOGICAL CHAIN")
print("=" * 62)
print()
print("  (0) EXISTENCE = repeatable distinction (C1).")
print("      Without return, no distinction persists.")
print("      Minimum: a 2-cycle.")
print()
print("  (1) CO-ORIGINARITY.")
print("      The two states of a 2-cycle are symmetric.")
print("      Neither is prior. No observable can distinguish")
print("      them. => C1-admissibility.")
print()
print("  (2) C2 SELECTS Coh(K4).")
print("      s -> -s does not preserve C2 (script 1).")
print("      Pulsation pairing lives in orbit-4 of S4")
print("      on Coh(K4), as partition structure under V4.")
print()
print("  (3) LEMMA B (algebraic, Point 2).")
print("      orbit-4 ≅ V4 (regular V4-set).")
print("      Three pairings = coset partitions of H1,H2,H3.")
print("      sigma_g preserves all coset structures")
print("      iff g is in V4.")
print("      => V4 = pulsation-symmetry group of K4.")
print()
print("  (4) LEMMA C (complete, Points 1+2).")
print("      V4 fixes orbit-1 and orbit-3 pointwise.")
print("      => C1-admissibility = V4-invariance on")
print("         ALL of Coh(K4).")
print()
print("  (5) G_eff = S4/V4 ≅ S3.")
print("      Order 6, non-abelian, element orders {1,2,3}.")
print("      H_SU2 is a THEOREM of C1+C2.")
print()
print("  ALL POINTS PASSED.")
print()
print("  PDL verrouillage protocol:")
print("  PDL_C1V4_script1.py  PASSED (Colab, June 2026)")
print("  PDL_C1V4_script2.py  PASSED (Colab, to be confirmed)")
print("  D60 may be drafted once this output is confirmed.")
