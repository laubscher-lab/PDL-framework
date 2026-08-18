# PDL_pulsation_regimes_script1.py
# ============================================================
# Verification script -- Pulsation regimes and the switching
# formulation of C1-C3
# PDL Framework -- preliminary to a possible document D68
#
# QUESTION UNDER TEST:
#   Is the simultaneous inversion of every entity at every cycle
#   a coherent dynamical regime, or is it empty? If empty, which
#   regime replaces it: random (asynchronous) state change, or
#   regular change with heterogeneous periods?
#
# LOGICAL ARCHITECTURE:
#
#   PART 1  Coherent configurations are exactly the vertex-induced
#           ones. |Coh(K_n)| = 2^(n-1). Each coherent config has
#           exactly 2 preimages x, -x. (Harary; consistent with D66.)
#
#   PART 2  Switching by a vertex subset S preserves C2 for EVERY S,
#           and is an involution. Hence every fixed S gives an exact
#           logical 2-cycle: C1 is satisfied by construction.
#
#   PART 3  S = empty and S = V act as the identity on edge signs.
#           GLOBAL SIMULTANEOUS INVERSION IS THE TRIVIAL ELEMENT.
#           Non-triviality requires delta(S) != empty, which for a
#           connected graph (C3) holds iff S is proper and non-empty.
#           Tested on a connected AND on a disconnected graph to
#           isolate the role of C3.
#
#   PART 4  The S4-orbit structure 1+3+4 of D60 is recovered from
#           cut sizes alone: |S| in {0,4} -> 1, {1,3} -> 4, {2} -> 3.
#           CANDIDATE IDENTIFICATION (not yet a corpus theorem):
#           the three 2|2 cuts together with the empty cut form a
#           Klein group under symmetric difference; test whether it
#           coincides with the V4 of D60 in its action on orbit-4.
#
#   PART 5  REGIME TEST. Entity i flips whenever t = 0 mod p_i.
#           Cumulative flip set F_t = {i : floor(t/p_i) is odd}.
#           Relational state s_t = switch(F_t, s_0).
#           (a) H_sync      : all p_i = 1.
#           (b) H_uniform   : all p_i = p, for p = 1..6.
#           (c) H_hetero    : all assignments in {1,..,4}^4, exhaustive.
#           (d) H_random    : random flip sets, sampled.
#           For each, compute the exact period of the RELATIONAL
#           sequence and report which regimes yield period exactly 2
#           with a non-constant sequence (i.e. genuine C1 compliance).
#
# All arithmetic is exact integer arithmetic. No floating point.
# Standard library only: itertools, random.
#
# PDL verrouillage protocol: execute independently in Google Colab
# and return full output BEFORE any LaTeX drafting.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from itertools import combinations, permutations
import random

print("=" * 64)
print("PDL_pulsation_regimes_script1.py")
print("Pulsation regimes and the switching formulation of C1-C3")
print("=" * 64)
print()


# ============================================================
# Generic signed-graph machinery
# ============================================================

def edges_complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def triangles_complete(n):
    return list(combinations(range(n), 3))


def edge_index(edges):
    return {e: k for k, e in enumerate(edges)}


def is_coherent(s, edges, tris):
    idx = edge_index(edges)

    def eid(a, b):
        return idx[(a, b)] if a < b else idx[(b, a)]

    for (a, b, c) in tris:
        if s[eid(a, b)] * s[eid(a, c)] * s[eid(b, c)] != 1:
            return False
    return True


def vertex_induced(x, edges):
    """s_ij = x_i * x_j."""
    return tuple(x[i] * x[j] for (i, j) in edges)


def switch(S, s, edges):
    """Switching by vertex subset S: flip every edge crossing the boundary."""
    return tuple(-v if ((i in S) != (j in S)) else v
                 for v, (i, j) in zip(s, edges))


def cut_edges(S, edges):
    return [e for e in edges if (e[0] in S) != (e[1] in S)]


# ============================================================
# PART 1 -- Coherent configurations are exactly the cuts
# ============================================================
print("PART 1 -- Coherent configurations = vertex-induced = bipartitions")
print("-" * 64)

for n in range(3, 7):
    edges = edges_complete(n)
    tris = triangles_complete(n)
    m = len(edges)

    all_configs = list(itertools.product([1, -1], repeat=m))
    coh = [s for s in all_configs if is_coherent(s, edges, tris)]

    induced = {}
    for x in itertools.product([1, -1], repeat=n):
        s = vertex_induced(x, edges)
        induced.setdefault(s, []).append(x)

    assert len(coh) == 2 ** (n - 1), f"n={n}: |Coh| mismatch"
    assert set(coh) == set(induced.keys()), f"n={n}: Coh != vertex-induced"
    assert all(len(v) == 2 for v in induced.values()), f"n={n}: preimage count"

    print(f"  n = {n}: |Coh(K_n)| = {len(coh):3d} = 2^(n-1)          PASSED")
    print(f"         Coh == vertex-induced configurations       PASSED")
    print(f"         every coherent config has exactly 2 preimages (x, -x)")
print()
print("  CONSEQUENCE: the relational state of a C2-admissible universe")
print("  is a BIPARTITION of its entities, not a list of edge signs.")
print()


# ============================================================
# PART 2 -- Switching preserves C2, and is an involution
# ============================================================
print("PART 2 -- Switching by any subset S preserves C2 and is involutive")
print("-" * 64)

n = 4
edges = edges_complete(n)
tris = triangles_complete(n)
COH = [s for s in itertools.product([1, -1], repeat=len(edges))
       if is_coherent(s, edges, tris)]
SUBSETS = [frozenset(c) for k in range(n + 1)
           for c in combinations(range(n), k)]

pres, invol = 0, 0
for S in SUBSETS:
    for s in COH:
        s1 = switch(S, s, edges)
        assert is_coherent(s1, edges, tris)
        pres += 1
        assert switch(S, s1, edges) == s
        invol += 1

print(f"  Subsets tested: {len(SUBSETS)}   Coherent configs: {len(COH)}")
print(f"  C2 preserved under switching:  {pres}/{pres} checks   PASSED")
print(f"  Switching is an involution:    {invol}/{invol} checks   PASSED")
print()
print("  CONSEQUENCE: every FIXED subset S generates an exact logical")
print("  2-cycle. C1 is satisfied by construction for any S.")
print()


# ============================================================
# PART 3 -- Global simultaneous inversion is the trivial element
# ============================================================
print("PART 3 -- Global simultaneous inversion: trivial, and the role of C3")
print("-" * 64)

triv = [S for S in SUBSETS
        if all(switch(S, s, edges) == s for s in COH)]
print(f"  Subsets acting as the IDENTITY on all coherent configs:")
for S in triv:
    print(f"    S = {sorted(S) if S else '(empty)'}   |delta(S)| = "
          f"{len(cut_edges(S, edges))}")
assert set(triv) == {frozenset(), frozenset(range(n))}
print("  CHECK: exactly {empty, V} act trivially            PASSED")
print()
print("  H_sync (every entity inverts at every cycle) => S = V => identity.")
print("  The relational state is a FIXED POINT. C1 explicitly excludes")
print("  fixed points. H_sync is not incoherent -- it is EMPTY.")
print("  This is the U(1) global phase of D46, restated combinatorially.")
print()

print("  Role of C3 (connectedness):")
# connected example: path 0-1-2-3 ; disconnected example: 0-1 and 2-3
for label, ed in [("connected path 0-1-2-3", [(0, 1), (1, 2), (2, 3)]),
                  ("disconnected 0-1 | 2-3", [(0, 1), (2, 3)])]:
    bad = [S for S in SUBSETS
           if S not in (frozenset(), frozenset(range(n)))
           and len(cut_edges(S, ed)) == 0]
    print(f"    {label:24s} proper non-empty S with empty cut: {len(bad)}")
print("  On a connected graph every proper non-empty S has a non-empty cut;")
print("  on a disconnected graph it does not. C3 is what makes the")
print("  pulsation OBSERVABLE.")
print()


# ============================================================
# PART 4 -- Recovering the 1+3+4 orbit structure of D60
# ============================================================
print("PART 4 -- Cut sizes reproduce the S4-orbit structure of D60")
print("-" * 64)

s0 = tuple([1] * len(edges))          # the all-plus reference
by_cutsize = {}
for S in SUBSETS:
    by_cutsize.setdefault(min(len(S), n - len(S)), set()).add(
        switch(S, s0, edges))

for k in sorted(by_cutsize):
    print(f"  cut type {k}|{n - k}: {len(by_cutsize[k])} distinct configurations")

sizes = sorted(len(v) for v in by_cutsize.values())
print(f"  Multiset of class sizes: {sizes}")
print(f"  D60 S4-orbit sizes:      [1, 3, 4]")
print(f"  CHECK: match = {sizes == [1, 3, 4]}")
print()

# Klein group of even cuts under symmetric difference
even_cuts = [S for S in SUBSETS if len(S) == 2] + [frozenset()]
closed = all((A ^ B) in [frozenset(c) for c in
                         [tuple(sorted(x)) for x in
                          [set(a) for a in even_cuts]]] or
             (A ^ B) in even_cuts or
             (A ^ B) == frozenset(range(n))
             for A in even_cuts for B in even_cuts)
print(f"  Three 2|2 cuts + empty cut, closed under symmetric difference")
print(f"  (modulo the trivial element V): {closed}")
print("  CANDIDATE IDENTIFICATION (not yet established): this Klein group")
print("  is the V4 of D60 and carries the three real axes of D66.")
print("  STATUS: to be proved or refuted; NOT claimed here.")
print()


# ============================================================
# PART 5 -- The three regimes
# ============================================================
print("PART 5 -- Regime test: which flipping law satisfies C1?")
print("-" * 64)

BASE = vertex_induced((1, 1, 1, 1), edges)   # all-plus ground reference


def flip_set(t, periods):
    """Entities that have flipped an odd number of times by step t."""
    return frozenset(i for i, p in enumerate(periods)
                     if (t // p) % 2 == 1)


def relational_sequence(periods, T):
    return [switch(flip_set(t, periods), BASE, edges) for t in range(T)]


def exact_period(seq):
    L = len(seq)
    for T in range(1, L // 2 + 1):
        if all(seq[t] == seq[t + T] for t in range(L - T)):
            return T
    return None


PMAX = 4
HORIZON = 2 * 3 * 4 * 4      # comfortably above lcm of all periods used

print("  (a) H_sync -- every entity flips at every cycle, p = (1,1,1,1):")
seq = relational_sequence((1, 1, 1, 1), HORIZON)
print(f"      distinct relational states visited: {len(set(seq))}")
print(f"      exact period: {exact_period(seq)}")
print(f"      C1-compliant (period 2 AND non-constant): "
      f"{exact_period(seq) == 2 and len(set(seq)) > 1}")
print()

print("  (b) H_uniform -- all entities share one period p:")
for p in range(1, 7):
    seq = relational_sequence((p, p, p, p), HORIZON)
    print(f"      p = {p}: distinct states = {len(set(seq))}, "
          f"period = {exact_period(seq)}")
print()

print("  (c) H_hetero -- exhaustive over all assignments in {1,..,%d}^4:" % PMAX)
compliant, tally = [], {}
for periods in itertools.product(range(1, PMAX + 1), repeat=n):
    seq = relational_sequence(periods, HORIZON)
    T = exact_period(seq)
    nstates = len(set(seq))
    tally[(T, nstates > 1)] = tally.get((T, nstates > 1), 0) + 1
    if T == 2 and nstates > 1:
        compliant.append(periods)

print(f"      total assignments tested: {PMAX ** n}")
for key in sorted(tally, key=lambda z: (z[0] is None, z[0], z[1])):
    T, nz = key
    print(f"      period {str(T):>4s}, non-constant={nz}: {tally[key]:4d}")
print(f"      C1-COMPLIANT assignments (period exactly 2, non-constant): "
      f"{len(compliant)}")
for periods in compliant[:24]:
    print(f"        p = {periods}")
if len(compliant) > 24:
    print(f"        ... and {len(compliant) - 24} more")
print()

print("  (d) H_random -- flip set drawn uniformly at random each cycle:")
random.seed(20260810)
TRIALS, RT = 20000, 12
hits = 0
for _ in range(TRIALS):
    seq, cur = [], BASE
    for _t in range(RT):
        seq.append(cur)
        S = frozenset(i for i in range(n) if random.getrandbits(1))
        cur = switch(S, cur, edges)
    T = exact_period(seq)
    if T == 2 and len(set(seq)) > 1:
        hits += 1
print(f"      trials: {TRIALS}, horizon: {RT}")
print(f"      sequences with exact period 2 and non-constant: {hits}")
print(f"      empirical fraction: {hits / TRIALS:.6f}")
print()

print("=" * 64)
print("SUMMARY OF WHAT THIS SCRIPT DECIDES")
print("=" * 64)
print("  1. C2 forces the relational state to be a bipartition (Part 1).")
print("  2. Any FIXED subset S gives an exact 2-cycle (Part 2).")
print("  3. Universal simultaneous inversion is the identity, hence a")
print("     fixed point, hence excluded by C1 -- it is empty, not wrong.")
print("     C3 is what guarantees a proper S has observable effect (Part 3).")
print("  4. The 1+3+4 orbit structure of D60 is a statement about cut")
print("     sizes (Part 4). The Klein-group identification is a CANDIDATE.")
print("  5. Which regular regimes survive C1 is decided in Part 5(c);")
print("     the random regime is quantified in Part 5(d).")
print("=" * 64)
