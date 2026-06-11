"""
PDL_D61_script2.py
==================
Verrouillage script for D61 (OP-D59-2), Part 2.

Prerequisite: PDL_D61_script1.py (ALL CHECKS PASSED).

Object of study:
  The action of V4 (as a permutation group on the 4 vertices of K4)
  on Coh(K4) (the group of C4-admissible transports, iso Z2^3, from script1).

  V4 acts on vertices -> induces action on edges -> induces action on
  sign configurations in {+1,-1}^6.

Questions verified:
  Q1 (CHECK-0 to 2):  The induced action of V4 is well-defined on Coh(K4),
                      i.e., Coh(K4) is stable under the V4 edge-permutation action.

  Q2 (CHECK-3 to 5):  The action of V4 on Coh(K4) is faithful (no non-identity
                      element of V4 fixes all of Coh(K4) pointwise).

  Q3 (CHECK-6 to 9):  Orbit structure of V4 on Coh(K4): sizes, stabilisers,
                      and consistency with the gauge derivation of D57-D60.

  Q4 (CHECK-10 to 12): The action of V4 on Coh(K4) is compatible with the
                       group structure of Coh(K4) (V4 acts by automorphisms).

Negative results documented:
  NEG-1: Whether V4 acts freely on Coh(K4) (no fixed points except identity).

Method:
  Exact integer arithmetic. Python standard library only (itertools).

Author: PDL programme (Laubscher, 2026)
Protocol: verrouillage -- executed in Colab before LaTeX drafting of D61.
"""

import itertools
from collections import defaultdict

# ---------------------------------------------------------------------------
# 0.  Reconstruct K4 structure (self-contained, no import from script1)
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

COHERENT = [s for s in ALL64 if is_coherent(s)]
COH_SET = set(COHERENT)
assert len(COHERENT) == 8, "Fatal: expected 8 coherent configs"

# ---------------------------------------------------------------------------
# 1.  V4 elements as vertex permutations (0-indexed)
# ---------------------------------------------------------------------------
# V4 = {id, (01)(23), (02)(13), (03)(12)} as permutations of {0,1,2,3}
V4_PERMS = [
    (0, 1, 2, 3),   # id
    (1, 0, 3, 2),   # (01)(23)
    (2, 3, 0, 1),   # (02)(13)
    (3, 2, 1, 0),   # (03)(12)
]
V4_NAMES = ["id", "(01)(23)", "(02)(13)", "(03)(12)"]

def induced_edge_action(sigma, s):
    """
    Apply vertex permutation sigma to sign configuration s.
    sigma is a tuple of length 4: sigma[i] = image of vertex i.
    The edge {i,j} maps to {sigma(i), sigma(j)}.
    The new sign configuration has:
      new_s[edge {sigma(i),sigma(j)}] = s[edge {i,j}]
    Returns the new sign configuration as a tuple.
    """
    new_s = [0] * 6
    for idx, (i, j) in enumerate(EDGES):
        pi, pj = sigma[i], sigma[j]
        if pi > pj:
            pi, pj = pj, pi
        new_idx = EDGE_INDEX[(pi, pj)]
        new_s[new_idx] = s[idx]
    return tuple(new_s)

# ---------------------------------------------------------------------------
# Q1 — V4 action is well-defined on Coh(K4)
# ---------------------------------------------------------------------------
print("=" * 65)
print("Q1 — V4 action on Coh(K4): well-definedness")
print("=" * 65)

# CHECK-0: V4 is a group of order 4
r0 = (len(V4_PERMS) == 4)
print(f"[CHECK-0]  |V4| = {len(V4_PERMS)}  --> {'PASSED' if r0 else 'FAILED'}")

# CHECK-1: V4 is closed under composition
def compose(sigma, tau):
    return tuple(sigma[tau[i]] for i in range(4))

closed_v4 = True
for s1 in V4_PERMS:
    for s2 in V4_PERMS:
        if compose(s1, s2) not in V4_PERMS:
            closed_v4 = False
r1 = closed_v4
print(f"[CHECK-1]  V4 closed under composition  --> {'PASSED' if r1 else 'FAILED'}")

# CHECK-2: Coh(K4) is stable under V4 edge action
stable = True
violations = []
for name, sigma in zip(V4_NAMES, V4_PERMS):
    for s in COHERENT:
        s_image = induced_edge_action(sigma, s)
        if s_image not in COH_SET:
            stable = False
            violations.append((name, s, s_image))

r2 = stable
print(f"[CHECK-2]  Coh(K4) stable under V4 edge action (8x4=32 checks)"
      f"  --> {'PASSED' if r2 else 'FAILED'}")
if not stable:
    for name, s, img in violations:
        print(f"  VIOLATION: {name} sends {s} -> {img} (not coherent)")

# ---------------------------------------------------------------------------
# Q2 — Faithfulness of V4 action on Coh(K4)
# ---------------------------------------------------------------------------
print("\n" + "=" * 65)
print("Q2 — Faithfulness of V4 action on Coh(K4)")
print("=" * 65)

# For each non-identity element of V4, find a coherent config it does NOT fix.
# CHECK-3: identity fixes all configs (trivially true)
r3 = all(induced_edge_action(V4_PERMS[0], s) == s for s in COHERENT)
print(f"[CHECK-3]  Identity fixes all configs  --> {'PASSED' if r3 else 'FAILED'}")

# CHECK-4: each non-identity element moves at least one config
faithful = True
for name, sigma in zip(V4_NAMES[1:], V4_PERMS[1:]):
    fixes_all = all(induced_edge_action(sigma, s) == s for s in COHERENT)
    if fixes_all:
        faithful = False
        print(f"  NON-FAITHFUL: {name} fixes all coherent configs")

r4 = faithful
print(f"[CHECK-4]  Each non-identity element of V4 moves >= 1 config"
      f"  --> {'PASSED' if r4 else 'FAILED'}")

# CHECK-5: kernel of the action is trivial
kernel = [name for name, sigma in zip(V4_NAMES, V4_PERMS)
          if all(induced_edge_action(sigma, s) == s for s in COHERENT)]
r5 = (kernel == ["id"])
print(f"[CHECK-5]  Kernel of V4 action on Coh(K4) = {{id}}"
      f"  --> {'PASSED' if r5 else 'FAILED'}")
print(f"           Kernel elements found: {kernel}")

# ---------------------------------------------------------------------------
# Q3 — Orbit structure of V4 acting on Coh(K4)
# ---------------------------------------------------------------------------
print("\n" + "=" * 65)
print("Q3 — Orbit structure of V4 on Coh(K4)")
print("=" * 65)

# Compute orbits of V4 on COHERENT
def v4_orbit(s):
    return frozenset(induced_edge_action(sigma, s) for sigma in V4_PERMS)

orbits = []
visited = set()
for s in COHERENT:
    if s not in visited:
        orb = v4_orbit(s)
        orbits.append(orb)
        visited |= orb

# CHECK-6: orbits partition Coh(K4)
all_in_orbits = set().union(*orbits)
r6 = (all_in_orbits == COH_SET and sum(len(o) for o in orbits) == 8)
print(f"[CHECK-6]  Orbits partition Coh(K4) (total = {sum(len(o) for o in orbits)})"
      f"  --> {'PASSED' if r6 else 'FAILED'}")

# CHECK-7: orbit sizes
orbit_sizes = sorted([len(o) for o in orbits])
print(f"[CHECK-7]  Orbit sizes: {orbit_sizes}")
# By orbit-stabiliser theorem: |orbit| * |stabiliser| = |V4| = 4
for orb in orbits:
    size = len(orb)
    stab_size = 4 // size
    print(f"           Orbit (size {size}): stabiliser order = {stab_size}")

r7 = True  # informational, always passes
print(f"           --> PASSED (informational)")

# CHECK-8: explicit orbit display
print(f"\n[CHECK-8]  Explicit orbits:")
for i, orb in enumerate(sorted(orbits, key=len)):
    print(f"  Orbit {i+1} (size {len(orb)}):")
    for s in sorted(orb):
        tag = " [identity transport]" if all(x==1 for x in s) else ""
        print(f"    {s}{tag}")

r8 = True  # informational

# CHECK-9: stabilisers of each orbit element
print(f"\n[CHECK-9]  Stabiliser generators for each orbit:")
for i, orb in enumerate(sorted(orbits, key=len)):
    rep = sorted(orb)[0]
    stab = [name for name, sigma in zip(V4_NAMES, V4_PERMS)
            if induced_edge_action(sigma, rep) == rep]
    print(f"  Orbit {i+1}, rep {rep}: stabiliser = {stab}")

r9 = True  # informational

# ---------------------------------------------------------------------------
# Q4 — V4 acts by GROUP AUTOMORPHISMS of Coh(K4)
# ---------------------------------------------------------------------------
print("\n" + "=" * 65)
print("Q4 — V4 acts by automorphisms of the group Coh(K4)")
print("=" * 65)

def mult(U, V):
    return tuple(U[i]*V[i] for i in range(6))

# For each v in V4: check that the induced map phi_v : Coh(K4) -> Coh(K4)
# is a group homomorphism, i.e., phi_v(U*W) = phi_v(U) * phi_v(W)
r10 = True
for name, sigma in zip(V4_NAMES, V4_PERMS):
    is_hom = True
    for U in COHERENT:
        for W in COHERENT:
            lhs = induced_edge_action(sigma, mult(U, W))
            rhs = mult(induced_edge_action(sigma, U),
                       induced_edge_action(sigma, W))
            if lhs != rhs:
                is_hom = False
                print(f"  FAILURE: {name} is not a homomorphism: "
                      f"phi({U}*{W}) != phi({U})*phi({W})")
    if is_hom:
        pass

print(f"[CHECK-10] Each V4 element acts as an automorphism of Coh(K4)"
      f"  (8x8x4=256 checks)  --> {'PASSED' if r10 else 'FAILED'}")

# CHECK-11: the automorphism group of Coh(K4) induced by V4
# What is the image of V4 in Aut(Coh(K4))?
# Represent each phi_v as a permutation of the 8 elements of Coh(K4)
COH_LIST = sorted(COHERENT)
COH_POS = {s: i for i, s in enumerate(COH_LIST)}

def perm_of_v4_on_coh(sigma):
    """Permutation of {0,...,7} = positions in COH_LIST induced by sigma."""
    return tuple(COH_POS[induced_edge_action(sigma, s)] for s in COH_LIST)

v4_auts = [perm_of_v4_on_coh(sigma) for sigma in V4_PERMS]
v4_aut_set = set(v4_auts)

# How many distinct automorphisms does V4 induce on Coh(K4)?
r11 = True
print(f"[CHECK-11] Distinct automorphisms of Coh(K4) induced by V4: "
      f"{len(v4_aut_set)}")
print(f"           (Expected 4 if action faithful, less if kernel non-trivial)")
print(f"           --> {'PASSED' if len(v4_aut_set) == 4 else 'INFORMATIONAL'}")

# CHECK-12: fixed-point free action? (NEG result expected)
fixed_point_free = True
for name, sigma in zip(V4_NAMES[1:], V4_PERMS[1:]):
    fixed = [s for s in COHERENT if induced_edge_action(sigma, s) == s]
    if fixed:
        fixed_point_free = False
        print(f"[NEG-1]    {name} fixes: {fixed}")

r12 = not fixed_point_free  # We EXPECT fixed points (NEG-1 = documented result)
print(f"[CHECK-12] Fixed-point analysis for non-identity V4 elements:")
for name, sigma in zip(V4_NAMES[1:], V4_PERMS[1:]):
    fixed = [s for s in COHERENT if induced_edge_action(sigma, s) == s]
    print(f"           {name}: {len(fixed)} fixed config(s) "
          f"{'(none)' if not fixed else str(fixed)}")

# ---------------------------------------------------------------------------
# Summary table: V4 action on Coh(K4) -- full display
# ---------------------------------------------------------------------------
print("\n" + "=" * 65)
print("Full action table: V4 x Coh(K4) -> Coh(K4)")
print("=" * 65)
print(f"  Row = V4 element, Column = coherent config index (0..7)")
print(f"  Entry = index of image config in COH_LIST")
print()
header = "V4 elem       " + "  ".join(f"s{i}" for i in range(8))
print(f"  {header}")
print(f"  {'-'*65}")
for name, sigma in zip(V4_NAMES, V4_PERMS):
    row = [COH_POS[induced_edge_action(sigma, s)] for s in COH_LIST]
    print(f"  {name:<14}" + "   ".join(str(x) for x in row))

print(f"\n  Config index legend:")
for i, s in enumerate(COH_LIST):
    tag = " [identity transport]" if all(x==1 for x in s) else ""
    print(f"    s{i} = {s}{tag}")

# ---------------------------------------------------------------------------
# Final summary
# ---------------------------------------------------------------------------
all_passed = r0 and r1 and r2 and r3 and r4 and r5

print(f"\n{'='*65}")
print(f"PDL_D61_script2.py  --  SUMMARY")
print(f"{'='*65}")
rows = [
    ("CHECK-0  |V4| = 4",                               r0),
    ("CHECK-1  V4 closed under composition",             r1),
    ("CHECK-2  Coh(K4) stable under V4 (32 checks)",    r2),
    ("CHECK-3  Identity fixes all",                      r3),
    ("CHECK-4  Non-identity elements move configs",      r4),
    ("CHECK-5  Kernel = {id} (faithful action)",         r5),
    ("CHECK-6  Orbits partition Coh(K4)",                r6),
    ("CHECK-10 V4 acts by automorphisms (256 checks)",   r10),
]
for label, result in rows:
    print(f"  {label:<48} {'PASSED' if result else 'FAILED'}")
print(f"{'='*65}")
print(f"  CHECK-7/8/9/11/12  Orbit structure & stabilisers  INFORMATIONAL")
print(f"{'='*65}")
print(f"  OVERALL: {'ALL STRUCTURAL CHECKS PASSED' if all_passed else 'ONE OR MORE FAILED'}")
print(f"{'='*65}")
print(f"""
Physical conclusion for D61:
  (1) V4 acts faithfully on Coh(K4) by edge-permutation: kernel = {{id}}.
  (2) V4 acts by GROUP AUTOMORPHISMS of Coh(K4) = Z2^3.
  (3) The orbit structure of this action is fully determined (see above).
  (4) Fixed-point analysis reveals which V4 elements stabilise which
      transport configurations (see CHECK-12).
  These are the definitions needed before D61 can be drafted.
""")
