# PDL_rule_P_script10.py
# ============================================================
# Rule P: exhaustive verification of the bipartite dichotomy
#
# Standalone graph theory. No corpus reference.
#
# DEFINITION (Rule P)
#   G = (V,E) finite simple connected graph, x : V -> {+1,-1}.
#       same(v) = #{ w ~ v : x_w = x_v },   M(x) = max_v same(v).
#   P selects the assignments minimising M. P is invariant under
#   the global inversion x -> -x, which preserves every same(v).
#
# WHAT THIS SCRIPT VERIFIES (D69, Theorem 4.1)
#   For connected G:   min M = 0  <=>  G is bipartite,
#   and in that case the minimiser is unique up to inversion.
#
#   The proof is two lines: M(x) = 0 means no vertex has a
#   neighbour in its own state, i.e. every edge is bichromatic,
#   i.e. x is a proper 2-colouring; and a connected bipartite
#   graph has exactly one proper 2-colouring up to inversion.
#   The verification below is exhaustive over every connected
#   LABELLED graph on at most 6 vertices and is offered as a check
#   on the statement, not as its support.
#
# WHAT THIS SCRIPT DELIBERATELY DOES NOT DO
#   An earlier version attempted an exhaustive sweep over all
#   connected graphs up to ISOMORPHISM for n <= 7, cross-tabulating
#   orbit multiplicity against automorphism strength, odd girth and
#   vertex-transitivity. That version was intractable: it computed
#   a canonical form per graph as a minimum over all n! vertex
#   permutations, which at n = 7 means 5040 permutations applied to
#   each of 2^21 edge masks. The design fault is recorded here
#   rather than silently repaired, because the sweep is exactly
#   what OP-D69-1 asks for and it needs a genuine isomorphism test
#   (nauty, or a partition-refinement canonical labelling) rather
#   than brute force. PART 3 reports the sizes involved so that a
#   future attempt can be dimensioned honestly.
#
#   Consequently the only claim this script supports is the
#   bipartite dichotomy. The orbit-multiplicity results cited in
#   D69 come from script8 (fifteen named structures) and script9b
#   (the cycle family in closed form), not from here.
#
# Exact integer arithmetic. Standard library only.
# Runtime: a few seconds.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
import math
from itertools import combinations
from math import comb

print("=" * 70)
print("PDL_rule_P_script10.py -- the bipartite dichotomy, verified")
print("=" * 70)
print()

try:
    (1).bit_count(); pc = lambda z: z.bit_count()
except AttributeError:
    pc = lambda z: bin(z).count("1")


# ============================================================
# Machinery
# ============================================================

def edge_list(n):
    return list(combinations(range(n), 2))


def adj_from_mask(mask, edges, n):
    adj = [0] * n
    for k, (u, v) in enumerate(edges):
        if (mask >> k) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def connected(adj, n):
    seen, stack = 1, [0]
    while stack:
        v = stack.pop()
        nb = adj[v] & ~seen
        while nb:
            b = nb & -nb
            seen |= b
            stack.append(b.bit_length() - 1)
            nb ^= b
    return seen == (1 << n) - 1


def bipartite(adj, n):
    col = [-1] * n
    col[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        nb = adj[v]
        while nb:
            b = nb & -nb
            w = b.bit_length() - 1
            nb ^= b
            if col[w] == -1:
                col[w] = 1 - col[v]
                stack.append(w)
            elif col[w] == col[v]:
                return False
    return True


def min_M_and_count(adj, n):
    full = (1 << n) - 1
    best, arg = None, []
    for x in range(1 << n):
        nx = full ^ x
        m = 0
        for v in range(n):
            s = pc(adj[v] & (x if (x >> v) & 1 else nx))
            if s > m:
                m = s
        if best is None or m < best:
            best, arg = m, [x]
        elif m == best:
            arg.append(x)
    reps = {min(a, full ^ a) for a in arg}
    return best, len(reps)


# ============================================================
# PART 1 -- The dichotomy, exhaustively
# ============================================================
print("PART 1 -- min M = 0 iff bipartite, over all connected labelled")
print("          graphs with 3 <= n <= 6")
print("-" * 70)
print(f"  {'n':>3s} {'graphs tested':>14s} {'bipartite':>10s} "
      f"{'min M = 0':>10s} {'unique minimiser':>17s} {'violations':>11s}")

grand_total = grand_bad = 0
for n in range(3, 7):
    edges = edge_list(n)
    m = len(edges)
    tested = bip = zero = uniq = bad = 0
    for mask in range(1 << m):
        adj = adj_from_mask(mask, edges, n)
        if not connected(adj, n):
            continue
        tested += 1
        b = bipartite(adj, n)
        best, cnt = min_M_and_count(adj, n)
        if b:
            bip += 1
        if best == 0:
            zero += 1
        if b and cnt == 1:
            uniq += 1
        if (best == 0) != b:
            bad += 1
        if b and cnt != 1:
            bad += 1
    grand_total += tested
    grand_bad += bad
    print(f"  {n:3d} {tested:14d} {bip:10d} {zero:10d} {uniq:17d} {bad:11d}")

print()
print(f"  TOTAL connected labelled graphs tested : {grand_total}")
print(f"  TOTAL violations of the claim          : {grand_bad}")
print(f"  THEOREM VERIFIED                       : {grand_bad == 0}")
print()


# ============================================================
# PART 2 -- The non-bipartite side, on complete graphs
# ============================================================
print("PART 2 -- On the non-bipartite side, degeneracy is the rule")
print("-" * 70)
print("  The same computation on complete graphs, where min M =")
print("  ceil(n/2) - 1 and the minimisers are the balanced bipartitions")
print("  (D69, Theorem 4.2).")
print()
print(f"  {'n':>3s} {'min M':>6s} {'predicted':>10s} {'minimisers':>11s} "
      f"{'predicted':>10s} {'match':>6s}")
ok2 = True
for n in range(3, 9):
    edges = edge_list(n)
    adj = adj_from_mask((1 << len(edges)) - 1, edges, n)
    best, cnt = min_M_and_count(adj, n)
    pred_M = (n + 1) // 2 - 1
    pred_c = comb(n, n // 2) // 2 if n % 2 == 0 else comb(n, n // 2)
    good = (best == pred_M and cnt == pred_c)
    ok2 &= good
    print(f"  {n:3d} {best:6d} {pred_M:10d} {cnt:11d} {pred_c:10d} "
          f"{str(good):>6s}")
print()
print(f"  Theorem 4.2 verified on this range: {ok2}")
print()


# ============================================================
# PART 3 -- Dimensioning the sweep that OP-D69-1 asks for
# ============================================================
print("PART 3 -- Why the isomorphism sweep is deferred, with numbers")
print("-" * 70)
print("  OP-D69-1 asks which non-bipartite connected graphs have a single")
print("  Aut-orbit of minimisers. A brute-force canonical form costs n!")
print("  permutations per graph, applied to every edge mask:")
print()
print(f"  {'n':>3s} {'edge masks':>14s} {'perms n!':>10s} "
      f"{'naive product':>15s} {'connected graphs up to iso':>27s}")
known_iso = {4: 6, 5: 21, 6: 112, 7: 853, 8: 11117}
for n in range(4, 9):
    masks = 2 ** (n * (n - 1) // 2)
    perms = math.factorial(n)
    print(f"  {n:3d} {masks:14d} {perms:10d} {masks*perms:15.3e} "
          f"{known_iso.get(n, 0):27d}")
print()
print("  The product is the operation count of the naive method. At n = 7")
print("  it is already beyond a scripted run, while the number of graphs")
print("  actually needing analysis is 853. The gap is entirely the cost of")
print("  the canonical form, which a proper isomorphism test removes. That")
print("  is the tool OP-D69-1 requires; this script does not attempt the")
print("  sweep and makes no claim about it.")
print()

print("=" * 70)
print("WHAT THIS SCRIPT ESTABLISHES")
print("=" * 70)
print("  The bipartite dichotomy, exhaustively over every connected")
print("  labelled graph on at most 6 vertices, in both directions, with")
print("  uniqueness of the minimiser on the bipartite side; and Theorem")
print("  4.2 on complete graphs up to n = 8.")
print()
print("  It establishes nothing about orbit multiplicity on non-bipartite")
print("  graphs beyond the complete-graph case. That question is OP-D69-1")
print("  and is open.")
print("=" * 70)
