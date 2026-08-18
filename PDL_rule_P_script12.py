# PDL_rule_P_script12.py
# ============================================================
# Rule P: the geometry of the hole decides both the rigidity of
# the sea and the frustration of the interface
#
# ############################################################
# TERMINOLOGY (corpus rule, non-negotiable)
#   Valence cores are K_24 and K_28: complete graphs on 24 and 28
#   ENTITIES (no K_4 blocks inside them). The literal K_4 of D61
#   denotes the electron closure only and does not appear here.
#   Composite nucleon closures (K_nuc) are not treated.
# ############################################################
#
# DEFINITION (Rule P)
#   x : V -> {+1,-1};  same(v) = #{w ~ v : x_w = x_v};
#   M(x) = max_v same(v);  P selects the x minimising M.
#   Invariant under x -> -x. Local, minimax, and NOT invariant
#   under switching -- so it sees what switching-invariant
#   functionals cannot (established scripts 8, 9b).
#
# ESTABLISHED SO FAR
#   - min M = 0 <=> G bipartite (connected), and the minimiser is
#     then unique up to inversion. Theorem, no computation needed.
#   - On K_n: min M = ceil(n/2) - 1 at the balanced split; degree
#     n-1 odd for n even, so the same/opposite gap is 1 and can
#     never vanish. K_24 has 1 352 078 ground states, K_28 has
#     20 058 300 -- one Aut-orbit, but enormous.
#   - Euler forbids a 4-regular quadrangulation of S^2 (it needs
#     chi = 0, i.e. the torus). Quadrangulations of S^2 are
#     bipartite, hence rigid under P.
#   - Sea proxies: C_a x C_b is bipartite iff both a,b even, and
#     then has exactly ONE ground state; an odd factor gives
#     min M >= 1 and several.
#   - So under rule P the SEA is the rigid side and the CORES the
#     free side -- the reverse of the picture assumed earlier in
#     the session.
#
# THE HAND CALCULATION THIS SCRIPT TESTS
#   Let o be the outward vertex of a core K_n, lying in a camp of
#   size k, and let s be the number of its three sea attachments
#   carrying the same state as o. Then, on the core side,
#        M_core = max(k - 1 + s,  n - k - 1),
#   which depends on the sea only through s. Minimising over k:
#     s = 0 gives back ceil(n/2) - 1, the core's own optimum, so
#            the two regimes coexist at NO cost;
#     s > 0 raises it, and the excess is independent of n.
#   Moreover s_min is the size of the MINORITY colour class among
#   the three attachment points, since o may take either state.
#   Hence the criterion:
#
#     the interface is frustration-free  <=>  the three attachment
#     points share one colour in the sea's ground state.
#
#   Because the core contributes analytically, this script does NOT
#   enumerate core states: it uses the REAL n = 24 and n = 28
#   rather than small proxies. Only the sea is enumerated.
#
# WHY THE HOLE GEOMETRY IS THE DECIDING FACTOR
#   If the three attachments are the corners of a triangular hole
#   boundary they are mutually adjacent, hence necessarily of three
#   different colours, forcing s_min = 1; and the triangle is
#   itself an odd cycle, which destroys the bipartiteness of the
#   sea. Both effects arrive together. If the boundary cycle is
#   even and the attachments are pairwise at even distance, both
#   effects are absent. PART 3 sweeps boundary length and
#   attachment placement to see which combinations occur.
#
# SEA MODEL
#   A quadrangulated annulus C_L x P_h: a cycle of length L (the
#   hole boundary, row 0) times a path of height h. All faces are
#   quadrilaterals; interior vertices have degree 4, boundary
#   vertices degree 3. Bipartite iff L is even. This is the
#   simplest honest model of a quadrangular sea around one hole.
#
# Exact integer arithmetic. Standard library only.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from math import comb

print("=" * 74)
print("PDL_rule_P_script12.py -- hole geometry, sea rigidity, interface")
print("=" * 74)
print()

try:
    (1).bit_count(); pc = lambda z: z.bit_count()
except AttributeError:
    pc = lambda z: bin(z).count("1")


# ============================================================
# Sea: quadrangulated annulus C_L x P_h
# ============================================================

def annulus(L, h):
    """Row 0 = hole boundary. Returns n, edges, boundary vertex list."""
    idx = lambda i, j: j * L + i          # i around, j outward
    e = set()
    for j in range(h):
        for i in range(L):
            e.add(tuple(sorted((idx(i, j), idx((i + 1) % L, j)))))
            if j + 1 < h:
                e.add(tuple(sorted((idx(i, j), idx(i, j + 1)))))
    return L * h, sorted(e), [idx(i, 0) for i in range(L)]


def adj_masks(n, edges):
    adj = [0] * n
    for (u, v) in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def same_counts(x, adj, n, full):
    nx = full ^ x
    return [pc(adj[v] & (x if (x >> v) & 1 else nx)) for v in range(n)]


def is_bipartite(n, adj):
    col = [-1] * n
    for s in range(n):
        if col[s] != -1:
            continue
        col[s] = 0; st = [s]
        while st:
            v = st.pop(); nb = adj[v]
            while nb:
                b = nb & -nb; w = b.bit_length() - 1; nb ^= b
                if col[w] == -1:
                    col[w] = 1 - col[v]; st.append(w)
                elif col[w] == col[v]:
                    return False
    return True


def sea_ground_states(n, adj):
    full = (1 << n) - 1
    best, arg = None, []
    for x in range(1 << n):
        m = max(same_counts(x, adj, n, full))
        if best is None or m < best:
            best, arg = m, [x]
        elif m == best:
            arg.append(x)
    reps = sorted({min(a, full ^ a) for a in arg})
    return best, reps


# ============================================================
# PART 1 -- The core contributes analytically
# ============================================================
print("PART 1 -- Core side: M_core = max(k-1+s, n-k-1), minimised over k")
print("-" * 74)
print("  The core enters only through s, so the real n = 24 and n = 28 can")
print("  be used directly. No core state is enumerated anywhere below.")
print()


def core_min_M(n, s):
    return min(max(k - 1 + s, n - k - 1) for k in range(1, n))


print(f"  {'n':>4s} {'s=0':>6s} {'s=1':>6s} {'s=2':>6s} {'s=3':>6s} "
      f"{'core alone':>11s} {'excess at s=1':>14s}")
for n in (4, 6, 12, 24, 28, 100):
    row = [core_min_M(n, s) for s in range(4)]
    alone = (n + 1) // 2 - 1 if n % 2 else n // 2 - 1
    print(f"  {n:4d} {row[0]:6d} {row[1]:6d} {row[2]:6d} {row[3]:6d} "
          f"{alone:11d} {row[1]-row[0]:14d}")
print()
print("  s = 0 returns exactly the core's own optimum: no cost at all.")
print("  The excess at s = 1 is the same for n = 4 and for n = 28, so it")
print("  is NOT a small-size artefact -- the earlier reservation is lifted.")
print()


# ============================================================
# PART 2 -- Sea rigidity as a function of hole boundary length
# ============================================================
print("PART 2 -- Sea C_L x P_h: rigidity depends on the parity of L")
print("-" * 74)
print(f"  {'L':>3s} {'h':>3s} {'V':>4s} {'E':>4s} {'bipartite':>10s} "
      f"{'min M':>6s} {'ground states':>14s} {'rigid?':>7s}")
SEA = {}
for L in (3, 4, 5, 6, 7, 8):
    for h in (2, 3):
        n, e, bd = annulus(L, h)
        if n > 18:
            continue
        adj = adj_masks(n, e)
        bip = is_bipartite(n, adj)
        best, reps = sea_ground_states(n, adj)
        SEA[(L, h)] = (n, e, bd, adj, bip, best, reps)
        print(f"  {L:3d} {h:3d} {n:4d} {len(e):4d} {str(bip):>10s} "
              f"{best:6d} {len(reps):14d} {str(len(reps) == 1):>7s}")
print()
print("  L even: bipartite, min M = 0, a single ground state -- rigid.")
print("  L odd : an odd cycle on the hole boundary, min M rises, and the")
print("          ground state becomes degenerate.")
print()


# ============================================================
# PART 3 -- Attachment placement: when is s_min = 0?
# ============================================================
print("PART 3 -- Three attachment points on the hole boundary")
print("-" * 74)
print("  s_min = size of the minority colour class among the three")
print("  attachments, over all sea ground states. s_min = 0 means the")
print("  three can be made monochromatic, hence zero interface cost.")
print()
print(f"  {'L':>3s} {'h':>3s} {'placement':>16s} {'s_min':>6s} "
      f"{'joint min M (n=24)':>19s} {'core alone':>11s} {'excess':>7s}")

RESULTS = {}
for (L, h) in sorted(SEA):
    n_sea, e, bd, adj, bip, sea_best, reps = SEA[(L, h)]
    full = (1 << n_sea) - 1
    # placements of 3 attachment points on the boundary cycle, up to rotation
    placements = []
    seen = set()
    for trio in itertools.combinations(range(L), 3):
        gaps = tuple(sorted(((trio[(i + 1) % 3] - trio[i]) % L
                             for i in range(3))))
        if gaps in seen:
            continue
        seen.add(gaps)
        placements.append((trio, gaps))
    for trio, gaps in placements:
        tv = [bd[i] for i in trio]
        best_s, best_joint = None, None
        for x in reps:
            for xo in (0, 1):
                s = sum(1 for t in tv if ((x >> t) & 1) == xo)
                # sea side: attachment vertices matching o gain one
                sc = same_counts(x, adj, n_sea, full)
                for t in tv:
                    if ((x >> t) & 1) == xo:
                        sc[t] += 1
                sea_side = max(sc)
                for n_core in (24,):
                    cm = core_min_M(n_core, s)
                    j = max(sea_side, cm)
                    if best_joint is None or j < best_joint:
                        best_joint, best_s = j, s
                    elif j == best_joint and s < best_s:
                        best_s = s
        alone = 24 // 2 - 1
        RESULTS[(L, h, gaps)] = (best_s, best_joint, alone)
        print(f"  {L:3d} {h:3d} {str(gaps):>16s} {best_s:6d} "
              f"{best_joint:19d} {alone:11d} {best_joint-alone:7d}")
print()


# ============================================================
# PART 4 -- The criterion, stated and checked
# ============================================================
print("PART 4 -- Frustration-free iff the three attachments are monochromatic")
print("-" * 74)
ok = True
free = [k for k, v in RESULTS.items() if v[1] == v[2]]
frus = [k for k, v in RESULTS.items() if v[1] > v[2]]
for k, v in RESULTS.items():
    s, joint, alone = v
    if (s == 0) != (joint == alone):
        ok = False
print(f"  configurations tested          : {len(RESULTS)}")
print(f"  frustration-free (joint=alone) : {len(free)}")
print(f"  frustrated (joint>alone)       : {len(frus)}")
print(f"  criterion 's_min = 0  <=>  no frustration' holds: {ok}")
print()
print("  Frustration-free placements, by (L, h, gap pattern):")
for k in sorted(free):
    print(f"    L={k[0]}, h={k[1]}, gaps={k[2]}")
if not free:
    print("    NONE -- every placement tested is frustrated.")
print()
print("  Frustrated placements:")
for k in sorted(frus)[:12]:
    print(f"    L={k[0]}, h={k[1]}, gaps={k[2]}  (excess "
          f"{RESULTS[k][1]-RESULTS[k][2]})")
if len(frus) > 12:
    print(f"    ... and {len(frus)-12} more")
print()


# ============================================================
# PART 5 -- The triangular hole, exhibited
# ============================================================
print("PART 5 -- The triangular hole: both effects arrive together")
print("-" * 74)
print("  If the hole boundary is a triangle (L=3) the three attachments")
print("  are mutually adjacent, so no two can share a colour, and the")
print("  triangle is itself an odd cycle destroying bipartiteness.")
print()
for h in (2, 3):
    if (3, h) not in SEA:
        continue
    n_sea, e, bd, adj, bip, sea_best, reps = SEA[(3, h)]
    print(f"  L=3, h={h}: bipartite = {bip}, sea min M = {sea_best}, "
          f"ground states = {len(reps)}")
    key = [k for k in RESULTS if k[0] == 3 and k[1] == h]
    for k in key:
        s, joint, alone = RESULTS[k]
        print(f"            s_min = {s}, joint min M = {joint}, "
              f"core alone = {alone}, excess = {joint-alone}")
print()
print("  For comparison, an even boundary with attachments at even mutual")
print("  distance:")
for (L, h) in [(6, 2), (8, 2)]:
    if (L, h) not in SEA:
        continue
    for k in [k for k in RESULTS if k[0] == L and k[1] == h]:
        s, joint, alone = RESULTS[k]
        tag = "  <-- frustration-free" if joint == alone else ""
        print(f"    L={L}, h={h}, gaps={k[2]}: s_min={s}, "
              f"excess={joint-alone}{tag}")
print()

print("=" * 74)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 74)
print("  PART 1  the interface cost depends on the core only through s,")
print("          and the excess at s=1 is identical for n=4 and n=28 --")
print("          so the frustration seen in script 11 is not an artefact")
print("          of using small proxies.")
print("  PART 2  the parity of the hole boundary decides whether the sea")
print("          is rigid (one ground state) or degenerate.")
print("  PART 3  whether the three attachment points can be monochromatic.")
print("  PART 4  the criterion, checked against every configuration.")
print("  PART 5  the triangular hole, where both effects coincide.")
print()
print("  A run in which EVERY placement is frustration-free would mean")
print("  rule P imposes no interface constraint at all, and the")
print("  interface line of enquiry would close. That outcome is")
print("  possible and would be reported as such.")
print("=" * 74)
