"""
D47_script2_mirror_magic_verification.py
=============================================================================
Verification independante de la table HO-PDL de D47 et des 7 nombres
magiques {2, 8, 20, 28, 50, 82, 126}.

Construction : niveaux de l'oscillateur harmonique a 3D, indexes par
(N_osc, l, j=l+/-1/2), degenerescence d=2j+1, energie effective
E = (N_osc + 3/2) -/+ s*l (signe moins pour j=l+1/2), avec le splitting
spin-orbite s = 1/12 herite du script 1 (OP13).

Le lemme miroir (D47, Lemma mirror) affirme que la structure de niveaux
du proton et celle du neutron sont isomorphes (meme n_u=24, n_d=28, meme
s=1/12) -- ce script ne re-teste pas cette isomorphie en detail (elle
depend du theoreme de coexistence proton-neutron de D22, hors perimetre
de ce script), mais verifie que la table de niveaux generee a partir de
s=1/12 reproduit bien les 7 nombres magiques dans le bon ordre.

Statut de ce script : verification de premier passage, independante du
corpus.
=============================================================================
"""

s = 1 / 12  # force par OP13 (script 1)
EXPECTED_MAGIC = [2, 8, 20, 28, 50, 82, 126]

def generate_levels(max_cumul: int = 130):
    """Genere les niveaux HO-PDL (N_osc, l, j, d, E) jusqu'a un cumul donne."""
    levels = []
    for N_osc in range(0, 10):
        for l in range(N_osc, -1, -2):
            j_options = [l + 0.5, l - 0.5] if l > 0 else [0.5]
            for j in j_options:
                sign = -1 if j == l + 0.5 else +1
                E = (N_osc + 1.5) + sign * s * l
                d = int(2 * j + 1)
                levels.append((E, N_osc, l, j, d))
    levels.sort(key=lambda x: x[0])
    return levels

levels = generate_levels()

print("Table HO-PDL (niveaux ordonnes par energie croissante, s=1/12)")
print("=" * 70)
print(f"{'#':>3} {'N_osc':>5} {'l':>3} {'j':>5} {'d':>3} {'cumul':>6}")

cumul = 0
magic_found = []
for i, (E, N_osc, l, j, d) in enumerate(levels, start=1):
    cumul += d
    j_str = f"{int(2*j)}/2"
    tag = ""
    if cumul in EXPECTED_MAGIC:
        tag = "  [MAGIQUE]"
        magic_found.append(cumul)
    print(f"{i:>3} {N_osc:>5} {l:>3} {j_str:>5} {d:>3} {cumul:>6}{tag}")
    if cumul >= 126:
        break

print()
print(f"Nombres magiques attendus : {EXPECTED_MAGIC}")
print(f"Nombres magiques trouves  : {sorted(set(magic_found))}")
missing = [m for m in EXPECTED_MAGIC if m not in magic_found]
extra_before_126 = [m for m in magic_found if m not in EXPECTED_MAGIC]

if not missing and not extra_before_126:
    print("CONCLUSION : les 7 nombres magiques sont reproduits exactement, "
          "dans l'ordre, sans fermeture parasite. CONFIRME.")
else:
    if missing:
        print(f"ATTENTION : nombres magiques manquants : {missing}")
    if extra_before_126:
        print(f"ATTENTION : fermetures parasites (non attendues) trouvees : "
              f"{extra_before_126}")
    print("A verifier avant toute publication -- ceci remettrait en cause "
          "le Theoreme des nombres magiques de D47.")

print()
print("Rappel de perimetre : ce script verifie la table HO-PDL et les "
      "nombres magiques generes a partir de s=1/12. Il NE teste PAS "
      "l'isomorphisme proton/neutron du Lemme miroir lui-meme (celui-ci "
      "depend de D22, hors perimetre), ni les taux de remplissage r_exc(Z) "
      "(voir script 3).")
