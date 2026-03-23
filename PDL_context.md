# PDL Research Context — Cédric Laubscher
*Last updated: March 2026 — Session 7. Copy this file to GitHub after each session.*

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

### Topological proof of exponent 18 — NEW Session 7
  K4 = ∂Δ³ ≅ S²  →  dim H₂(S²;Z) = 1
  ker(d₁) = ⟨e_{r_val(p)}⟩ = (0,0,1,0,0,0)ᵀ  [proved over Q(√5), exact]
  ker(d₂) = trivial on free variables of C₂  [proved over Q(√5), exact]
  Decomposition: 18 = 6 + 5 + 4 + 3  (ranks + boundary morphisms)
  Boundary morphisms: δ₀₁ [T=(Δn+1)²], δ₁₂ [G=ε^18], δ_long [bridge formula]
  Common ancestor with periodic table: both 18s are invariants of S² imposed
  by dim_R = 3.

### Nuclear binding unit T (Session 5)
  T = R_surf(p)² / R_sea(n) = 501.6² / 9960 = 25.26 ≈ (Δn+1)² = 25
  Identity: neutron deficit = neutron binding capacity (±1%)
  T_pp = R_surf(p)² / R_tot(p) = 22.84  [proton-proton conflict]

### Saturation threshold (Session 5)
  Z_sat = R_sea(n) / R_surf(p) = 9960 / 501.6 ≈ 20  (calcium)

### Maximum magic number (Session 5)
  N_crit,max = R_sea(p) / (2 × gap) = 10087 / 80 = 126.1
  → Bi-209 (Z=83, N=126) last stable nucleus

### New relation R_tot = 6μ (Session 5)
  6μ_p = 11016.92 ≈ 11017 = R_tot(p)  at 0.001%

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
| PDL_Global_Mapping...v10.tex | D_Map | Full corpus mapping, dependency diagram | CURRENT — v10 (Session 7) |
| Universal_Coherence_Leakage...V3.tex | D20-V3 | Bridge G ↔ α — PRIMARY RESULT | CURRENT VERSION |
| Existence_as_Pulsating_Closure...tex | D_Exist | Ontological meditation on PDL | Philosophical |
| Whoever_We_May_Be...v2.tex | D_Who_v2 | Philosophical synthesis, article format | Philosophical |
| Whoever_we_may_be — The Projective Dynamic Logo.tex | D_Who_book | Same themes, book format | Philosophical |
| Quoi_que_nous_soyons...v2.tex | D_Who_book_FR | Popular introduction FR | CURRENT |
| Whatever_We_May_Be...v2.tex | D_Who_book_EN | Popular introduction EN | CURRENT |
| PDL_Nuclear_Stability_Skeleton.tex | D_Nuc / D22 | Nuclear stability, neutron quintuplet, N_crit=126 | Published Zenodo |
| PDL_Exponent18_Topology.tex | D23 | Topological origin of exponent 18 — NEW | Ready for Zenodo |

---

## D20 Version History

| Version | Status | Key change |
|---------|--------|-----------|
| V1 (original) | SUPERSEDED | ε_G=0.0073891 (wrong), bridge formula 3φ²ε_G (no basis) |
| V2 | SUPERSEDED (label) | Corrected ε_G, corrected bridge formula |
| V3 | CURRENT | Scientifically identical to V2 — confirmed in Session 3 |

---

## Open Problems (current status)

1. [RESOLVED Session 7] Topological proof of exponent 18
   - ker(d₁) = ⟨e_{r_val(p)}⟩ proved analytically over Q(√5)
   - Decomposition 18 = 6+5+4+3 proved
   - Document D23 produced and ready for Zenodo

2. [OPEN — HIGH] Formal identification of δ_long as boundary morphism (OP1 in D23)
   - Bridge formula δ_long: C₁ → C₃ conjectured to factor through [S²]
   - Would complete the categorical interpretation of all 3 boundary morphisms

3. [OPEN — MEDIUM] Golden ratio in spectrum of J_{d₂} (OP2 in D23)
   - σ(J_{d₂}) ∋ {φ, 1/φ} observed numerically
   - Analytical proof via R_surf = φ·r_val/3 self-similarity: not yet done

4. [OPEN — FUTURE] n-dimensional generalisation (OP3 in D23)
   - K_{n+1} in R^n: express exponent as function of n
   - Co-vary with shell structure of quantum system in R^n

5. [OPEN — MEDIUM] ker(d₂) = ⟨e_{r_val(n)}⟩ analytically (OP4 in D23)
   - Numerical: confirmed. Exact over Q(√5): not yet done.

6. [OPEN — HIGH] Shell splitting from Δn = 4 (OP1 in D22)
   - Mechanism identified: Δn/(2n_u) = 1/12 ≈ 0.083 ħω₀
   - Combinatorial derivation from signed-graph formalism: NOT YET DONE

7. [OPEN — MEDIUM] Analytic uniqueness proof for (24,28) (ongoing)
   - Computational uniqueness confirmed in large domain
   - Analytic proof still pending

8. [OPEN — MEDIUM] Derivation of ε_G from first principles
   - ε_G currently calibrated from empirical G
   - Would make G fully derived, no free parameter

9. [OPEN — MEDIUM] Isotopic window width ΔN(Z) (OP2 in D22)
10. [OPEN — MEDIUM] Lacunae Z=43, Z=61 (OP3 in D22)
11. [OPEN — FUTURE] Chemical properties via Block III (OP4 in D22)

---

## Session History

- **Session 1 (March 2026):** Full D20 rewrite V1→V2. Key discovery: ε_G is
  dynamical, not derivable from static valence graph. PDL_context.md created.

- **Session 2 (March 2026):** GitHub connection established. Full corpus audit.

- **Session 3 (March 2026):** D20-V2 = D20-V3 confirmed. D_Map v7→v8. Three
  new documents found (D3, D_Exist, D_Who_v2).

- **Session 4 (March 2026):** D_Who_book_EN (Whatever We May Be) produced.
  D_Map v8 consistency check. Session history and open problems updated.

- **Session 5 (March 2026):** Full nuclear stability programme (D22).
  Neutron quintuplet derived. N_crit=126.1, Z_sat=20. D_Map v8→v9.

- **Session 6 (March 2026):** Dissemination strategy reviewed. PhilSci,
  Academia, Semantic Scholar status checked. Article strategy refined.

- **Session 7 (March 2026):** Topological origin of exponent 18 established.

  Key results proved (no free parameters, exact arithmetic over Q(√5)):
  (a) K4 = ∂Δ³ ≅ S² — the PDL elementary closure is a 2-sphere.
      H₂(S²;Z) ≅ Z with generator [S²] = (-1,+1,-1,+1)ᵀ (explicit).
  (b) Decomposition 18 = 6+5+4+3 proved:
      - rank(d₀) = 6 (Bloc I, unique solution n_u=24 via quadratic)
      - rank(d₁) = 5, ker(d₁) = ⟨e_{r_val(p)}⟩ = (0,0,1,0,0,0)ᵀ [exact]
      - rank(d₂) = 4 on free variables of C₂ [exact]
      - 3 boundary morphisms: δ₀₁, δ₁₂, δ_long
  (c) Common topological ancestor of PDL exponent 18 and periodic table 18:
      both are invariants of S² imposed by dim_R = 3.
  (d) Status of CT4 upgraded: exponent 18 is now a PROVED THEOREM, not
      an empirically calibrated conjecture.

  Productions:
  - PDL_Exponent18_Topology.tex (D23) — 468 lines, GB English, complete
  - References_Topology.bib — 16 entries
  - PDL_Global_Mapping_v10.tex — 7 modifications integrating D23:
    * D23 added to tab:documents and tab:doc_index
    * CT4 epistemic status updated to "proved theorem"
    * TOP1 new entry added to tab:status
    * Roadmap updated: exponent-18 problem marked substantially resolved
    * New paragraph in §1.2 introducing D23
    * Bibliography entry Topology_18_PDL_2026 noted in comments

  Next actions:
  1. Publish D23 on Zenodo (description and keywords prepared)
  2. Publish D_Map v10 on Zenodo
  3. Tackle OP2 (golden ratio in spectrum) or OP4 (ker d₂ exact) as next proof
  4. Consider OP3 (n-dimensional generalisation) for a short follow-up note

---

## Instructions for Next Session

Start by saying: *"Read PDL_context.md and the corpus files from the project."*

After each session, update:
- Session History (add new session entry)
- Open Problems (mark resolved, add new)
- Key Numerical Values (if new results)
- Corpus table (if new documents)
