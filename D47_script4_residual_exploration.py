"""
D47_script4_residual_exploration.py
=============================================================================
Exploration du residu de ~25.8% (script 3, Partie C) et test de pistes
alternatives pour comprendre/deriver r_exc(Z), en vue de savoir comment
formuler la reouverture d'OP14 dans l'errata.

Deux questions independantes sont testees ici :

  (Q1) Le residu de 25.8% de D40 vient-il d'une definition de "stable"
       trop stricte (IAEA, champ half_life='STABLE') qui exclut des
       isotopes quasi-stables a tres longue duree de vie (ex. 50-Cr,
       T1/2 ~ 1.3e18 ans) que les tables classiques de "vallee de
       stabilite" comptent comme stables ? On teste en assouplissant le
       seuil de demi-vie.

  (Q2) La regle "r_exc=1 generique, sauf 0 aux 3 fermetures magiques" de
       D47 est refutee (script 3, 0%). Existe-t-il une regle plus fine,
       basee sur des quantites deja etablies dans le corpus (degenerescence
       d du sous-niveau HO-PDL actif, position dans la couche, etc.),
       qui reproduit mieux le r_exc(Z) REEL (calcule directement depuis
       les donnees experimentales) ? Ceci est un TEST EXPLORATOIRE --
       un resultat negatif ici est aussi utile qu'un resultat positif
       (voir le principe du corpus : "les resultats negatifs sont des
       contributions de premier ordre").

Statut de ce script : exploratoire, conjectural. Aucune conclusion ici ne
doit etre presentee comme theoreme sans nouvelle derivation formelle et
relecture de Cedric.
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

CLOSURES = {28, 50, 82}

NMIN_EXP_FROZEN_STRICT = {
    20: 20, 22: 24, 24: 28, 26: 28, 28: 30, 30: 34, 32: 38, 34: 40,
    36: 42, 38: 46, 40: 50, 42: 50, 44: 52, 46: 56, 48: 58, 50: 62,
    52: 68, 54: 72, 56: 74, 58: 78, 60: 82, 62: 82, 64: 90, 66: 90,
    68: 94, 70: 98, 72: 104, 74: 108, 76: 111, 78: 114, 80: 116, 82: 124,
}

D40_NMIN_FIXED = {
    20: 20, 22: 24, 24: 26, 26: 28, 28: 30, 30: 34, 32: 38, 34: 40,
    36: 42, 38: 46, 40: 50, 42: 50, 44: 52, 46: 56, 48: 58, 50: 62,
    52: 68, 54: 70, 56: 74, 58: 78, 60: 82, 62: 82, 64: 88, 66: 90,
    68: 94, 70: 98, 72: 102, 74: 106, 76: 108, 78: 112, 80: 116, 82: 122,
}

print("=" * 79)
print("Q1 -- Le residu s'explique-t-il par la definition de 'stable' ?")
print("=" * 79)
print("""
On tente de recuperer, en plus du flag STABLE strict, les isotopes a demi-vie
tres longue (> 1e15 ans, seuil arbitraire englobant les cas connus comme
50-Cr [1.3e18 ans], 113-Cd, 144-Nd, etc.), classes "quasi-stables" dans de
nombreuses tables classiques de vallee de stabilite mais PAS dans le flag
STABLE strict de l'IAEA.
""")

def fetch_iaea_full():
    try:
        url = "https://www-nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; PDL-audit-script/1.0)"}
        resp = requests.get(url, headers=headers, timeout=60)
        resp.raise_for_status()
        from io import StringIO
        return pd.read_csv(StringIO(resp.text))
    except Exception as exc:
        print(f"  (recuperation IAEA impossible : {exc})")
        return None

df = fetch_iaea_full()

if df is not None:
    df.columns = [c.strip().lower() for c in df.columns]
    # Colonnes attendues : z, n, half_life, half_life_sec (ou similaire),
    # unit_hl, ... le nom exact peut varier -- inspecter avant de filtrer.
    print("Colonnes disponibles :", list(df.columns))
    # Tentative de filtre elargi : STABLE, ou demi-vie numerique tres longue.
    hl_sec_col = next((c for c in df.columns if "half_life_sec" in c or c == "t1_2_sec"), None)
    stable_col = next((c for c in ("half_life", "halflife") if c in df.columns), None)
    if stable_col and hl_sec_col:
        is_stable = df[stable_col].astype(str).str.upper().str.contains("STABLE", na=False)
        is_quasi = pd.to_numeric(df[hl_sec_col], errors="coerce") > 1e15 * 3.15e7  # >1e15 ans en secondes
        df_broad = df[is_stable | is_quasi.fillna(False)]
        Nmin_broad = {}
        for z in range(1, 83):
            sub = df_broad[df_broad["z"] == z]
            if len(sub) > 0:
                Nmin_broad[z] = int(sub["n"].min())
        n_match = sum(1 for z, v in D40_NMIN_FIXED.items()
                      if z in Nmin_broad and Nmin_broad[z] == v)
        n_tot = sum(1 for z in D40_NMIN_FIXED if z in Nmin_broad)
        print(f"Precision de D40 (formule corrigee) vs definition 'stable "
              f"elargie' (T1/2 > 1e15 ans inclus) : {n_match}/{n_tot} "
              f"({100*n_match/n_tot:.1f}% si n_tot>0)")
    else:
        print("Colonnes half_life_sec / half_life non trouvees sous les noms "
              "attendus -- inspection manuelle necessaire (voir liste de "
              "colonnes ci-dessus).")
else:
    print("Recuperation impossible depuis ce sandbox -- a relancer depuis "
          "Colab pour repondre a Q1.")

print()
print("=" * 79)
print("Q2 -- Une regle plus fine que 'r_exc=1 sauf fermetures' existe-t-elle ?")
print("=" * 79)
print("""
On calcule r_exc_reel(Z) = (N_min(Z) - N_min(Z-2)) / 2 directement depuis
D40 (formule corrigee, deja validee en script 3), et on le confronte a
plusieurs candidats structurels simples.
""")

# r_exc reel, tel qu'implicitement defini par D40 (deja = la colonne r
# d'origine, on le recalcule ici pour ne dependre d'aucun tableau externe)
Zs = sorted(D40_NMIN_FIXED.keys())
r_real = {}
for i in range(1, len(Zs)):
    z0, z1 = Zs[i - 1], Zs[i]
    if z1 - z0 != 2:
        continue
    r_real[z1] = (D40_NMIN_FIXED[z1] - D40_NMIN_FIXED[z0]) // 2

# Table HO-PDL (reprise du script 2) pour associer a chaque Z le sous-niveau
# actif et sa degenerescence d.
s = 1 / 12
def generate_levels(max_cumul=130):
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
cumul = 0
level_boundaries = []  # (cumul_start_exclusive, cumul_end_inclusive, d)
prev_cumul = 0
for E, N_osc, l, j, d in levels:
    cumul += d
    level_boundaries.append((prev_cumul, cumul, d))
    prev_cumul = cumul
    if cumul >= 90:
        break

def active_degeneracy(Z):
    """Degenerescence du sous-niveau HO-PDL actif pour un nombre de
    protons Z (i.e. celui en cours de remplissage a ce Z)."""
    for start, end, d in level_boundaries:
        if start < Z <= end:
            return d
    return None

print(f"{'Z':>4} {'r_exc reel':>10} {'d actif':>8} {'r_exc=d/2?':>11} "
      f"{'match d/2':>10}")
n_match_d2 = 0
n_tested = 0
for z in sorted(r_real.keys()):
    d = active_degeneracy(z)
    if d is None:
        continue
    n_tested += 1
    candidate = d / 2  # conjecture H_d2 : r_exc = d/2 (degenerescence/2)
    match = abs(candidate - r_real[z]) < 1e-9
    n_match_d2 += match
    print(f"{z:>4} {r_real[z]:>10} {d:>8} {candidate:>11} {str(match):>10}")

print()
print(f"Conjecture H_d2 (r_exc = degenerescence_active / 2) : "
      f"{n_match_d2}/{n_tested} ({100*n_match_d2/n_tested:.1f}% si n_tested>0)")
if n_match_d2 / max(n_tested, 1) > 0.8:
    print("=> Piste prometteuse, a formaliser comme nouvelle conjecture pour OP14.")
else:
    print("=> Conjecture H_d2 REFUTEE (resultat negatif, a documenter tel quel "
          "dans l'errata -- ne pas la proposer comme piste de derivation).")

print()
print("=" * 79)
print("CONCLUSION Q1/Q2 (pour errata)")
print("=" * 79)
print("""
Q1 : a completer depuis Colab (acces IAEA necessaire). Objectif : savoir si
     le residu de 25.8% de D40 (formule corrigee) se resorbe avec une
     definition de stabilite plus large (incluant les isotopes quasi-
     stables a tres longue duree de vie). Si oui, le residu n'est pas un
     defaut du corpus mais un artefact de la source de donnees utilisee
     pour la comparaison -- important a preciser dans l'errata pour ne pas
     sous-estimer la qualite de D40.

Q2 : la conjecture la plus simple (r_exc proportionnel a la degenerescence
     du sous-niveau actif) est testee ci-dessus. Que le resultat soit
     positif ou negatif, il doit etre consigne dans l'errata comme point de
     depart (ou piste eliminee) pour une future tentative de derivation
     d'OP14 -- conformement au principe du corpus voulant que les resultats
     negatifs soient documentes avec la meme rigueur que les resultats
     positifs.
""")
