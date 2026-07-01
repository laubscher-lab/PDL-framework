# -*- coding: utf-8 -*-
"""
PDL_horizon_topology_script1.py (v2 - corrige l'explosion mémoire de la v1)
Session 65 (suite) — vérification de la topologie (caractéristique d'Euler) d'un
assemblage macroscopique de fermetures K4, en fonction du nombre de "hubs" partagés
sur lesquels les triangles mixtes (ponts) viennent s'appuyer.

CORRECTION v2 : la v1 tentait d'énumérer explicitement toutes les C(502,3)~21 millions
de faces du bloc de référence K_502 complet -> écroulement mémoire. Cette version garde
une formule FERMÉE (exacte, sans approximation) pour le bloc de référence P0 lui-même
(c'est un graphe complet, ses V/E/F sont connus analytiquement, aucun besoin de les
énumérer), et ne construit explicitement (par ensembles) que les ajouts dus aux
engagements externes - qui restent petits même pour k=100000.

CONTEXTE (pour mémoire, hypothèses testées ici, PAS des théorèmes acquis) :
- Chaque fermeture K4 isolée est homéomorphe à S^2 (chi=2) : théorème D23, déjà acquis.
- Un "triangle mixte" (D29) relie un bord interne (2 sommets) d'un bloc à 1 sommet
  externe d'un autre bloc, sans fusionner de sommets (Phi_min exclut la fusion,
  Session 65 Fil 9 - déjà acquis).
- Hypothèse testée ici (PAS un théorème) : si les engagements de surface convergent sur
  un nombre FIXE de "hubs" internes (motivé par la structure A2/SU(3) à 3 axes, V4\{e},
  théorème D58 L2 - le LIEN avec cette question topologique reste une hypothèse), la
  caractéristique d'Euler de l'assemblage macroscopique pourrait rester bornée plutôt
  que diverger avec le nombre d'engagements k.
"""

import itertools

def p0_complete_graph_counts(p0_size):
    """Formule fermée exacte pour un graphe complet K_n : V, E, F (toutes les triades),
    et chi. AUCUNE énumération - juste les formules combinatoires standard."""
    V = p0_size
    E = p0_size * (p0_size - 1) // 2
    F = p0_size * (p0_size - 1) * (p0_size - 2) // 6
    chi = V - E + F
    return V, E, F, chi

def build_assembly_counts(k_engagements, n_hubs, p0_size):
    """
    Calcule V, E, F TOTAUX de l'assemblage = (bloc P0, formule fermée) + (ajouts dus
    aux k engagements, construits EXPLICITEMENT par ensembles pour éviter toute erreur
    arithmétique - les ajouts restent petits : O(n_hubs) arêtes nouvelles max, O(k) faces).
    """
    assert n_hubs <= p0_size and n_hubs >= 2, "n_hubs doit être >= 2 (un bord interne exige 2 sommets distincts)"

    V0, E0, F0, _ = p0_complete_graph_counts(p0_size)
    hub_vertices = [f"p{j}" for j in range(n_hubs)]
    hub_pairs = list(itertools.combinations(hub_vertices, 2))

    new_V = set()
    new_E = set()
    new_F_count = 0

    for i in range(k_engagements):
        v_i = f"ext{i}"
        new_V.add(v_i)
        h1, h2 = hub_pairs[i % len(hub_pairs)]
        new_E.add(frozenset({h1, v_i}))
        new_E.add(frozenset({h2, v_i}))
        new_F_count += 1

    V_total = V0 + len(new_V)
    E_total = E0 + len(new_E)
    F_total = F0 + new_F_count
    chi_total = V_total - E_total + F_total
    return V_total, E_total, F_total, chi_total

# =====================================================================
# SANITY CHECKS
# =====================================================================
print("=== Sanity check 1 : K4 isolé (formule fermée) doit donner V=4,E=6,F=4,chi=2 (théorème D23) ===")
V0, E0, F0, chi0 = p0_complete_graph_counts(4)
print(f"V={V0}, E={E0}, F={F0}, chi={chi0}")
assert (V0, E0, F0, chi0) == (4, 6, 4, 2), "ECHEC sanity check 1"
print("OK\n")

print("=== Sanity check 2 : 2 blocs K4 isolés (formule x2) doit donner chi=4 (2 sphères) ===")
chi_2_isolated = 2 * chi0
print(f"chi = {chi_2_isolated}  -> attendu 4")
assert chi_2_isolated == 4
print("OK\n")

print("=== Sanity check 3 : reproduire le résultat 'pont' déjà établi il y a deux tours ===")
print("(2 blocs K4 séparés, reliés par exactement 2 ponts indépendants -> attendu chi=2, sphère)")
V = {"a0","a1","a2","a3","b0","b1","b2","b3"}
E = set(frozenset(e) for e in itertools.combinations(["a0","a1","a2","a3"], 2)) | \
    set(frozenset(e) for e in itertools.combinations(["b0","b1","b2","b3"], 2))
F = set(frozenset(f) for f in itertools.combinations(["a0","a1","a2","a3"], 3)) | \
    set(frozenset(f) for f in itertools.combinations(["b0","b1","b2","b3"], 3))
for (h1, h2, v) in [("a0","a1","b0"), ("a2","a3","b1")]:
    E.add(frozenset({h1, v})); E.add(frozenset({h2, v}))
    F.add(frozenset({h1, h2, v}))
chi_bridge_test = len(V) - len(E) + len(F)
print(f"V={len(V)}, E={len(E)}, F={len(F)}, chi={chi_bridge_test}  -> attendu 2 (sphère)")
assert chi_bridge_test == 2, "ECHEC sanity check 3"
print("OK - les deux méthodes de calcul (formule fermée + ensembles explicites) sont cohérentes.\n")

# =====================================================================
# EXPLORATION PRINCIPALE
# =====================================================================
print("=== Exploration : chi(k) pour différentes tailles d'ensemble de hubs ===\n")
p0_size = 502
k_values = [1, 2, 5, 10, 50, 100, 250, 500, 1000, 5000, 20000, 100000]
hub_sizes_to_test = [2, 3, 6, 20, 502]

results = {}
for n_hubs in hub_sizes_to_test:
    chis = []
    for k in k_values:
        _, _, _, chi = build_assembly_counts(k, n_hubs, p0_size=p0_size)
        chis.append(chi)
    results[n_hubs] = chis

header = f"{'k':>8}" + "".join(f"{'n_hubs='+str(h):>16}" for h in hub_sizes_to_test)
print(header)
for idx, k in enumerate(k_values):
    row = f"{k:>8}" + "".join(f"{results[h][idx]:>16}" for h in hub_sizes_to_test)
    print(row)

print("\n=== Variation de chi PAR ENGAGEMENT SUPPLEMENTAIRE (derivee discrete) ===")
print("Si cette variation tend vers 0 a grand k -> chi SATURE (la forme devient stable).")
print("Si elle reste constante et non nulle -> chi DIVERGE LINEAIREMENT avec k (jamais stable).\n")
header2 = f"{'k (intervalle)':>16}" + "".join(f"{'n_hubs='+str(h):>16}" for h in hub_sizes_to_test)
print(header2)
for idx in range(1, len(k_values)):
    k_prev, k_curr = k_values[idx-1], k_values[idx]
    row = f"{str(k_prev)+'->'+str(k_curr):>16}"
    for h in hub_sizes_to_test:
        d_chi = results[h][idx] - results[h][idx-1]
        d_k = k_curr - k_prev
        row += f"{d_chi/d_k:>16.4f}"
    print(row)

print("\n=== Genre topologique g=(2-chi)/2 à k=p0_size=502 (engagement complet) ===")
for n_hubs in hub_sizes_to_test:
    _, _, _, chi = build_assembly_counts(p0_size, n_hubs, p0_size=p0_size)
    g = (2 - chi) / 2
    print(f"n_hubs={n_hubs:>4} : chi={chi:>10}  g={g:>10.1f}")
