"""
PDL–OFN Bridge — Script 2
=========================
Orbites de S4 sur K4 signé et comparaison avec la décomposition OFN.

CONTEXTE
--------
Dans OFN, les 13 états CP-crossing de Ω21 se décomposent sous A5×Z2 en :
    8 ⊕ 3 ⊕ 1 ⊕ 1  (dimensions 8+3+1+1 = 13)
Ce qui donne le groupe de jauge SU(3)×SU(2)×U(1)×U(1)'.

Dans PDL (D36), la représentation de permutation de S4 sur les 6 arêtes
de K4 se décompose en représentations irréductibles de S4 :
    1 ⊕ 2 ⊕ 3_std  (dimensions 1+2+3 = 6)

QUESTION
--------
1. Les orbites de S4 sur les 64 configurations signées de K4
   donnent-elles une décomposition analogue à OFN ?
2. En particulier, y a-t-il une partition 8+3+1+1 = 13 ou similaire
   parmi les orbites sur les configurations signées ?
3. Les 8 configurations balancées ont-elles un rôle structurel
   analogue aux 8 états self-conjugate de OFN ?

MÉTHODE
-------
1. Calculer toutes les orbites de S4 sur les 64 configurations signées de K4.
2. Identifier les tailles d'orbites.
3. Comparer avec la structure OFN (8 self-conjugate + 13 CP-crossing).
4. Vérifier si les configurations balancées correspondent aux self-conjugate.
"""

import itertools
from collections import defaultdict

print("=" * 65)
print("PDL–OFN Script 2: Orbites de S4 sur K4 signé")
print("=" * 65)

# ─────────────────────────────────────────────────────────────
# SETUP : K4 ET SON GROUPE DE SYMÉTRIE S4
# ─────────────────────────────────────────────────────────────

# Arêtes de K4 dans l'ordre lexicographique
K4_EDGES = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
EDGE_IDX = {e: i for i, e in enumerate(K4_EDGES)}

# S4 : toutes les permutations de {0,1,2,3}
S4 = list(itertools.permutations([0,1,2,3]))

def permute_edge(perm, edge):
    """Applique une permutation à une arête et retourne l'arête canonique."""
    u, v = perm[edge[0]], perm[edge[1]]
    return (min(u,v), max(u,v))

def permute_config(perm, config):
    """Applique une permutation de S4 à une configuration signée de K4.
    config : tuple de 6 bits (0=négatif, 1=positif)
    Retourne la nouvelle configuration signée.
    """
    new_config = [0] * 6
    for i, edge in enumerate(K4_EDGES):
        new_edge = permute_edge(perm, edge)
        new_idx = EDGE_IDX[new_edge]
        new_config[new_idx] = config[i]
    return tuple(new_config)

# Toutes les 64 configurations
ALL_CONFIGS = list(itertools.product([0,1], repeat=6))

print(f"\nK4 edges: {K4_EDGES}")
print(f"|S4| = {len(S4)}")
print(f"Configurations totales: {len(ALL_CONFIGS)}")

# ─────────────────────────────────────────────────────────────
# CALCUL DES ORBITES DE S4
# ─────────────────────────────────────────────────────────────

def compute_orbits(configs, group):
    """Calcule les orbites d'un groupe sur un ensemble de configurations."""
    remaining = set(configs)
    orbits = []
    while remaining:
        config = next(iter(remaining))
        orbit = set()
        for perm in group:
            orbit.add(permute_config(perm, config))
        orbits.append(frozenset(orbit))
        remaining -= orbit
    return orbits

orbits = compute_orbits(ALL_CONFIGS, S4)
print(f"\nNombre d'orbites de S4 sur les 64 configurations: {len(orbits)}")

# Trier par taille
orbit_sizes = sorted([len(o) for o in orbits])
from collections import Counter
size_counts = Counter(orbit_sizes)
print(f"\nDistribution des tailles d'orbites:")
for size, count in sorted(size_counts.items()):
    print(f"  Taille {size:2d} : {count} orbite(s)")

# ─────────────────────────────────────────────────────────────
# IDENTIFICATION DES CONFIGURATIONS BALANCÉES
# ─────────────────────────────────────────────────────────────

TRIANGLES = [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]

def sign_of_edge(config, i, j):
    idx = EDGE_IDX[(min(i,j), max(i,j))]
    return 1 if config[idx] == 1 else -1

def is_balanced(config):
    for (a,b,c) in TRIANGLES:
        if sign_of_edge(config,a,b) * sign_of_edge(config,b,c) * sign_of_edge(config,a,c) == -1:
            return False
    return True

def is_antibalanced(config):
    for (a,b,c) in TRIANGLES:
        if sign_of_edge(config,a,b) * sign_of_edge(config,b,c) * sign_of_edge(config,a,c) == 1:
            return False
    return True

BALANCED = [c for c in ALL_CONFIGS if is_balanced(c)]
ANTIBALANCED = [c for c in ALL_CONFIGS if is_antibalanced(c)]
print(f"\nConfigurations balancées: {len(BALANCED)}")
print(f"Configurations anti-balancées: {len(ANTIBALANCED)}")

# ─────────────────────────────────────────────────────────────
# INVOLUTION COMPLÉMENTAIRE (analogue CP)
# ─────────────────────────────────────────────────────────────
# Dans OFN, l'involution CP est C(x) = 63-x (NOT bit-à-bit).
# Sur K4 signé, l'involution naturelle est l'inversion globale des signes.

def invert_config(config):
    """Inverse tous les signes : 0↔1."""
    return tuple(1-b for b in config)

# Partition en self-conjugate et crossing
self_conjugate = []
crossing = []
for config in ALL_CONFIGS:
    inv = invert_config(config)
    if inv == config:
        self_conjugate.append(config)
    elif config < inv:  # éviter les doublons
        crossing.append(config)

print(f"\nSous l'involution globale des signes :")
print(f"  Self-conjugate (invariants) : {len(self_conjugate)}")
print(f"  Paires crossing : {len(crossing)} paires = {len(crossing)*2} configs")

# ─────────────────────────────────────────────────────────────
# COMPARAISON AVEC OFN
# ─────────────────────────────────────────────────────────────

print(f"\n{'═'*65}")
print("COMPARAISON STRUCTURE PDL vs OFN")
print(f"{'═'*65}")

print(f"""
OFN (espace Q6 = {{0,1}}^6, 64 états) :
  Total                    : 64 états
  Vacuum manifold Ω21      : 21 états (filtre en 3 étapes)
  Self-conjugate (CP)      :  8 états (4 paires CP complètes)
  CP-crossing              : 13 états (1 point de 13 paires)
  Décomposition CP-crossing: 8 ⊕ 3 ⊕ 1 ⊕ 1 → SU(3)×SU(2)×U(1)×U(1)'
  Complémentaire E43       : 43 états (excitations)

PDL (K4 signé, 2^6 = 64 configurations) :
  Total                    : 64 configurations
  Balancées                : {len(BALANCED)} (cohérentes, C1–C4)
  Anti-balancées           : {len(ANTIBALANCED)}
  Self-conjugate (inversion): {len(self_conjugate)}
  Paires crossing          : {len(crossing)} paires
  Orbites de S4            : {len(orbits)} orbites
  Décomposition S4 sur arêtes: 1 ⊕ 2 ⊕ 3_std (D36)
""")

# Orbites des configurations balancées sous S4
balanced_orbits = compute_orbits(BALANCED, S4)
print(f"Orbites de S4 sur les 8 configurations balancées: {len(balanced_orbits)}")
for orb in sorted(balanced_orbits, key=len):
    sample = list(orb)[0]
    print(f"  Taille {len(orb)}: exemple {sample}")

# ─────────────────────────────────────────────────────────────
# DÉCOMPOSITION EN REPRÉSENTATIONS IRRÉDUCTIBLES DE S4
# ─────────────────────────────────────────────────────────────

print(f"\n{'═'*65}")
print("DÉCOMPOSITION EN REPRÉSENTATIONS IRRÉDUCTIBLES DE S4")
print(f"{'═'*65}")

print("""
Les représentations irréductibles de S4 (ordre 24) :
  ρ_trivial  : dim 1  (tous les éléments agissent trivialement)
  ρ_sign     : dim 1  (signature de la permutation)
  ρ_standard : dim 3  (restriction de S4 à l'hyperplan de R^4)
  ρ_2        : dim 2  (produit tensoriel sign ⊗ standard restreint)
  ρ_4        : dim 3  (autre représentation 3-dim)

D36 confirme : représentation sur les 6 arêtes = 1 ⊕ 2 ⊕ 3_std
""")

# Calcul des caractères de la représentation de permutation sur les 6 arêtes
def char_edge_perm(perm):
    """Trace de la matrice de permutation sur les 6 arêtes."""
    count = 0
    for edge in K4_EDGES:
        new_edge = permute_edge(perm, edge)
        if new_edge == edge:
            count += 1
    return count

# Classes de conjugaison de S4
def cycle_type(perm):
    """Type cyclique d'une permutation."""
    visited = [False] * 4
    cycles = []
    for i in range(4):
        if not visited[i]:
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j]
                cycle_len += 1
            cycles.append(cycle_len)
    return tuple(sorted(cycles, reverse=True))

classes = defaultdict(list)
for perm in S4:
    ct = cycle_type(perm)
    classes[ct].append(perm)

print("Classes de conjugaison de S4 et caractères :")
print(f"{'Cycle type':<15} {'|class|':>8} {'χ(arêtes)':>12} {'χ^2':>8}")
print("-" * 50)
for ct in sorted(classes.keys()):
    perms = classes[ct]
    chi = char_edge_perm(perms[0])
    print(f"{str(ct):<15} {len(perms):>8} {chi:>12} {chi**2:>8}")

# ─────────────────────────────────────────────────────────────
# RÉSUMÉ ET CONCLUSION
# ─────────────────────────────────────────────────────────────

print(f"\n{'═'*65}")
print("RÉSUMÉ COMPARATIF PDL vs OFN")
print(f"{'═'*65}")

print(f"""
POINT 1 — Espace à 64 états
  PDL : 2^6 = 64 via 6 arêtes signées de K4
  OFN : 2^6 = 64 via 6 qubits de Q6
  → Même cardinalité, interprétation différente des 6 dimensions

POINT 2 — Involution naturelle
  PDL : inversion globale des signes (balanced ↔ anti-balanced)
  OFN : CP-involution bitwise NOT (C(x) = 63-x)
  Self-conjugate PDL : {len(self_conjugate)} configs  |  Self-conjugate OFN : 8 états

POINT 3 — Décomposition du groupe de symétrie
  PDL : S4 agit sur 6 arêtes → 1 ⊕ 2 ⊕ 3_std  (D36)
  OFN : A5×Z2 agit sur 13 CP-crossing → 8 ⊕ 3 ⊕ 1 ⊕ 1
  → Groupes différents (S4 vs A5×Z2), décompositions différentes

POINT 4 — Configurations privilégiées
  PDL : 8 configs balancées (C1–C4 cohérentes), {len(balanced_orbits)} orbite(s) sous S4
  OFN : 8 états self-conjugate (CP-invariants) dans Ω21
  → Coïncidence remarquable : 8 dans les deux cas

POINT 5 — Décomposition en Standard Model
  PDL (D36) : 1 ⊕ 2 ⊕ 3_std → pas directement SU(3)×SU(2)×U(1)
  OFN : 8 ⊕ 3 ⊕ 1 ⊕ 1 → SU(3)×SU(2)×U(1)×U(1)'
  → OFN a une route directe vers le Modèle Standard depuis cette décomposition
    PDL n'a pas encore cette route (ouvert — OP10 dans le corpus)

CONCLUSION :
  Les structures sont analogues mais pas identiques.
  La coïncidence des 8 (balancés/self-conjugate) est notable.
  La décomposition S4 de PDL (1⊕2⊕3) est différente de
  la décomposition A5×Z2 d'OFN (8⊕3⊕1⊕1).
  β1 = 3 reste le pont le plus solide entre les deux frameworks.
""")
print("Script 2 terminé.")
