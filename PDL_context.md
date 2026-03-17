# PDL Research Context — Cédric Laubscher
*Last updated: March 2026 — Session 3. Copy this file to GitHub after each session.*

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

5. [MEDIUM] Series conjecture for bridge formula
   - Δr_val/ε_G = R · n_u²/(n_u²+1) = 6.3781 (residual < 0.001%)
   - Would be next-order correction to C = (n_u²-1)/n_u²
   - Not yet derived

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

---

## Instructions for Next Session

Start by saying: *"Read PDL_context.md and the corpus files from the project."*

After each session, update:
- Session History (add new session entry)
- Open Problems (mark resolved, add new)
- Key Numerical Values (if new results)
- Corpus table (if new documents)
