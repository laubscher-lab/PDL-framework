# PDL_rule_P_script9b.py
# ============================================================
# Rule P on cycles: closed-form counts for minimisers and orbits
#
# REPLACES PDL_rule_P_script9.py, whose PART 2 and PART 4 were
# intractable. Two design faults are acknowledged: the orbit
# routine rebuilt each orbit by scanning the whole automorphism
# group (quadratic, with a discard() patch masking a logic bug),
# and PART 4 computed a canonical form over all n! permutations
# per graph. Both are replaced here by closed formulas, verified
# against brute force on the range where brute force is cheap.
#
# Standalone graph theory. No corpus reference.
#
# DEFINITION (Rule P)
#   G = (V,E), x : V -> {+1,-1}. same(v) = #{w ~ v : x_w = x_v},
#   M(x) = max_v same(v). P selects the x minimising M. P is
#   invariant under the global inversion x -> -x.
#
# WHAT THE PARTIAL RUN OF script9 ESTABLISHED (data supplied by
# the author, C_5..C_12):
#     n :  5   6   7   8   9  10  11  12
#   minM:  1   0   1   0   1   0   1   0
#   mins:  5   1  14   1  39   1  99   1     (up to inversion)
#   orbs:  1   1   2   1   4   1   7   1
#   |Aut| = 2n throughout, growing 10 -> 24 while the orbit count
#   jumps 1,2,4,7. Orbit count therefore does NOT track |Aut|:
#   hypothesis (H-aut) is REFUTED. Every odd cycle from 7 onward
#   shows several orbits and every even cycle exactly one:
#   hypothesis (H-par) is CONFIRMED. C_7 is not an accident but
#   the first member of a family.
#
# THE STRUCTURE THEOREM CONJECTURED HERE
#   On C_n every vertex has exactly two neighbours, so
#   same(v) in {0,1,2}, and same(v) = 2 exactly when v lies in the
#   interior of a maximal run of >= 3 equal states. Hence
#       M(x) <= 1  <=>  every maximal run has length 1 or 2.
#   For n even, the strictly alternating state gives M = 0 and is
#   unique up to inversion. For n odd, M = 0 is impossible (an odd
#   cycle is not bipartite), so min M = 1 and the minimisers are
#   exactly the states whose runs all have length 1 or 2.
#
# THE TWO CLOSED FORMULAS
#   Write a minimiser as a cyclic sequence of k maximal runs with
#   sizes in {1,2} summing to n. Signs alternate from run to run,
#   so k must be EVEN. With j = n - k runs of size 2:
#
#     (F1)  minimisers up to inversion:
#             N(n) = sum over even k of (n/k) * C(k, n-k)
#
#     (F2)  orbits under Aut(C_n) = D_n, together with inversion:
#             O(n) = sum over even k of B(k, n-k)
#           where B(k,j) is the number of binary BRACELETS of
#           length k with j beads of one colour (necklaces up to
#           rotation AND reflection).
#
#   Hand check against the author's data:
#     n=7:  k=4 -> (7/4)C(4,3)=7 ; k=6 -> (7/6)C(6,1)=7 ; N=14  OK
#           k=4 -> B(4,3)=1 ; k=6 -> B(6,1)=1 ; O=2            OK
#     n=9:  k=6 -> (9/6)C(6,3)=30 ; k=8 -> (9/8)C(8,1)=9 ; N=39 OK
#           k=6 -> B(6,3)=3 ; k=8 -> B(8,1)=1 ; O=4            OK
#     n=11: 11 + 77 + 11 = 99                                  OK
#           B(6,5)+B(8,3)+B(10,1) = 1+5+1 = 7                  OK
#
#   PART 1 verifies both formulas by brute force for n <= 15.
#   PART 3 then extends them to n = 31 at no cost.
#
# Bracelets are counted by Burnside over the dihedral group, with
# fixed colourings per group element obtained by dynamic
# programming over the cycle structure -- never by enumerating
# subsets, which is what made the previous script intractable.
#
# Exact integer arithmetic. Standard library only.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from math import comb, gcd

print("=" * 70)
print("PDL_rule_P_script9b.py -- closed-form counts for rule P on cycles")
print("=" * 70)
print()


# ============================================================
# Brute force (cheap range only)
# ============================================================

def M_cycle(x):
    n = len(x)
    return max(sum(1 for w in ((i - 1) % n, (i + 1) % n) if x[w] == x[i])
               for i in range(n))


def dihedral(n):
    perms = []
    for r in range(n):
        perms.append(tuple((i + r) % n for i in range(n)))
    for r in range(n):
        perms.append(tuple((r - i) % n for i in range(n)))
    return perms


def brute(n):
    best, arg = None, []
    for x in itertools.product((1, -1), repeat=n):
        m = M_cycle(x)
        if best is None or m < best:
            best, arg = m, [x]
        elif m == best:
            arg.append(x)
    perms = dihedral(n)
    canon = set()
    for x in arg:
        forms = []
        for p in perms:
            y = tuple(x[p[i]] for i in range(n))
            forms.append(y)
            forms.append(tuple(-v for v in y))
        canon.add(min(forms))
    mod_inv = {min(x, tuple(-v for v in x)) for x in arg}
    return best, len(mod_inv), len(canon)


def runs_ok(x):
    """every maximal cyclic run has length <= 2"""
    n = len(x)
    if len(set(x)) == 1:
        return n <= 2
    start = next(i for i in range(n) if x[i] != x[(i - 1) % n])
    L, cur = 1, x[start]
    for t in range(1, n):
        v = x[(start + t) % n]
        if v == cur:
            L += 1
            if L > 2:
                return False
        else:
            L, cur = 1, v
    return True


# ============================================================
# Closed formulas
# ============================================================

def N_closed(n):
    """(F1) minimisers up to inversion."""
    if n % 2 == 0:
        return 1
    tot = 0
    for k in range(2, n + 1, 2):
        j = n - k
        if 0 <= j <= k:
            assert (n * comb(k, j)) % k == 0
            tot += n * comb(k, j) // k
    return tot


def euler_phi(m):
    r, p = m, 2
    res = m
    tmp = m
    primes = []
    while p * p <= tmp:
        if tmp % p == 0:
            primes.append(p)
            while tmp % p == 0:
                tmp //= p
        p += 1
    if tmp > 1:
        primes.append(tmp)
    for q in primes:
        res -= res // q
    return res


def fixed_with_j_ones(cycle_lengths, j):
    """Colourings constant on each cycle, with exactly j ones."""
    dp = [0] * (j + 1)
    dp[0] = 1
    for L in cycle_lengths:
        nd = [0] * (j + 1)
        for c in range(j + 1):
            if dp[c] == 0:
                continue
            nd[c] += dp[c]                  # colour 0
            if c + L <= j:
                nd[c + L] += dp[c]          # colour 1
        dp = nd
    return dp[j]


def cycles_of(perm):
    n = len(perm)
    seen, out = [False] * n, []
    for s in range(n):
        if seen[s]:
            continue
        L, i = 0, s
        while not seen[i]:
            seen[i] = True
            i = perm[i]
            L += 1
        out.append(L)
    return out


def bracelets(k, j):
    """Binary bracelets, length k, j beads of one colour (Burnside)."""
    if k == 0:
        return 1 if j == 0 else 0
    if j < 0 or j > k:
        return 0
    total = 0
    for p in dihedral(k):
        total += fixed_with_j_ones(cycles_of(p), j)
    assert total % (2 * k) == 0
    return total // (2 * k)


def O_closed(n):
    """(F2) orbits under D_n together with inversion."""
    if n % 2 == 0:
        return 1
    return sum(bracelets(k, n - k)
               for k in range(2, n + 1, 2) if 0 <= n - k <= k)


# ============================================================
# PART 1 -- Verify both formulas against brute force
# ============================================================
print("PART 1 -- Brute-force verification, n = 3..15")
print("-" * 70)
print(f"  {'n':>3s} {'minM':>5s} {'mins BF':>8s} {'N(n)':>8s} {'ok':>4s} "
      f"{'orbits BF':>10s} {'O(n)':>6s} {'ok':>4s} {'runs<=2 ok':>11s}")

ok_all = True
for n in range(3, 16):
    best, nmin, norb = brute(n)
    Nc, Oc = N_closed(n), O_closed(n)
    # structural check: minimisers are exactly the all-runs<=2 states
    mins = [x for x in itertools.product((1, -1), repeat=n)
            if M_cycle(x) == best]
    struct = (all(runs_ok(x) for x in mins) if best <= 1 else None)
    a, b = (nmin == Nc), (norb == Oc)
    ok_all &= a and b
    print(f"  {n:3d} {best:5d} {nmin:8d} {Nc:8d} {str(a):>4s} "
          f"{norb:10d} {Oc:6d} {str(b):>4s} {str(struct):>11s}")
print()
print(f"  ALL FORMULAS VERIFIED: {ok_all}")
print()


# ============================================================
# PART 2 -- The two hypotheses
# ============================================================
print("PART 2 -- (H-par) versus (H-aut)")
print("-" * 70)
print(f"  {'n':>3s} {'parity':>7s} {'|Aut| = 2n':>11s} {'orbits':>7s}")
for n in range(5, 16):
    print(f"  {n:3d} {'odd' if n % 2 else 'even':>7s} {2*n:11d} "
          f"{O_closed(n):7d}")
print()
print("  |Aut| grows strictly and linearly; the orbit count is 1 for every")
print("  even n and grows irregularly for odd n. Orbit count therefore does")
print("  not track automorphism strength.")
print("    (H-aut) automorphism strength  : REFUTED")
print("    (H-par) parity of the cycle    : CONFIRMED on this family")
print()
print("  C_7 is the first member of a family, not an accident. The cause")
print("  is that an odd cycle is not bipartite, so M = 0 is unreachable")
print("  and the minimum at M = 1 is attained by many inequivalent")
print("  run-structures.")
print()


# ============================================================
# PART 3 -- Extension to n = 31
# ============================================================
print("PART 3 -- Closed formulas extended to n = 31")
print("-" * 70)
print(f"  {'n':>3s} {'min M':>6s} {'minimisers N(n)':>16s} {'orbits O(n)':>12s}")
for n in range(5, 32):
    print(f"  {n:3d} {0 if n % 2 == 0 else 1:6d} {N_closed(n):16d} "
          f"{O_closed(n):12d}")
print()
print("  Odd-n sequences, for identification against OEIS:")
print("    N: " + ", ".join(str(N_closed(n)) for n in range(5, 32, 2)))
print("    O: " + ", ".join(str(O_closed(n)) for n in range(5, 32, 2)))
print()
print("  N(n) for odd n is the Lucas number L(n) minus a correction;")
print("  the script does NOT assert this -- the sequences are printed so")
print("  that the identification can be made or refuted independently.")
lucas = [2, 1]
for _ in range(40):
    lucas.append(lucas[-1] + lucas[-2])
print("    Lucas L(n) for the same n: "
      + ", ".join(str(lucas[n]) for n in range(5, 32, 2)))
print("    N(n) - L(n): "
      + ", ".join(str(N_closed(n) - lucas[n]) for n in range(5, 32, 2)))
print()


# ============================================================
# PART 4 -- Even cycles: why uniqueness is forced
# ============================================================
print("PART 4 -- Even cycles: uniqueness, stated and checked")
print("-" * 70)
print("  For n even the strictly alternating state gives same(v) = 0 at")
print("  every vertex, so M = 0, the least possible value. Any other")
print("  state has two adjacent equal entries somewhere, hence some")
print("  vertex with same(v) >= 1. The minimiser is therefore unique up")
print("  to inversion, and its orbit count is 1.")
print()
for n in range(4, 17, 2):
    best, nmin, norb = brute(n) if n <= 15 else (0, 1, 1)
    tag = "" if n <= 15 else "  (by the argument above)"
    print(f"    C_{n:<3d} min M = {best}, minimisers = {nmin}, "
          f"orbits = {norb}{tag}")
print()

print("=" * 70)
print("WHAT THIS SCRIPT ESTABLISHES")
print("=" * 70)
print("  1. On C_n, min M = 0 for n even and 1 for n odd, and the")
print("     minimisers are exactly the states all of whose maximal runs")
print("     have length 1 or 2 (verified n <= 15).")
print("  2. Two closed formulas, (F1) for the number of minimisers up to")
print("     inversion and (F2) for the number of orbits, both verified")
print("     against brute force for n <= 15 and extended to n = 31.")
print("  3. (H-aut) is refuted and (H-par) confirmed on this family.")
print()
print("  NOT established: whether (H-par) explains multi-orbit behaviour")
print("  on graphs OTHER than cycles. The exhaustive sweep over all")
print("  connected graphs, which was intractable as written, is left")
print("  open and needs a genuine isomorphism test rather than a")
print("  canonical form computed over all n! permutations.")
print("=" * 70)
