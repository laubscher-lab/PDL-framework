# PDL_pulsation_regimes_script2.py
# ============================================================
# Verification script -- Phase, not period: which pulsation laws
# satisfy C1?
# PDL Framework -- preliminary to a possible document D68
#
# CONTEXT:
#   Script 1 established (all PASSED):
#     - C2 <=> the relational state is a bipartition of entities;
#     - switching by ANY fixed subset S preserves C2 and is an
#       involution, hence generates an exact logical 2-cycle;
#     - S = V (universal simultaneous inversion) acts as the
#       identity: it is the trivial element, a fixed point,
#       excluded by C1;
#     - random flip sets: 0 / 20000 give period 2;
#     - heterogeneous FINITE periods p_i in {1,..,4}: 0 / 256 give
#       period 2. Period 2 is entirely absent from the spectrum
#       (observed: 1, 3, 4, 8, 12, 24).
#
#   Script 1 therefore CONTRADICTED ITSELF: Part 2 proves 2-cycles
#   exist, Part 5 found none. Diagnosed cause: the parametrisation
#   "entity i flips at t = 0 mod p_i" admits neither p_i = infinity
#   (an entity that never flips) nor a PHASE OFFSET. Both are
#   restored here.
#
# CLAIM UNDER TEST (hand-derived, NOT yet established):
#   The C1-compliant regime is: every entity has the SAME period 2,
#   entities differing only by a phase offset phi_i in {0,1}. The
#   two phase classes A, B partition V; the relational sequence is
#   trivial / delta(B) / trivial / delta(B) / ..., of exact period 2.
#   At t = 2 every entity has flipped exactly once: the vertex
#   pattern is fully inverted, and that full inversion is
#   relationally the identity.
#
# SUBSIDIARY CLAIMS TESTED:
#   (S1) The regime "S flips every cycle, V\S never" and the regime
#        "uniform period 2, two phase classes A = S" generate the
#        IDENTICAL relational sequence.
#   (S2) For every C1-compliant law, each entity flips exactly once
#        per relational cycle.
#   (S3) The observed coherent configuration at odd t is the
#        vertex-induced configuration whose bipartition IS the phase
#        bipartition.
#   (S4) The result is not specific to n = 4: tested for n = 3..6.
#
# FLIP LAW (general form):
#   Entity i is characterised by (p_i, phi_i). It flips at every
#   time s >= 1 with s = phi_i (mod p_i). p_i = None means "never
#   flips". Cumulative parity: F_t = {i : (number of flips of i in
#   [1,t]) is odd}. Relational state: s_t = switch(F_t, s_0).
#   Note switch(F) = switch(V \ F): only the cut matters.
#
# All arithmetic is exact integer arithmetic. No floating point.
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

print("=" * 66)
print("PDL_pulsation_regimes_script2.py")
print("Phase, not period: which pulsation laws satisfy C1?")
print("=" * 66)
print()


# ============================================================
# Machinery (repeated in full; no dependency on script 1)
# ============================================================

def edges_complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def triangles_complete(n):
    return list(combinations(range(n), 3))


def is_coherent(s, edges, tris):
    idx = {e: k for k, e in enumerate(edges)}

    def eid(a, b):
        return idx[(a, b)] if a < b else idx[(b, a)]

    return all(s[eid(a, b)] * s[eid(a, c)] * s[eid(b, c)] == 1
               for (a, b, c) in tris)


def vertex_induced(x, edges):
    return tuple(x[i] * x[j] for (i, j) in edges)


def switch(S, s, edges):
    return tuple(-v if ((i in S) != (j in S)) else v
                 for v, (i, j) in zip(s, edges))


def flips_by(t, p, phi):
    """Number of flips of an entity (p, phi) in the interval [1, t]."""
    if p is None:
        return 0
    return sum(1 for u in range(1, t + 1) if u % p == phi % p)


def parity_set(t, law):
    """F_t: entities having flipped an odd number of times by time t."""
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


def compliant(seq):
    """C1: exact period 2 AND not a fixed point."""
    return exact_period(seq) == 2 and len(set(seq)) > 1


# ============================================================
# PART 1 -- Closing the gap of script 1: p_i = None restored
# ============================================================
print("PART 1 -- Restoring p_i = None (an entity that never flips)")
print("-" * 66)

n = 4
edges = edges_complete(n)
tris = triangles_complete(n)
S0 = vertex_induced(tuple([1] * n), edges)
HORIZON = 48

found = []
for mask in range(2 ** n):
    S = frozenset(i for i in range(n) if (mask >> i) & 1)
    law = tuple((1, 0) if i in S else (None, 0) for i in range(n))
    seq = sequence(law, S0, edges, HORIZON)
    if compliant(seq):
        found.append(S)

print(f"  Laws of the form 'S flips every cycle, V\\S never': {2 ** n} tested")
print(f"  C1-compliant among them: {len(found)}")
print(f"  Subsets S found: {sorted(sorted(S) for S in found)}")
print(f"  CHECK: exactly the proper non-empty subsets "
      f"({2 ** n - 2} expected): {len(found) == 2 ** n - 2}")
print()
print("  This closes the contradiction of script 1: 2-cycles DO exist")
print("  in the flip-law family; script 1 excluded them by construction.")
print()


# ============================================================
# PART 2 -- Exhaustive search over (period, phase)
# ============================================================
print("PART 2 -- Exhaustive search over laws (p_i, phi_i), p_i in {None,1..6}")
print("-" * 66)

PMAX = 6
CHOICES = [(None, 0)] + [(p, phi) for p in range(1, PMAX + 1)
                         for phi in range(p)]
print(f"  Distinct (p, phi) options per entity: {len(CHOICES)}")
print(f"  Total laws to test on n = {n}: {len(CHOICES) ** n}")

HORIZON2 = 2 * 3 * 4 * 5 * 6 // 6 * 2   # 240; comfortably > 2*lcm(1..6)
HORIZON2 = 260

good, spectrum = [], {}
for law in itertools.product(CHOICES, repeat=n):
    seq = sequence(law, S0, edges, HORIZON2)
    T = exact_period(seq)
    key = (T, len(set(seq)) > 1)
    spectrum[key] = spectrum.get(key, 0) + 1
    if T == 2 and len(set(seq)) > 1:
        good.append(law)

print(f"  C1-COMPLIANT laws (exact period 2, non-constant): {len(good)}")
print()
print("  Period spectrum (period, non-constant) -> count:")
for key in sorted(spectrum, key=lambda z: (z[0] is None, z[0] or 0, z[1])):
    print(f"    {str(key[0]):>5s}, non-constant={str(key[1]):5s}: "
          f"{spectrum[key]:6d}")
print()


# ============================================================
# PART 3 -- Structure of the compliant laws
# ============================================================
print("PART 3 -- What do the C1-compliant laws look like?")
print("-" * 66)

periods_used = {}
for law in good:
    key = tuple(sorted(set(p for (p, _) in law), key=lambda z: (z is None, z)))
    periods_used[key] = periods_used.get(key, 0) + 1

print("  Multiset of period values appearing in compliant laws:")
for key in sorted(periods_used, key=str):
    print(f"    periods {str(key):28s}: {periods_used[key]:5d} laws")
print()

uniform2 = [law for law in good if all(p == 2 for (p, _) in law)]
mixed1none = [law for law in good
              if all(p in (1, None) for (p, _) in law)]
print(f"  Compliant laws with UNIFORM period 2 (all entities identical")
print(f"  in nature, differing only by phase): {len(uniform2)}")
print(f"  Compliant laws of the degenerate type p in {{1, None}}: "
      f"{len(mixed1none)}")
print(f"  Compliant laws that are NEITHER of these two types: "
      f"{len(good) - len(uniform2) - len(mixed1none)}")
print()

if uniform2:
    print("  Phase-class structure of the uniform-period-2 laws:")
    shapes = {}
    for law in uniform2:
        A = frozenset(i for i, (_, phi) in enumerate(law) if phi == 0)
        shapes[(len(A), n - len(A))] = shapes.get((len(A), n - len(A)), 0) + 1
    for key in sorted(shapes):
        print(f"    phase split {key[0]}|{key[1]}: {shapes[key]} laws")
    print("  CHECK: no compliant uniform-period-2 law has an empty phase")
    print(f"  class: {all(0 < k[0] < n for k in shapes)}")
print()


# ============================================================
# PART 4 -- Subsidiary claims S1, S2, S3
# ============================================================
print("PART 4 -- Subsidiary claims")
print("-" * 66)

# (S1) equivalence of the two descriptions
print("  (S1) 'S flips every cycle, rest never'  ==  'uniform period 2,")
print("       phase class A = S'  as relational sequences:")
s1_ok, s1_tested = True, 0
for mask in range(1, 2 ** n - 1):
    S = frozenset(i for i in range(n) if (mask >> i) & 1)
    lawA = tuple((1, 0) if i in S else (None, 0) for i in range(n))
    lawB = tuple((2, 0) if i in S else (2, 1) for i in range(n))
    seqA = sequence(lawA, S0, edges, HORIZON)
    seqB = sequence(lawB, S0, edges, HORIZON)
    s1_tested += 1
    if seqA != seqB:
        s1_ok = False
        print(f"       MISMATCH for S = {sorted(S)}")
print(f"       {s1_tested} proper non-empty subsets tested; identical: {s1_ok}")
print()

# (S2) each entity flips exactly once per relational cycle
print("  (S2) In a compliant uniform-period-2 law, each entity flips")
print("       exactly once over one full relational cycle (t = 0 -> 2):")
s2_ok = True
for law in uniform2:
    counts = [flips_by(2, p, phi) for (p, phi) in law]
    if any(c != 1 for c in counts):
        s2_ok = False
        print(f"       COUNTEREXAMPLE law={law} counts={counts}")
        break
print(f"       verified over {len(uniform2)} compliant laws: {s2_ok}")
print()

# (S3) the observed configuration's bipartition IS the phase bipartition
print("  (S3) The coherent configuration observed at odd t is the")
print("       vertex-induced configuration of the phase bipartition:")
s3_ok, s3_tested = True, 0
for law in uniform2:
    A = frozenset(i for i, (_, phi) in enumerate(law) if phi == 0)
    observed = sequence(law, S0, edges, 4)[1]
    x = tuple(-1 if i in A else 1 for i in range(n))
    predicted = vertex_induced(x, edges)
    s3_tested += 1
    if observed != predicted and observed != vertex_induced(
            tuple(-v for v in x), edges):
        s3_ok = False
        print(f"       MISMATCH law={law}")
        break
    if not is_coherent(observed, edges, tris):
        s3_ok = False
        print(f"       NOT COHERENT law={law}")
        break
print(f"       verified over {s3_tested} compliant laws: {s3_ok}")
print()


# ============================================================
# PART 5 -- Is the result specific to n = 4?
# ============================================================
print("PART 5 -- Independence from n (tested for n = 3, 4, 5, 6)")
print("-" * 66)
print("  Reduced option set (p in {None, 1, 2, 3}) to keep the search finite.")

CHOICES_S = [(None, 0)] + [(p, phi) for p in range(1, 4) for phi in range(p)]
for nn in range(3, 7):
    ed = edges_complete(nn)
    tr = triangles_complete(nn)
    s0 = vertex_induced(tuple([1] * nn), ed)
    tot, comp, unif = 0, 0, 0
    for law in itertools.product(CHOICES_S, repeat=nn):
        tot += 1
        seq = sequence(law, s0, ed, 60)
        if exact_period(seq) == 2 and len(set(seq)) > 1:
            comp += 1
            if all(p == 2 for (p, _) in law):
                unif += 1
    print(f"    n = {nn}: laws tested = {tot:7d}, C1-compliant = {comp:6d}, "
          f"of which uniform period 2 = {unif:5d}")
print()

print("=" * 66)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 66)
print("  Part 1 closes the self-contradiction of script 1.")
print("  Part 2 gives the exhaustive list of C1-compliant pulsation laws.")
print("  Part 3 tests whether 'uniform period 2 + heterogeneous phase' is")
print("         among them, and whether any OTHER structural type occurs.")
print("  Part 4 tests the three subsidiary claims S1, S2, S3.")
print("  Part 5 tests independence from the number of entities.")
print()
print("  If Part 3 reports compliant laws of a type that is neither")
print("  uniform-period-2 nor the degenerate {1, None} family, the")
print("  hand-derived claim is INCOMPLETE and must be restated.")
print("=" * 66)
