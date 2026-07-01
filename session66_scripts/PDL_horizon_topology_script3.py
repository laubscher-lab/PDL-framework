# -*- coding: utf-8 -*-
"""
PDL_horizon_topology_script3.py
Session 65 (suite) — script 3 : test de la contrainte de parité des ponts à N > 2 blocs.

PIEGE METHODOLOGIQUE A EVITER (identifié avant de coder, pas après) :
chi = V - E + F ne dépend QUE des totaux (nombre de sommets, arêtes, faces) -- PAS de
QUI est relié à QUI. Donc obtenir chi=2 ne suffit JAMAIS à conclure qu'on a une seule
sphère : un assemblage pourrait avoir chi=2 globalement tout en étant en réalité
DECONNECTE (par exemple une sphère isolée + une paire d'objets de genres opposés qui
se compensent numériquement sans former un seul objet). On vérifie donc ICI deux
conditions INDEPENDANTES et OBLIGATOIRES : (a) chi=2, ET (b) connexité totale (un seul
morceau), via un vrai graphe NetworkX, pas une formule.

RAPPEL DES FAITS DEJA ETABLIS CETTE SESSION (a ne pas redémontrer, juste réutiliser) :
- 1 bloc K4 isolé : chi=2 (théorème D23).
- N blocs K4 isolés (aucun pont) : chi = 2N (additif, trivial).
- 1 pont entre 2 sommets déjà existants (aucun nouveau sommet) : Δchi = -1 exactement
  (vérifié scripts 1 et 2, cohérent avec la théorie des surfaces : connect-sum).
- 2 ponts indépendants entre 2 blocs : chi=2 ET connexe -> sphère unique confirmée
  (sanity check script 2).

QUESTION DE CE SCRIPT : pour N>2 blocs, quelle distribution du nombre total de ponts
B donne a la fois chi=2 ET la connexité complète ? Est-ce que "2 ponts par paire
directement reliée" (l'intuition naïve généralisant le cas N=2) est nécessaire, ou
existe-t-il des distributions plus économiques (ex: un arbre couvrant doublé) qui
suffisent également ?
"""

import itertools
import networkx as nx

def build_n_blocks(n_blocks, bridge_list, block_size=4):
    """
    n_blocks : nombre de blocs K_{block_size} isolés au départ.
    bridge_list : liste de tuples (i, j, hub_i, hub_i2, hub_j) où i,j sont les indices
                  de deux blocs distincts, et on forme un triangle mixte en utilisant
                  2 sommets du bloc i (hub_i, hub_i2, déjà existants, formant un bord
                  interne réel du bloc i) + 1 sommet du bloc j (hub_j, déjà existant).
                  AUCUN nouveau sommet n'est créé par un pont (cohérent avec D29 :
                  un triangle mixte réutilise un bord interne existant + 1 sommet
                  externe existant - jamais un sommet neuf).
    Retourne : V (set), E (set de frozenset), F (set de frozenset), et le graphe
    NetworkX (pour test de connexité, indépendant du calcul de chi).
    """
    V, E, F = set(), set(), set()
    blocks = []
    for b in range(n_blocks):
        verts = [f"b{b}_v{k}" for k in range(block_size)]
        blocks.append(verts)
        V |= set(verts)
        E |= set(frozenset(e) for e in itertools.combinations(verts, 2))
        F |= set(frozenset(f) for f in itertools.combinations(verts, 3))

    for (i, j, hi1, hi2, hj) in bridge_list:
        h1 = blocks[i][hi1]
        h2 = blocks[i][hi2]
        v  = blocks[j][hj]
        E.add(frozenset({h1, v}))
        E.add(frozenset({h2, v}))
        F.add(frozenset({h1, h2, v}))

    chi = len(V) - len(E) + len(F)

    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(tuple(e) for e in E)
    is_connected = nx.is_connected(G)
    n_components = nx.number_connected_components(G)

    return chi, is_connected, n_components, len(V), len(E), len(F)

# =====================================================================
# SANITY CHECKS (reproduire exactement ce qui est déjà établi, avant d'aller plus loin)
# =====================================================================
print("=== Sanity check 1 : N=2 blocs, 0 pont -> chi=4, DECONNECTE (2 composantes) ===")
chi, conn, ncomp, V, E, F = build_n_blocks(2, [])
print(f"chi={chi}, connexe={conn}, composantes={ncomp}  -> attendu chi=4, connexe=False, composantes=2")
assert chi == 4 and not conn and ncomp == 2
print("OK\n")

print("=== Sanity check 2 : N=2 blocs, 2 ponts indépendants -> chi=2, CONNEXE (résultat déjà établi) ===")
bridges = [(0, 1, 0, 1, 0), (0, 1, 2, 3, 1)]  # 2 ponts utilisant des sommets différents des deux côtés
chi, conn, ncomp, V, E, F = build_n_blocks(2, bridges)
print(f"chi={chi}, connexe={conn}, composantes={ncomp}  -> attendu chi=2, connexe=True, composantes=1")
assert chi == 2 and conn and ncomp == 1
print("OK\n")

print("=== Sanity check 3 : N=2 blocs, 1 SEUL pont -> chi=3, mais DEJA connexe (cas non-sphère) ===")
chi, conn, ncomp, V, E, F = build_n_blocks(2, [(0, 1, 0, 1, 0)])
print(f"chi={chi}, connexe={conn}, composantes={ncomp}  -> attendu chi=3, connexe=True (1 pont suffit a connecter,")
print(f"  mais chi=3 n'est PAS une sphère valide -> confirme que connexité seule NE SUFFIT PAS non plus,")
print(f"  il faut les DEUX conditions simultanément : chi=2 ET connexe.")
assert chi == 3 and conn and ncomp == 1
print("OK\n")

# =====================================================================
# EXPLORATION 1 : N=3 blocs, plusieurs distributions de ponts pour le MEME total B
# =====================================================================
print("=== Exploration 1 : N=3 blocs (chi isolé = 6, besoin théorique B=2N-2=4 ponts pour chi=2) ===\n")

scenarios = {
    "A: 2+2 (chaîne, doublée a chaque maillon)": [
        (0,1,0,1,0), (0,1,2,3,1),   # 2 ponts entre bloc 0 et bloc 1
        (1,2,0,1,0), (1,2,2,3,1),   # 2 ponts entre bloc 1 et bloc 2
    ],
    "B: 4 ponts repartis en etoile (tous depuis bloc 0, B=4)": [
        (0,1,0,1,0), (0,1,2,3,1),
        (0,2,0,1,0), (0,2,2,3,1),
    ],
    "C: arbre couvrant simple NON double (B=2, minimal pour connexite seule)": [
        (0,1,0,1,0), (1,2,0,1,0),
    ],
    "D: B=4 mais mal distribue (3 ponts bloc0-bloc1, 1 seul bloc1-bloc2)": [
        (0,1,0,1,0), (0,1,2,3,1), (0,1,0,2,0),
        (1,2,0,1,0),
    ],
}

for name, bridges in scenarios.items():
    chi, conn, ncomp, V, E, F = build_n_blocks(3, bridges)
    valid_sphere = (chi == 2 and conn)
    print(f"{name}")
    print(f"   B={len(bridges)} ponts -> chi={chi}, connexe={conn}, composantes={ncomp}  => {'SPHERE VALIDE' if valid_sphere else 'PAS une sphere valide'}")
print()

# =====================================================================
# EXPLORATION 2 : généralisation systématique - structure en chaîne doublée, N=3..10
# =====================================================================
print("=== Exploration 2 : la structure 'chaîne doublée' (2 ponts par maillon consécutif) généralise-t-elle ? ===\n")
for n_blocks in range(2, 11):
    bridges = []
    for k in range(n_blocks - 1):
        bridges.append((k, k+1, 0, 1, 0))
        bridges.append((k, k+1, 2, 3, 1))
    chi, conn, ncomp, V, E, F = build_n_blocks(n_blocks, bridges)
    valid_sphere = (chi == 2 and conn)
    print(f"N={n_blocks:>3} blocs, chaîne doublée, B={len(bridges):>3} ponts (= 2(N-1)) "
          f"-> chi={chi:>4}, connexe={conn}, composantes={ncomp}  => {'SPHERE VALIDE' if valid_sphere else 'ECHEC'}")

print("\n=== Conclusion à vérifier ===")
print("Si TOUS les N de l'exploration 2 donnent 'SPHERE VALIDE' : la règle 'doubler chaque")
print("arête d'un arbre couvrant' (B=2(N-1) ponts) généralise PROPREMENT a N>2, et la 'parité'")
print("se reformule ainsi : ce n'est pas une parité par paire isolée, mais un arbre couvrant")
print("dont CHAQUE arête doit être doublée -- une règle topologique précise, pas un simple compte.")
