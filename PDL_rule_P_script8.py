# PDL_rule_P_script8.py
# ============================================================
# The proximity rule P: a standalone mathematical study
#
# This script studies ONE object, on its own terms, with no
# reference to any corpus document, no quintuplet, no nucleon
# structure, no axioms beyond what is defined here. Everything
# below is graph theory.
#
# DEFINITION (Rule P)
#   Let G = (V, E) be a finite simple graph and x : V -> {+1,-1}
#   an assignment of STATES to vertices. For a vertex v put
#       same(v) = #{ w adjacent to v : x_w = x_v }.
#   Rule P selects the assignments minimising
#       M(x) = max_v same(v).
#
#   P is invariant under the global inversion x -> -x, since that
#   map preserves every same(v). It is therefore a legitimate rule
#   on relational data: it never refers to WHICH state a vertex
#   holds, only to how many neighbours agree with it.
#
#   P is LOCAL (a condition per vertex) and MINIMAX (it bounds the
#   worst vertex, not the total). The total-count variant is the
#   MaxCut problem; the minimax variant is studied here.
#
# THE FOUR QUESTIONS
#   Q1  For which graphs is the minimiser UNIQUE up to inversion?
#   Q2  What group acts on the set of minimisers, and how?
#   Q3  Is a minimiser COHERENT in the sense of signed-graph
#       balance (every cycle has positive sign product), where the
#       induced signs are s_ij = x_i x_j?
#   Q4  How does P behave under SWITCHING, i.e. under flipping the
#       states of a vertex subset?
#
# ANTICIPATED ANSWER TO Q3, WRITTEN BEFORE COMPUTING
#   Under s_ij = x_i x_j, an edge is POSITIVE exactly when its two
#   endpoints share a state. So same(v) counts positive incident
#   edges, and P minimises positive edges vertex-wise. But balance
#   (C2-style coherence) is AUTOMATIC for any vertex-induced sign
#   assignment: every cycle product is a product of squares, hence
#   +1. So EVERY assignment is coherent, and Q3 should be trivially
#   yes -- with the interesting content lying elsewhere: namely that
#   P and a "maximise coherence" principle pull in OPPOSITE
#   directions, since the all-positive state is perfectly coherent
#   and maximises same(v). If confirmed, P and any coherence-
#   maximising principle are ANTAGONISTIC, and one must say which
#   dominates. This prediction is recorded here so that the script
#   can refute it.
#
# ANTICIPATED ANSWER TO Q4
#   Switching a vertex subset S is exactly x -> x with x_i negated
#   for i in S. So P is NOT switching-invariant: switching changes
#   same(v). Only the global S = V leaves it fixed. If confirmed,
#   this is the key structural point: P sees precisely what
#   switching-invariant quantities cannot see.
#
# Exact integer arithmetic. Standard library only.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from itertools import combinations

print("=" * 68)
print("PDL_rule_P_script8.py -- the proximity rule P, studied alone")
print("=" * 68)
print()


# ============================================================
# Machinery
# ============================================================

def adjacency(n, edges):
    adj = {v: set() for v in range(n)}
    for (u, v) in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def same_counts(x, adj):
    return [sum(1 for w in adj[v] if x[w] == x[v]) for v in adj]


def M(x, adj):
    return max(same_counts(x, adj))


def total_positive(x, edges):
    return sum(1 for (u, v) in edges if x[u] == x[v])


def minimisers(n, adj):
    best, arg = None, []
    for x in itertools.product((1, -1), repeat=n):
        m = M(x, adj)
        if best is None or m < best:
            best, arg = m, [x]
        elif m == best:
            arg.append(x)
    return best, arg


def canonical(x):
    """Representative of {x, -x}."""
    return min(x, tuple(-v for v in x))


def graph_automorphisms(n, edges):
    E = {frozenset(e) for e in edges}
    auts = []
    for p in itertools.permutations(range(n)):
        if {frozenset((p[u], p[v])) for (u, v) in edges} == E:
            auts.append(p)
    return auts


def orbits_of(states, auts):
    """Orbits of a set of canonical states under Aut(G) x {global inversion}."""
    rem = set(states)
    out = []
    while rem:
        s = next(iter(rem))
        orb = set()
        for p in auts:
            t = tuple(s[p.index(i)] for i in range(len(s)))
            orb.add(canonical(t))
        orb &= set(states)
        out.append(orb)
        rem -= orb
    return out


# ============================================================
# Test graphs
# ============================================================

def K(n):
    return n, [(i, j) for i in range(n) for j in range(i + 1, n)]


def cycle(n):
    return n, [(i, (i + 1) % n) for i in range(n)]


def path(n):
    return n, [(i, i + 1) for i in range(n - 1)]


def grid(a, b):
    idx = lambda i, j: i * b + j
    e = []
    for i in range(a):
        for j in range(b):
            if j + 1 < b:
                e.append((idx(i, j), idx(i, j + 1)))
            if i + 1 < a:
                e.append((idx(i, j), idx(i + 1, j)))
    return a * b, e


def petersen():
    outer = [(i, (i + 1) % 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    spokes = [(i, 5 + i) for i in range(5)]
    return 10, outer + inner + spokes


GRAPHS = [
    ("K_3", K(3)), ("K_4", K(4)), ("K_5", K(5)), ("K_6", K(6)),
    ("K_7", K(7)), ("K_8", K(8)),
    ("C_4", cycle(4)), ("C_5", cycle(5)), ("C_6", cycle(6)),
    ("C_7", cycle(7)),
    ("path P_5", path(5)),
    ("grid 2x3", grid(2, 3)), ("grid 3x3", grid(3, 3)),
    ("grid 2x4", grid(2, 4)),
    ("Petersen", petersen()),
]


# ============================================================
# Q1 and Q2 -- uniqueness and the group action
# ============================================================
print("Q1/Q2 -- Minimisers of M(x) = max_v same(v): count and orbits")
print("-" * 68)
print(f"  {'graph':>10s} {'n':>3s} {'m':>4s} {'min M':>6s} {'minimisers':>11s} "
      f"{'mod inv':>8s} {'|Aut|':>6s} {'orbits':>7s} {'unique?':>8s}")

STORE = {}
for label, (n, edges) in GRAPHS:
    adj = adjacency(n, edges)
    best, arg = minimisers(n, adj)
    canon = {canonical(x) for x in arg}
    auts = graph_automorphisms(n, edges)
    orb = orbits_of(canon, auts)
    STORE[label] = (n, edges, adj, best, arg, canon, auts, orb)
    print(f"  {label:>10s} {n:3d} {len(edges):4d} {best:6d} {len(arg):11d} "
          f"{len(canon):8d} {len(auts):6d} {len(orb):7d} "
          f"{str(len(canon) == 1):>8s}")
print()
print("  'mod inv' counts minimisers up to the global inversion x -> -x.")
print("  'unique?' is True when exactly one minimiser survives that")
print("  quotient -- the strongest form of selection P can achieve.")
print()


# ============================================================
# Q1 continued -- when IS the minimiser unique?
# ============================================================
print("Q1 (continued) -- structural pattern of uniqueness")
print("-" * 68)
uniq = [l for l in STORE if len(STORE[l][5]) == 1]
nonu = [l for l in STORE if len(STORE[l][5]) > 1]
print(f"  unique up to inversion : {uniq}")
print(f"  NOT unique             : {nonu}")
print()
print("  Parity check on complete graphs (min M = ceil(n/2) - 1):")
for n in range(3, 9):
    lab = f"K_{n}"
    if lab in STORE:
        best = STORE[lab][3]
        k = n // 2
        pred = k - 1 if n % 2 == 0 else (n + 1) // 2 - 1
        print(f"    K_{n}: min M = {best}, predicted {pred}, "
              f"match {best == pred}; balanced split "
              f"{k}|{n-k}; imbalance "
              f"{abs((k-1)-(n-k))}")
print()


# ============================================================
# Q3 -- coherence of the minimisers
# ============================================================
print("Q3 -- Are minimisers coherent (all cycle sign products = +1)?")
print("-" * 68)
print("  Induced signs s_ij = x_i x_j. Test every cycle in a cycle basis.")
print()


def cycle_basis_signs(n, edges, x):
    """Every vertex-induced signing is balanced; verify directly on
       all cycles of length up to 6 by brute force."""
    bad = 0
    for L in range(3, min(n, 6) + 1):
        for verts in itertools.permutations(range(n), L):
            if verts[0] != min(verts) or verts[1] > verts[-1]:
                continue
            ok = all(frozenset((verts[i], verts[(i + 1) % L])) in
                     {frozenset(e) for e in edges} for i in range(L))
            if not ok:
                continue
            prod = 1
            for i in range(L):
                a, b = verts[i], verts[(i + 1) % L]
                prod *= x[a] * x[b]
            if prod != 1:
                bad += 1
    return bad


for label in ("K_4", "K_5", "C_5", "grid 2x3", "Petersen"):
    n, edges, adj, best, arg, canon, auts, orb = STORE[label]
    x = arg[0]
    bad = cycle_basis_signs(n, edges, x)
    allpos = tuple([1] * n)
    print(f"  {label:>10s}: minimiser has {bad} cycles with negative product")
    print(f"              M(minimiser) = {M(x, adj)},  "
          f"M(all-same) = {M(allpos, adj)},  "
          f"positive edges: {total_positive(x, edges)} vs "
          f"{total_positive(allpos, edges)}")
print()
print("  READING: every vertex-induced signing is automatically balanced,")
print("  so coherence cannot distinguish states. The real content is the")
print("  comparison above: the all-same state is perfectly coherent and")
print("  MAXIMISES M. P therefore pushes AWAY from it.")
print()


# ============================================================
# Q4 -- behaviour under switching
# ============================================================
print("Q4 -- Is P invariant under switching (flipping a vertex subset)?")
print("-" * 68)

for label in ("K_4", "K_5", "C_6", "grid 2x3"):
    n, edges, adj, best, arg, canon, auts, orb = STORE[label]
    x0 = arg[0]
    vals = set()
    trivial = []
    for r in range(n + 1):
        for S in combinations(range(n), r):
            x1 = tuple(-v if i in S else v for i, v in enumerate(x0))
            vals.add(M(x1, adj))
            if M(x1, adj) == M(x0, adj):
                trivial.append(S)
    print(f"  {label:>10s}: M takes {len(vals)} distinct values over all "
          f"{2**n} switchings -> invariant: {len(vals) == 1}")
    print(f"              values {sorted(vals)};  "
          f"{len(trivial)} subsets preserve M")
print()
print("  If M is NOT switching-invariant, then P sees exactly what every")
print("  switching-invariant functional is blind to. That is the whole")
print("  structural point of the rule, and it is decided here.")
print()


# ============================================================
# Q4 continued -- P versus the total-count variant (MaxCut)
# ============================================================
print("Q4 (continued) -- minimax P versus the total-count variant")
print("-" * 68)
print(f"  {'graph':>10s} {'P minimisers':>13s} {'MaxCut optima':>14s} "
      f"{'P subset of MaxCut?':>20s}")
for label, (n, edges) in GRAPHS:
    adj = adjacency(n, edges)
    _, argP = minimisers(n, adj)
    canP = {canonical(x) for x in argP}
    bestT, argT = None, []
    for x in itertools.product((1, -1), repeat=n):
        t = total_positive(x, edges)
        if bestT is None or t < bestT:
            bestT, argT = t, [x]
        elif t == bestT:
            argT.append(x)
    canT = {canonical(x) for x in argT}
    print(f"  {label:>10s} {len(canP):13d} {len(canT):14d} "
          f"{str(canP <= canT):>20s}")
print()
print("  The two variants are different optimisation problems. Where P's")
print("  minimisers are a strict subset, P is the finer rule; where they")
print("  are not nested, the two are genuinely inequivalent and a choice")
print("  between them must be argued, not assumed.")
print()

print("=" * 68)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 68)
print("  Q1  the graphs on which P selects uniquely up to inversion;")
print("  Q2  the orbit structure of the minimisers under Aut(G);")
print("  Q3  whether coherence discriminates (predicted: no, trivially),")
print("      and whether P opposes coherence-maximisation (predicted: yes);")
print("  Q4  whether P is switching-invariant (predicted: no), and how it")
print("      relates to the total-count/MaxCut variant.")
print()
print("  Predictions were written before running. Any mismatch is a")
print("  result about the rule, not an error to be patched.")
print("=" * 68)
