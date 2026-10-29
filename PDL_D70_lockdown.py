#!/usr/bin/env python3
# =============================================================================
#  PDL_D70_lockdown.py — lockdown of every result marked [E] in Part I of D70
#  Standard library only. Deterministic. Prints PASS/FAIL per check.
#  Expected runtime on Colab: a few minutes (check 6 dominates).
# =============================================================================

from itertools import combinations, product
from math import comb, sqrt, log, pi
import heapq
import random

RESULTS = []


def check(name, cond, detail=''):
    RESULTS.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ''))


def pc(x):
    return bin(x).count('1')


# -----------------------------------------------------------------------------
print('1. Compatibility law 2^(1-k)  (Proposition 3.1)')
for k in range(1, 9):
    states = list(product((1, -1), repeat=k))
    ok = sum(1 for a in states for b in states
             if a == b or all(x == -y for x, y in zip(a, b)))
    frac = ok / len(states) ** 2
    check(f'k={k}', abs(frac - 2.0 ** (1 - k)) < 1e-15, f'{ok}/{len(states)**2}')


# -----------------------------------------------------------------------------
def frustration_index(verts, s):
    verts = list(verts)
    m = len(verts)
    if m < 2:
        return 0
    P = [(verts[i], verts[j]) for i in range(m) for j in range(i + 1, m)]
    best = len(P)
    for sw in product((1, -1), repeat=m - 1):
        sig = dict(zip(verts, (1,) + sw))
        best = min(best, sum(1 for x, y in P if s[(x, y)] * sig[x] * sig[y] == -1))
    return best


print('2. Coupling decomposition  (Theorem 3.2)')
rng = random.Random(20260921)
for n in (4, 5, 6):
    A = list(range(n))
    PA = [(i, j) for i in A for j in A if i < j]
    ok = True
    for _ in range(100):
        s = {p: rng.choice((1, -1)) for p in PA}
        kk = rng.randint(2, n)
        N = tuple(sorted(rng.sample(A, kk)))
        best = None
        for cs in product((1, -1), repeat=kk):
            sg = dict(zip(N, cs))
            v = 0
            for x, y in combinations(A, 2):
                if x in sg and y in sg:
                    v += s[(x, y)] * sg[x] * sg[y] == -1
                else:
                    v += 1
            best = v if best is None else min(best, v)
        pred = comb(n, 2) - comb(kk, 2) + frustration_index(N, s)
        ok &= (best == pred)
    check(f'n={n}, 100 random cases', ok)


# -----------------------------------------------------------------------------
print('3. Minimal frustration of unbalanced K_n = n-2  (Section 3.3)')
for n in (4, 5, 6):
    P = list(combinations(range(n), 2))
    T = list(combinations(range(n), 3))
    idx = {p: i for i, p in enumerate(P)}
    mn = None
    for bits in range(1 << len(P)):
        v = 0
        for a, b, c in T:
            par = ((bits >> idx[(a, b)]) ^ (bits >> idx[(a, c)]) ^ (bits >> idx[(b, c)])) & 1
            v += par
        if v and (mn is None or v < mn):
            mn = v
    check(f'n={n}', mn == n - 2, f'min={mn}')


# -----------------------------------------------------------------------------
def two_block_profile(n, kmax):
    """Exhaustive: two K_n blocks, all signs +, remove k internal, add k cross."""
    A = list(range(n)); B = list(range(n, 2 * n)); V = 2 * n
    INTRA = list(combinations(A, 2)) + list(combinations(B, 2))
    CROSS = [(a, b) for a in A for b in B]
    T = comb(V, 3)

    def tris(edges):
        adj = [0] * V
        for x, y in edges:
            adj[x] |= 1 << y; adj[y] |= 1 << x
        return sum(pc(adj[x] & adj[y]) for x, y in edges) // 3

    base = T - tris(INTRA)
    prof = [0]
    for k in range(1, kmax + 1):
        best = None
        for rem in combinations(range(len(INTRA)), k):
            rs = set(rem)
            kept = [INTRA[i] for i in range(len(INTRA)) if i not in rs]
            for add in combinations(range(len(CROSS)), k):
                v = T - tris(kept + [CROSS[i] for i in add])
                best = v if best is None else min(best, v)
        prof.append(best - base)
    return base, T, prof


print('4. Barrier profile delta(k) = k(n-1-k)  (Proposition 3.4)')
base4, T4, p4 = two_block_profile(4, 6)
check('n=4, k=0..3', p4[:4] == [k * (3 - k) for k in range(4)], f'{p4[:4]}')
check('n=4 global minimum 45/56 at k=5', base4 + min(p4) == 45 and p4.index(min(p4)) == 5,
      f'profile {p4}')
_, _, p5 = two_block_profile(5, 3)
check('n=5, k=0..3', p5 == [k * (4 - k) for k in range(4)], f'{p5}')


# -----------------------------------------------------------------------------
print('5. Collapse barrier, 7 vertices, 12 edges  (Section 3.5)')
Nv = 7
PAIRS = list(combinations(range(Nv), 2))
NP = len(PAIRS)


def tri_mask(m):
    adj = [0] * Nv
    for i in range(NP):
        if m >> i & 1:
            x, y = PAIRS[i]; adj[x] |= 1 << y; adj[y] |= 1 << x
    return sum(pc(adj[PAIRS[i][0]] & adj[PAIRS[i][1]]) for i in range(NP) if m >> i & 1) // 3


def connected(m):
    adj = [0] * Nv
    for i in range(NP):
        if m >> i & 1:
            x, y = PAIRS[i]; adj[x] |= 1 << y; adj[y] |= 1 << x
    seen, st = 1, [0]
    while st:
        u = st.pop(); nb = adj[u] & ~seen
        while nb:
            lo = nb & -nb; seen |= lo; st.append(lo.bit_length() - 1); nb ^= lo
    return seen == (1 << Nv) - 1


states = {}
for idx in combinations(range(NP), 12):
    m = 0
    for i in idx:
        m |= 1 << i
    if connected(m):
        states[m] = 35 - tri_mask(m)
check('number of connected states = 290745', len(states) == 290745, f'{len(states)}')
asm = 0
for e in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6)]:
    asm |= 1 << PAIRS.index(e)
c_asm = states[asm]; c_min = min(states.values())
check('assembly cost 27, optimum 25', c_asm == 27 and c_min == 25, f'{c_asm}, {c_min}')
improving = 0
for i in range(NP):
    if asm >> i & 1:
        m1 = asm & ~(1 << i)
        for j in range(NP):
            if not (asm >> j & 1):
                m2 = m1 | (1 << j)
                if m2 in states and states[m2] < c_asm:
                    improving += 1
check('strict local minimum (0 improving moves)', improving == 0)
best = {asm: c_asm}; pq = [(c_asm, asm)]; peak_opt = None
while pq:
    pk, m = heapq.heappop(pq)
    if pk > best.get(m, 1 << 30):
        continue
    if states[m] == c_min:
        peak_opt = pk; break
    for i in range(NP):
        if m >> i & 1:
            m1 = m & ~(1 << i)
            for j in range(NP):
                if not (m >> j & 1):
                    m2 = m1 | (1 << j)
                    if m2 in states:
                        p2 = max(pk, states[m2])
                        if p2 < best.get(m2, 1 << 30):
                            best[m2] = p2; heapq.heappush(pq, (p2, m2))
check('collapse barrier = 1', peak_opt - c_asm == 1, f'peak {peak_opt}')


# -----------------------------------------------------------------------------
print('6. Simultaneity capacity n-1  (Section 3.6)')


def balanced(verts, s):
    verts = list(verts)
    if len(verts) < 3:
        return True
    for sw in product((1, -1), repeat=len(verts) - 1):
        sig = dict(zip(verts, (1,) + sw))
        if all(s[(x, y)] * sig[x] * sig[y] == 1 for x, y in combinations(verts, 2)):
            return True
    return False


for n in range(4, 11):
    s = {p: 1 for p in combinations(range(n), 2)}
    s[(0, 1)] = -1
    kf = next(k for k in range(n, 1, -1)
              if any(balanced(sub, s) for sub in combinations(range(n), k)))
    check(f'n={n}', kf == n - 1, f'k_free={kf}')


# -----------------------------------------------------------------------------
print('7. Pooling probabilities  (Section 3.7)')
for s_, m_, target in ((1, 5, 1.0), (2, 6, 3.125e-2), (3, 8, 6.1035e-5)):
    V = m_ * 4 - (m_ - 1) * s_
    prob = 2 ** (V - 1) / (2 ** 3) ** m_
    rel = m_ * 6 - (m_ - 1) * comb(s_, 2)
    check(f's={s_}, m={m_}', abs(prob - target) / target < 1e-3 and rel >= 27,
          f'prob={prob:.4e}, relations={rel}')


# -----------------------------------------------------------------------------
print('8. Corpus-derived numerical checks')
h = 6.62607015e-34; c = 299792458.0; hbar = h / (2 * pi)
m_p = 1.67262192595e-27
mpc2 = 938.27208816; mec2 = 0.51099895000
e_p = mpc2 / 11017 * 1000; e_e = mec2 / 6 * 1000
check('energy per relation equal to 7.6 ppm',
      abs(abs(e_p / e_e - 1) * 1e6 - 7.62) < 0.05, f'{e_p:.5f} vs {e_e:.5f} keV')
phi = (1 + sqrt(5)) / 2
kappa = 310 * phi / 11017
sig = lambda N: 1 - (1 - kappa) ** N
lamC = hbar / (m_p * c); VC = 4 / 3 * pi * lamC ** 3
rho = lambda N: sig(N) * kappa * m_p / VC
v = 2.2e5
ratios = [(m_p ** 2 * ((rho(N) / m_p) * v) ** 2 / rho(N)) / (rho(N) * c ** 2) for N in (1, 10, 40, 120, 1000)]
check('C_orb/C_mass = (v/c)^2, density independent',
      max(abs(r / (v / c) ** 2 - 1) for r in ratios) < 1e-12, f'{ratios[0]:.6e}')
check('sigma <= 1 (ceiling)', all(sig(N) <= 1 for N in (1, 10, 100, 1000, 10 ** 6)))
Nmw = 60e9 * 1.98892e30 / m_p
kneed = -((0.5 ** (1 / Nmw)) - 1) if Nmw < 1e300 else log(2) / Nmw
kneed = log(2) / Nmw
check('kappa needed at Milky Way scale ~ 9.7e-69', abs(kneed / 9.715e-69 - 1) < 0.01, f'{kneed:.4e}')
epsG = 0.0075194
G_pdl = hbar * c / m_p ** 2 * epsG ** 18
check('G_PDL within 20 ppm of CODATA', abs(G_pdl / 6.67430e-11 - 1) * 1e6 < 20,
      f'{abs(G_pdl/6.67430e-11-1)*1e6:.1f} ppm')
a0 = 1.20e-10
n_req = log(a0 / (c ** 2 / lamC)) / log(epsG)
check('exponent required for a0 = 20.035 (not 18)', abs(n_req - 20.0354) < 1e-3, f'{n_req:.4f}')
check('rho_coh(1) >= 8.9e16 kg/m^3', rho(1) > 8.89e16, f'{rho(1):.4e}')

# -----------------------------------------------------------------------------
npass = sum(1 for _, ok in RESULTS if ok)
print()
print(f'SUMMARY: {npass} PASS, {len(RESULTS) - npass} FAIL, {len(RESULTS)} checks')
