# -*- coding: utf-8 -*-
"""
PDL_horizon_topology_script2.py
Session 65 (suite) — script 2 : isole la VRAIE variable identifiée par le script 1.

CE QUE LE SCRIPT 1 A MONTRE (confirmé, sanity checks valides) :
chi ne dépend PAS du nombre de hubs internes réutilisés, tant que chaque engagement
amène un NOUVEAU partenaire externe distinct (1 sommet neuf, 2 aretes neuves, 1 face
neuve -> delta_chi=0 systematiquement, quel que soit le nombre de hubs).

NOUVELLE HYPOTHESE A TESTER ICI :
la variable qui contrôle vraiment chi n'est pas "combien de hubs internes" mais
"combien de connexions INDEPENDANTES un MEME partenaire externe donné établit avec
la surface". On fait varier ici m = nombre de triangles mixtes distincts formés avec
UN SEUL partenaire externe fixe (sans lui ajouter de nouveaux sommets - un partenaire
réel, physique, a un nombre fini et petit de "points de contact" possibles, pas un par
triangle), et on regarde comment chi évolue avec m, PUIS comment il évolue quand on
répète ce schéma pour N partenaires différents simultanément (le cas réaliste d'un
assemblage macroscopique).

Toujours : formule fermée pour P0 (évite l'explosion mémoire), comptage explicite par
ensembles uniquement pour les ajouts (évite les erreurs arithmétiques).
"""

import itertools

def p0_complete_graph_counts(p0_size):
    V = p0_size
    E = p0_size * (p0_size - 1) // 2
    F = p0_size * (p0_size - 1) * (p0_size - 2) // 6
    chi = V - E + F
    return V, E, F, chi

def build_assembly_v2(N_partners, m_per_partner, partner_size, p0_size, n_hubs):
    """
    P0 : bloc de référence (formule fermée).
    N_partners : nombre de partenaires externes DISTINCTS (chacun ajoute partner_size
                 nouveaux sommets - un partenaire réaliste a une taille fixe, pas un
                 sommet par connexion).
    m_per_partner : nombre de triangles mixtes (connexions independantes) que CHAQUE
                 partenaire forme avec P0, en utilisant jusqu'à partner_size de ses
                 propres sommets comme "bord interne côté partenaire" excentré sur les
                 n_hubs hubs côté P0 (cyclé).
    Chaque partenaire est un graphe complet K_{partner_size} isolé (formule fermée),
    PLUS m_per_partner triangles mixtes le reliant à P0.
    """
    assert n_hubs <= p0_size and n_hubs >= 2
    assert m_per_partner <= partner_size, "un partenaire ne peut pas former plus de connexions que sa propre taille (pas de sommet réutilisé deux fois côté partenaire dans ce modèle simple)"

    V0, E0, F0, _ = p0_complete_graph_counts(p0_size)
    hub_vertices = [f"p{j}" for j in range(n_hubs)]
    hub_pairs = list(itertools.combinations(hub_vertices, 2))

    total_V_partners = 0
    total_E_partners = 0   # arêtes internes à chaque partenaire (formule fermée par partenaire)
    total_F_partners = 0
    new_E_bridge = set()
    new_F_bridge_count = 0

    for p_idx in range(N_partners):
        # Partenaire p_idx : graphe complet K_{partner_size}, sommets nommés uniquement
        Vp, Ep, Fp, _ = p0_complete_graph_counts(partner_size)
        total_V_partners += Vp
        total_E_partners += Ep
        total_F_partners += Fp

        partner_vertices = [f"P{p_idx}_q{j}" for j in range(partner_size)]
        for c in range(m_per_partner):
            h1, h2 = hub_pairs[c % len(hub_pairs)]
            v = partner_vertices[c]  # un sommet DIFFERENT du partenaire pour chaque connexion (déjà existant, pas nouveau)
            new_E_bridge.add(frozenset({h1, v}))
            new_E_bridge.add(frozenset({h2, v}))
            new_F_bridge_count += 1

    V_total = V0 + total_V_partners
    E_total = E0 + total_E_partners + len(new_E_bridge)
    F_total = F0 + total_F_partners + new_F_bridge_count
    chi_total = V_total - E_total + F_total
    return V_total, E_total, F_total, chi_total

# =====================================================================
# SANITY CHECKS
# =====================================================================
print("=== Sanity check : 1 partenaire K4 isolé (m=0), pas de pont -> chi = 2+2 = 4 ===")
_, _, _, chi_iso = build_assembly_v2(N_partners=1, m_per_partner=0, partner_size=4, p0_size=4, n_hubs=2)
print(f"chi = {chi_iso}  -> attendu 4")
assert chi_iso == 4
print("OK\n")

print("=== Sanity check : 1 partenaire K4, 1 SEULE connexion (m=1) -> attendu chi=3 (cas deja vu il y a deux tours) ===")
_, _, _, chi_1c = build_assembly_v2(N_partners=1, m_per_partner=1, partner_size=4, p0_size=4, n_hubs=2)
print(f"chi = {chi_1c}  -> attendu 3 (comparer au calcul 'k engages, independant, k=1' d'il y a deux tours)")
assert chi_1c == 3
print("OK\n")

# =====================================================================
# EXPLORATION 1 : un seul partenaire, on fait varier m (connexions independantes
# avec CE partenaire), pour confirmer que c'est bien CA qui fait chuter chi
# =====================================================================
print("=== Exploration 1 : chi en fonction de m (connexions a UN partenaire), partner_size=20 ===")
for m in [0, 1, 2, 4, 8, 16, 20]:
    _, _, _, chi = build_assembly_v2(N_partners=1, m_per_partner=m, partner_size=20, p0_size=502, n_hubs=20)
    print(f"  m={m:>3} : chi = {chi}")
print("(si chi decroit avec m -> confirme que 'connexions multiples a un meme partenaire' est bien la variable causale)\n")

# =====================================================================
# EXPLORATION 2 : le cas REALISTE -- N partenaires distincts, CHACUN formant un nombre
# REALISTE de connexions independantes m (pas juste 1 -- un nucleon engageant peut
# tres bien toucher plusieurs triangles mixtes a la fois, pas necessairement un seul).
# On regarde si chi reste stable (proche de 2) ou s'effondre, en fonction de m fixe,
# quand N grandit -- LA VRAIE QUESTION DE CETTE SESSION.
# =====================================================================
print("=== Exploration 2 (la question centrale) : N partenaires, chacun avec m connexions fixes ===")
print("(partner_size=20, p0_size=502, n_hubs=20 -- valeurs realistes Z_sat/R_surf)\n")
N_values = [1, 2, 5, 10, 19]   # limite a 19 (Z_sat~19.86, D22) - au-dela, P0 est sature par construction physique
m_values_to_test = [1, 2, 5, 10, 20]

header = f"{'N partenaires':>15}" + "".join(f"{'m='+str(m):>12}" for m in m_values_to_test)
print(header)
for N in N_values:
    row = f"{N:>15}"
    for m in m_values_to_test:
        try:
            _, _, _, chi = build_assembly_v2(N_partners=N, m_per_partner=m, partner_size=20, p0_size=502, n_hubs=20)
            row += f"{chi:>12}"
        except AssertionError:
            row += f"{'n/a':>12}"
    print(row)

print("\n=== Interprétation à vérifier ===")
print("Pour m=1 (chaque partenaire ne forme qu'UNE connexion) : chi devrait rester PROCHE de 2")
print("quel que soit N (cas 'pont simple', cohérent avec le mécanisme de base D29).")
print("Pour m grand (chaque partenaire forme PLUSIEURS connexions independantes) : chi devrait")
print("chuter d'autant plus que m est grand, MEME pour un seul partenaire (N=1) deja.")
print("=> La variable causale reelle est m (connexions par partenaire), PAS N (nombre de partenaires)")
print("   ni le nombre de hubs internes (deja exclu par le script 1).")
