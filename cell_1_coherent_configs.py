# ============================================================
# D66 -- CELLULE 1 / 4
# Verification: nombre de configurations coherentes (equilibrees,
# Harary) de K_n vaut exactement 2^(n-1), pour n=3..6.
# Cellule autonome -- aucune dependance a une cellule precedente.
# ============================================================
import itertools

def coherent_Kn_configs(n):
    """Retourne la liste des configurations de signes equilibrees de K_n."""
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

print(f"{'n':>3} {'#edges':>8} {'#coherentes':>12} {'2^(n-1) attendu':>16} {'OK?':>6}")
results = {}
for n in [3, 4, 5, 6]:
    configs, edges = coherent_Kn_configs(n)
    expected = 2**(n-1)
    ok = (len(configs) == expected)
    results[n] = (configs, edges)
    print(f"{n:>3} {len(edges):>8} {len(configs):>12} {expected:>16} {'OK' if ok else '*** ECHEC ***':>6}")
    assert len(configs) == expected, f"ECHEC pour n={n}: attendu {expected}, obtenu {len(configs)}"

print()
print("Assertion globale reussie: 2^(n-1) confirme pour n=3,4,5,6.")
