"""
PDL_D61_script1.py  (version 3 -- final)
=========================================
Verrouillage script for D61 (OP-D59-2):
  The Minimal Covariant Derivative as a C4 Survival Theorem.

Prerequisite clarification (established here before D61 is drafted):
  The 8 coherent configurations of K4 are those satisfying C2 (product +1
  on every triangle). The pulsation partner s^(2) = -s^(1) has all triangle
  products = -1: it is NOT coherent in the C2 sense. The pulsation is the
  alternation between a C2-coherent state and a C2-violated state; this
  is the source of dynamics (C1). This is consistent with D46 and the corpus.

Main claim verified:
  The discrete transports U : E(K4) -> {+1,-1} that map every C2-coherent
  configuration to a C2-coherent configuration (under pointwise multiplication)
  are EXACTLY the 8 elements of Coh(K4) itself. These form a group isomorphic
  to Z2^3 under pointwise multiplication.

  All 56 remaining transports introduce nu > 0 on at least one coherent
  configuration and are eliminated by C4.

Documented negative result:
  The initial conjecture (admissible group = V4, order 4) is INCORRECT.
  The correct group is Coh(K4) isomorphic to Z2^3, order 8.
  This is a structurally informative negative result: the C4-admissible
  transports are richer than V4. The relationship between Coh(K4) and V4
  (as a permutation subgroup) must be analysed in D61.

Method:
  Exact integer arithmetic on {+1,-1}^6.
  No floating-point. Python standard library only (itertools).
  2048 checks (64 transports x 8 coherent configs x 4 triangles).

Author: PDL programme (Laubscher, 2026)
Protocol: verrouillage -- to be executed in Colab before LaTeX drafting.
"""

import itertools

# ---------------------------------------------------------------------------
# 0.  K4 structure
# ---------------------------------------------------------------------------
EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
TRIANGLES = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]

def tri_edges(tri):
    i, j, k = tri
    return (EDGE_INDEX[(i,j)], EDGE_INDEX[(i,k)], EDGE_INDEX[(j,k)])

TRI_IDX = [tri_edges(t) for t in TRIANGLES]

ALL64 = list(itertools.product([+1,-1], repeat=6))

def is_coherent(s):
    return all(s[a]*s[b]*s[c] == +1 for (a,b,c) in TRI_IDX)

def cost(U, s):
    """Number of violated triangles in U*s."""
    Us = tuple(U[i]*s[i] for i in range(6))
    return sum(1 for (a,b,c) in TRI_IDX if Us[a]*Us[b]*Us[c] != +1)

def mult(U, V):
    return tuple(U[i]*V[i] for i in range(6))

# ---------------------------------------------------------------------------
# 1.  Coherent configurations
# ---------------------------------------------------------------------------
COHERENT = [s for s in ALL64 if is_coherent(s)]

r0 = len(COHERENT) == 8
print(f"[CHECK-0]  |Coh(K4)| = {len(COHERENT)}  --> {'PASSED' if r0 else 'FAILED'}")

# Pulsation pairs: {s, -s}. Note: -s is NOT coherent (product=-1 on each triangle).
# The pulsation alternates between a coherent and an incoherent state (C1 dynamics).
pulsation_partners = []
for s in COHERENT:
    neg_s = tuple(-x for x in s)
    is_neg_coherent = is_coherent(neg_s)
    pulsation_partners.append((s, neg_s, is_neg_coherent))

all_partners_incoherent = all(not ok for (_,_,ok) in pulsation_partners)
r1 = all_partners_incoherent
print(f"[CHECK-1]  Pulsation partners -s are all INCOHERENT (C2-violated)"
      f"  --> {'PASSED' if r1 else 'FAILED'}")
print(f"           (This confirms: K4 pulsation alternates coherent <-> incoherent)")

# ---------------------------------------------------------------------------
# 2.  C4-admissible transports
# ---------------------------------------------------------------------------
admissible = [U for U in ALL64 if all(cost(U,s)==0 for s in COHERENT)]
adm_set = set(admissible)

r2 = (len(admissible) == 8)
print(f"\n[CHECK-2]  C4-admissible transports = {len(admissible)}"
      f"  --> {'PASSED' if r2 else 'FAILED'}")

coh_set = set(COHERENT)
r3 = (adm_set == coh_set)
print(f"[CHECK-3]  Admissible transports = Coh(K4)"
      f"  --> {'PASSED' if r3 else 'FAILED'}")

# ---------------------------------------------------------------------------
# 3.  Group structure
# ---------------------------------------------------------------------------
identity = (1,)*6
r4 = all(mult(U,V) in adm_set for U in admissible for V in admissible)
r5 = identity in adm_set
r6 = all(mult(U,U)==identity for U in admissible)
r7 = all(mult(U,V)==mult(V,U) for U in admissible for V in admissible)
r8 = (len(admissible)==8 and r6 and r7)  # Z2^3: order 8, abelian, exponent 2

print(f"[CHECK-4]  Closure under pointwise multiplication"
      f"  --> {'PASSED' if r4 else 'FAILED'}")
print(f"[CHECK-5]  Identity (1,...,1) present"
      f"  --> {'PASSED' if r5 else 'FAILED'}")
print(f"[CHECK-6]  Every element self-inverse (order divides 2)"
      f"  --> {'PASSED' if r6 else 'FAILED'}")
print(f"[CHECK-7]  Group is abelian"
      f"  --> {'PASSED' if r7 else 'FAILED'}")
print(f"[CHECK-8]  Structure consistent with Z2^3 (order 8, abelian, exponent 2)"
      f"  --> {'PASSED' if r8 else 'FAILED'}")

# ---------------------------------------------------------------------------
# 4.  Non-admissible transports have positive cost
# ---------------------------------------------------------------------------
non_adm = [U for U in ALL64 if U not in adm_set]
r9 = all(any(cost(U,s)>0 for s in COHERENT) for U in non_adm)
print(f"[CHECK-9]  All {len(non_adm)} non-admissible transports have nu>0"
      f" on >= 1 coherent config  --> {'PASSED' if r9 else 'FAILED'}")

# ---------------------------------------------------------------------------
# 5.  Cost distribution for non-admissible transports
# ---------------------------------------------------------------------------
cost_dist = {}
for U in non_adm:
    max_cost = max(cost(U,s) for s in COHERENT)
    cost_dist[max_cost] = cost_dist.get(max_cost, 0) + 1
print(f"\n  Cost distribution (max over 8 configs) for {len(non_adm)} non-admissible:")
for k in sorted(cost_dist):
    print(f"    max nu = {k}/4 : {cost_dist[k]} transports")

# ---------------------------------------------------------------------------
# 6.  The 8 admissible transports
# ---------------------------------------------------------------------------
print(f"\n--- The 8 C4-admissible transports (= Coh(K4)) ---")
print(f"  Edges: e01, e02, e03, e12, e13, e23")
for U in sorted(adm_set):
    tag = " [identity]" if U == identity else ""
    print(f"  {U}{tag}")

# ---------------------------------------------------------------------------
# 7.  Negative result: global flip is NOT admissible
# ---------------------------------------------------------------------------
global_flip = (-1,-1,-1,-1,-1,-1)
r_neg = (global_flip not in adm_set)
print(f"\n[NEG-1]   Global flip (-1,...,-1) NOT in admissible set"
      f"  --> {'VERIFIED' if r_neg else 'FAILED'}")
print(f"           Cost on first coherent config: {cost(global_flip, COHERENT[0])}/4")
print(f"           (Global flip maps coherent -> incoherent: eliminated by C4)")

# ---------------------------------------------------------------------------
# 8.  Documented negative result on initial conjecture
# ---------------------------------------------------------------------------
print(f"\n[NEG-2]   Initial conjecture refuted:")
print(f"           Conjectured: admissible group = V4 (order 4)")
print(f"           Actual:      admissible group = Coh(K4) (order 8 = Z2^3)")
print(f"           Status: NEGATIVE RESULT DOCUMENTED -- scientifically informative")
print(f"           Consequence for D61: must analyse the relationship between")
print(f"           Coh(K4) as a multiplication group and V4 as a permutation group.")

# ---------------------------------------------------------------------------
# 9.  Summary
# ---------------------------------------------------------------------------
checks = [r0,r1,r2,r3,r4,r5,r6,r7,r8,r9]
all_passed = all(checks)

total = len(ALL64)*len(COHERENT)*len(TRIANGLES)
print(f"\n{'='*65}")
print(f"PDL_D61_script1.py  (v3 final)  --  SUMMARY")
print(f"{'='*65}")
labels = [
    "CHECK-0  |Coh(K4)| = 8",
    "CHECK-1  Pulsation partners incoherent",
    "CHECK-2  8 C4-admissible transports",
    "CHECK-3  Admissible = Coh(K4)",
    "CHECK-4  Closure",
    "CHECK-5  Identity present",
    "CHECK-6  Self-inverse",
    "CHECK-7  Abelian",
    "CHECK-8  Z2^3 structure",
    "CHECK-9  Non-admissible have nu>0",
]
for label, result in zip(labels, checks):
    print(f"  {label:<45} {'PASSED' if result else 'FAILED'}")
print(f"{'='*65}")
print(f"  NEG-1  Global flip not admissible            VERIFIED")
print(f"  NEG-2  Initial conjecture (V4) refuted        DOCUMENTED")
print(f"{'='*65}")
print(f"  Total checks: {total}  (exact integer arithmetic, no float)")
print(f"  OVERALL: {'ALL CHECKS PASSED' if all_passed else 'ONE OR MORE CHECKS FAILED'}")
print(f"{'='*65}")
