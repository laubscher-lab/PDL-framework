# ============================================================
# D66 -- CELLULE 2 / 4
# Preuve computationnelle: la stabilite (A)^(B) simultanee sur les
# n(n-1)/2 aretes de K_n, avec signes croises CLASSIQUES (+-1),
# est IMPOSSIBLE -- 0 solution, pour tout n teste.
# Mecanisme algebrique: un jeu de signes de sommets induit
# TOUJOURS une configuration d'arete EQUILIBREE (produit de
# triangle = +1). La condition (B) exige P2 = -s_K(i,j), qui est
# TOUJOURS DESEQUILIBREE quand s_K est equilibree (n-1 flips par
# triangle a n-1 impair... plus precisement: 3 flips par triangle
# pour un negatif total). Donc (A) et (B) exigent simultanement
# une cible equilibree et son oppose desequilibre -- contradiction.
# Cellule autonome.
# ============================================================
import itertools

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

def s_val(config, i, j):
    return config[(i, j)] if (i, j) in config else config[(j, i)]

def count_simultaneous_stable_CLASSIQUE(n, config, edges):
    """Cross-signes classiques (+-1) aux n sommets, 2 demi-cycles.
       Retourne (nb_solutions, total_espace)."""
    count, total = 0, 0
    for bits1 in itertools.product([1, -1], repeat=n):
        for bits2 in itertools.product([1, -1], repeat=n):
            ex1 = {v: bits1[v] for v in range(n)}
            ex2 = {v: bits2[v] for v in range(n)}
            total += 1
            ok = True
            for (i, j) in edges:
                P1 = ex1[i] * ex1[j]
                P2 = ex2[i] * ex2[j]
                if not (P1 == s_val(config, i, j) and P2 == -P1):
                    ok = False
                    break
            if ok:
                count += 1
    return count, total

print(f"{'n':>3} {'#config coh.':>12} {'espace (2^2n)':>14} {'solutions (toutes config)':>26}")
for n in [3, 4]:  # n=5,6 laisses a la cellule suivante (optimisee) -- 2^(2n) devient grand
    configs, edges = coherent_Kn_configs(n)
    solutions = []
    for cfg in configs:
        cnt, tot = count_simultaneous_stable_CLASSIQUE(n, cfg, edges)
        solutions.append(cnt)
    print(f"{n:>3} {len(configs):>12} {2**(2*n):>14} {str(solutions):>26}")
    assert all(s == 0 for s in solutions), f"ECHEC: n={n} a une solution non-nulle -- l'obstruction ne tient pas!"

print()
print("CONFIRME: 0 solution dans TOUS les cas testes (n=3,4), pour")
print("TOUTES les configurations coherentes. L'obstruction de parite")
print("est verifiee exhaustivement, pas seulement pour K4.")
print()
print("NOTE: n=5,6 -- l'espace 2^(2n) devient couteux en Python pur")
print("(2^10=1024, 2^12=4096 -- faisable mais lent avec cette boucle")
print("non optimisee). Utiliser la cellule 3 (version vectorisee) si")
print("besoin de les verifier aussi.")
