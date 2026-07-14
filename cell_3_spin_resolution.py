# ============================================================
# D66 -- CELLULE 3 / 4
# Resolution de l'obstruction: cycle 1 = signes classiques (carre=+1,
# cf. tau_3 dans D33), cycle 2 = signes de type spin (carre=-1,
# insere via -1*ex2[i]*ex2[j], cf. T=i*tau_2 dans D33).
# Verifie que le nombre de solutions vaut TOUJOURS exactement 4,
# et que la fraction resultante est 4^(1-n), pour n=3..7.
# Version vectorisee (numpy) pour rester rapide meme a n=7.
# Cellule autonome.
# ============================================================
import itertools
import numpy as np

def coherent_Kn_configs(n):
    edges = list(itertools.combinations(range(n), 2))
    configs = []
    for bits in itertools.product([1, -1], repeat=len(edges)):
        s = dict(zip(edges, bits))
        def sgn(i, j):
            return s[(i, j)] if (i, j) in s else s[(j, i)]
        coherent = True
        for tri in itertools.combinations(range(n), 3):
            a, b, c = tri
            if sgn(a, b) * sgn(a, c) * sgn(b, c) != 1:
                coherent = False
                break
        if coherent:
            configs.append(s)
    return configs, edges

def count_simultaneous_stable_SPIN_vectorized(n, config, edges):
    """Version vectorisee: cycle1 classique, cycle2 type-spin (signe -1 insere)."""
    all_bits = np.array(list(itertools.product([1, -1], repeat=n)))  # (2^n, n)
    N = all_bits.shape[0]
    ok_mask = np.ones((N, N), dtype=bool)  # [i,j] = (bits1=all_bits[i], bits2=all_bits[j]) valide ?

    s_target = np.zeros(len(edges), dtype=int)
    for idx, (i, j) in enumerate(edges):
        s_target[idx] = config[(i, j)] if (i, j) in config else config[(j, i)]

    for idx, (i, j) in enumerate(edges):
        P1 = all_bits[:, i] * all_bits[:, j]          # (2^n,) -- cycle 1, classique, une valeur par choix de bits1
        P2 = -1 * all_bits[:, i] * all_bits[:, j]      # (2^n,) -- cycle 2, type-spin, une valeur par choix de bits2
        target = s_target[idx]
        # (A): P1 == target  -- ne depend que de bits1 (indice i)
        # (B): P2 == -P1 == -target (puisque (A) impose P1=target) -- ne depend que de bits2 (indice j)
        valid1 = (P1 == target)           # (2^n,) sur l'axe bits1
        valid2 = (P2 == -target)          # (2^n,) sur l'axe bits2 -- CORRIGE: compare a -target, pas a -P1
        ok_mask &= valid1[:, None] & valid2[None, :]

    return int(ok_mask.sum()), N * N

print(f"{'n':>3} {'#solutions':>11} {'espace (2^2n)':>14} {'fraction':>14} {'4^(1-n) attendu':>16} {'OK?':>6}")
for n in [3, 4, 5, 6, 7]:
    configs, edges = coherent_Kn_configs(n)
    cfg = configs[0]  # symetrie S_n deja verifiee pour n=4 en amont -- 1 suffit ici
    count, total = count_simultaneous_stable_SPIN_vectorized(n, cfg, edges)
    frac = count / total
    expected = 4.0**(1 - n)
    ok = abs(frac - expected) < 1e-12
    print(f"{n:>3} {count:>11} {total:>14} {frac:>14.10f} {expected:>16.10f} {'OK' if ok else '*** ECHEC ***':>6}")
    assert count == 4, f"ECHEC n={n}: attendu exactement 4 solutions, obtenu {count}"
    assert ok, f"ECHEC n={n}: fraction ne correspond pas a 4^(1-n)"

print()
print("CONFIRME: exactement 4 solutions pour tout n=3..7 (independant de n),")
print("fraction = 4^(1-n) verifiee exactement dans chaque cas.")

print()
print("="*70)
print("VERIFICATION DE L'UNICITE DE n=4 (exposant = nombre d'aretes)")
print("="*70)
print(f"{'n':>3} {'exposant 2n-2':>14} {'#aretes C(n,2)':>15} {'egaux?':>8}")
for n in range(2, 12):
    exp = 2*n - 2
    nedges = n*(n-1)//2
    match = (exp == nedges)
    print(f"{n:>3} {exp:>14} {nedges:>15} {'OUI <==' if match else 'non':>8}")

print()
print("Verification algebrique: (n-1)(n-4)=0 <=> n=1 ou n=4.")
for n in range(2, 12):
    lhs = 2*n - 2
    rhs = n*(n-1)//2
    assert (lhs == rhs) == (n == 4), f"Coherence rompue a n={n}"
print("Coherence confirmee pour n=2..11: n=4 est l'unique solution non triviale.")
