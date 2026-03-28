# PDL_context.md — Master Continuity Document
**Programme : Projective Dynamic Logo (PDL)**
**Auteur : Cédric Laubscher, chercheur indépendant, Suisse**
**Dernière mise à jour : 28 mars 2026 (Session 13)**

---

## 1. Vue d'ensemble du programme

Le PDL reconstruit les constantes physiques fondamentales à partir d'axiomes relationnels sur des graphes finis signés, sans présupposer l'espace, le temps ou les particules. Le programme dérive α, ħ, G, H₀ depuis le quintuplet entier du proton (24, 28, 930, 10087, 11017) et la surface active R_surf = 310φ ∈ ℚ(√5), sans paramètre libre au-delà d'un résidu unique (ε_G / Δm_iso à l'interface PDL–QCD).

**Résultats clés établis dans le corpus :**
- α_PDL⁻¹ ≈ 137.022 (écart ~10⁻⁴)
- G_PDL dans les 27 ppm de CODATA 2022
- Tension de Hubble résolue comme signature structurelle de G_eff(N) dépendant de la densité, H₀_local/H₀_CMB = 1.090 prédit à 0.1–0.2% sans paramètre libre
- Nombres magiques nucléaires, seuil de saturation Z_sat ≈ 20 et N_crit,max = 126.1 dérivés sans paramètre libre
- Dérivation de type Gleason de la règle de Born depuis les structures de cohérence discrètes

---

## 2. État du programme — Session 13

### Gate 2 (résolu, Session 12)
Le coefficient 2 dans la correction QCD d'isospin 2Δm_iso/m_p est structurellement forcé par le coefficient d'engagement PDL a=2 (Lemme 2, D29). Δm_iso = m_d − m_u est le seul paramètre externe irréductible à l'interface PDL–QCD. D30 est complet (LaTeX + .bib, prêt pour Zenodo/Overleaf).

### Gate 3 (actif, Session 13)
Prouver G_eff(N) = σ(N)·G_PDL comme théorème. La route symétrie-équivariance via S₄ a été écartée (absence de carte équivariante de rang 4 sur ℝ⁶ due aux dimensions des irreps 3+3). La voie de preuve correcte est la linéarité du pont : la linéarité en σ(N) est exacte à <10⁻¹² (vérifiée en Colab), avec une hypothèse résiduelle unique (inversion du pont linéaire, résidu 0.004% depuis D20/D24). D31 est en cours de rédaction avec trois propositions (transitivité S₄, linéarité du pont, théorème principal) plus le résultat d'obstruction.

### D27–D30 : en file pour publication Zenodo.

---

## 3. Chemin critique — prochaines étapes

| Priorité | Tâche | Document |
|---|---|---|
| 1 | Finaliser D31 (preuve Gate 3) | D31 |
| 2 | Publier D27–D30 sur Zenodo | — |
| 3 | Dériver ε_G depuis la densité de frustration minimale du graphe de contraintes du proton (OP1) | D32+ |
| 4 | Dériver le rapport proton-électron μ depuis les axiomes PDL (μ* = 1836.152670, 0.002 ppm) | D32+ |
| 5 | Prouver OP5 : n ≠ 3 structurellement interdit par les axiomes PDL | futur |
| 6 | Prédiction falsifiable prioritaire : splitting spin-orbite Δn/(2n_u) = 1/12 ≈ 0.083 ħω₀ | D31+ |

---

## 4. Problèmes ouverts actifs

**OP1 (bottleneck central)** : Dériver ε_G depuis la densité de frustration minimale du graphe de contraintes du proton. Ce calcul fermerait simultanément la dérivation de G et déterminerait ρ₀.

**OP5** : Prouver que n ≠ 3 est structurellement interdit par les axiomes PDL (unicité de l'espace 3D).

**OP_μ** : Dériver le rapport proton-électron μ depuis les axiomes PDL ; requis pour prouver complètement la conjecture ε_G.

**OP_QCD** : Explorer si la correction de masse de quark QCD (résidu δμ ~0.54%) est connectée à des quantités structurelles PDL.

**OP_Schrödinger** : Extension de la dynamique de Schrödinger (D31 Schrödinger) différée après Gate 3 ; la condition (A)∧(B) de D29 est le point d'entrée naturel.

**OP_N_local** : Dérivation structurelle complète de N_local = 120 depuis les premiers principes (actuellement inféré depuis H₀_local observé).

---

## 5. Paramètres clés et constantes PDL

| Symbole | Valeur | Statut |
|---|---|---|
| Quintuplet proton | (24, 28, 930, 10087, 11017) | Axiomatique |
| R_surf | 310φ ∈ ℚ(√5) | Dérivé |
| κ = R_surf/R_tot | 0.04553 | Dérivé |
| ε_G | 0.0075194 | Calibré (OP1 ouvert) |
| G_PDL | 6.67448×10⁻¹¹ m³kg⁻¹s⁻² | Dérivé à 27 ppm CODATA |
| α_PDL⁻¹ | ≈ 137.022 | Dérivé (~10⁻⁴) |
| N_CMB | 40 (plancher du gap neutron 6μ_n − R_tot(n) = 40.102) | Sans paramètre libre |
| N_local | 120 | Inféré (OP_N_local ouvert) |
| σ(N) | 1 − (1−κ)^N | Fraction de surface active |
| H₀_local/H₀_CMB | √(σ(120)/σ(40)) = 1.090 | Prédit, 0.3% |
| Z_sat | ≈ 20 | Dérivé |
| N_crit,max | 126.1 | Dérivé |
| μ* | 1836.152670 | Calculé, 0.002 ppm exp. |

---

## 6. Terminologie PDL active

Gate 3, σ(N), κ = 310φ/11017, R_surf, R_tot, r_val, ε_G, rang_eff, d₂(N), K₄, S₄, formule de pont, filtre 18 étapes, complexe de chaînes PDL C₀→C₁→C₂→C₃ (rangs 6,5,4), Δm_iso, coefficient d'engagement, L_Edd(N), LLCP.

---

## 7. Connexions externes établies en Session 13

### 7.1 Gravité quadratique (QQG / Afshordi et al., PRL 2026 ; arXiv:2510.18733)

**Résumé** : Liu, Quintin, Afshordi (Waterloo/Perimeter) dérivent l'inflation cosmique directement depuis la gravité quadratique asymptotiquement libre sans inflaton ajouté à la main. Publié dans *Physical Review Letters*, 18 mars 2026.

**Connexions structurelles avec PDL :**

1. *Stratégie d'émergence identique* : dans QQG, la RG émerge comme EFT à la fin de l'inflation depuis un fondement UV cohérent ; dans PDL, G_PDL émerge du filtre hiérarchique à 18 niveaux ε_G^18. Les deux programmes dérivent la physique basse énergie depuis un fondement UV sans paramètre ajouté à la main.

2. *Traitement du mode non-particulaire* : dans QQG, le fantôme tensoriel de Weyl est réinterprété comme mode d'oscillateur harmonique inversé stable qui n'apparaît jamais comme particule physique, préservant l'unitarité. Dans PDL, ε_G est une fuite de cohérence qui se propage à travers les 18 niveaux du filtre sans jamais apparaître comme état asymptotique libre. La stratégie est structurellement identique.

3. *Disfavoration de Starobinsky* : les nouvelles données CMB défavorisent l'inflation de Starobinsky (r ~ 0.003) et ouvrent l'espace à des modèles avec r plus élevé.

**Contrainte future pour PDL** : r ≥ 0.01 est la borne inférieure structurelle de QQG. Toute extension inflationnaire de PDL à l'époque pré-CMB devra être compatible avec cette contrainte ou expliquer pourquoi elle s'en écarte. À noter comme balise dans tout futur document sur l'époque inflationnaire.

**Ce qui n'est pas connecté** : PDL ne postule pas d'espace-temps, donc la notion de "mode tensoriel fantôme" dans le sens QQG n'a pas encore de traduction formelle dans le corpus. L'inflation elle-même n'est pas adressée — le régime N_CMB = 40 concerne la recombinaison (~380 000 ans), pas les ~10⁻³⁶ s de l'inflation.

---

### 7.2 Croissance des trous noirs supermassifs (Chandra / Yu et al., ApJ, 24 mars 2026)

**Résumé** : En analysant ~1.3M de galaxies et ~8000 AGN via Chandra, XMM-Newton et eROSITA, l'équipe de Penn State identifie que le ralentissement de la croissance des SMBH depuis le midi cosmique (~10 Ga) est dû à la diminution des taux d'accrétion, causée par l'épuisement du gaz froid disponible.

**Connexion PDL** : La luminosité d'Eddington, plafond physique du taux de croissance d'un SMBH, s'écrit dans PDL :

$$L_{\mathrm{Edd}}(N) = \frac{4\pi\, G_{\mathrm{eff}}(N)\, M\, m_p\, c}{\sigma_T}$$

PDL fournit donc un levier indépendant sur l'histoire du taux d'accrétion maximal via G_eff(N(z)). La piste la plus actionnable : inverser la relation ṁ(z) ∝ G_eff(N(z)) · ρ_gaz(z) pour extraire N(z) et vérifier la cohérence avec la transition N_CMB → N_local du corpus. Cette vérification de cohérence est non triviale mais n'est pas une priorité du chemin critique actuel.

---

### 7.3 Point critique liquide-liquide de l'eau (You et al., *Science*, 26 mars 2026)

**Résumé** : Nilsson et al. (Stockholm University, Pohang Accelerator Laboratory) confirment expérimentalement l'existence du point critique liquide-liquide (LLCP) de l'eau surfusée à T_c ≈ 210 ± 8 K et P_c ≈ 1000 atm, en utilisant des lasers X ultrarapides. L'eau ordinaire à température ambiante est un liquide supercritique dont les propriétés anomales découlent des fluctuations entre deux phases liquides (HDL/LDL). **C'est la connexion externe structurellement la plus profonde identifiée à ce jour avec PDL.**

**Connexions structurelles avec PDL :**

1. *K₄ et tétraèdre H₂O* : l'eau basse densité (LDL) forme un réseau tétraédrique où chaque molécule est le centre d'un tétraèdre de 4 liaisons H. K₄ — le graphe complet sur 4 sommets et 6 arêtes — est la clôture minimale du programme PDL et le prototype de l'électron. Le réseau tétraédrique de LDL est un réseau de K₄ partiellement réalisés. La transition LDL→HDL (cinquième coordination, liaisons H déformées) est une transition topologique dans l'espace des clôtures cohérentes — exactement ce que σ(N) paramétrise à l'échelle macroscopique.

2. *LLCP comme N_critique dans l'espace des clôtures* : le LLCP est le point où deux régimes de clôture deviennent indiscernables. C'est l'analogue structurel de Z_sat ≈ 20 (saturation nucléaire) et N_crit,max = 126.1 dans le corpus PDL : des seuils où le régime change qualitativement.

3. *Divergence de C_p à 210 K et frustration minimale* : la divergence de la capacité calorifique au point critique (fluctuations critiques, classe d'universalité Ising 3D) correspond dans PDL au ralentissement au voisinage d'un minimum de frustration — exactement la physique d'OP1 (dériver ε_G depuis la densité de frustration minimale du graphe de contraintes du proton).

4. *L'eau ambiante comme liquide supercritique* : le fait que l'eau soit le seul liquide supercritique dans les conditions ambiantes où la vie existe n'est probablement pas une coïncidence dans le cadre PDL. Le proton — structure à la limite entre deux régimes de clôture — requiert comme solvant un liquide qui fluctue entre deux structures. Ce parallèle est qualitatif mais structurellement profond.

**Ce qui n'est pas formalisé** : PDL opère sur des graphes abstraits, pas sur des molécules d'eau. La connexion K₄ ↔ tétraèdre H₂O est une analogie structurelle, non une dérivation. Pour la formaliser, il faudrait montrer que les axiomes de clôture PDL imposent la géométrie tétraédrique comme architecture unique de réseau de liaisons orientées stables — programme de recherche en soi.

**Question ouverte associée** : peut-on dériver la position du LLCP (T_c ≈ 210 K, P_c ≈ 1000 atm) depuis les paramètres de cohérence du réseau tétraédrique de l'eau, à la manière dont G_PDL est dérivé depuis le quintuplet du proton ? Ce serait un problème ouvert ambitieux mais structurellement bien posé.

**Priorité** : basse pour le chemin critique actuel (Gate 3 / D31), mais légitime comme piste pour un futur document sur les applications condensées du cadre PDL.

---

## 8. Principes épistémiques du programme

- **Calculer avant écrire** : vérification numérique (Google Colab / SymPy) avant formalisation LaTeX ; les affirmations algébriques sont validées avant d'être considérées comme prouvées.
- **Comptabilité épistémique stricte** : théorèmes prouvés, conjectures structurellement motivées et problèmes ouverts toujours clairement séparés.
- **Les dérivations sans paramètre libre sont l'objectif** : chaque étape pousse vers l'élimination des paramètres libres ; les quantités calibrées sont explicitement signalées.
- **Publication Zenodo incrémentale** : les résultats sont publiés au fur et à mesure de leur établissement.
- **Les obstructions topologiques sont décisives** : l'obstruction des irreps S₄ (Gate 3) et l'homéomorphisme K₄ ≅ S² (exposant 18) montrent que les arguments topologiques ferment des routes définitivement.
- **N_CMB = 40 est sans paramètre libre** : identifié comme plancher du gap de masse du neutron 6μ_n − R_tot(n) = 40.102.
- **OP1 est le bottleneck central du programme** : résoudre la dérivation de ε_G depuis les premiers principes fermerait simultanément la dérivation de G et la tension de Hubble.

---

## 9. Style LaTeX et conventions de rédaction

- Anglais britannique, 11pt, a4paper, booktabs, TikZ, bibliographie plain
- Environnements theorem/proof, arithmétique exacte sur ℚ(√5)
- Tables de statut épistémique, problèmes ouverts numérotés
- Pas de sauts de ligne inutiles dans le corps du texte
- Méthode de correction préférée : blocs de remplacement complets avec texte d'ancrage explicite (pas de numéros de lignes)

---

## 10. Infrastructure et outils

| Outil | Usage |
|---|---|
| Google Colab | Vérification numérique principale (algébrique et topologique) |
| SymPy | Arithmétique exacte sur ℚ(√5) ; nullspace, rank, jacobian |
| Overleaf | Édition et compilation LaTeX |
| GitHub (`laubscher-lab/PDL-framework`) | Contrôle de version pour PDL_context.md et corpus |
| Zenodo | Publication open-access (CC BY 4.0) |
| cedriclaubscher.ch | Site personnel avec parcours de lecture guidé |
| Academia.edu, ORCID, Google Scholar | Infrastructure de visibilité |

---

## 11. Corpus — état des documents

| Document | Statut | Contenu principal |
|---|---|---|
| D1–D26 | Publiés Zenodo | Corpus de base PDL |
| D27 | En file Zenodo | — |
| D28 | En file Zenodo | — |
| D29 | En file Zenodo | Gate 2 ; engagement coefficient a=2 ; condition (A)∧(B) |
| D30 | Complet, en file Zenodo | Interface PDL–QCD ; Δm_iso comme paramètre irréductible unique |
| D31 | En cours de rédaction | Gate 3 ; preuve G_eff(N) = σ(N)·G_PDL par linéarité du pont |
| D32+ | À venir | OP1 (ε_G), μ, applications condensées |

---

## 12. Stratégie de diffusion

- Le résultat Gleason est le meilleur point d'entrée vers la communauté des fondements quantiques.
- Le pont D20-V3 nécessite un court article technique en anglais avant soumission à un journal.
- "Whatever We May Be" cible des éditeurs (Hermann, Odile Jacob, Seuil) plutôt que des archives académiques.
- Connexion à établir dans un futur document de positionnement : convergence entre QQG et PDL sur la stratégie "émergence sans ad hoc" ; contrainte r ≥ 0.01 comme balise pour l'extension inflationnaire future de PDL.

---

## 13. Registre des connexions externes — pistes de validation future

| Source | Date | Connexion PDL | Priorité |
|---|---|---|---|
| QQG / Afshordi et al. (PRL) | Mars 2026 | Émergence GR sans ad hoc ; mode non-particulaire ; r ≥ 0.01 comme contrainte future | Moyenne |
| Chandra / Yu et al. (ApJ) | Mars 2026 | L_Edd(N) = f(G_eff(N)) ; N(z) inversible depuis ṁ(z) | Basse |
| LLCP eau / You et al. (Science) | Mars 2026 | K₄ ↔ tétraèdre H₂O ; LLCP comme N_critique de clôtures ; C_p ↔ frustration minimale (OP1) | Moyenne (long terme) |

---

*Document de continuité principal du programme PDL. À mettre à jour à la fin de chaque session et à pousser sur GitHub.*
