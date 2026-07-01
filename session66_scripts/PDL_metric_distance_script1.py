# -*- coding: utf-8 -*-
"""
PDL_metric_distance_script1.py
Session 65 (suite) — Pivot A : attaque directe d'OP-D64-3 (métrique relationnelle manquante).

IDEE TESTEE (pas un théorème, une hypothèse de travail) :
Si la pseudométrique de coût de cohérence J(C1,C2) (D08, jamais construite) se traduit,
au premier ordre, par une distance de graphe (nombre de sauts relationnels, cohérent avec
le taux de propagation fini déjà déduit de D33 — discuté plus tôt cette session), alors
on peut TESTER, sur le réseau déjà établi (chaque nucléon limité à Z_sat~20 voisins
directs, D40, théorème), comment le diamètre du réseau (distance centre->bord) croît
avec N -- SANS halls de comptage de paires, juste de la pure théorie des graphes sur une
structure déjà acquise.

POURQUOI C'EST IMPORTANT : la cible Bekenstein-Hawking (aire ~ N^2) suppose un rayon
physique R ~ N (rayon de Schwarzschild, PAS R~N^(1/3) comme la matière ordinaire). Si le
réseau PDL déjà établi a un diamètre de graphe qui croît comme N (lui-même), il y a un
chemin de coherence vers la cible. S'il croît comme N^(1/3) (matière ordinaire géométrique)
ou comme log(N) (réseau "petit monde", typique des graphes a degré borné), c'est un FAIT
NOUVEAU et IMPORTANT a interpreter honnêtement (potentiellement un autre echec, ou un
indice sur ce qui doit changer structurellement a tres haute densite).

METHODE : construction explicite (pas de formule devinée) d'un graphe a degré borné par
Z_sat (~20), puis calcul du diamètre / distance moyenne par BFS (recherche en largeur),
pour plusieurs N, puis ajustement (regression log-log) pour identifier l'exposant réel de
la loi d'échelle diamètre(N) ~ N^p ou diamètre(N) ~ log(N).
"""

import networkx as nx
import numpy as np

ZSAT = 20  # D40, theoreme (arrondi a l'entier pour la construction du graphe)

def build_saturated_network(N, degree=ZSAT, seed=0):
    """
    Construit un graphe ALEATOIRE REGULIER de degre fixe (chaque noeud a EXACTEMENT
    `degree` voisins), modelisant le reseau de couplage nucleon-nucleon SATURE (chaque
    nucleon engage Z_sat partenaires, pas plus - deja theoreme D40). Aleatoire car on n'a
    PAS encore de regle PDL qui dit PRECISEMENT qui se connecte a qui (c'est exactement
    OP-D64-3, le probleme qu'on attaque) - le graphe aleatoire regulier est le modele le
    PLUS NEUTRE possible compatible avec la seule contrainte connue et prouvee (degre
    borne par Z_sat), sans ajouter d'hypothese supplementaire non justifiee.
    """
    if (N * degree) % 2 != 0:
        N += 1  # random_regular_graph exige N*degree pair
    G = nx.random_regular_graph(degree, N, seed=seed)
    return G

def diameter_and_avg_path(G, n_samples=50, seed=0):
    """Calcul par BFS depuis des noeuds echantillonnes (le diametre exact est couteux a
    grande echelle ; on estime via le maximum de distance observee sur un echantillon de
    sources, methode standard et honnete pour de grands graphes)."""
    rng = np.random.default_rng(seed)
    nodes = list(G.nodes())
    sample = rng.choice(nodes, size=min(n_samples, len(nodes)), replace=False)
    max_dist = 0
    all_dists = []
    for s in sample:
        lengths = nx.single_source_shortest_path_length(G, s)
        m = max(lengths.values())
        max_dist = max(max_dist, m)
        all_dists.extend(lengths.values())
    avg_dist = np.mean(all_dists)
    return max_dist, avg_dist

# =====================================================================
# SANITY CHECK : un graphe regulier de degre d sur N noeuds doit avoir un diametre
# de l'ordre de log(N)/log(d-1) (fait standard de theorie des graphes aleatoires,
# PAS une hypothese PDL - on verifie juste que notre construction se comporte normalement)
# =====================================================================
print("=== Sanity check : comportement 'petit monde' attendu pour un graphe regulier ===")
N_test = 1000
G_test = build_saturated_network(N_test, degree=ZSAT)
diam, avg = diameter_and_avg_path(G_test, n_samples=30)
expected_log = np.log(N_test) / np.log(ZSAT - 1)
print(f"N={N_test}, degree={ZSAT} : diametre estime={diam}, distance moyenne={avg:.2f}")
print(f"Prediction theorique standard (petit monde) : ~log(N)/log(d-1) = {expected_log:.2f}")
print(f"(Les deux devraient etre du meme ordre de grandeur si la construction est correcte)\n")

# =====================================================================
# EXPLORATION PRINCIPALE : diametre(N) pour le reseau sature, sur plusieurs ordres
# de grandeur de N, ajustement de la loi d'echelle
# =====================================================================
print("=== Exploration : diametre du reseau sature en fonction de N ===\n")
N_values = [100, 300, 1000, 3000, 10000, 30000, 100000, 300000]
diameters = []
avg_dists = []

for N in N_values:
    G = build_saturated_network(N, degree=ZSAT, seed=42)
    diam, avg = diameter_and_avg_path(G, n_samples=30, seed=42)
    diameters.append(diam)
    avg_dists.append(avg)
    print(f"N={N:>7} : diametre estime={diam:>4}, distance moyenne={avg:>7.3f}")

# =====================================================================
# Ajustement : comparer 3 lois candidates
# =====================================================================
print("\n=== Test de 3 lois d'echelle candidates (regression sur les donnees ci-dessus) ===\n")
logN = np.log(N_values)
log_diam = np.log(diameters)

# (a) loi de puissance : diam ~ N^p
slope_power, intercept_power = np.polyfit(logN, log_diam, 1)
print(f"(a) Loi de puissance diam ~ N^p : exposant ajuste p = {slope_power:.4f}")
print(f"    -> N^(1/3) attendu si geometrie 3D ordinaire : p=0.333")
print(f"    -> N^1 attendu si echelle Schwarzschild directe : p=1.000")

# (b) loi logarithmique : diam ~ a*log(N) + b
log_log_N = np.log(np.log(N_values))  # juste pour comparaison visuelle, pas un vrai test ici
a_log, b_log = np.polyfit(np.log(N_values), diameters, 1)
print(f"\n(b) Loi logarithmique diam ~ a*ln(N)+b : a={a_log:.4f}, b={b_log:.4f}")
predicted_log = [a_log*np.log(n)+b_log for n in N_values]
residuals_log = [abs(d-p) for d,p in zip(diameters,predicted_log)]
print(f"    Residus moyens (log) : {np.mean(residuals_log):.4f}")

residuals_power = [abs(np.log(d) - (slope_power*np.log(n)+intercept_power)) for d,n in zip(diameters,N_values)]
print(f"    Residus moyens (puissance, en log) : {np.mean(residuals_power):.4f}")

print(f"\n=> Conclusion a verifier : si (b) ajuste BEAUCOUP mieux que (a) avec p proche de 1/3 ou 1,")
print(f"   le reseau SATURE actuel (degre borne, Z_sat) est de type 'petit monde' (log N),")
print(f"   PAS de type geometrique ordinaire (N^1/3) NI de type horizon (N^1).")
print(f"   Cela signifierait que la SATURATION ELLE-MEME (degre fixe Z_sat) est incompatible")
print(f"   avec une distance physique 3D coherente -- un nouveau diagnostic, pas encore vu cette session.")
