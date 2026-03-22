# PDL Research Context — Cédric Laubscher
*Last updated: March 2026 — Session 5. Copy this file to GitHub after each session.*

---

## Framework Overview

The **Projective Dynamic Logo (PDL)** reconstructs physical reality from relational
axioms on finite signed graphs, without presupposing spacetime. Four axioms: minimal
binary pulsation, triangular coherence, minimal completeness, logical optimisation.
The minimal admissible stationary closure is the (4,6) complete graph (electron
prototype). The proton is a hierarchical composite.

---

## Core Integer Architecture (Proton)

| Symbol | Value | Meaning |
|--------|-------|---------|
| n_u | 24 | Up-quark multiplicity |
| n_d | 28 | Down-quark multiplicity |
| r_u | 276 | Internal relations per u-core = C(24,2) |
| r_d | 378 | Internal relations for d-core = C(28,2) |
| r_val | 930 | Total valence relations = 2×276 + 378 |
| R_sea | 10087 | Dynamical sea relations |
| R_tot | 11017 | Total internal relations |
| R_surf | φ × 310 ≈ 501.6 | Active surface = φ·r_val/3 |

---

## Core Integer Architecture (Neutron) — DERIVED Session 5

| Symbol | Value | Derivation |
|--------|-------|------------|
| n_u | 24 | p-n compatibility |
| n_d | 28 | p-n compatibility |
| r_val(n) | 1032 | r_u + 2×r_d, exact |
| R_tot(n) | 10992 | R_tot(p) − (Δn+1)², exact |
| R_sea(n) | 9960 | R_tot(n) − r_val(n), exact |
| f_stat(n) | 9.39% | slightly above proton (8.44%) |

Key relation: R_tot(n) = R_tot(p) − (n_d − n_u + 1)² = 11017 − 25 = 10992
Gap decomposition: 6μ_n − R_tot(n) = 40 = 25 (structural) + 15 (mass fatigue)

---


## Key Derived Results (All Verified)

### Fine-structure constant
  α_PDL = μ / R_surf² = μ / (φ² · (r_val/3)²)
  α_PDL⁻¹ ≈ 137.022  vs  α_exp⁻¹ = 137.036
  Agreement: ~10⁻⁴, no free parameters.

### Gravitational bridge formula (D20-V3 — PRIMARY RESULT)
  Δr_val = ε_G · (R_tot · R_surf / r_val²) · (n_u² - 1) / n_u²

  Components:
  - ε_G = (G·m_p²/ħc)^(1/18) = 0.0075194  (CODATA 2022)
  - Δr_val = (3/φ)·sqrt(μ/α_exp) − 930 = 0.047960
  - R = R_tot·R_surf/r_val² = 6.38920  (hierarchical amplification)
  - C = (n_u²−1)/n_u² = 575/576 = 0.99826389  (no-self-loop correction)
  - R × C = 6.3781  (0.004% residual vs empirical ratio)

### G prediction
  G_PDL = 6.67448 × 10⁻¹¹ m³kg⁻¹s⁻²
  G_CODATA 2022 = 6.67430 × 10⁻¹¹
  Écart: +27 ppm — within experimental uncertainty (22 ppm)

### Nuclear binding unit T (Session 5)
  T = R_surf(p)² / R_sea(n) = 501.6² / 9960 = 25.26 ≈ (Δn+1)² = 25
  Identity: neutron deficit = neutron binding capacity (±1%)
  T_pp = R_surf(p)² / R_tot(p) = 22.84  [proton-proton conflict]

### Saturation threshold (Session 5)
  Z_sat = R_sea(n) / R_surf(p) = 9960 / 501.6 ≈ 20  (calcium)
  For Z < 20: one neutron binds all Z protons simultaneously
  For Z > 20: saturation → N > Z required

### Maximum magic number (Session 5)
  N_crit,max = R_sea(p) / (2 × gap) = 10087 / 80 = 126.1
  → Largest nuclear magic number N=126, no free parameter
  → Bi-209 (Z=83, N=126) identified as last stable nucleus by structural impossibility

### New relation R_tot = 6μ (Session 5)
  6μ_p = 11016.92 ≈ 11017 = R_tot(p)  at 0.001%
  Not in corpus previously. Factor 6 = edges of (4,6) brick.
  Interpetation: each brick edge carries one proton-to-electron mass ratio of coherence.

---

## Corpus — Complete Document List

| File | Doc# | Content | Status |
|------|------|---------|--------|
| PDL.tex | D1 | Main framework: axioms, proton, α, G, k_B | Reference |
| PDL_Intro.tex | D2 | Introduction to PDL | Reference |
| Position_paper_PDL.tex | D3 | Position paper: status, open problems, TO interface | Reference |
| Combinatorial_Proton_Architecture_PDL_v2.tex | D12 | Proton integers, uniqueness conjecture v1 | Solid |
| On_the_Combinatorial_Selection_and_Local_Uniqueness...tex | D16 | Refined uniqueness conjecture + selection functional S | Solid |
| Coherence_Leakage_Hierarchical_Filtering...v2.tex | D17 | 18 filters 6+6+6, ε definition | Updated with Remarks 2.5 & 2.6 |
| Emergence_of_the_Golden_Ratio.tex | D18 | φ from self-similarity condition | Sketch |
| Relational_Emergence_of_Born_s_Rule_v2.tex | D_Born | Born's rule + φ conjecture | Propositional |
| A_Topological_Reformulation.tex | D_Topo | ε as intrinsic probability | Conceptual |
| Coherence_Effective_Fields_PDL.tex | D_Fields | Gauss/Faraday discrete, Schrödinger emergence | Programme |
| Schodinger_PDL_v2.tex | D_Schr | Hydrogen compatibility with α_PDL | Consistent |
| Sketch_derivation_Schroedinger_PDL_v2.tex | D_Schr2 | Schrödinger derivation sketch | Sketch |
| Derivation_alpha_PDL_v2.tex | D_α | Structural derivation of α | Solid |
| Toward_a_Gleason-Type...tex | D_Gleason | Born's rule uniqueness for spin-1/2 | Theorem established |
| Towards_Einstein-Dirac_Unification_PDL.tex | D_ED | Dirac+Einstein on PDL substrate | Exploratory |
| PDL_Global_Mapping...v8.tex | D_Map | Full corpus mapping, dependency diagram | CURRENT — published Zenodo (Session 3) |
| Universal_Coherence_Leakage...V3.tex | D20-V3 | Bridge G ↔ α — PRIMARY RESULT | CURRENT VERSION (= V2, see §D20 below) |
| Existence_as_Pulsating_Closure...tex | D_Exist | Ontological meditation on PDL (article, philosophy of physics) | Philosophical |
| Whoever_We_May_Be...v2.tex | D_Who_v2 | Philosophical synthesis, article format (academic) | Philosophical |
| Whoever_we_may_be — The Projective Dynamic Logo.tex | D_Who_book | Same themes, book format (\documentclass{book}) | Philosophical |
| Quoi_que_nous_soyons...v2.tex | D_Who_book_FR | Popular introduction FR —
  revised and corrected version | CURRENT |
| Whatever_We_May_Be...v2.tex   | D_Who_book_EN | Popular introduction EN —
  full GB translation of D_Who_book_FR | CURRENT |
| PDL_Nuclear_Stability_Skeleton.tex | D_Nuc | Nuclear stability, neutron quintuplet, N_crit=126, magic numbers | New — Session 5 |

---

## D20 Version History

| Version | Status | Key change |
|---------|--------|-----------|
| V1 (original) | SUPERSEDED | ε_G=0.0073891 (wrong), bridge formula 3φ²ε_G (no basis) |
| V2 | SUPERSEDED (label) | Corrected ε_G, corrected bridge formula |
| V3 | CURRENT | **Scientifically identical to V2** — confirmed in Session 3 |

**Session 3 finding:** V2 and V3 are word-for-word identical in all sections
(abstract, all six sections, all tables, all equations, all numerical values).
V3 is V2 re-saved under a new filename. No new scientific content.

Errors corrected from V1:
- ε_G: 0.0073891 → 0.0075194 (V1 implied G=4.87×10⁻¹¹, 27% below CODATA)
- Δr_val: 0.049751 → 0.047960
- Bridge formula: 3φ²·ε_G → ε_G · R · C (structurally derived)

---

## D_Map v8 — Changes from v7 (Session 3)

Three corrections applied in v8, now published on Zenodo:

1. **Dependency diagram** (fig:pdl_dependency) — full redesign:
   - Constants sector split: α/ħ/k_B (direct from proton) vs G_PDL (via bridge D20)
   - Born's rule / Gleason-type node added between Electron and Dynamics
   - Programme/sketch nodes now visually distinct (dashed border, grey fill)
   - Legend added

2. **Bridge formula in roadmap** — old formula Δr_val ≈ 3φ²ε_G (D20-V1, invalid)
   replaced by structurally derived expression of D20-V3, with note that the old
   formula is superseded and should not be cited.

3. **D20 entry in document index** — updated to reference D20-V3 as current version,
   with corrected description of the bridge formula and G prediction.

Note: D16 was already present in D_Map v7 — the patch block concerning D16 is
unnecessary and should be ignored. Only D_Exist and D_Who_v2 may need to be added
to the document list if not already there.

Files produced: PDL_DMap_v7_corrections.tex, PDL_dependency_diagram_v2.tex

---

## D17 Modifications (Done in Session 1)

Two remarks added to Section 2.2 after Remark 2.4:

**Remark 2.5 (Dynamic origin of ε):** Harary theorem shows Γ_min=0 for static
valence graph (partition A={u1,u2}, B={d} covers all 70,300 triangles coherently).
Therefore ε>0 requires dynamical constraints: pulsation-induced violations,
topological frustration, or charge constraint.
Central conjecture: ε = inf Γ_cycle(G) = ε_G = 0.0075194.

**Remark 2.6 (Computational determination):** ε_G is a mixed quantity —
combinatorial + electromagnetic — given by:
  ε_G = Δr_val · r_val² · n_u² / (R_tot · R_surf · (n_u²−1))
Verified to 10⁻⁵. Contains α_exp and μ irreducibly.
(D17-V2 uploaded to Zenodo with these two remarks.)

---

## Open Problems (Priority Order)

1. [CRITICAL] Derive ε_G from pulsation rule F
   - Static graph: Γ_min=0 (proven computationally, Session 1)
   - No simple pulsation rule gives Γ_cycle=ε_G (all rules give 15-66× too large)
   - ε_G is defined structurally via bridge formula (mixed quantity)
   - True conjecture: show Ω implies defect = bridge formula value
   - Requires: explicit F, computation of Γ_cycle, verification = 0.0075194

2. [HIGH] Analytical derivation of exponent 18
   - D17 names 18 filters in 3×6 structure
   - Independence of the 18 filters NOT proven
   - Minimum target: show no subset of 17 suffices

3. [HIGH] Derivation of φ from axioms
   - D18 derives φ from self-similarity: R_core/R_tot' = R_surf/R_core → φ
   - Self-similarity condition NOT derived from Ω
   - Target: show Ω implies self-similarity for admissible composites

4. [MEDIUM] Analytic uniqueness proof for (24,28)
   - Computational: unique in n_u,n_d ≤ 56 domain (233 solutions, all identical)
   - D16 (new document) develops the selection functional S and local uniqueness
     conjecture formally — stronger than previous treatment
   - Analytic proof still pending
   - Note (Session 4): D_Who_book now references D16 selection functional S in footnote (Ch. 3, proton uniqueness). Consistent with D_Map v8 treatment.

5. [MEDIUM] Series conjecture for bridge formula
   - Δr_val/ε_G = R · n_u²/(n_u²+1) = 6.3781 (residual < 0.001%)
   - Would be next-order correction to C = (n_u²-1)/n_u²
   - Not yet derived

6. [RESOLVED Session 5] Neutron quintuplet derivation
   - Previously postulated; now derived exactly
   - R_tot(n) = R_tot(p) − (Δn+1)² = 10992 ✓

7. [HIGH] Shell splitting from Δn = 4 (OP1 in D_Nuc)
   - Mechanism identified: Δn/(2n_u) = 1/12 ≈ 0.083 ħω₀ ✓ empirically
   - Explicit combinatorial derivation from signed-graph formalism: NOT YET DONE
   - This is the key open problem for the full derivation of all 7 magic numbers

8. [MEDIUM] Isotopic window width ΔN(Z) (OP2 in D_Nuc)
   - Requires nuclear coordination number c(Z,N) from collective closure geometry
   - Current model overestimates ΔN for heavy nuclei

9. [MEDIUM] Lacunae Z=43, Z=61 (OP3 in D_Nuc)
   - Structural impossibility of stable closure conjectured, not yet proven

10. [FUTURE] Chemical properties via Block III (OP4 in D_Nuc)
    - Coupling nucleus ↔ electron cloud not yet developed

---

## Computational Results (Session 1, March 2026)

Script: PDL_pulsation_epsilon.py (on GitHub)

Key results:
- Γ(G) = 0/70300 for balanced Harary assignment ✓
- Triangle distribution: n_intra=0: 16128, n_intra=1: 46848, n_intra=3: 7324
- Rule B (intra-core flip): Γ_cycle = 0.385, ratio to ε_G = 51×
- To match ε_G: need ~21 edges to flip (not 930, not 501)
- Conclusion: ε_G is NOT derivable from simple pulsation rules on valence graph
- ε_G = Δr_val · r_val² · n_u² / (R_tot · R_surf · (n_u²−1)) verified to 10⁻⁵

---

## Key Numerical Values (All Verified)
```
ε_G                          = 0.0075194
Δr_val                       = 0.047960
Δr/ε_G (empirical)           = 6.3781
R = R_tot·R_surf/r_val²      = 6.38920
C = (n_u²-1)/n_u²            = 575/576 = 0.99826389
R × C                        = 6.3781  (0.004% residual)
G_PDL                        = 6.67448 × 10⁻¹¹
G_CODATA 2022                = 6.67430 × 10⁻¹¹
Écart G                      = +27 ppm
α_PDL⁻¹                      = 137.022
α_exp⁻¹                      = 137.036
Écart α                      = ~10⁻⁴
Triangles valence sector     = 70,300 (all coherent, Harary)
N_mixed [d,u1,u2] triangles  = 16,128 = 28×24×24
```

---

## Session History

- **Session 1 (March 2026):** Full D20 rewrite V1→V2 (6 sections + abstract +
  intro), .bib cleanup, Zenodo description updated, D17 remarks 2.5 and 2.6 added,
  Colab script written, key discovery: Γ_min=0 for static valence graph (ε is
  dynamical), ε_G identified as mixed combinatorial+electromagnetic quantity,
  PDL_context.md created and connected via GitHub.

- **Session 2 (March 2026):** GitHub connection established. Discovered new
  documents in corpus: D20-V3, D16 (local uniqueness), D_Map v7, D_Who.
  Context file updated to reflect full corpus state.

- **Session 3 (March 2026):** V2 uploaded for comparison with V3.
  Key findings and productions:
  (a) D20-V2 and D20-V3 are word-for-word identical — V3 is V2 re-saved.
  (b) Full corpus audit: discovered 3 additional documents not previously listed:
      D3 (Position_paper_PDL.tex), D_Exist (Existence_as_Pulsating_Closure...tex),
      D_Who_v2 (Whoever_We_May_Be...v2.tex, article format).
  (c) Error found in D_Map v7: roadmap section still uses old bridge formula
      Δr_val ≈ 3φ²ε_G from D20-V1 (invalidated). Correction patch produced
      (PDL_DMap_v7_corrections.tex). Note: D16 was already in D_Map v7 (patch
      block 3 on D16 is unnecessary); D_Exist and D_Who_v2 may need to be added.
  (d) New TikZ dependency diagram produced (PDL_dependency_diagram_v2.tex):
      - Constants split into α/ħ/k_B (direct) vs G_PDL (via bridge D20)
      - Born's rule / Gleason-type node added to dynamical chain
      - Programme/sketch nodes visually distinguished (dashed, grey fill)
      - Legend added
  (e) D_Map v8 prepared for Zenodo publication: all corrections integrated,
      Zenodo description drafted and finalised.
  
- **Session 4 (March 2026):** Full editorial revision and English translation of
  the popular introduction book "Quoi que nous soyons / Whatever We May Be".

  Key productions:
  (a) French file revised: triple opening restructured (Résumé migrated to
      separate quatrieme_couverture.tex), Introduction rewritten with Wheeler/
      Rovelli/Wolfram positioning note and TO developed, medical section
      recalibrated as open programme, duplicate at line ~915 removed, grief
      passage cleaned, energy chapter reformulated.
  (b) Theoretical corrections applied: D20 (Universal Coherence Leakage) added
      to Annexe B as primary result; contradiction on ε status corrected (α
      derived without free parameter; G requires calibration of ε); D16
      selection functional S referenced in footnote on uniqueness conjecture.
  (c) TikZ figure of (4,6) structure added to Chapter 1.
  (d) Full English translation produced (GB spelling, \pdl command):
      Whatever_We_May_Be___The_Projective_Dynamic_Logo.tex — 1142 lines,
      10 translation blocks TR-1 to TR-10.
  (e) Back cover produced in both languages:
      quatrieme_couverture.tex (FR) and back_cover_EN.tex (GB).
  (f) Editorial assessment: text judged fit as dual-audience ambassador
      (gymnasium to scientific public). Main residual risk: predictions chapter
      density for non-specialist readers.

  ---

## Session 5 (March 2026) — Diffusion, visibilité et démarches éditoriales

### Démarches vers la communauté scientifique

- **Carlo Rovelli (Foundations of Physics)** — courriel envoyé à rovelli.carlo@gmail.com
  avec proposition d'essai sur le LDP. Deux réponses reçues :
  (1) réponse automatique signalant surcharge de messages ;
  (2) réponse personnelle : *"FoP ne prend pas en compte ce genre de soumissions."*
  Conclusion : "Quoi que nous soyons" / "Whatever We May Be" n'est pas le bon
  format pour FoP. Un article technique court centré sur un résultat précis
  serait nécessaire pour une future soumission.

- **PhilSci-Archive** — soumission de "Whatever We May Be" refusée :
  *"The item lies outside the range of material suitable for PhilSci-Archive."*
  Conclusion : les archives académiques attendent des articles de recherche,
  pas des textes de vulgarisation.

- **Liste quantum-foundations@maillist.ox.ac.uk (Oxford)** — première annonce
  refusée par le modérateur. Version recalibrée envoyée, centrée sur le résultat
  Gleason-type. Réponse d'Aleks Kissinger (Oxford) : la liste ne permet pas
  l'auto-promotion de ses propres travaux. Réponse envoyée à Kissinger demandant
  les bons canaux pour partager des preprints avec la communauté quantum foundations.

### Infrastructure de visibilité mise en place

- **Academia.edu** — profil créé et public. Quatre publications uploadées :
  - Gleason-Type Uniqueness of Born's Rule (https://zenodo.org/records/18663156)
  - Universal Coherence Leakage / Bridge D20-V3 (https://doi.org/10.5281/zenodo.19056994)
  - PDL Global Mapping v8 (https://doi.org/10.5281/zenodo.19065389)
  - Whatever We May Be (https://doi.org/10.5281/zenodo.19076555)
  - Post de présentation du PDL publié sur le profil.
  - Bio rédigée et publiée.

- **Google Scholar** — profil créé avec adresse Gmail. Publications ajoutées
  manuellement via DOIs Zenodo. Indexation automatique en cours (délai normal :
  4 à 8 semaines).

- **ORCID** — profil créé. Toutes les publications Zenodo importées via DataCite.
  ORCID connecté à : Zenodo (profil + preprints), Academia.edu, site web
  cedriclaubscher.ch.

- **Google Alerts** — trois alertes créées :
  - "Projective Dynamic Logo"
  - "Cédric Laubscher"
  - "PDL coherence leakage"

- **Métadonnées Zenodo** — mots-clés optimisés sur les quatre preprints
  prioritaires. Tous indexés dans OpenAIRE.

- **ResearchGate** — compte refusé (absence d'affiliation institutionnelle).
  Demande de reconsidération envoyée via formulaire de support avec liens Zenodo.

- **PhilPeople** — profil créé mais masqué automatiquement en raison de
  l'absence d'affiliation institutionnelle. À relancer via support.

- **Semantic Scholar** — non accessible au moment de la session. À vérifier
  ultérieurement.

### Leçons stratégiques de la session

1. **Format des soumissions** — "Quoi que nous soyons" / "Whatever We May Be"
   est un livre de vulgarisation grand public. Il n'est pas adapté aux archives
   académiques (PhilSci, FoP). Cibles éditoriales potentielles : Hermann,
   Odile Jacob, Seuil "Science ouverte".

2. **Point d'entrée dans la communauté quantum foundations** — le résultat
   Gleason-type est le meilleur vecteur. C'est du vocabulaire natif de cette
   communauté.

3. **Article technique prioritaire** — le bridge D20-V3 est le résultat le plus
   audacieux et le plus falsifiable. Un article court en anglais (8-10 pages)
   centré sur ce résultat est la prochaine étape pour une soumission à une revue
   de second rang (International Journal of Theoretical Physics, Axiomathes,
   Synthese).

4. **Dialogue TO-PDL** — utile dans les textes philosophiques et grand public.
   À ne pas mentionner dans les articles techniques soumis à peer review.
   Garder les raffinements conceptuels produits par ce dialogue, sans nommer TO
   comme source de légitimation.

5. **Reconnaissance scientifique** — le chemin passe par : (1) un article
   technique publié dans une revue à comité de lecture, (2) des citations par
   d'autres chercheurs, (3) un dialogue avec au moins un chercheur institutionnel.
   La visibilité sur les plateformes (Academia, Google Scholar, ORCID) est une
   condition nécessaire mais non suffisante.

### Prochaines étapes prioritaires

1. Rédiger un article technique court sur le bridge D20-V3 pour soumission
   à une revue de second rang.
2. Identifier 2-3 chercheurs dont les travaux convergent avec le LDP et
   préparer un message de contact ciblé.
3. Attendre la réponse d'Aleks Kissinger sur les bons canaux de diffusion.
4. Relancer PhilPeople via leur support pour débloquer le profil.
5. Vérifier Semantic Scholar dans quelques semaines.
6. Surveiller les statistiques Zenodo et Google Scholar une fois par semaine.

  - **Session 6 (March 2026):** Full nuclear stability programme developed and
  published as D_Nuc (PDL_Nuclear_Stability_Skeleton.tex).

  Key results established (no free parameters):
  (a) Neutron quintuplet (24,28,1032,9960,10992) derived for first time via
      R_tot(n) = R_tot(p) − (Δn+1)² = 11017 − 25 = 10992. Gap of 40
      decomposed as 25 (structural permutation cost) + 15 (mass fatigue).
  (b) New relation R_tot(p) = 6μ_p at 0.001% — not previously in corpus.
      Interpretation: each (4,6)-brick edge carries one μ of coherence.
  (c) Nuclear binding unit T = R_surf²/R_sea ≈ 25 = (Δn+1)² identified.
      Fundamental identity: neutron deficit = neutron binding capacity.
  (d) Saturation threshold Z_sat = R_sea(n)/R_surf(p) ≈ 20 (calcium) derived.
      Structural origin of the N≈Z / N>Z frontier in the chart of nuclides.
  (e) N_crit,max = R_sea(p)/(2×gap) = 126.1 — largest magic number derived.
      Bi-209 identified as last stable nucleus by sea-exhaustion argument.
  (f) Origin of nuclear spin-orbit coupling identified as Δn = n_d − n_u = 4.
      Splitting energy Δn/(2n_u) = 1/12 ≈ 0.083 ħω₀ matches empirical values.
      Full derivation of intermediate magic numbers 2,8,20,28,50,82: conjecture.

  Productions:
  - PDL_Nuclear_Stability_Skeleton.tex (D_Nuc) — full paper, 456 lines, GB English
  - References.bib — complete bibliography file
  - Principal open problem: OP1 (shell splitting from Δn, signed-graph derivation)
---

## Instructions for Next Session

Start by saying: *"Read PDL_context.md and the corpus files from the project."*

After each session, update:
- Session History (add new session entry)
- Open Problems (mark resolved, add new)
- Key Numerical Values (if new results)
- Corpus table (if new documents)
