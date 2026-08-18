# PDL_rule_P_script11.py
# ============================================================
# Rule P on the structures that matter: cores, sea, interface
#
# ############################################################
# TERMINOLOGY (corpus rule, non-negotiable)
#   K_4 in the literal sense (Coh(K_4) = Z_2^3 : V_4, D61) denotes
#   the ELECTRON closure only. Valence cores are written K_24 and
#   K_28 and are complete graphs on 24 and 28 ENTITIES (confirmed
#   by the author: there are no K_4 blocks inside them). Composite
#   nucleon-level closures are written K_nuc and are not treated
#   here.
# ############################################################
#
# DEFINITION (Rule P)
#   x : V -> {+1,-1};  same(v) = #{w ~ v : x_w = x_v};
#   M(x) = max_v same(v);  P selects the x minimising M.
#   P is invariant under the global inversion x -> -x. It is LOCAL
#   and MINIMAX, and -- established in scripts 8/9b -- it is NOT
#   invariant under switching, so it sees exactly what every
#   switching-invariant functional is blind to.
#
# TWO FACTS DERIVED BY HAND BEFORE ANY COMPUTATION, both tested
# in PART 2 below:
#
#   (E) EULER FORBIDS a 4-regular quadrangulation of the sphere.
#       With E = 2V (4-regular) and F = E/2 = V (quadrangular),
#       V - E + F = V - 2V + V = 0, not 2. Such a mesh exists on
#       the TORUS (chi = 0), not on S^2. The mean degree 3.961
#       reported by the D43 simulation is therefore consistent with
#       boundary or holes, not with strict 4-regularity.
#
#   (B) EVERY QUADRANGULATION OF THE SPHERE IS BIPARTITE (all faces
#       even + planar => bipartite). Combined with the theorem
#       established in this session --- for connected G,
#       min M = 0 <=> G bipartite, and the minimiser is then unique
#       up to inversion --- a purely quadrangular sea would be
#       RIGID under rule P: exactly one ground state.
#
# THE REVERSAL THIS IMPLIES, and the question it raises
#   Throughout this session the working picture was: cores
#   stationary, sea dynamic. Rule P suggests the opposite. A
#   bipartite sea has a UNIQUE minimiser; the cores, being complete
#   graphs of odd degree (23 and 27), have min M = 11 and 13 with
#   C(24,12)/2 = 1 352 078 and C(28,14)/2 = 20 058 300 minimisers
#   respectively. The degeneracy would sit in the CORES, not in the
#   sea.
#
#   Unless the sea carries odd cycles. The three valence holes are
#   exactly where odd cycles could enter a quadrangulation. PART 3
#   tests this on torus grids C_a x C_b, which are 4-regular and
#   quadrangular, and which are bipartite iff BOTH a and b are even.
#
# WHAT PART 4 ACTUALLY DECIDES
#   The interface question, posed so that it can fail. Join a core
#   proxy to a sea proxy by three edges from one outward vertex and
#   compute rule P on the JOINT graph. Then ask whether a joint
#   minimiser restricts to a minimiser of each part. If it does,
#   the two regimes coexist without tension and there is no motor.
#   If it does not, the junction forces at least one side away from
#   its own optimum, and the cost of that compromise is measurable.
#   Both outcomes are informative; neither is assumed.
#
# Exact integer arithmetic. Standard library only. Bit-parallel
# evaluation of same(v) via popcount on adjacency masks.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
from math import comb

print("=" * 72)
print("PDL_rule_P_script11.py -- rule P on cores, sea, and interface")
print("=" * 72)
print()

try:
    (1).bit_count()
    pc = lambda z: z.bit_count()
except AttributeError:
    pc = lambda z: bin(z).count("1")


# ============================================================
# Machinery
# ============================================================

def adj_masks(n, edges):
    adj = [0] * n
    for (u, v) in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def M_of(x, adj, n, full):
    """x is a bitmask: bit set = state +1. Returns max_v same(v)."""
    nx = full ^ x
    best = 0
    for v in range(n):
        s = pc(adj[v] & (x if (x >> v) & 1 else nx))
        if s > best:
            best = s
    return best


def scan(n, edges, collect=True):
    adj = adj_masks(n, edges)
    full = (1 << n) - 1
    best, arg = None, []
    for x in range(1 << n):
        m = M_of(x, adj, n, full)
        if best is None or m < best:
            best, arg = m, ([x] if collect else [])
        elif m == best and collect:
            arg.append(x)
    reps = {min(a, full ^ a) for a in arg}
    return best, len(arg), reps, adj


def is_bipartite(n, adj):
    col = [-1] * n
    for s in range(n):
        if col[s] != -1:
            continue
        col[s] = 0
        st = [s]
        while st:
            v = st.pop()
            nb = adj[v]
            while nb:
                b = nb & -nb
                w = b.bit_length() - 1
                nb ^= b
                if col[w] == -1:
                    col[w] = 1 - col[v]
                    st.append(w)
                elif col[w] == col[v]:
                    return False
    return True


def complete(n, offset=0):
    return [(offset + i, offset + j)
            for i in range(n) for j in range(i + 1, n)]


def torus(a, b, offset=0):
    idx = lambda i, j: offset + (i % a) * b + (j % b)
    e = set()
    for i in range(a):
        for j in range(b):
            e.add(tuple(sorted((idx(i, j), idx(i, j + 1)))))
            e.add(tuple(sorted((idx(i, j), idx(i + 1, j)))))
    return sorted(e)


# ============================================================
# PART 1 -- The valence cores under rule P
# ============================================================
print("PART 1 -- Cores K_24 and K_28 (complete graphs on entities)")
print("-" * 72)
print("  On K_n every vertex has n-1 neighbours. At a split k | n-k a")
print("  vertex of the k-side has k-1 same-state and n-k opposite-state")
print("  neighbours, so max_v same(v) = max(k,n-k) - 1, minimal at the")
print("  balanced split. Hence min M = ceil(n/2) - 1.")
print()
print(f"  {'n':>4s} {'deg':>4s} {'min M':>6s} {'same':>5s} {'opp':>4s} "
      f"{'gap':>4s} {'gap=0?':>7s} {'minimisers (mod inv)':>21s}")
for n in (4, 6, 8, 10, 24, 28):
    deg = n - 1
    k = n // 2
    same, opp = k - 1, n - k
    mins = comb(n, k) // 2 if n % 2 == 0 else comb(n, k)
    print(f"  {n:4d} {deg:4d} {max(k, n-k)-1:6d} {same:5d} {opp:4d} "
          f"{abs(same-opp):4d} {str(deg % 2 == 0):>7s} {mins:21d}")
print()
print("  Brute-force check on the small cases:")
for n in (4, 6, 8):
    best, cnt, reps, adj = scan(n, complete(n))
    print(f"    K_{n}: min M = {best} (predicted {n//2 - 1}), "
          f"minimisers mod inversion = {len(reps)} "
          f"(predicted {comb(n, n//2)//2})")
print()
print("  K_24: 23 neighbours, 11 same / 12 opposite, gap 1 -- ODD degree,")
print("        so the gap can never be 0.")
print("  K_28: 27 neighbours, 13 same / 14 opposite, gap 1 -- likewise.")
print("  All balanced splits are equivalent under Aut(K_n) = S_n, so the")
print("  minimisers form a SINGLE orbit, but an enormous one:")
print(f"        K_24: {comb(24,12)//2:,} minimisers")
print(f"        K_28: {comb(28,14)//2:,} minimisers")
print("  Rule P therefore fixes the SHAPE of the core state (balanced)")
print("  and leaves its labelling entirely free.")
print()


# ============================================================
# PART 2 -- Euler, and the bipartite rigidity of a quad sea
# ============================================================
print("PART 2 -- Can the sea be a 4-regular quadrangulation, and where?")
print("-" * 72)
print("  Euler: V - E + F = chi. For 4-regular, E = 2V; for quadrangular,")
print("  F = E/2 = V. Then V - E + F = 0 identically, so chi must be 0.")
print()
print(f"  {'surface':>12s} {'chi':>4s} {'4-reg quadrangulation possible?':>34s}")
for name, chi in (("sphere S^2", 2), ("torus T^2", 0),
                  ("genus 2", -2), ("sphere, 3 holes", -1)):
    print(f"  {name:>12s} {chi:4d} {str(chi == 0):>34s}")
print()
print("  So a strictly 4-regular quadrangular sea cannot close on a")
print("  sphere. The D43 simulation's mean degree 3.961 (V=5144,")
print("  E=10188) is consistent with boundary effects and the three")
print("  valence holes, not with exact 4-regularity.")
print(f"    check: 2*10188/5144 = {2*10188/5144:.6f}")
print()
print("  Every quadrangulation of S^2 is bipartite (even faces + planar).")
print("  Combined with the theorem of this session -- min M = 0 <=> ")
print("  bipartite, minimiser then unique up to inversion -- a purely")
print("  quadrangular sea is RIGID under rule P.")
print()


# ============================================================
# PART 3 -- Sea proxies: torus grids, bipartite and not
# ============================================================
print("PART 3 -- Sea proxies C_a x C_b (4-regular, quadrangular)")
print("-" * 72)
print("  C_a x C_b is bipartite iff BOTH a and b are even. An odd factor")
print("  introduces odd cycles -- exactly what a hole in a quadrangulation")
print("  can do.")
print()
print(f"  {'grid':>10s} {'V':>4s} {'E':>4s} {'bip':>6s} {'min M':>6s} "
      f"{'minimisers':>11s} {'mod inv':>8s} {'rigid?':>7s}")
SEA = {}
for (a, b) in [(4, 4), (4, 6), (6, 4), (3, 4), (4, 3), (3, 6), (5, 4), (3, 3)]:
    n = a * b
    if n > 20:
        continue
    e = torus(a, b)
    best, cnt, reps, adj = scan(n, e)
    bip = is_bipartite(n, adj)
    SEA[(a, b)] = (n, e, best, len(reps), bip)
    print(f"  C_{a} x C_{b:<4d} {n:4d} {len(e):4d} {str(bip):>6s} {best:6d} "
          f"{cnt:11d} {len(reps):8d} {str(len(reps) == 1):>7s}")
print()
print("  READING: even x even grids are bipartite, min M = 0, and the")
print("  ground state is unique up to inversion -- the sea is RIGID.")
print("  A grid with an odd factor is non-bipartite, min M rises, and")
print("  the ground state becomes degenerate. If the three valence holes")
print("  introduce odd cycles, the sea acquires exactly this degeneracy;")
print("  if they do not, the sea has no freedom at all under rule P.")
print()


# ============================================================
# PART 4 -- The interface, posed so that it can fail
# ============================================================
print("PART 4 -- Joining a core proxy to a sea proxy")
print("-" * 72)
print("  A core proxy K_m is joined to a sea proxy by THREE edges from a")
print("  single outward vertex (c = 3, the count D43 attributes to each")
print("  boundary block). Question: does a minimiser of the JOINT graph")
print("  restrict to a minimiser of each part?")
print()
print("    - if YES, the two regimes coexist at no cost and there is no")
print("      interface motor;")
print("    - if NO, the junction forces one side off its own optimum, and")
print("      the excess max_v same(v) measures the cost.")
print()
print(f"  {'core':>6s} {'sea':>10s} {'V':>4s} {'minM core':>10s} "
      f"{'minM sea':>9s} {'minM joint':>11s} {'restricts?':>11s} "
      f"{'joint mins':>11s}")

for m in (4, 6):
    for (a, b) in [(4, 4), (3, 4), (3, 3)]:
        n_sea = a * b
        n = m + n_sea
        if n > 21:
            continue
        core_e = complete(m)
        sea_e = torus(a, b, offset=m)
        out_v = 0                      # outward vertex of the core
        targets = [m + 0, m + 1, m + b]  # three distinct sea vertices
        link = [(out_v, t) for t in targets]
        edges = core_e + sea_e + link

        bc, _, _, _ = scan(m, core_e)
        bs, _, _, _ = scan(n_sea, torus(a, b))
        bj, cntj, repsj, adjj = scan(n, edges)

        # does some joint minimiser restrict to minimisers of both parts?
        core_adj = adj_masks(m, core_e)
        sea_adj = adj_masks(n_sea, torus(a, b))
        fullc, fulls = (1 << m) - 1, (1 << n_sea) - 1
        restricts = False
        for x in repsj:
            xc = x & fullc
            xs = (x >> m) & fulls
            if (M_of(xc, core_adj, m, fullc) == bc and
                    M_of(xs, sea_adj, n_sea, fulls) == bs):
                restricts = True
                break
        print(f"  K_{m:<4d} C_{a}xC_{b:<5d} {n:4d} {bc:10d} {bs:9d} "
              f"{bj:11d} {str(restricts):>11s} {len(repsj):11d}")
print()
print("  A joint min M strictly above max(core, sea) means the junction")
print("  itself is frustrated. A joint min M equal to that maximum, with")
print("  'restricts?' False, means the parts must be re-labelled to")
print("  coexist -- a weaker but still real constraint.")
print()


# ============================================================
# PART 5 -- Where the freedom actually sits
# ============================================================
print("PART 5 -- Counting the freedom on each side of the interface")
print("-" * 72)
print("  The question of the session has been which side of the interface")
print("  carries the dynamics. Rule P answers it by counting ground")
print("  states, and the answer is not the one assumed.")
print()
print(f"  {'structure':>22s} {'degree':>7s} {'bipartite':>10s} "
      f"{'min M':>6s} {'ground states (mod inv)':>24s}")
print(f"  {'core K_24':>22s} {23:7d} {'no':>10s} {11:6d} "
      f"{comb(24,12)//2:24,}")
print(f"  {'core K_28':>22s} {27:7d} {'no':>10s} {13:6d} "
      f"{comb(28,14)//2:24,}")
for (a, b) in [(4, 4), (4, 6)]:
    if (a, b) in SEA:
        n, e, best, reps, bip = SEA[(a, b)]
        print(f"  {'sea proxy C_%d x C_%d' % (a, b):>22s} {4:7d} "
              f"{('yes' if bip else 'no'):>10s} {best:6d} {reps:24,}")
print()
print("  If the sea proxy is bipartite it has exactly ONE ground state")
print("  while each core has millions. Under rule P the sea is the rigid")
print("  side and the cores are the free side -- the reverse of the")
print("  picture assumed earlier in the session. Whether the real sea is")
print("  bipartite depends on whether the three valence holes introduce")
print("  odd cycles, which PART 3 shows is exactly what decides the")
print("  degeneracy. That is the next thing to settle, and it is a")
print("  question about the topology of the sea, not about rule P.")
print()

print("=" * 72)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 72)
print("  PART 1  the cores: min M = ceil(n/2)-1, gap 1 irreducible")
print("          (odd degree), one orbit but millions of ground states.")
print("  PART 2  Euler forbids a 4-regular quadrangular sea on S^2;")
print("          a quadrangular sea would be bipartite, hence rigid.")
print("  PART 3  whether odd cycles restore degeneracy to the sea.")
print("  PART 4  whether the interface is frustrated, posed so that")
print("          'no frustration' is a possible and reportable answer.")
print("  PART 5  which side of the interface actually carries freedom.")
print("=" * 72)
