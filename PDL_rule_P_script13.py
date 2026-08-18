# PDL_rule_P_script13.py
# ============================================================
# Rule P: the odd-boundary case characterised
#
# ############################################################
# TERMINOLOGY (corpus rule, non-negotiable)
#   Valence cores are K_24 and K_28: complete graphs on 24 and 28
#   ENTITIES. The literal K_4 of D61 denotes the electron closure
#   only and does not appear here. Composite nucleon closures
#   (K_nuc) are not treated.
# ############################################################
#
# WHERE THIS PICKS UP
#   Script 12 established, on the quadrangulated annulus C_L x P_h:
#     - L even: sea bipartite, min M = 0, exactly ONE ground state
#       (rigid); interface frustration-free iff the three
#       attachment points have pairwise EVEN separation, which
#       requires L >= 6. So L = 4 admits no frustration-free
#       placement at all.
#     - the interface excess is always exactly 1, never more, and
#       is INDEPENDENT of core size (identical for n = 4 and
#       n = 28), so it is not a small-proxy artefact;
#     - L odd: NOT characterised. Ground-state counts came out
#       3, 5, 14 for L = 3, 5, 7 at h = 2 -- equal to L for L = 3,5
#       but 2L for L = 7. And the placement (1,3,3) at L = 7 is
#       frustration-free although all three separations are odd,
#       contradicting the naive extension of the even criterion.
#
#   The jump at L = 7 and the (1,3,3) anomaly are what this script
#   is for. Both are questions about how the defects distribute
#   between the boundary ring and the interior, and neither
#   requires any assumption about the corpus.
#
# STRUCTURE PREDICTED BY HAND, to be confirmed or refuted
#   For h = 2 the annulus is the PRISM over C_L: every vertex has
#   degree 3 (two ring neighbours, one rung). Hence:
#     (P1) min M = 1 means no vertex carries more than one
#          same-state neighbour, i.e. the MONOCHROMATIC edges form
#          a MATCHING;
#     (P2) the complement of the monochromatic set is a cut, and
#          cuts are bipartite, so the monochromatic set is an
#          ODD-CYCLE TRANSVERSAL;
#     (P3) for L odd the two rings are disjoint odd cycles, so any
#          transversal needs at least one edge in each: the
#          minimum monochromatic set has size >= 2.
#   Ground states should therefore be exactly the matchings of size
#   2 (or the minimum, whatever it turns out to be) that are also
#   odd-cycle transversals and are realisable as cut-complements.
#   If the counts do not match, (P1)-(P3) are wrong somewhere and
#   that is the result.
#
# WHAT PART 3 DECIDES
#   For which triples of boundary vertices does there EXIST a
#   ground state making all three the same state? That is exactly
#   s_min = 0, hence exactly the frustration-free condition proved
#   in script 12. For L even the answer is "pairwise even
#   separation". For L odd the extra ground states buy extra
#   freedom, and the point is to find the actual criterion rather
#   than to assume the even one carries over -- it demonstrably
#   does not.
#
# Exact integer arithmetic. Standard library only.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from itertools import combinations

print("=" * 74)
print("PDL_rule_P_script13.py -- the odd-boundary case characterised")
print("=" * 74)
print()

try:
    (1).bit_count(); pc = lambda z: z.bit_count()
except AttributeError:
    pc = lambda z: bin(z).count("1")


# ============================================================
# Machinery
# ============================================================

def annulus(L, h):
    """Row 0 = hole boundary, rows 0..h-1 outward. Quadrangular."""
    idx = lambda i, j: j * L + i
    ring, rung = [], []
    for j in range(h):
        for i in range(L):
            ring.append((idx(i, j), idx((i + 1) % L, j), j))
            if j + 1 < h:
                rung.append((idx(i, j), idx(i, j + 1), None))
    edges = [(min(a, b), max(a, b)) for (a, b, _) in ring + rung]
    kind = ["ring%d" % j for (_, _, j) in ring] + ["rung"] * len(rung)
    return L * h, edges, kind, [idx(i, 0) for i in range(L)]


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


def ground_states(n, edges):
    adj = adj_masks(n, edges)
    full = (1 << n) - 1
    best, arg = None, []
    for x in range(1 << n):
        m = max(same_counts(x, adj, n, full))
        if best is None or m < best:
            best, arg = m, [x]
        elif m == best:
            arg.append(x)
    reps = sorted({min(a, full ^ a) for a in arg})
    return best, reps, adj


def mono_edges(x, edges):
    return [k for k, (u, v) in enumerate(edges)
            if ((x >> u) & 1) == ((x >> v) & 1)]


def is_matching(idxs, edges):
    seen = set()
    for k in idxs:
        u, v = edges[k]
        if u in seen or v in seen:
            return False
        seen.add(u); seen.add(v)
    return True


# ============================================================
# PART 1 -- Ground-state counts and the structure of the defects
# ============================================================
print("PART 1 -- Prism over C_L (h=2): counts and defect structure")
print("-" * 74)
print(f"  {'L':>3s} {'V':>4s} {'bip':>6s} {'min M':>6s} {'ground':>7s} "
      f"{'|mono| set':>12s} {'all matchings?':>15s} {'ratio to L':>11s}")

DATA = {}
for L in (3, 4, 5, 6, 7, 8, 9):
    n, edges, kind, bd = annulus(L, 2)
    if n > 20:
        continue
    best, reps, adj = ground_states(n, edges)
    sizes = sorted({len(mono_edges(x, edges)) for x in reps})
    allm = all(is_matching(mono_edges(x, edges), edges) for x in reps)
    DATA[L] = (n, edges, kind, bd, best, reps, adj)
    print(f"  {L:3d} {n:4d} {str(is_bipartite(n, adj)):>6s} {best:6d} "
          f"{len(reps):7d} {str(sizes):>12s} {str(allm):>15s} "
          f"{len(reps)/L:11.2f}")
print()
print("  (P1) predicts the monochromatic edges form a matching whenever")
print("  min M = 1; (P3) predicts at least two of them for L odd, one in")
print("  each ring. The columns above test both.")
print()

print("  Where do the monochromatic edges sit? (odd L only)")
for L in sorted(DATA):
    if L % 2 == 0:
        continue
    n, edges, kind, bd, best, reps, adj = DATA[L]
    tally = {}
    for x in reps:
        me = mono_edges(x, edges)
        key = tuple(sorted(kind[k] for k in me))
        tally[key] = tally.get(key, 0) + 1
    print(f"    L={L}: " + ", ".join(f"{k} -> {v}"
                                     for k, v in sorted(tally.items())))
print()


# ============================================================
# PART 2 -- Explaining the jump at L = 7
# ============================================================
print("PART 2 -- Why 3, 5, 14 and not 3, 5, 7?")
print("-" * 74)
print("  Counting the ground states by how the two ring defects are")
print("  positioned relative to one another (angular offset).")
print()
for L in sorted(DATA):
    if L % 2 == 0:
        continue
    n, edges, kind, bd, best, reps, adj = DATA[L]
    offs = {}
    for x in reps:
        me = mono_edges(x, edges)
        r0 = [k for k in me if kind[k] == "ring0"]
        r1 = [k for k in me if kind[k] == "ring1"]
        ru = [k for k in me if kind[k] == "rung"]
        if len(r0) == 1 and len(r1) == 1:
            i0 = edges[r0[0]][0] % L
            i1 = edges[r1[0]][0] % L
            d = (i1 - i0) % L
            offs[d] = offs.get(d, 0) + 1
        else:
            key = ("other", len(r0), len(r1), len(ru))
            offs[key] = offs.get(key, 0) + 1
    print(f"    L={L}: offsets -> counts: " +
          ", ".join(f"{k}:{v}" for k, v in sorted(offs.items(), key=str)))
print()


# ============================================================
# PART 3 -- The interface criterion, odd case
# ============================================================
print("PART 3 -- Which triples on the boundary can be made monochromatic?")
print("-" * 74)
print("  s_min = 0 means: SOME ground state gives the three attachment")
print("  points a common state. Script 12 proved this is exactly the")
print("  frustration-free condition, with excess 1 otherwise.")
print()
print(f"  {'L':>3s} {'gaps':>14s} {'s_min':>6s} {'free?':>7s} "
      f"{'all gaps even?':>15s} {'#even gaps':>11s}")

CRIT = {}
for L in sorted(DATA):
    n, edges, kind, bd, best, reps, adj = DATA[L]
    seen = set()
    for trio in combinations(range(L), 3):
        gaps = tuple(sorted(((trio[(i + 1) % 3] - trio[i]) % L
                             for i in range(3))))
        if gaps in seen:
            continue
        seen.add(gaps)
        tv = [bd[i] for i in trio]
        smin = 3
        for x in reps:
            for xo in (0, 1):
                s = sum(1 for t in tv if ((x >> t) & 1) == xo)
                smin = min(smin, s)
        neven = sum(1 for g in gaps if g % 2 == 0)
        CRIT[(L, gaps)] = smin
        print(f"  {L:3d} {str(gaps):>14s} {smin:6d} "
              f"{str(smin == 0):>7s} {str(neven == 3):>15s} {neven:11d}")
    print()


# ============================================================
# PART 4 -- Extracting the criterion
# ============================================================
print("PART 4 -- The criterion, separated by parity of L")
print("-" * 74)

for parity, label in ((0, "L EVEN"), (1, "L ODD")):
    rows = [(L, g, s) for (L, g), s in CRIT.items() if L % 2 == parity]
    if not rows:
        continue
    free = [(L, g) for (L, g, s) in rows if s == 0]
    frus = [(L, g) for (L, g, s) in rows if s > 0]
    print(f"  --- {label}: {len(free)} free, {len(frus)} frustrated ---")
    # test: all gaps even
    ok_even = all((s == 0) == all(x % 2 == 0 for x in g)
                  for (L, g, s) in rows)
    print(f"      criterion 'all three gaps even': {ok_even}")
    # test: at most one odd gap
    ok_one = all((s == 0) == (sum(1 for x in g if x % 2) <= 1)
                 for (L, g, s) in rows)
    print(f"      criterion 'at most one odd gap' : {ok_one}")
    # test: no gap equal to 1
    ok_no1 = all((s == 0) == (1 not in g) for (L, g, s) in rows)
    print(f"      criterion 'no gap equal to 1'   : {ok_no1}")
    print(f"      free patterns   : {sorted(set(g for (L, g) in free))}")
    print(f"      frustrated ones : {sorted(set(g for (L, g) in frus))}")
    print()

print("  A criterion that holds for one parity and fails for the other is")
print("  itself the result: it says the two regimes are not governed by")
print("  the same rule, and names what changes.")
print()


# ============================================================
# PART 5 -- h = 3, the degree-4 interior
# ============================================================
print("PART 5 -- h = 3: interior vertices of degree 4")
print("-" * 74)
print("  The real sea has interior degree 4. With h = 3 the middle row")
print("  has degree 4 while the two boundary rows have degree 3, which is")
print("  the closest honest small model.")
print()
print(f"  {'L':>3s} {'V':>4s} {'bip':>6s} {'min M':>6s} {'ground':>7s} "
      f"{'free placements':>16s} {'of':>4s}")
for L in (3, 4, 5, 6):
    n, edges, kind, bd = annulus(L, 3)
    if n > 18:
        continue
    best, reps, adj = ground_states(n, edges)
    seen, free, tot = set(), 0, 0
    for trio in combinations(range(L), 3):
        gaps = tuple(sorted(((trio[(i + 1) % 3] - trio[i]) % L
                             for i in range(3))))
        if gaps in seen:
            continue
        seen.add(gaps); tot += 1
        tv = [bd[i] for i in trio]
        smin = 3
        for x in reps:
            for xo in (0, 1):
                smin = min(smin, sum(1 for t in tv
                                     if ((x >> t) & 1) == xo))
        if smin == 0:
            free += 1
    print(f"  {L:3d} {n:4d} {str(is_bipartite(n, adj)):>6s} {best:6d} "
          f"{len(reps):7d} {free:16d} {tot:4d}")
print()

print("=" * 74)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 74)
print("  PART 1  whether ground states are matchings and odd-cycle")
print("          transversals, and where the defects sit.")
print("  PART 2  the origin of the 3, 5, 14 jump.")
print("  PART 3  s_min for every placement, both parities.")
print("  PART 4  which criterion actually governs each parity.")
print("  PART 5  whether degree-4 interior changes the picture.")
print()
print("  If (P1)-(P3) fail anywhere, that is a result about rule P and")
print("  not an error to be patched.")
print("=" * 74)
