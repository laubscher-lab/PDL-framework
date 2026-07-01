# -*- coding: utf-8 -*-
"""
PDL_metric_distance_script4.py
Session 65 (suite) — test du modele HYBRIDE : amas locaux satures (Z_sat~20, deja
theoreme D40, satisfait la liaison) relies par une charpente GLOBALE econome
(arbre couvrant doublé, motive par Phi_min, deja theoreme, Session 65 Fil 9).

HYPOTHESE (motivee par deux theoremes deja acquis, combines pour la premiere fois
sous cet angle - pas une nouvelle invention) :
- Localement : chaque amas de ~Z_sat nucleons forme un sous-graphe dense (satisfait
  la capacite de liaison prouvee, D40).
- Globalement : les amas eux-memes sont relies par le MINIMUM necessaire pour rester
  une sphere topologique valide (arbre couvrant doublé, script3 de cette session).
On teste si CETTE structure hybride change la loi d'echelle du diametre, par rapport
au reseau purement aleatoire dense (script1) et au reseau a fermeture triadique
(script3), aucun des deux n'ayant suffi.
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

def build_hybrid(n_clusters, cluster_size=20, backbone="tree"):
    """
    n_clusters amas de taille cluster_size (~Z_sat), chacun un graphe DENSE interne
    (degre eleve, satisfait la liaison locale, D40).
    Les amas sont relies entre eux par une charpente GLOBALE :
    - "tree"   : arbre couvrant MINIMAL entre amas (1 lien entre amas adjacents,
                 Phi_min - economie maximale, mais PAS de parite -> on verifie aussi)
    - "random" : meme nombre de liens inter-amas, mais distribues AU HASARD entre
                 n'importe quelle paire d'amas (comparaison, deja teste indirectement)
    """
    G = nx.Graph()
    cluster_nodes = []
    for c in range(n_clusters):
        # amas dense : graphe aleatoire dense interne (degre eleve, ~cluster_size-1, complet ou presque)
        Gc = nx.gnp_random_graph(cluster_size, p=0.6, seed=c)
        mapping = {i: f"c{c}_n{i}" for i in Gc.nodes()}
        Gc = nx.relabel_nodes(Gc, mapping)
        G.add_nodes_from(Gc.nodes())
        G.add_edges_from(Gc.edges())
        cluster_nodes.append(list(Gc.nodes()))

    if backbone == "tree":
        # arbre couvrant MINIMAL entre amas (chaine simple, 1 lien par paire adjacente)
        for c in range(n_clusters - 1):
            u = cluster_nodes[c][0]
            v = cluster_nodes[c+1][0]
            G.add_edge(u, v)
    elif backbone == "random":
        # meme NOMBRE de liens inter-amas (n_clusters-1), mais entre amas choisis au hasard
        rng = np.random.default_rng(0)
        for _ in range(n_clusters - 1):
            c1, c2 = rng.choice(n_clusters, size=2, replace=False)
            u = cluster_nodes[c1][rng.integers(cluster_size)]
            v = cluster_nodes[c2][rng.integers(cluster_size)]
            G.add_edge(u, v)
    return G

print("=== Modele hybride : amas denses (Z_sat~20) + charpente globale en CHAINE (la plus econome) ===\n")
n_clusters_values = [5, 10, 30, 100, 300, 1000]
diams_tree = []
for nc in n_clusters_values:
    G = build_hybrid(nc, cluster_size=20, backbone="tree")
    N_total = nc * 20
    d = diameter_estimate(G, n_samples=min(20, nc), seed=42)
    diams_tree.append(d)
    print(f"n_clusters={nc:>5} (N_total={N_total:>6}) : diametre = {d}")

logN = np.log([nc*20 for nc in n_clusters_values])
slope_tree, _ = np.polyfit(logN, np.log(diams_tree), 1)
print(f"\nExposant ajuste (charpente en chaine) : p_fit = {slope_tree:.4f}  (attendu proche de 1.0 si chaine = lineaire)")

print("\n=== Comparaison : meme structure d'amas, mais charpente ALEATOIRE (meme nb de liens inter-amas) ===\n")
diams_rand = []
for nc in n_clusters_values:
    G = build_hybrid(nc, cluster_size=20, backbone="random")
    d = diameter_estimate(G, n_samples=min(20, nc), seed=42)
    diams_rand.append(d)
    print(f"n_clusters={nc:>5} : diametre = {d}")

slope_rand, _ = np.polyfit(logN, np.log(diams_rand), 1)
print(f"\nExposant ajuste (charpente aleatoire, meme nb de liens) : p_fit = {slope_rand:.4f}")

print("\n=== Interpretation ===")
print(f"Charpente en CHAINE (la plus econome, motivee par Phi_min) : exposant = {slope_tree:.3f}")
print(f"Charpente ALEATOIRE (meme nb de liens, mais mal distribues) : exposant = {slope_rand:.3f}")
print("Si la chaine donne un exposant proche de 1 et l'aleatoire reste proche de 0,")
print("alors CE N'EST PAS la densite locale (Z_sat) qui bloquait tout depuis le debut --")
print("c'est uniquement la FACON dont les amas eux-memes sont relies entre eux qui compte.")
