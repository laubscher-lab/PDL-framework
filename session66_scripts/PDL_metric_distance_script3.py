# -*- coding: utf-8 -*-
"""
PDL_metric_distance_script3.py
Session 65 (suite) — test : la fermeture triadique (mecanisme NATIF de PDL : un triangle
mixte cree naturellement un lien entre les DEUX partenaires d'un meme troisieme noeud)
suffit-elle, a elle seule, a deplacer le reseau hors du regime "petit monde" (log N),
SANS inventer de nouvelle metrique externe ?

IDEE (pas une nouvelle hypothese PDL, juste une consequence STRUCTURELLE du mecanisme
de triangle mixte deja etabli, D29) : si un nucleon C s'engage preferentiellement avec
des partenaires DEJA engages avec ses propres partenaires (plutot qu'avec n'importe qui
au hasard dans tout l'assemblage), le reseau resultant a, par construction, plus de
triangles que l'aleatoire pur (script precedent) -- on teste si CA SEUL change la loi
d'echelle du diametre.

METHODE : modele de Holme-Kim (croissance avec biais de fermeture triadique explicite,
standard en theorie des graphes, PAS une invention PDL) avec degre cible ~20 (Z_sat),
en faisant varier la probabilite de fermeture triadique p_triangle de 0 (aleatoire pur,
deja teste) a 1 (fermeture maximale).
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

N_values = [200, 500, 1000, 3000, 10000, 30000]
p_triangle_values = [0.0, 0.3, 0.6, 0.9, 0.99]
m_edges = 10  # ~degre cible 2*m=20, coherent avec Z_sat

print("=== Diametre(N) pour differents niveaux de fermeture triadique (Holme-Kim, m=10 -> degre~20) ===\n")
results = {}
for p_tri in p_triangle_values:
    diams = []
    for N in N_values:
        G = nx.powerlaw_cluster_graph(N, m=m_edges, p=p_tri, seed=42)
        d = diameter_estimate(G, n_samples=20, seed=42)
        diams.append(d)
    results[p_tri] = diams
    avg_clustering = nx.average_clustering(nx.powerlaw_cluster_graph(min(N_values[-1],5000), m=m_edges, p=p_tri, seed=42))
    print(f"p_triangle={p_tri:.2f} (clustering moyen ~{avg_clustering:.3f}) : diametres = {diams}")

print(f"\n=== Exposants ajustes (diam ~ N^p) pour chaque niveau de fermeture triadique ===\n")
logN = np.log(N_values)
for p_tri, diams in results.items():
    slope, _ = np.polyfit(logN, np.log(diams), 1)
    print(f"p_triangle={p_tri:.2f} : exposant ajuste p_fit = {slope:.4f}")

print("\n=== Interpretation ===")
print("Si p_fit AUGMENTE de facon significative avec p_triangle (s'eloigne de 0 vers 1/3 ou plus),")
print("la fermeture triadique -- un mecanisme DEJA natif a PDL (le triangle mixte lui-meme,")
print("pas une nouvelle hypothese) -- est une piste reelle pour sortir du regime petit-monde,")
print("SANS avoir besoin d'inventer une metrique spatiale externe.")
print("Si p_fit reste proche de 0 meme a p_triangle=0.99, la fermeture triadique seule NE SUFFIT")
print("PAS -- il faudrait alors un ingredient supplementaire, encore non identifie.")
