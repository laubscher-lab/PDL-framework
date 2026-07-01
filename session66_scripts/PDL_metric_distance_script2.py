# -*- coding: utf-8 -*-
"""
PDL_metric_distance_script2.py
Session 65 (suite) — test de la VRAIE variable : aleatoire vs local, a degre fixe.

HYPOTHESE TESTEE : ce n'est pas le DEGRE (nombre de connexions par noeud) qui determine
si le diametre croit en log(N), N^(1/3) ou N -- c'est si les connexions sont ALEATOIRES
(partenaire choisi n'importe ou dans le reseau) ou LOCALES (partenaire choisi parmi des
voisins deja proches, selon UNE METRIQUE PREEXISTANTE).

Trois constructions, TOUTES a petit degre fixe (pas de croissance avec N) :
(a) Graphe aleatoire regulier, degre Z_sat~20 (deja teste, script precedent -> log N)
(b) Grille reguliere 3D, degre 6 (chaque noeud relie a ses 6 voisins immediats dans un
    cube N^(1/3) x N^(1/3) x N^(1/3)) -- modelise une matiere ORDINAIRE, deja plongee
    dans un espace 3D pre-existant (PAS construit depuis C1-C4, juste un point de
    comparaison externe connu)
(c) Anneau (chaine fermee), degre 2 -- cas le plus pauvre possible

SI (b) donne bien diam~N^(1/3) et (c) donne bien diam~N, MAIS (a) donne log(N) malgre
un degre INTERMEDIAIRE (20, entre 2 et 6) -- la conclusion est que LE DEGRE N'EST PAS
LA VARIABLE CAUSALE. C'est la LOCALITE (une notion de proximite/metrique preexistante)
qui determine la loi d'echelle, pas le nombre de connexions. Et PDL, a ce stade, n'a
PRECISEMENT aucune notion de proximite (c'est OP-D64-3 lui-meme) -- donc le reseau
qu'on peut construire AUJOURD'HUI avec les seuls outils prouves (Z_sat, degre borne,
SANS metrique) est NECESSAIREMENT du type (a), quel que soit le degre choisi.
"""

import networkx as nx
import numpy as np

def diameter_estimate(G, n_samples=20, seed=0):
    rng = np.random.default_rng(seed)
    nodes = list(G.nodes())
    idx = rng.choice(len(nodes), size=min(n_samples, len(nodes)), replace=False)
    sample = [nodes[i] for i in idx]
    max_dist = 0
    for s in sample:
        lengths = nx.single_source_shortest_path_length(G, s)
        max_dist = max(max_dist, max(lengths.values()))
    return max_dist

N_values = [125, 1000, 3375, 8000, 27000, 64000]  # cubes parfaits pour la grille 3D : 5^3,10^3,15^3,20^3,30^3,40^3

print(f"{'N':>8} {'(a) aleatoire d=20':>20} {'(b) grille 3D d=6':>20} {'(c) anneau d=2':>16}\n")

results_a, results_b, results_c = [], [], []
for N in N_values:
    side = round(N ** (1/3))
    N_grid = side**3  # ajuste N exactement a un cube parfait pour la grille

    # (a) aleatoire, degre 20
    Ga = nx.random_regular_graph(20, N if (N*20)%2==0 else N+1, seed=42)
    da = diameter_estimate(Ga, seed=42)

    # (b) grille 3D, degre 6 (periodique pour eviter les effets de bord -> tore 3D)
    Gb = nx.grid_graph(dim=[side, side, side], periodic=True)
    db = diameter_estimate(Gb, seed=42)

    # (c) anneau, degre 2
    Gc = nx.cycle_graph(N)
    dc = diameter_estimate(Gc, seed=42)

    results_a.append(da); results_b.append(db); results_c.append(dc)
    print(f"{N_grid:>8} {da:>20} {db:>20} {dc:>16}")

logN = np.log(N_values)
for label, res in [("(a) aleatoire d=20", results_a), ("(b) grille 3D d=6", results_b), ("(c) anneau d=2", results_c)]:
    slope, _ = np.polyfit(logN, np.log(res), 1)
    print(f"\n{label} : exposant de loi de puissance ajuste p = {slope:.4f}  (attendu : a~0(log), b~0.333, c~1.0)")

print("\n=== Interpretation ===")
print("Si (a) reste proche de 0 (log N) alors que (b) et (c) collent a leurs exposants")
print("geometriques attendus (1/3 et 1), la conclusion est : LE DEGRE N'EST PAS LA VARIABLE")
print("CAUSALE -- c'est la LOCALITE qui compte, et PDL (avec seulement Z_sat, sans metrique)")
print("ne PEUT PAS, structurellement, produire autre chose que (a), quel que soit le degre choisi.")
