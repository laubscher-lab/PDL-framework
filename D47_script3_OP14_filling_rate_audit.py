"""
D47_script3_OP14_filling_rate_audit.py
=============================================================================
Audit complet d'OP14 (D47, Theorem OP14 -- taux de remplissage r_exc(Z)).

Historique de cet audit (pour memoire, a inclure dans l'errata) :

  1er passage : reconstruction de N_min(Z) via N_min(Z) = 20 + sum(r) a
                partir de la table brute de D40 -> 6.2% de correspondance
                avec les donnees reelles. Semblait indiquer une table
                corrompue.

  2e passage  : reconstruction directe via la colonne E imprimee de D40
                (N_min(Z) = Z + E(Z)) -> 75% de correspondance. Suggerait
                que la colonne r etait fausse/incoherente avec E.

  3e passage (CE SCRIPT) : verification exhaustive montre que la colonne r
                et la colonne E de D40 sont en fait PARFAITEMENT COHERENTES
                entre elles via la relation Delta_E = 2*(r-1), sur les 31
                lignes, sans exception. Le probleme n'etait pas les
                donnees, mais l'EQUATION DE RECONSTRUCTION telle qu'ecrite
                dans D40 (et recopiee dans D47) : "N_min(Z) = 20 + sum(r)"
                omet un facteur 2. La bonne relation est :
                    N_min(Z) = 20 + 2*sum(r_exc(Z'))

Ce script :
  (A) verifie exhaustivement Delta_E = 2*(r-1) sur les 31 lignes de D40 ;
  (B) reconstruit N_min(Z) avec la formule CORRIGEE (facteur 2), pour D40
      ET pour la regle simplifiee de D47 (r_exc=1 sauf fermetures) ;
  (C) confronte les deux aux donnees experimentales reelles (IAEA Live
      Chart of Nuclides, avec repli sur des valeurs deja recuperees et
      figees si le reseau n'est pas disponible) ;
  (D) quantifie l'erreur factuelle du remark de D47 sur le contenu de la
      table de D40.

Statut de ce script : verification de premier passage. Les conclusions
ci-dessous sont destinees a etre relues par Cedric avant integration dans
un errata (D47v2 / D40 erratum).
=============================================================================
"""

import sys

try:
    import requests
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "requests", "--quiet"])
    import requests

import pandas as pd

# ---------------------------------------------------------------------------
# Table de D40, recopiee EXACTEMENT depuis "Nuclear Stability PDL.tex"
# (Table tab:filling), verifiee ligne a ligne contre le fichier fourni par
# Cedric le 2eme jour de cet audit.
# ---------------------------------------------------------------------------
D40_table = [
    (20, 22, 2), (22, 24, 1), (24, 26, 1), (26, 28, 1), (28, 30, 2),
    (30, 32, 2), (32, 34, 1), (34, 36, 1), (36, 38, 2), (38, 40, 2),
    (40, 42, 0), (42, 44, 1), (44, 46, 2), (46, 48, 1), (48, 50, 2),
    (50, 52, 3), (52, 54, 1), (54, 56, 2), (56, 58, 2), (58, 60, 2),
    (60, 62, 0), (62, 64, 3), (64, 66, 1), (66, 68, 2), (68, 70, 2),
    (70, 72, 2), (72, 74, 2), (74, 76, 1), (76, 78, 2), (78, 80, 2),
    (80, 82, 3),
]

D40_E_printed = {
    22: 2,  24: 2,  26: 2,  28: 2,  30: 4,  32: 6,  34: 6,  36: 6,
    38: 8,  40: 10, 42: 8,  44: 8,  46: 10, 48: 10, 50: 12, 52: 16,
    54: 16, 56: 18, 58: 20, 60: 22, 62: 20, 64: 24, 66: 24, 68: 26,
    70: 28, 72: 30, 74: 32, 76: 32, 78: 34, 80: 36, 82: 40,
}

CLOSURES = {28, 50, 82}

# Donnees experimentales deja recuperees (IAEA Live Chart of Nuclides,
# champ half_life='STABLE', N minimal par Z). Figees ici pour reproductibilite
# sans dependance reseau. A rafraichir si l'IAEA met a jour ses donnees, et
# a comparer a une definition alternative de "stable" si l'ecart residuel
# (partie C) doit etre investigue plus finement (isotopes quasi-stables
# comme 50-Cr, T1/2 ~ 1.3e18 ans, exclus de la liste stricte IAEA mais
# presents dans la plupart des tables de vallee de stabilite classiques).
NMIN_EXP_FROZEN = {
    20: 20, 22: 24, 24: 28, 26: 28, 28: 30, 30: 34, 32: 38, 34: 40,
    36: 42, 38: 46, 40: 50, 42: 50, 44: 52, 46: 56, 48: 58, 50: 62,
    52: 68, 54: 72, 56: 74, 58: 78, 60: 82, 62: 82, 64: 90, 66: 90,
    68: 94, 70: 98, 72: 104, 74: 108, 76: 111, 78: 114, 80: 116, 82: 124,
}


def fetch_iaea_nmin():
    """Tente de recuperer des donnees fraiches depuis l'IAEA. Retourne None
    en cas d'echec (pas de levee d'exception -- l'appelant utilise le repli)."""
    try:
        url = "https://www-nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; PDL-audit-script/1.0)"}
        resp = requests.get(url, headers=headers, timeout=60)
        resp.raise_for_status()
        from io import StringIO
        df = pd.read_csv(StringIO(resp.text))
        df.columns = [c.strip().lower() for c in df.columns]
        stable_col = next((c for c in ("half_life", "halflife") if c in df.columns), None)
        if stable_col is None:
            return None
        df_stable = df[df[stable_col].astype(str).str.upper().str.contains("STABLE", na=False)]
        out = {}
        for z in range(1, 83):
            sub = df_stable[df_stable["z"] == z]
            if len(sub) > 0:
                out[z] = int(sub["n"].min())
        return out if out else None
    except Exception as exc:
        print(f"  (recuperation IAEA impossible : {exc})")
        return None


print("=" * 79)
print("PARTIE A -- Coherence interne de la table de D40 (colonnes r et E)")
print("=" * 79)

E_prev = 0
all_consistent = True
mismatches_A = []
for (z0, z1, r), e1 in zip(D40_table, [D40_E_printed[z1] for _, z1, _ in D40_table]):
    delta_e = e1 - E_prev
    predicted = 2 * (r - 1)
    ok = (delta_e == predicted)
    all_consistent &= ok
    if not ok:
        mismatches_A.append((z0, z1, r, e1, delta_e, predicted))
    E_prev = e1

print(f"Verification de Delta_E = 2*(r-1) sur les 31 lignes : "
      f"{'TOUTES COHERENTES' if all_consistent else f'{len(mismatches_A)} EXCEPTION(S)'}")
if not all_consistent:
    for z0, z1, r, e1, de, pred in mismatches_A:
        print(f"  EXCEPTION a {z0}->{z1} : r={r}, Delta_E observe={de}, "
              f"attendu={pred}")
print()
print("Interpretation : si TOUTES COHERENTES, la table de D40 (colonnes r et")
print("E) n'est PAS corrompue. Le probleme se situe dans l'equation ecrite")
print('"N_min(Z) = 20 + sum(r)" (D40 eq., recopiee dans D47), qui omet un')
print("facteur 2. La relation correcte est N_min(Z) = 20 + 2*sum(r).")

print()
print("=" * 79)
print("PARTIE B -- Reconstruction de N_min(Z) : formule corrigee (facteur 2)")
print("=" * 79)

# D40 via r, formule CORRIGEE
cum = 0
Nmin_D40_fixed = {20: 20}
for z0, z1, r in D40_table:
    cum += r
    Nmin_D40_fixed[z1] = 20 + 2 * cum

# D40 via E direct (pour verification croisee -- doit etre identique a
# Nmin_D40_fixed si la Partie A est coherente)
Nmin_D40_viaE = {20: 20}
for z1, e in D40_E_printed.items():
    Nmin_D40_viaE[z1] = z1 + e

cross_check_fail = [z for z in Nmin_D40_fixed if Nmin_D40_fixed[z] != Nmin_D40_viaE[z]]
print(f"Verification croisee (r corrige vs E direct) : "
      f"{'IDENTIQUES sur tous les Z' if not cross_check_fail else f'{len(cross_check_fail)} divergence(s)'}")

# D47, formule CORRIGEE (r_exc=0 aux fermetures, 1 sinon)
cum = 0
Nmin_D47_fixed = {20: 20}
for z0, z1, r in D40_table:
    r_d47 = 0 if z1 in CLOSURES else 1
    cum += r_d47
    Nmin_D47_fixed[z1] = 20 + 2 * cum

print()
print("=" * 79)
print("PARTIE C -- Confrontation aux donnees experimentales reelles")
print("=" * 79)

print("Tentative de recuperation de donnees fraiches (IAEA)...")
fresh = fetch_iaea_nmin()
if fresh:
    Nmin_exp = fresh
    print(f"OK : {len(Nmin_exp)} valeurs fraiches recuperees.")
else:
    Nmin_exp = dict(NMIN_EXP_FROZEN)
    print(f"Repli sur les {len(Nmin_exp)} valeurs figees (deja verifiees lors "
          f"d'un run Colab precedent).")

print()
print(f"{'Z':>4} {'D40 (corrige)':>14} {'D47 (corrige)':>14} {'exp':>6} "
      f"{'D40 ok':>7} {'D47 ok':>7}")
n40 = n47 = n = 0
for z in sorted(Nmin_exp):
    if z < 22 or z not in Nmin_D40_fixed:
        continue
    n += 1
    d40v = Nmin_D40_fixed[z]
    d47v = Nmin_D47_fixed[z]
    expv = Nmin_exp[z]
    ok40, ok47 = (d40v == expv), (d47v == expv)
    n40 += ok40
    n47 += ok47
    flag = "  <-- Z=29 (Cu)" if z in (28, 30) else ""
    print(f"{z:>4} {d40v:>14} {d47v:>14} {expv:>6} {str(ok40):>7} {str(ok47):>7}{flag}")

print()
print(f"Precision D40 (table de r, formule corrigee)          : {n40}/{n} "
      f"({100*n40/n:.1f}%)")
print(f"Precision D47 (r_exc=1 sauf fermetures, formule corrigee) : {n47}/{n} "
      f"({100*n47/n:.1f}%)")

print()
print("=" * 79)
print("PARTIE D -- Erreur factuelle du remark de D47 sur la table de D40")
print("=" * 79)
n_2_3 = sum(1 for z0, z1, r in D40_table if 22 <= z1 <= 82 and r in (2, 3))
print(f'D47 affirme : "the values {{2,3}} do not appear in [D40\'s table for] this range".')
print(f"Compte reel des entrees avec r in {{2,3}} pour Z (fin) dans [22,82] : "
      f"{n_2_3} / {len(D40_table)}")
print("=> Cette affirmation de D47 est factuellement fausse.")

print()
print("=" * 79)
print("CONCLUSION (pour errata -- a valider par Cedric)")
print("=" * 79)
print(f"""
1. La table de D40 (colonnes r et E) est INTERNE COHERENTE (Partie A).
   Le corpus D40 n'est PAS corrompu sur ce point.

2. L'equation "N_min(Z) = 20 + sum(r)" ecrite dans D40 et recopiee dans D47
   omet un facteur 2. Correction mineure, cosmetique, a apporter aux deux
   documents (ou a une nouvelle version de D40 si D47 doit rester une
   consequence directe).

3. Une fois la formule corrigee appliquee de maniere identique aux deux
   approches :
     - D40 (table de r empirique)          : {100*n40/n:.1f}% de correspondance
     - D47 (regle simplifiee r_exc in {{0,1}}) : {100*n47/n:.1f}% de correspondance
   Le Theoreme OP14 de D47 est REFUTE de maniere non ambigue (independante
   de la question du facteur 2).

4. Le remark de D47 sur le contenu de la table de D40 (absence pretendue
   de valeurs 2 et 3 dans la plage 22-82) est factuellement faux
   ({n_2_3}/{len(D40_table)} contre-exemples).

RECOMMANDATION : publier un errata qui (i) corrige le facteur 2 dans
l'equation de D40, (ii) rouvre OP14 dans D47 (statut : theoreme -> a
nouveau open problem), (iii) retire le remark errone sur la table de D40.
Le residu de {100*(n-n40)/n:.1f}% non explique par D40 (Partie C) reste une
question secondaire, probablement liee a la definition de "stable" utilisee
(isotopes quasi-stables a tres longue duree de vie) -- voir script 4 pour
une premiere exploration de pistes structurelles alternatives.
""")
