# -*- coding: utf-8 -*-
"""
PDL_metric_distance_script5.py
Session 65 (suite) — la charpente en chaine EMERGE-t-elle d'une regle de croissance
motivee par BH-1 (D37, theoreme), plutot que d'etre imposee a la main (script4) ?

MECANISME (fonde sur BH-1, deja theoreme - pas une invention) :
BH-1 etablit que l'interieur d'une structure devient GELE (une seule configuration),
seule la SURFACE ACTIVE (un sous-ensemble BORNE et RECENT de la structure) reste libre
de participer a de nouveaux engagements. On modelise cela simplement : chaque nouvel
amas ne peut s'attacher qu'a un amas appartenant a un ensemble "actif" de taille FIXE W
(les W derniers amas ajoutes, PAS toute la structure) -- pas a n'importe quel amas
ancien (deja gele).

On compare :
- W petit (surface active etroite, ex: W=5) -> croissance par accretion sur une
  frontiere bornee, mecanisme motive par BH-1.
- W = N (tous les amas restent "actifs" indefiniment) -> equivaut au cas aleatoire
  deja teste (script1), pour verifier la coherence.
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

def build_accretion_backbone(n_clusters, W, seed=0):
    """
    Construit la charpente inter-amas par accretion : chaque nouvel amas (index c)
    s'attache a UN amas choisi au hasard parmi les W derniers amas ajoutes (la
    'surface active', motivee par BH-1) -- pas a n'importe quel amas ancien.
    W=1 : chaine pure (chaque nouvel amas s'attache forcement au precedent).
    W=N : equivalent au cas aleatoire deja teste (toute la structure reste 'active').
    """
    rng = np.random.default_rng(seed)
    G = nx.Graph()
    G.add_node(0)
    for c in range(1, n_clusters):
        active_pool = list(range(max(0, c - W), c))  # les W derniers amas ajoutes
        target = rng.choice(active_pool)
        G.add_edge(c, target)
    return G

print("=== Diametre de la charpente inter-amas, croissance par accretion sur une surface")
print("    active de largeur W (motivee par BH-1, theoreme deja acquis) ===\n")

n_clusters_values = [100, 300, 1000, 3000, 10000, 30000, 100000]
W_values = [1, 5, 20, 100, "N (aleatoire complet)"]

results = {}
for W_label in W_values:
    diams = []
    for nc in n_clusters_values:
        W = nc if W_label == "N (aleatoire complet)" else W_label
        G = build_accretion_backbone(nc, W, seed=42)
        d = diameter_estimate(G, n_samples=min(20, nc), seed=42)
        diams.append(d)
    results[W_label] = diams
    print(f"W={str(W_label):>22} : diametres = {diams}")

print(f"\n=== Exposants ajustes (diam ~ N^p) ===\n")
logN = np.log(n_clusters_values)
for W_label, diams in results.items():
    slope, _ = np.polyfit(logN, np.log(diams), 1)
    print(f"W={str(W_label):>22} : p_fit = {slope:.4f}")

print("\n=== Interpretation ===")
print("W petit (surface active etroite et BORNEE, motivee par BH-1) -> exposant attendu proche de 1 (chaine).")
print("W=N (aucune notion de surface bornee, toute la structure reste accessible) -> exposant attendu proche de 0 (deja confirme script1).")
print("Si la transition est nette entre les deux, la largeur de la surface active W")
print("EST la variable causale recherchee depuis le debut du pivot A -- et elle est")
print("directement liee a un theoreme deja acquis (BH-1), pas a une regle inventee.")
