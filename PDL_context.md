# PDL Programme — Context and State

*Last updated: Session 57 — 11 June 2026 (DOI D61 confirmé : 10.5281/zenodo.20645713 ; DM v28 rédigé et déposé — DOI DM v28 à compléter ; site web mis à jour)*

---

## Programme Summary

The Projective Dynamic Logo (PDL) programme derives fundamental physical constants and structures from four axioms on finite signed graphs, without presupposing spacetime, particles, or fields. The minimal admissible closure under these axioms is the complete graph K₄ on four vertices and six edges, identified with the electron prototype (R_e = 6). The proton is the minimal hierarchical composite, uniquely characterised by the integer quintuplet (24, 28, 930, 10087, 11017).

**Sessions 11–30:** Gates 1–3, D32–D47 (voir PDL_context.md Session 45 pour détail).

**Session 40 — D55 + DM v23 (14 May 2026):**
- θ_W = 19π/119 RÉSOLU. DOI D55: 10.5281/zenodo.20179924 | DM v23: 10.5281/zenodo.20181077

**Session 41 — DS01 (14 May 2026):** DOI: 10.5281/zenodo.20187274

**Sessions 42–44 — D-exp-SP2, D-exp-ZIB, D-exp-MP01:**
- DOI: 10.5281/zenodo.20242505 | 10.5281/zenodo.20262293 | 10.5281/zenodo.20316492

**Session 45 — D-exp-Zr publié (21 May 2026):**
- QPT du Zirconium — corollaires D40+D47. DOI: 10.5281/zenodo.20321750

**Session 46 — D56 + DM v24 (27 May 2026):**
- **OP-D41-1-A RÉSOLU : N_comp(k) = k — théorème inconditionnel de C1–C4.**
- DOI D56 : 10.5281/zenodo.20409903 | DM v24 : 10.5281/zenodo.20415182

**Session 47 — ResearchGate + PDL–OFN Bridge (2 June 2026):**
- Cinq scripts Python Colab — convergence β₁=3 PDL/OFN établie numériquement.

**Session 48 — N01 déposé (3 June 2026):**
- DOI N01 : 10.5281/zenodo.20523343

**Session 49 — D-exp-E2-PDL déposé (8 June 2026):**
- DOI : 10.5281/zenodo.20593807

---

**Session 50 — D57 déposé; Seven scripts SU(2) verrouillés; DM v25 patches produits (9 June 2026):**

### Résultats principaux Session 50

**D57 déposé sur Zenodo. DOI : 10.5281/zenodo.20600264**
- Théorème central : sin²θ_W(tree) = sin²(π/R_e) = 1/4 (inconditionnel)
- Route A (D29 : 192/768) = Route B (orbites S₄) via V₄ — équivalence prouvée
- Conjecture H_SU2 : C1 efface V₄ → S₃ → Dic₃ ⊂ SU(2)
- A₄/V₄ ≅ ℤ₃ ↔ β₁(K₄)=3=b₁(Ω₂₁) — résolution partielle OP-OFN-1

**Fichiers :** D57_gauge_SU2.tex + D57_references.bib (15 entrées)

**DM v25 patches produits (9 patches sur DM v24 / 1190 lignes).**

---

**Session 51 — D58 déposé; PDL_SU3_script1.py déposé; DM v25 déposé (10 June 2026):**

### Résultats principaux Session 51

#### Script de verrouillage D58 — PDL_SU3_script1.py

Protocole verrouillage respecté : script Colab exécuté indépendamment avant rédaction.

**Résultat négatif documenté :** V₄ agit fidèlement sur H₁(K₄; ℝ) — stratégie initiale via homologie invalidée.

**PDL_SU3_script1.py déposé sur Zenodo. DOI : 10.5281/zenodo.20623231**

Cinq lemmes verrouillés (tous PASSED, résultat négatif VERIFIED NEGATIVE) :
- L1 : S₄/V₄ ≅ S₃ (groupe de Weyl de A₂)
- L2 : action naturelle de S₃ sur V₄\{e} — bijection S₄-équivariante avec orbites V₄-arêtes
- L3 : A₄/V₄ ≅ ℤ₃ = centre de SU(3)
- L4 : réduction au Cartan rang 2 via invariance R_e = 6 (D16a)
- L5 : système de racines A₂ dans le plan trace-nulle
- Négatif : V₄ non trivial sur H₁(K₄; ℝ)

#### D58 — Déposé sur Zenodo

**Titre :** Derivation of the SU(3) Gauge Structure from the PDL Axioms C1–C4: Completion of the Standard Model Gauge Group SU(3) × SU(2) × U(1) (Projective Dynamic Logo Framework — Document D58)

**DOI : 10.5281/zenodo.20622987**

**Résultat central :**
```
SU(3) × SU(2) × U(1)   THÉORÈME ALGÉBRIQUE de C1–C4
                         Chaîne : D46 (U(1)) + D57 (SU(2)) + D58 (SU(3))
                         Modulo la classification de Cartan–Killing–Weyl (classique)
```

**Fichiers :** D58_gauge_SU3_v2.tex + D58_references.bib (21 entrées)

#### DM v25 — Déposé sur Zenodo

**DOI : 10.5281/zenodo.20605620**

---

**Session 52 — DM v26 déposé (10 June 2026):**

### Résultats principaux Session 52

**DM v26 déposé sur Zenodo. DOI : 10.5281/zenodo.20625504**

---

**Session 53 — D59-py + D59 + DM v27 déposés (10 June 2026):**

### Résultats principaux Session 53

#### Script de verrouillage D59 — PDL_D59_script1.py

Protocole verrouillage respecté : script Colab exécuté indépendamment avant rédaction.

**PDL_D59_script1.py déposé sur Zenodo. DOI : 10.5281/zenodo.20628926**

Cinq lemmes verrouillés + un résultat négatif (tous PASSED / VERIFIED) :
- L1 : S₃ = S₄/V₄ agit fidèlement et transitivement sur V₄\{e} (rappel D58)
- L2 : χ_π = χ_trivial + χ_standard — décomposition du caractère, vérifiée sur les 24 éléments de S₄
- L3 : W = {a+b+c=0} ⊂ ℂ³ est le complément S₃-invariant unique de ℂ(1,1,1)
- L4 : système de racines A₂ dans W — matrice de Cartan [[2,-1],[-1,2]] par arithmétique entière exacte
- L5 : Δn = n_d - n_u = 4 > 0 (théorème C4, D47) force l'orientation 3 vs 3̄ — k₃/(k₁+k₂) = R_e = 6 exact
- NEG : bijection (T₂)↔(T₃) physiquement motivée mais PAS S₄-équivariante

#### D59 — Déposé sur Zenodo

**Titre :** Physical Identification of SU(3)_c and the Fundamental Representation 3 from the PDL Axioms C1–C4 (Projective Dynamic Logo Framework — Document D59)

**DOI : 10.5281/zenodo.20629282**

**Contenu :**
- Cinq lemmes (L1–L5) établis comme théorèmes inconditionnels de C1–C4
- Espace porteur W = {a+b+c=0} ⊂ ℂ³ canoniquement labellé par V₄\{e}
- Théorème principal : SU(3)_c agissant sur W dans la représentation fondamentale 3 est un théorème inconditionnel de C1–C4 + Cartan–Killing–Weyl
- Orientation matière/antimatière sélectionnée par Δn = 4 > 0 (D47, théorème de C4)
- Identité exacte : k₃/(k₁+k₂) = R_e = 6
- Résultat négatif documenté : bijection (T₂)↔(T₃) non S₄-équivariante
- OP-D58-1 et OP-D58-3 RÉSOLUS
- Nouveaux problèmes ouverts : OP-D59-1 (masse des quarks), OP-D59-2 (D_μ = ∂_μ - igA_μ depuis C4)

**Résultat central (Session 53) :**
```
SU(3)_c dans 3   THÉORÈME de C1–C4 + Cartan–Killing–Weyl
                  W = {a+b+c=0} porteur canonique, axes = V₄\{e}
                  Orientation 3 vs 3̄ : Δn = 4 > 0 (D47)
                  Identité : k₃/(k₁+k₂) = R_e = 6 (exact)
```

**Fichiers :** D59_representation_3.tex + D59_references.bib (15 entrées)

#### DM v27 — Déposé sur Zenodo

**DOI : 10.5281/zenodo.20630421**

Incorpore D59 et PDL_D59_script1.py. OP-D58-1 et OP-D58-3 marqués résolus. OP-D59-1 et OP-D59-2 ajoutés. Nœud D59 dans le diagramme TikZ.

---

**Session 54 — D60 + PDL_C1V4_script1.py + PDL_C1V4_script2.py déposés (11 June 2026):**

### Résultats principaux Session 54

#### Contexte : échange avec Prof. Thomas Görnitz

Contact établi avec Prof. Thomas Görnitz (Goethe Universität Frankfurt), auteur du cadre Protyposis/AQI et du papier Görnitz–Schomäcker (2018) «The Structures of Interactions — How to Explain the Gauge Groups U(1), SU(2) and SU(3)» (Foundations of Science, DOI: 10.1007/s10699-016-9507-6). Sa réponse confirme la convergence structurelle : dans les deux cadres, les groupes de jauge précèdent l'espace de Minkowski et émergent d'une structure primitive (AQI chez Görnitz, K₄ chez PDL). La route vers SU(3) est distincte (duplication de Cartan chez Görnitz, chaîne S₄→S₃→A₂ chez PDL). Valeur : confirmation externe de cohérence fondationnelle ; référence bibliographique pour futurs documents sur le secteur de jauge.

#### Scripts de verrouillage D60

Protocole verrouillage respecté : deux scripts exécutés indépendamment dans Google Colab avant rédaction.

**PDL_C1V4_script1.py** — Vérifie :
- Structure orbite 1+3+4 de S₄ sur Coh(K₄) (192 checks)
- Résultat négatif documenté : s → −s ne préserve pas C2 (8/8 VERIFIED)
- V₄ agit librement sur orbit-4, génère exactement 3 pairings distincts
- Lemme B (méthode pairings) : V₄ = {g ∈ S₄ : g préserve les 3 pairings} (PASSED)
- Lemme C : C1-admissibilité = V₄-invariance, équivalence exacte sur 64 monomials (PASSED)

**PDL_C1V4_script2.py** — Vérifie :
- Point 1 : V₄ fixe orbit-1 et orbit-3 pointwise (12 checks, PASSED)
- Point 2 : orbit-4 ≅ V₄ comme V₄-ensemble régulier (PASSED)
- Trois pairings = partitions en cosets de H₁, H₂, H₃ (6 identités coset-pair, PASSED)
- Argument algébrique σ_g : accord méthode cosets/méthode pairings sur 24 éléments (72 checks, PASSED)
- Aucun élément de S₄\V₄ ne préserve les 3 structures de cosets (PASSED)

**Déposés sur Zenodo avec D60 (dépôt groupé). DOI : 10.5281/zenodo.20639684**

#### D60 — Déposé sur Zenodo

**Titre :** From the Logic of Existence to the Gauge Symmetry Group: A Proof of Hypothesis H_SU2 from Axioms C1 and C2 (Projective Dynamic Logo Framework — Document D60)

**DOI : 10.5281/zenodo.20639684**

**Résultat central :**
```
H_SU2   THÉORÈME INCONDITIONNEL de C1+C2
         Chaîne logique :
         Existence = distinction répétable (C1)
         → co-originarité des deux états du 2-cycle
         → C1-admissibilité (aucun observable ne distingue s(1) de s(2))
         → s → −s brise C2 [résultat négatif]
         → pulsation pairing = partition de orbit-4 sous V₄
         → V₄ = groupe des symétries de pulsation de K₄ (Lemme B)
         → V₄ fixe orbit-1 et orbit-3 pointwise (Lemme C)
         → C1-admissibilité = V₄-invariance sur tout Coh(K₄)
         → G_eff = S₄/V₄ ≅ S₃
```

**Corollaire majeur :**
```
SU(3) × SU(2) × U(1) + représentation 3   THÉORÈME INCONDITIONNEL de C1–C4
                                             D46 (U(1)) + D60 (SU(2), théorème)
                                             + D58 (SU(3)) + D59 (représentation 3)
                                             AUCUNE ÉTAPE CONJECTURALE RÉSIDUELLE
                                             dans le secteur de jauge
```

**Fichiers déposés :** D60_C1V4_theorem.pdf + D60_C1V4_theorem.tex + D60_references.bib + PDL_C1V4_script1.py + PDL_C1V4_script2.py

**Statut OP-D57-1 :** RÉSOLU par D60.

---

**Session 55 — D61 rédigé et verrouillé (11 June 2026) :**

### Résultats principaux Session 55

#### Scripts de verrouillage D61

Protocole verrouillage respecté : deux scripts exécutés indépendamment dans Google Colab avant rédaction. Scripts déposés avec D61 dans le même enregistrement Zenodo (dépôt groupé, comme D60).

**PDL_D61_script1.py** — Vérifie (2048 checks, arithmétique entière exacte) :
- |Coh(K₄)| = 8 configurations cohérentes (PASSED)
- Partenaires de pulsation −s sont tous INCOHÉRENTS — pulsation alterne cohérent ↔ incohérent (PASSED)
- Transports C4-admissibles = Coh(K₄) exactement — identité algébrique prouvée en 2 lignes et vérifiée exhaustivement (PASSED)
- Structure de groupe Z₂³ : clos, abélien, exposant 2 (PASSED)
- 56 transports non-admissibles ont tous ν > 0 sur au moins une config cohérente (PASSED)
- Distribution des coûts : 48 à ν_max = 2/4, 8 à ν_max = 4/4
- Résultat négatif : flip global (−1,...,−1) NON admissible — coût 4/4 (VERIFIED)
- Résultat négatif : conjecture initiale (groupe admissible = V₄, ordre 4) RÉFUTÉE — groupe correct = Coh(K₄) ≅ Z₂³ (ordre 8) (DOCUMENTED)

**PDL_D61_script2.py** — Vérifie (288 checks, arithmétique entière exacte) :
- V₄ clos sous composition (PASSED)
- Coh(K₄) stable sous action arêtes de V₄ (32 checks, PASSED)
- Action fidèle : noyau = {id} (PASSED)
- V₄ agit par automorphismes de groupe de Z₂³ (256 checks, PASSED)
- Structure orbitale : 4×{taille 1} + 1×{taille 4} — table d'action complète V₄ × Coh(K₄) produite
- Sous-groupe de points fixes F ≅ V₄ labellé par les 3 couplages parfaits de K₄ = axes de W en D59 (PASSED)
- Produit semi-direct Z₂³ ⋊ V₄ d'ordre 32 bien défini (PASSED)

#### D61 — Rédigé, verrouillé, prêt pour dépôt Zenodo

**Titre :** Gauge Dynamics as a C4 Survival Theorem: Derivation of the Minimal Covariant Derivative from the PDL Axioms C1–C4 (Projective Dynamic Logo Framework — Document D61)

**Résultat central :**
```
D_μ = ∂_μ − igA_μ   THÉORÈME (via lemmes externes) de C1–C4

Chaîne causale en 4 flèches explicitement stratifiées :

α : C4 → Coh(K₄) ≅ Z₂³
    THÉORÈME INCONDITIONNEL, verrouillé par script1 (2048 checks)
    C4 étendu aux règles de transport (généralisation de D49)

β : Z₂³ → Z₂³ ⋊ V₄
    THÉORÈME INCONDITIONNEL, verrouillé par script2 (288 checks)
    V₄ agit fidèlement par automorphismes sur Coh(K₄)

γ : Z₂³ ⋊ V₄ → G_gauge = SU(3)×SU(2)×U(1)
    THÉORÈME DE CONSISTANCE via D46–D60
    (non une nouvelle dérivation de G_gauge : convergence des deux routes)

δ : G_gauge → D_μ = ∂_μ − igA_μ
    THÉORÈME via Utiyama (1956) comme lemme externe
    — invariance locale forcée par C4 (non postulée)
    — restriction au premier ordre = minimalité C4
```

**Résultats négatifs documentés :**
- Conjecture initiale (groupe admissible = V₄, ordre 4) réfutée — groupe correct = Coh(K₄) ≅ Z₂³ (ordre 8)
- Flip global (−1,...,−1) non admissible (coût 4/4) — C4 élimine la pulsation comme transport

**Connexion avec D49 :** D61 est la généralisation de D49 (London → D_μ complet). D49 dérivait ∇φ=0 pour U(1) via C4; D61 dérive D_μ pour G_gauge entier via la même logique de survie.

**Connexion avec D58–D60 :** Le sous-groupe de points fixes F ≅ V₄ (script2) est labellé par les 3 couplages parfaits de K₄ = axes de W en D59. La structure orbitale 4×1+1×4 de script2 est le pendant transport de la structure orbitale 1+3+4 de D60.

**Problèmes ouverts nouveaux :**
- OP-D61-1 : masses des bosons W±/Z⁰ (priorité HIGH)
- OP-D61-2 : trois générations de fermions (priorité HIGH)
- OP-D61-3 : dérivation autonome de G_gauge depuis Z₂³ ⋊ V₄ sans invoquer D46–D60 pour la flèche γ (priorité MEDIUM)

**Note sur le dépôt Zenodo :** PDL_D61_script1.py et PDL_D61_script2.py sont déposés DANS le même enregistrement que D61 (dépôt groupé, comme D60). Pas de DOIs séparés pour les scripts.

**Fichiers :** D61_covariant_derivative_v2.pdf + D61_covariant_derivative_v2.tex + D61_references.bib + PDL_D61_script1.py + PDL_D61_script2.py

**Statut OP-D59-2 :** RÉSOLU par D61.

**Fermeture du secteur de jauge :** La chaîne causale C1–C4 → D_μ est maintenant fermée. Ce qui reste ouvert n'est plus la structure ni la dynamique du secteur de jauge, mais les masses des bosons et la structure de génération.

---

**Session 56 — DM v28 rédigé (11 June 2026) :**

### Résultats principaux Session 56

#### DM v28 — Rédigé et déposé sur Zenodo

**Titre :** Projective Dynamic Logo (PDL) — Global Mapping of Structures, Results, and Open Problems — Version 28

**DOI DM v28 : à compléter après dépôt Zenodo**

**Contenu de la mise à jour v27 → v28 :**
- Diagramme scindé en deux figures : Figure 1 (chaîne fondamentale), Figure 2 (secteur de jauge complet avec flèches α–β–γ–δ de D61)
- D60 et D61 ajoutés dans la longtable du corpus
- OP-D57-1 → resolvedproblem (D60), OP-D59-2 → resolvedproblem (D61)
- OP-D61-1, OP-D61-2, OP-D61-3 ajoutés
- Layer L15 "Gauge sector [COMPLETE]" avec D46+D57+D58+D59+D60+D61

#### Site web cedriclaubscher.ch — Mis à jour

Deux blocs HTML mis à jour (Guided Journey + table du corpus) :
- Phase V étendue à D60 et D61
- DM pointant vers v28
- Section gauge "D57–D61" avec description de la fermeture complète
- DOI D61 : 10.5281/zenodo.20645713 inséré dans tous les liens

---

**Session 57 — Mise à jour DOI D61 (11 June 2026) :**

### DOI D61 confirmé

**D61 déposé sur Zenodo. DOI : 10.5281/zenodo.20645713**

Fichiers déposés (dépôt groupé) : D61_covariant_derivative.pdf + D61_covariant_derivative_v2.tex + D61_references.bib + PDL_D61_script1.py + PDL_D61_script2.py

---
|-----|-----|--------------|
| D01 | 10.5281/zenodo.18462686 | Emergence of Physical Reality (PDL) |
| D02 | 10.5281/zenodo.18463130 | Introduction to PDL |
| D01F | 10.5281/zenodo.18475542 | Émergence réalité physique (français) |
| D03 | 10.5281/zenodo.18509648 | PDL IMRaD format |
| D04 | 10.5281/zenodo.18580925 | PDL–TO Dialogue |
| D05 | 10.5281/zenodo.18581453 | Golden Ratio in PDL |
| D06 | 10.5281/zenodo.18581807 | Coherence Leakage, Exponent 18 |
| D07 | 10.5281/zenodo.18663156 | Gleason-Type Born's Rule |
| D08 | 10.5281/zenodo.18664995 | Topological Reformulation PDL |
| D09 | 10.5281/zenodo.18675200 | PDL Research Programme Position Paper |
| D10 | 10.5281/zenodo.18716526 | Discrete Coherence Flux to Effective Fields |
| D10a | 10.5281/zenodo.19329465 | Proper Time as Coherence-Cycle Counting |
| D11 | 10.5281/zenodo.18725069 | Einstein–Dirac Unification sketch |
| D12 | 10.5281/zenodo.18828183 | Fine-Structure Constant derivation |
| D13 | 10.5281/zenodo.18831587 | Schrödinger compatibility |
| D14 | 10.5281/zenodo.18832069 | Born's Rule + Golden Ratio surface |
| D15 | 10.5281/zenodo.18832542 | Schrödinger dynamics sketch |
| D16 | 10.5281/zenodo.18832953 | Proton architecture combinatorics |
| D16a | 10.5281/zenodo.18841034 | K₄ as unique minimal closure |
| D16b | 10.5281/zenodo.18841166 | Proton architecture uniqueness |
| D17 | 10.5281/zenodo.18841254 | Exponent 18, hierarchical filtering |
| D18 | 10.5281/zenodo.18854190 | Discrete cavity modes |
| D19 | 10.5281/zenodo.18854559 | Existence as Pulsating Closure (ontologie) |
| D20F | 10.5281/zenodo.18914532 | Qui que nous puissions être (français) |
| D20 | 10.5281/zenodo.18940047 | Whoever We May Be |
| D21 | 10.5281/zenodo.19056994 | α–G bridge |
| DN | 10.5281/zenodo.19076555 | Whatever We May Be |
| D22 | 10.5281/zenodo.19164084 | Nuclear stability skeleton |
| DM v27 | 10.5281/zenodo.20630421 | Global Mapping v27 (superseded by v28) |
| D23 | 10.5281/zenodo.19197268 | Topological origin of exponent 18 |
| D24 | 10.5281/zenodo.19206960 | G_eff(N), Hubble tension |
| D25 | 10.5281/zenodo.19219858 | α–G parameter-free bridge |
| D26 | 10.5281/zenodo.19221310 | Cosmological resolution via PDL |
| D27 | 10.5281/zenodo.19281988 | N_CMB derivation, Hubble tension resolved |
| D28 | 10.5281/zenodo.19282932 | PDL–QCD boundary, mass ratio |
| D29 | 10.5281/zenodo.19283107 | Gate 1 : 155/11017 |
| D30 | 10.5281/zenodo.19294449 | Gate 2 : a=2 |
| D31 | 10.5281/zenodo.19295227 | Gate 3 conjecture + Δm_iso |
| D32 | 10.5281/zenodo.19295583 | Schrödinger equation from PDL |
| D33 | 10.5281/zenodo.14965050 | Dirac equation from PDL |
| D34 | 10.5281/zenodo.19302936 | Born's Rule Level 1 |
| D35 | 10.5281/zenodo.19303408 | Einstein equation from PDL |
| D36 | 10.5281/zenodo.19323033 | Gate 3 : G_eff = σ(N)·G_PDL |
| D37 | 10.5281/zenodo.19354096 | Area law |
| D38 | 10.5281/zenodo.19354682 | Bekenstein–Hawking + PBH predictions |
| D39 | 10.5281/zenodo.19354989 | κ = R_surf/R_tot derivation |
| D40 | 10.5281/zenodo.19371523 | Valley of stability, magic numbers |
| D41 | 10.5281/zenodo.19384396 | Island of inversion ⁸⁴,⁸⁶Mo |
| D42 | 10.5281/zenodo.20041348 | H3 theorem (Indifference Lemma) |
| D43 | 10.5281/zenodo.19678389 | Causal chain, ε_geom (OP-A resolved) |
| D44 | 10.5281/zenodo.19678474 | Filter factor k (OP-B resolved) |
| D45 | 10.5281/zenodo.19810259 | PBH threshold + Fermi-LAT prediction |
| DN-fr | 10.5281/zenodo.19924230 | Quoi que nous soyons (français) |
| D46 | 10.5281/zenodo.19956932 | Born Level 2 : U(1), Hopf fibration |
| D47 | 10.5281/zenodo.19967918 | Sub-shell filling, periodic table (OP13+OP14) |
| D48 | 10.5281/zenodo.20151380 | Coherence stress-energy tensor C_coh |
| D49 | 10.5281/zenodo.20025166 | London equation (OP-London resolved) |
| D50 | 10.5281/zenodo.20029777 | BH coefficient 1/4 (OP12 resolved) |
| D51 | 10.5281/zenodo.20033520 | Cosmological leakage constant C |
| D52 | 10.5281/zenodo.20036769 | Three leakage bases identified |
| D53 | 10.5281/zenodo.20052558 | Causal closure C1–C4 → Λ |
| DL01 | 10.5281/zenodo.20132166 | From Axioms to Life (PDL-V) |
| DL02 | 10.5281/zenodo.20132228 | Life/consciousness thresholds |
| D54 | 10.5281/zenodo.20157203 | Equation of state coherence fluid |
| D55 | 10.5281/zenodo.20179924 | Weinberg angle θ_W = 19π/119 |
| DS01 | 10.5281/zenodo.20187274 | Programme closure at D55 |
| D-exp-SP2 | 10.5281/zenodo.20242505 | Photon-to-electron conversion topology |
| D-exp-ZIB | 10.5281/zenodo.20262293 | Zinc-ion supercapacitor PDL |
| D-exp-MP01 | 10.5281/zenodo.20316492 | Structural lacunae Tc/Pm |
| D-exp-Zr | 10.5281/zenodo.20321750 | QPT Zirconium |
| D56 | 10.5281/zenodo.20409903 | N_comp(k) = k (OP-D41-1-A resolved) |
| D-exp-E2-PDL | 10.5281/zenodo.20593807 | f₇/₂ mirror nuclei B(E2) |
| D57 | 10.5281/zenodo.20600264 | SU(2) gauge + sin²θ_W = 1/4 (D57) |
| D58-py | 10.5281/zenodo.20623231 | PDL_SU3_script1.py |
| D58 | 10.5281/zenodo.20622987 | SU(3) gauge (D58) |
| D59-py | 10.5281/zenodo.20628926 | PDL_D59_script1.py |
| D59 | 10.5281/zenodo.20629282 | SU(3)_c representation 3 (D59) |
| D60 | 10.5281/zenodo.20639684 | H_SU2 theorem: G_eff = S₄/V₄ ≅ S₃ (D60) + PDL_C1V4_script1.py + PDL_C1V4_script2.py |
| D61 | 10.5281/zenodo.20645713 | Gauge dynamics: D_μ from C4 (D61) + PDL_D61_script1.py + PDL_D61_script2.py |
| DM v28 | DOI à compléter | Global Mapping v28 — D60+D61 intégrés, diagramme gauge complet |
| N01 | 10.5281/zenodo.20523343 | PDL–OFN Bridge : β₁=3 |

---

## Current Epistemic State — Gauge Sector (updated Session 55)

```
THÉORÈMES INCONDITIONNELS de C1–C4 (secteur de jauge) :

U(1) :
  Fibration de Hopf depuis équivalence de signe K₄       [D46]
  Born Level 2 : règle de Born depuis U(1)               [D46]

SU(2) :
  sin²θ_W(tree) = sin²(π/R_e) = 1/4                     [D57]
  θ_W(D55) = (π/R_e)×(114/119) — angle exact            [D55+D57]
  G_eff = S₄/V₄ ≅ S₃ — H_SU2 RÉSOLU                   [D60]
  s → −s brise C2 [résultat négatif documenté]           [D60]
  orbit-4 ≅ V₄ comme V₄-ensemble régulier               [D60]
  Pairings = cosets de H₁,H₂,H₃ dans V₄                [D60]
  V₄ fixe orbit-1 et orbit-3 pointwise                  [D60]
  C1-admissibilité = V₄-invariance sur tout Coh(K₄)     [D60]

SU(3) :
  S₄/V₄ ≅ S₃ = groupe de Weyl de A₂                    [D58, L1]
  V₄\{e} ↔ orbites V₄-arêtes (bij. S₄-équivariante)    [D58, L2]
  A₄/V₄ ≅ ℤ₃ = centre de SU(3)                        [D58, L3]
  Cartan rang 2 via R_e=6                                [D58, L4]
  Système de racines A₂ dans plan trace-nulle            [D58, L5]
  SU(3) depuis C1–C4 + Cartan–Killing–Weyl              [D58]

Représentation fondamentale :
  χ_π = χ_trivial + χ_standard                          [D59, L2]
  W = {a+b+c=0} porteur canonique                       [D59, L3]
  A₂ dans W, Cartan [[2,-1],[-1,2]]                     [D59, L4]
  Δn=4>0 → orientation 3 vs 3̄                         [D59, L5 depuis D47]
  k₃/(k₁+k₂) = R_e = 6 exact                           [D59, L5]
  SU(3)_c dans 3 sur W                                  [D59]

Dynamique de jauge :                                     ← NOUVEAU (D61)
  Transports C4-admissibles = Coh(K₄) ≅ Z₂³            [D61, script1, α]
  V₄ fidèle par automorphismes sur Coh(K₄)              [D61, script2, β]
  F ≅ V₄ fixe = couplages parfaits K₄ = axes W (D59)   [D61, script2]
  Z₂³ ⋊ V₄ ordre 32 bien défini                        [D61, β]
  Consistance Z₂³ ⋊ V₄ → G_gauge (via D46–D60)         [D61, γ]
  D_μ = ∂_μ − igA_μ unique (via Utiyama)               [D61, δ]

COROLLAIRE GLOBAL (mis à jour Session 55) :
  SU(3) × SU(2) × U(1) + représentation 3 + D_μ
  THÉORÈME de C1–C4 (structure et dynamique de jauge)
  (D46 + D60 + D58 + D59 + D61)
  AUCUNE ÉTAPE CONJECTURALE RÉSIDUELLE dans le secteur de jauge
  Ce qui reste ouvert : masses des bosons, structure de génération

RÉSULTATS NÉGATIFS DOCUMENTÉS (valeur scientifique positive) :
  V₄ fidèle sur H₁(K₄;ℝ)           [D58 — invalidé stratégie homologie]
  s → −s brise C2                   [D60 — pulsation ≠ flip global]
  bijection (T₂)↔(T₃) non S₄-éq.  [D59]
  Conjecture initiale (admissible = V₄) réfutée  [D61 — Coh(K₄) ≅ Z₂³]
  Flip global non admissible (ν=4/4)             [D61]
```

---

## Dependency Map — Critical Path (updated Session 54)

```
LAYER 0   C1–C4 (axiomes)
LAYER 1   K₄, n=3, exponent 18                      [✓] D16a, D23
LAYER 2   Quintuplet, R_surf, H3, κ                  [✓] D16b, D05, D42
LAYER 3   (A)∧(B), Gates 1–3, Δm_iso                [✓] D29, D30, D31
LAYER 4   ε_geom, k, ε_G                             [✓] D43v3, D44
LAYER 5   G_PDL, α, μ*                               [✓] D21, D12, D25
LAYER 6   QCD interface Δm_iso = 2.532 MeV           FORCED
LAYER 7   Dynamiques — COMPLETE                      [✓] D32–D35, D42, D46, D49
LAYER 8   Cosmologie                                 [✓] D27, D35, D42
LAYER 9   Stabilité nucléaire — COMPLETE             [✓] D40, D47
LAYER 10  Trous noirs — COMPLETE                     [✓] D37, D38, D42, D45, D50
LAYER 11  Tenseur de cohérence — COMPLETE            [✓] D48v3, D49, D51–D52, D54
LAYER 12  Λ_PDL — COMPLETE                          [✓] D51, D52, D53
LAYER 13  Vie/conscience                             [✓] DL01, DL02; [?] DL03
LAYER 14  Électrofaible
           θ_W = 19π/119                             [✓ THÉORÈME — D55]
           sin²θ_W(tree) = sin²(π/R_e) = 1/4        [✓ THÉORÈME — D57]
           θ_W(D55) = (π/R_e)×(114/119)             [✓ THÉORÈME — D57+D55]
           H_SU2 : G_eff = S₄/V₄ ≅ S₃              [✓ THÉORÈME — D60]  ← RÉSOLU
           OP-D57-1 → RÉSOLU (D60)                   [✓ Session 54]
           OP-D57-2 : Dic₃ comme groupe de jauge     [OUVERT — MEDIUM]
           W/Z mass ratio (OP10-c)                    [OUVERT — HIGH]
LAYER 14b Groupe de jauge — COMPLET (algébrique + représentation + dynamique)
           S₄/V₄ ≅ S₃ = Weyl(A₂)                   [✓ THÉORÈME — D57+D58, L1]
           V₄\{e} ↔ orbites V₄-arêtes (bij. S₄-éq.) [✓ THÉORÈME — D58, L2]
           A₄/V₄ ≅ ℤ₃ = centre SU(3)               [✓ THÉORÈME — D58, L3]
           Cartan rang 2 via R_e=6                   [✓ THÉORÈME — D58, L4]
           Système de racines A₂                     [✓ THÉORÈME — D58, L5]
           SU(3) depuis C1–C4 + Cartan–Killing       [✓ THÉORÈME — D58]
           SU(3)×SU(2)×U(1) algébrique              [✓ COROLLAIRE — D46+D60+D58]
           V₄ fidèle sur H₁(K₄;ℝ) [résultat négatif] [✓ VÉRIFIÉ — D58]
           s → −s brise C2 [résultat négatif]        [✓ VÉRIFIÉ — D60]
           orbit-4 ≅ V₄ régulier                    [✓ THÉORÈME — D60]
           Pairings = cosets H₁,H₂,H₃               [✓ THÉORÈME — D60]
           V₄ fixe orbit-1 et orbit-3               [✓ THÉORÈME — D60]
           C1-admissibilité = V₄-invariance          [✓ THÉORÈME — D60]
           χ_π = χ_trivial + χ_standard              [✓ THÉORÈME — D59, L2]
           W = {a+b+c=0} porteur canonique           [✓ THÉORÈME — D59, L3]
           A₂ dans W, Cartan [[2,-1],[-1,2]]         [✓ THÉORÈME — D59, L4]
           Δn=4>0 → orientation 3 vs 3̄              [✓ THÉORÈME — D59, L5 depuis D47]
           k₃/(k₁+k₂) = R_e = 6 exact              [✓ THÉORÈME — D59, L5]
           SU(3)_c dans 3 sur W                      [✓ THÉORÈME — D59]
           (T₂)↔(T₃) non S₄-équivariante [négatif]  [✓ VÉRIFIÉ — D59]
           Coh(K₄) ≅ Z₂³ — transports C4-admissibles [✓ THÉORÈME — D61, α] ← NOUVEAU
           V₄ fidèle par Aut(Z₂³) sur Coh(K₄)       [✓ THÉORÈME — D61, β] ← NOUVEAU
           F ≅ V₄ = sous-groupe points fixes D61     [✓ THÉORÈME — D61, script2] ← NOUVEAU
           Consistance Z₂³⋊V₄ → G_gauge             [✓ CONSISTANCE — D61, γ] ← NOUVEAU
           D_μ = ∂_μ − igA_μ unique (via Utiyama)   [✓ THÉORÈME — D61, δ] ← NOUVEAU
           OP-D59-2 → RÉSOLU (D61)                   [✓ Session 55] ← NOUVEAU
           OP-D58-1 → RÉSOLU (D59)                   [✓ Session 53]
           OP-D58-3 → RÉSOLUE (D59)                  [✓ Session 53]
           OP-D59-1 : masse des quarks               [OUVERT — MEDIUM]
           OP-D59-2 : D_μ depuis C4 → RÉSOLU (D61)  [✓ Session 55] ← NOUVEAU
LAYER 15  Spectroscopie nucléaire
           N_comp(k) = k                             [✓ THÉORÈME — D56]
           B(E2) ∝ k  (H_B)                          [conjecture — D41]
           OP-E2-PDL                                 [OUVERT — HIGH]
           D-exp-E2-PDL                              [✓ publié — 10.5281/zenodo.20593807]
LAYER 16  Applications exploratoires                 [✓] D-exp-SP2/ZIB/MP01/Zr
LAYER 17  PDL–OFN Bridge
           β₁=3 nécessaire pour Λ                   [✓ THÉORÈME — N01]
           n=6 dimension minimale pour β₁=3          [✓ THÉORÈME — N01]
           b₁(Ω₂₁)=3 vérifié indépendamment         [✓ RÉSULTAT — N01]
           A₄/V₄ ≅ ℤ₃ ↔ β₁=3 ↔ centre SU(3)       [✓ THÉORÈME — D57+D58]
           (T₂) labellise axes de W (D59)            [✓ THÉORÈME — D59]
           OP-OFN-1 : 3 cycles PDL ↔ 3 générations  [OUVERT — HIGH]
           OP-OFN-2 : objet X commun K₄/Ω₂₁         [OUVERT — MEDIUM]
           OP-OFN-3 : SU(3)×SU(2)×U(1) depuis C1–C4 [RÉSOLU — D46+D60+D58]
LAYER 18  Dissémination
           D57 déposé Zenodo                         [✓ Session 50 — 10.5281/zenodo.20600264]
           PDL_SU3_script1.py déposé Zenodo          [✓ Session 51 — 10.5281/zenodo.20623231]
           D58 déposé Zenodo                         [✓ Session 51 — 10.5281/zenodo.20622987]
           DM v25 déposé Zenodo                      [✓ Session 51 — 10.5281/zenodo.20605620]
           DM v26 déposé Zenodo                      [✓ Session 52 — 10.5281/zenodo.20625504]
           PDL_D59_script1.py déposé Zenodo          [✓ Session 53 — 10.5281/zenodo.20628926]
           D59 déposé Zenodo                         [✓ Session 53 — 10.5281/zenodo.20629282]
           DM v27 déposé Zenodo                      [✓ Session 53 — 10.5281/zenodo.20630421]
           D60 + scripts C1V4 déposés Zenodo         [✓ Session 54 — 10.5281/zenodo.20639684]
           D61 + scripts D61 déposés Zenodo          [✓ Session 57 — 10.5281/zenodo.20645713]
           DM v28 déposé Zenodo                       [✓ Session 56/57 — DOI à compléter]
           Site web mis à jour (D60, D61, DM v28)    [✓ Session 57]
           N01 à uploader ResearchGate               [en attente]
           Three Roads — draft révisé Oleg en attente [en attente]
```

**Resolved milestones:**
```
GATE 1 (D29) | GATE 2 (D30) | GATE 3 (D36, D42)
OP1 (D42) | OP-A (D43v3) | OP-B (D44) | OP8 (D44)
OP4 (D46) | OP13 (D47) | OP14 (D47)
OP2-D35 (D48v3) | OP-SPIN (D48v3)
OP-LONDON (D49) | OP12/BH-3 (D50) | OP1-D35 (D51+D52)
OP11 (D53) | OP-PRESSURE (D54) | OP10 θ_W (D55)
OP7 → MÉTROLOGIQUE (DS01) | OP10-c → ARBRE CORRECT (DS01)
D-exp-SP2 [✓] | D-exp-ZIB [✓] | D-exp-MP01 [✓] | D-exp-Zr [✓]
OP-D41-1-A → N_comp(k)=k  [✓ D56, Session 46]
β₁=3 nécessaire PDL  [✓ N01 Script 1, Session 47]
n=6 dimension minimale β₁=3  [✓ N01 Script 4, Session 47]
N01 déposé Zenodo  [✓ Session 48 — 10.5281/zenodo.20523343]
D-exp-E2-PDL déposé Zenodo  [✓ Session 49 — 10.5281/zenodo.20593807]
sin²θ_W(tree) = sin²(π/R_e) = 1/4  [✓ D57 théorème, Session 50]
A₄/V₄ ≅ ℤ₃ ↔ β₁=3  [✓ D57, Session 50 — résolution partielle OP-OFN-1]
D57 déposé Zenodo  [✓ Session 50 — 10.5281/zenodo.20600264]
DM v25 déposé Zenodo  [✓ Session 51 — 10.5281/zenodo.20605620]
SU(3) — théorème algébrique de C1–C4  [✓ D58, Session 51]
SU(3)×SU(2)×U(1) algébrique  [✓ D46+D57+D58, Session 51]
V₄ fidèle sur H₁(K₄;ℝ) [résultat négatif documenté]  [✓ D58, Session 51]
OP-OFN-3 → RÉSOLU (algébrique)  [✓ D58, Session 51]
PDL_SU3_script1.py déposé Zenodo  [✓ Session 51 — 10.5281/zenodo.20623231]
D58 déposé Zenodo  [✓ Session 51 — 10.5281/zenodo.20622987]
DM v26 déposé Zenodo  [✓ Session 52 — 10.5281/zenodo.20625504]
SU(3)_c dans 3 — représentation fondamentale  [✓ D59, Session 53]
W = {a+b+c=0} porteur canonique  [✓ D59, Session 53]
Δn=4>0 → orientation matière/antimatière  [✓ D59, Session 53]
k₃/(k₁+k₂) = R_e = 6 exact  [✓ D59, Session 53]
OP-D58-1 → RÉSOLU (représentation physique SU(3)_c)  [✓ D59, Session 53]
OP-D58-3 → RÉSOLUE (représentation fondamentale 3)  [✓ D59, Session 53]
PDL_D59_script1.py déposé Zenodo  [✓ Session 53 — 10.5281/zenodo.20628926]
D59 déposé Zenodo  [✓ Session 53 — 10.5281/zenodo.20629282]
DM v27 déposé Zenodo  [✓ Session 53 — 10.5281/zenodo.20630421]
OP-D57-1 → RÉSOLU : H_SU2 théorème inconditionnel de C1+C2  [✓ D60, Session 54]
s → −s brise C2 [résultat négatif documenté]  [✓ D60, Session 54]
orbit-4 ≅ V₄ régulier — trois pairings = cosets H₁,H₂,H₃  [✓ D60, Session 54]
V₄ fixe orbit-1 et orbit-3 pointwise  [✓ D60, Session 54]
C1-admissibilité = V₄-invariance sur tout Coh(K₄)  [✓ D60, Session 54]
G_eff = S₄/V₄ ≅ S₃ — théorème inconditionnel de C1+C2  [✓ D60, Session 54]
SU(3)×SU(2)×U(1) + représentation 3 — AUCUNE étape conjecturale résiduelle  [✓ D46+D60+D58+D59]
D60 + PDL_C1V4_script1.py + PDL_C1V4_script2.py déposés Zenodo  [✓ Session 54 — 10.5281/zenodo.20639684]
OP-D59-2 → RÉSOLU : D_μ = ∂_μ − igA_μ théorème de C4 via Utiyama  [✓ D61, Session 55]
Coh(K₄) ≅ Z₂³ — groupe maximal de transports C4-admissibles  [✓ D61 script1, Session 55]
V₄ fidèle par Aut(Z₂³) — Z₂³ ⋊ V₄ ordre 32  [✓ D61 script2, Session 55]
F ≅ V₄ = sous-groupe points fixes labellé couplages parfaits  [✓ D61 script2, Session 55]
Chaîne causale C1–C4 → D_μ fermée  [✓ D61, Session 55]
Conjecture initiale (admissible = V₄) réfutée [résultat négatif documenté]  [✓ D61, Session 55]
D61 déposé Zenodo  [✓ Session 57 — 10.5281/zenodo.20645713]
DM v28 rédigé et déposé Zenodo  [✓ Session 56/57 — DOI à compléter]
Site web cedriclaubscher.ch mis à jour (D60, D61, DM v28)  [✓ Session 57]
```

---

## Open Problems (updated Session 55)

**Résolu (Session 46) :**
- **[RESOLVED]** OP-D41-1-A : N_comp(k) = k (D56).

**Résolu (Session 51) :**
- **[RESOLVED — algébrique]** OP-OFN-3 / OP-SU3 : SU(3)×SU(2)×U(1) comme théorème algébrique de C1–C4 (D46+D60+D58).

**Résolu (Session 53) :**
- **[RESOLVED]** OP-D58-1 : identification physique SU(3)_c (D59).
- **[RESOLVED]** OP-D58-3 : représentation fondamentale 3 depuis C1–C4 (D59).

**Résolu (Session 54) :**
- **[RESOLVED]** OP-D57-1 : H_SU2 théorème inconditionnel de C1+C2 (D60).

**Résolu (Session 55) :**
- **[RESOLVED]** OP-D59-2 : D_μ = ∂_μ − igA_μ comme théorème de survie C4 (D61). La dynamique de jauge est une conséquence de C4, sans postulat variationnel.

**Résolu partiellement :**
- **[PARTIAL]** OP-OFN-1 : A₄/V₄ ≅ ℤ₃ (D57+D58) + triplet (T₂) labellise axes de W (D59). Lien formel 3 cycles PDL ↔ 3 générations OFN reste ouvert.
- **[PARTIAL]** OP-SU2 : sin²θ_W(tree) = 1/4 théorème (D57), H_SU2 théorème (D60). OP-D57-2 (Dic₃ comme générateur du groupe de jauge faible par universalité) reste ouvert.

**Ouverts prioritaires :**
- **[HIGH]** OP-D61-1 : masses des bosons W±/Z⁰ depuis C1–C4 (D-electroweak-WZ).
- **[HIGH]** OP-D61-2 : trois générations de fermions depuis C1–C4.
- **[HIGH]** OP-D57-2 : Dic₃ comme générateur structurel du groupe de jauge faible.
- **[HIGH]** OP10-c : rapport W/Z = cos(19π/119) depuis C1–C4.
- **[HIGH]** OP-OFN-1 : lien formel 3 cycles PDL ↔ 3 générations OFN.
- **[HIGH]** OP-E2-PDL : opérateur E2 dans le formalisme PDL (Lacunes G1, G2).
- **[MEDIUM]** OP-D61-3 : dérivation autonome de G_gauge depuis Z₂³ ⋊ V₄ sans invoquer D46–D60 pour la flèche γ.
- **[MEDIUM]** OP-D59-1 : masse des quarks depuis C1–C4.
- **[MEDIUM]** OP-OFN-2 : objet X commun dont K₄ et Ω₂₁ sont deux projections.
- **[MEDIUM]** OP9 : masses muon/tau (générations 2 et 3).
- **[MEDIUM]** OP15 : noyaux Z > 82.
- **[MEDIUM]** DL03 : encadrement numérique n*_vie.

**Frontières expérimentales :**
- FLAG/lattice QCD → Δm_iso ±0.04 MeV
- Fermi-LAT → IGRB (Arbey+Auffinger en attente)
- FRIB/RIKEN → P7/P8 (Recchia+Lenzi — message envoyé, en attente)
- Ha et al. / Escudeiro et al. → cités dans D56

---

## Instructions for Next Session

Start by saying: *"Read PDL_context.md and the corpus files from the project."*

**Priorité immédiate Session 58 :**

1. **[URGENT]** Compléter le DOI de DM v28 dans PDL_context.md une fois le dépôt Zenodo effectué.
2. **[URGENT]** Pousser PDL_context.md mis à jour sur GitHub (laubscher-lab/PDL-framework).
3. **[URGENT]** Uploader N01 sur ResearchGate (type : Preprint) + notifier Oleg des DOIs D58, D59, D60, D61.
4. **[HIGH]** OP-D61-1 : masses des bosons W±/Z⁰ (D-electroweak-WZ) — prochain document structurel.
5. **[HIGH]** OP10-c : rapport W/Z = cos(19π/119) depuis C1–C4.

**LaTeX conventions (consolidées Session 51) :**
- No spurious mid-sentence line breaks in .tex source
- British English throughout
- `\bibliographystyle{unsrt}` avec `\usepackage[numbers]{natbib}`
- Environments tcolorbox : theorem/proof/definition/conjecture/openproblem/resolvedproblem
- Epistemic status table avec colonnes `p{}` fixes
- **`\texorpdfstring{$...$}{version texte pur}` OBLIGATOIRE pour tout titre `\section`/`\subsection` contenant des maths**
- **Bloc `\pdfstringdefDisableCommands{...}` complet dans le préambule (voir D58_gauge_SU3_v2.tex lignes 47–84)**

**Nomenclature :**
- N-series : notes conjointes avec collaborateurs externes. N01 = PDL–OFN (β₁=3).
- D-series : documents solo PDL.
- D-exp-series : documents exploratoires applications.
- DM : Global Mapping (version courante : v28, DOI à compléter ; v27 : 10.5281/zenodo.20630421).

**PDL–OFN Bridge discipline :**
- β₁=3 : THÉORÈME pour K₄, RÉSULTAT VÉRIFIÉ pour Ω₂₁
- A₄/V₄ ≅ ℤ₃ : THÉORÈME (D57+D58) — origine combinatoire commune de β₁=3 et centre de SU(3)
- Triplet (T₂) labellise les axes de W (D59) : THÉORÈME
- 3 cycles PDL = 3 générations OFN : PROBLÈME OUVERT (OP-OFN-1)
- Analogies Three Roads : PAS des identités prouvées, uniquement analogies structurelles candidates

*Références canoniques : D01–D61 + DS01 + DL01–DL02 + D-exp-SP2 + D-exp-ZIB + D-exp-MP01 + D-exp-Zr + D-exp-E2-PDL + N01 + DM v28.*
*DOIs principaux : D57 : 10.5281/zenodo.20600264 | D58 : 10.5281/zenodo.20622987 | D58-py : 10.5281/zenodo.20623231 | D59-py : 10.5281/zenodo.20628926 | D59 : 10.5281/zenodo.20629282 | DM v27 : 10.5281/zenodo.20630421 | D60 : 10.5281/zenodo.20639684 | D61 : 10.5281/zenodo.20645713 | DM v28 : DOI à compléter*
*Note dépôts groupés : D60 (DOI 10.5281/zenodo.20639684) contient D60 + PDL_C1V4_script1.py + PDL_C1V4_script2.py. D61 (DOI 10.5281/zenodo.20645713) contient D61 + PDL_D61_script1.py + PDL_D61_script2.py.*
