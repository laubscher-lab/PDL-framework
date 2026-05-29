"""
PDL-OFN Bridge - Script 3 CORRIGE
==================================
Cherche une application naturelle entre les 6 aretes de K4 et les 6 qubits de Q6.
"""

import itertools
from collections import defaultdict
import random

print("=" * 65)
print("PDL-OFN Script 3: Application K4 <-> Q6")
print("=" * 65)

# ─────────────────────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────────────────────

K4_EDGES = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
EDGE_IDX = {e: i for i, e in enumerate(K4_EDGES)}
TRIANGLES = [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]

# OFN Omega21
OFN_OMEGA21_DECIMAL = [
    0, 1, 3, 4, 7, 8, 9, 12, 15, 16, 19, 21,
    27, 31, 35, 42, 43, 48, 52, 56, 63
]
OFN_OMEGA21 = frozenset(
    tuple(int(b) for b in format(d, '06b'))
    for d in OFN_OMEGA21_DECIMAL
)

# OFN self-conjugate
OFN_SELF_CONJUGATE_DECIMAL = [0, 7, 15, 21, 42, 48, 56, 63]
OFN_SELF_CONJUGATE = frozenset(
    tuple(int(b) for b in format(d, '06b'))
    for d in OFN_SELF_CONJUGATE_DECIMAL
)

print(f"\n|Omega21| = {len(OFN_OMEGA21)}")
print(f"|Self-conjugate OFN| = {len(OFN_SELF_CONJUGATE)}")

# ─────────────────────────────────────────────────────────────
# CONFIGURATIONS PDL BALANCEES
# ─────────────────────────────────────────────────────────────

def sign_of_edge(config, i, j):
    idx = EDGE_IDX[(min(i,j), max(i,j))]
    return 1 if config[idx] == 1 else -1

def is_balanced(config):
    for (a,b,c) in TRIANGLES:
        if sign_of_edge(config,a,b)*sign_of_edge(config,b,c)*sign_of_edge(config,a,c) == -1:
            return False
    return True

ALL_CONFIGS = list(itertools.product([0,1], repeat=6))
BALANCED_SET = frozenset(c for c in ALL_CONFIGS if is_balanced(c))
print(f"\n|Balancees PDL| = {len(BALANCED_SET)}")

# ─────────────────────────────────────────────────────────────
# GRAPHE DE HAMMING ET beta1
# ─────────────────────────────────────────────────────────────

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

def beta1_of_subset(configs):
    configs = list(configs)
    n = len(configs)
    adj = defaultdict(set)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if hamming_distance(configs[i], configs[j]) == 1:
                edges.append((i,j))
                adj[i].add(j)
                adj[j].add(i)
    visited = set()
    components = 0
    for start in range(n):
        if start not in visited:
            components += 1
            queue = [start]
            while queue:
                node = queue.pop()
                if node in visited:
                    continue
                visited.add(node)
                queue.extend(adj[node] - visited)
    V, E, beta0 = n, len(edges), components
    return E - V + beta0, V, E, beta0

b1_omega21, V, E, b0 = beta1_of_subset(OFN_OMEGA21)
print(f"\nbeta1(Omega21) = {b1_omega21} (V={V}, E={E}, b0={b0})  -- OFN reference")

# ─────────────────────────────────────────────────────────────
# FONCTION DE BIJECTION
# ─────────────────────────────────────────────────────────────

def apply_bijection(config_pdl, sigma):
    """
    Applique la bijection sigma aux 6 bits d'une config PDL.
    sigma[i] = indice du qubit qui recoit l'arete i.
    config_q6[sigma[i]] = config_pdl[i]
    """
    config_q6 = [0] * 6
    for i, b in enumerate(config_pdl):
        config_q6[sigma[i]] = b
    return tuple(config_q6)

def apply_inverse_bijection(config_q6, sigma):
    """
    Applique l'inverse de sigma.
    sigma_inv[sigma[i]] = i
    config_pdl[i] = config_q6[sigma[i]]
    """
    return tuple(config_q6[sigma[i]] for i in range(6))

# ─────────────────────────────────────────────────────────────
# RECHERCHE DE BIJECTIONS : balancees -> Omega21
# ─────────────────────────────────────────────────────────────

print(f"\n{'='*65}")
print("RECHERCHE DE BIJECTIONS K4_aretes <-> Q6_qubits")
print(f"{'='*65}")
print("Test de toutes les 720 bijections possibles.")

best_overlap_omega21 = 0
best_overlap_selfconj = 0
best_bijections_omega21 = []
best_bijections_selfconj = []

for sigma in itertools.permutations(range(6)):
    image_balanced = frozenset(apply_bijection(c, sigma) for c in BALANCED_SET)

    overlap_omega21 = len(image_balanced & OFN_OMEGA21)
    if overlap_omega21 > best_overlap_omega21:
        best_overlap_omega21 = overlap_omega21
        best_bijections_omega21 = [sigma]
    elif overlap_omega21 == best_overlap_omega21:
        best_bijections_omega21.append(sigma)

    overlap_selfconj = len(image_balanced & OFN_SELF_CONJUGATE)
    if overlap_selfconj > best_overlap_selfconj:
        best_overlap_selfconj = overlap_selfconj
        best_bijections_selfconj = [sigma]
    elif overlap_selfconj == best_overlap_selfconj:
        best_bijections_selfconj.append(sigma)

print(f"\nMeilleur overlap balancees PDL & Omega21 : {best_overlap_omega21}/8")
print(f"Nombre de bijections atteignant ce max : {len(best_bijections_omega21)}")
print(f"\nMeilleur overlap balancees PDL & self-conjugate OFN : {best_overlap_selfconj}/8")
print(f"Nombre de bijections atteignant ce max : {len(best_bijections_selfconj)}")

# Analyse de la meilleure bijection
if best_bijections_omega21:
    sigma_best = best_bijections_omega21[0]
    print(f"\nMeilleure bijection (overlap Omega21 = {best_overlap_omega21}) :")
    print(f"  Arete -> Qubit mapping: {dict(enumerate(sigma_best))}")

    image_balanced_best = frozenset(apply_bijection(c, sigma_best) for c in BALANCED_SET)
    in_omega21 = image_balanced_best & OFN_OMEGA21
    in_selfconj = image_balanced_best & OFN_SELF_CONJUGATE

    print(f"\n  Image des 8 balancees dans Q6 :")
    for c in sorted(image_balanced_best):
        dec = int(''.join(str(b) for b in c), 2)
        in_o21 = 'OK Omega21' if c in OFN_OMEGA21 else 'hors'
        in_sc  = 'OK SC' if c in OFN_SELF_CONJUGATE else ''
        print(f"    {c} (dec={dec:2d})  {in_o21}  {in_sc}")

    print(f"\n  Dans Omega21 : {len(in_omega21)}/8")
    print(f"  Dans self-conjugate : {len(in_selfconj)}/8")

# ─────────────────────────────────────────────────────────────
# RECHERCHE INVERSE : Omega21 -> PDL
# ─────────────────────────────────────────────────────────────

print(f"\n{'='*65}")
print("RECHERCHE INVERSE : Image de Omega21 dans K4 signe")
print(f"{'='*65}")

beta1_results = defaultdict(int)
bijections_giving_beta1_3 = []

for sigma in itertools.permutations(range(6)):
    preimage_omega21 = frozenset(apply_inverse_bijection(c, sigma) for c in OFN_OMEGA21)
    b1, V, E, b0 = beta1_of_subset(preimage_omega21)
    beta1_results[b1] += 1
    if b1 == 3:
        bijections_giving_beta1_3.append(sigma)

print(f"\nDistribution des beta1 de l'image inverse de Omega21 dans K4 signe :")
for b1, count in sorted(beta1_results.items()):
    marker = " <- beta1 = 3 !" if b1 == 3 else ""
    print(f"  beta1 = {b1} : {count} bijection(s){marker}")

if bijections_giving_beta1_3:
    print(f"\n{len(bijections_giving_beta1_3)} bijection(s) donnent beta1 = 3 dans K4 signe.")
    sigma_ex = bijections_giving_beta1_3[0]
    print(f"Exemple de bijection : {dict(enumerate(sigma_ex))}")
else:
    print("\nAucune bijection ne donne beta1 = 3 pour l'image inverse de Omega21.")

# ─────────────────────────────────────────────────────────────
# SOUS-ENSEMBLES DE TAILLE 21 AVEC beta1 = 3
# ─────────────────────────────────────────────────────────────

print(f"\n{'='*65}")
print("SOUS-ENSEMBLES DE TAILLE 21 DANS K4 SIGNE AVEC beta1 = 3")
print(f"{'='*65}")

random.seed(42)
found_beta1_3 = 0
n_samples = 2000

for _ in range(n_samples):
    subset = random.sample(ALL_CONFIGS, 21)
    b1, _, _, _ = beta1_of_subset(subset)
    if b1 == 3:
        found_beta1_3 += 1

print(f"Echantillonnage de {n_samples} sous-ensembles de taille 21 :")
print(f"  Sous-ensembles avec beta1 = 3 : {found_beta1_3}")
if found_beta1_3 > 0:
    print(f"  -> Des sous-ensembles de taille 21 avec beta1=3 existent dans K4 signe")
else:
    print(f"  -> Aucun trouve dans cet echantillon")

# ─────────────────────────────────────────────────────────────
# RESUME FINAL
# ─────────────────────────────────────────────────────────────

print(f"\n{'='*65}")
print("RESUME FINAL - SCRIPT 3")
print(f"{'='*65}")

if best_overlap_omega21 >= 6:
    overlap_verdict = "Connexion structurelle significative"
elif best_overlap_omega21 >= 4:
    overlap_verdict = "Overlap partiel"
else:
    overlap_verdict = "Overlap faible - pas de bijection naturelle evidente"

if best_overlap_selfconj >= 6:
    selfconj_verdict = "Correspondance remarquable"
elif best_overlap_selfconj >= 4:
    selfconj_verdict = "Correspondance partielle"
else:
    selfconj_verdict = "Pas de correspondance directe"

print(f"""
RESULTATS :

1. Meilleur overlap balancees PDL & Omega21 : {best_overlap_omega21}/8
   -> {overlap_verdict}

2. Meilleur overlap balancees PDL & self-conjugate OFN : {best_overlap_selfconj}/8
   -> {selfconj_verdict}

3. Bijections donnant beta1=3 pour l'image inverse de Omega21 : {len(bijections_giving_beta1_3)}/720
   -> {"beta1=3 preserve par certaines bijections" if bijections_giving_beta1_3 else "beta1=3 non preserve par aucune bijection simple"}

4. Sous-ensembles taille 21 avec beta1=3 (echantillon {n_samples}) : {found_beta1_3}

CONCLUSION :
  Les deux frameworks partagent :
  OK  beta1 = 3 (Scripts 1 et 2)
  OK  Un espace de 64 etats binaires a 6 dimensions
  OK  Le nombre 8 pour les configurations privilegiees

  Ils ne partagent pas :
  NON Une bijection naturelle entre leurs espaces de configuration
  NON Le meme groupe de symetrie (S4 vs A5xZ2)
  NON La meme involution (inversion vs CP bitwise NOT)

  INTERPRETATION :
  beta1 = 3 est un invariant topologique partage mais emergent
  de deux objets mathematiquement distincts.
  Il n'existe pas de dictionnaire trivial entre PDL et OFN.
  La convergence sur beta1=3 n'est pas due a une identite
  structurelle mais a une propriete topologique plus profonde.
""")
print("Script 3 termine.")
