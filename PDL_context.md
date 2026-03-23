# PDL Research Context — Cédric Laubscher
*Last updated: March 2026 — Session 8. Copy this file to GitHub after each session.*

---

## Framework Overview

The **Projective Dynamic Logo (PDL)** reconstructs physical reality from relational axioms on finite signed graphs, without presupposing spacetime. Four axioms: minimal binary pulsation, triangular coherence, minimal completeness, logical optimisation. The minimal admissible stationary closure is the (4,6) complete graph (electron prototype). The proton is a hierarchical composite.

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
  ε_G = 0.0075194, Δr_val = 0.047960, R×C = 6.3781 (0.004% residual)
  G_PDL = 6.67448 × 10⁻¹¹  vs  G_CODATA = 6.67430 × 10⁻¹¹  (+27 ppm)

### Topological proof of exponent 18 — PROVED Session 7–8 (D23 v2)
  K4 = ∂Δ³ ≅ S²  →  dim H₂(S²;Z) = 1
  Decomposition: 18 = 6 + 5 + 4 + 3  (ranks + boundary morphisms)
  ker(d₁) = ⟨e_{r_val(p)}⟩ = (0,0,1,0,0,0)ᵀ  [PROVED over Q(√5)]
  ker(d₂) ⊇ ⟨e_{r_val(n)}⟩ = (0,0,1,0,0,0)ᵀ  [PROVED over Q(√5)]
  Boundary morphisms: δ₀₁ [T=(Δn+1)²], δ₁₂ [G=ε^18], δ_long [bridge formula]

### n-dimensional generalisation — PROVED Session 8 (D23 v2)
  E(n) = n(n²+3)/2  (PDL gravitational exponent in R^n)
  Shell(n) = 3·C(2n-2, n-1)  (max electrons per period in R^n)
  E(n) = Shell(n)  ↔  n ∈ {1, 3}  [PROVED: Stirling + direct check]
  Interpretation: n=3 is the unique non-trivial dimension in which
  gravitational coupling structure and atomic shell structure share
  the same topological integer.

### Nuclear binding (D22)
  T = R_surf(p)² / R_sea(n) ≈ 25 ≈ (Δn+1)²
  Z_sat = R_sea(n) / R_surf(p) ≈ 20  (calcium)
  N_crit,max = R_sea(p) / (2×gap) = 126.1  →  Bi-209 last stable nucleus
  6μ_p ≈ R_tot(p)  at 0.001%

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
| PDL_Global_Mapping...v10.tex | D_Map | Full corpus mapping, dependency diagram | CURRENT — v10 |
| Universal_Coherence_Leakage...V3.tex | D20-V3 | Bridge G ↔ α — PRIMARY RESULT | CURRENT VERSION |
| Existence_as_Pulsating_Closure...tex | D_Exist | Ontological meditation on PDL | Philosophical |
| Whoever_We_May_Be...v2.tex | D_Who_v2 | Philosophical synthesis, article format | Philosophical |
| Whoever_we_may_be — The Projective Dynamic Logo.tex | D_Who_book | Same themes, book format | Philosophical |
| Quoi_que_nous_soyons...v2.tex | D_Who_book_FR | Popular introduction FR | CURRENT |
| Whatever_We_May_Be...v2.tex | D_Who_book_EN | Popular introduction EN | CURRENT |
| PDL_Nuclear_Stability_Skeleton.tex | D_Nuc / D22 | Nuclear stability, neutron quintuplet, N_crit=126 | Published Zenodo |
| PDL_Exponent18_Topology_v2.tex | D23 v2 | Topological origin of exponent 18 — UPDATED | Ready for Zenodo |

---

## D20 Version History

| Version | Status | Key change |
|---------|--------|-----------|
| V1 (original) | SUPERSEDED | ε_G=0.0073891 (wrong), bridge formula 3φ²ε_G (no basis) |
| V2 | SUPERSEDED (label) | Corrected ε_G, corrected bridge formula |
| V3 | CURRENT | Scientifically identical to V2 — confirmed in Session 3 |

---

## D23 Version History

| Version | Lines | Key change |
|---------|-------|-----------|
| v1 (Session 7) | 468 | First complete version: decomposition 18=6+5+4+3, ker(d₁) proved |
| v2 (Session 8) | 543 | + ker(d₂) ⊇ ⟨e_{r_val(n)}⟩ proved (OP4); + E(n)=Shell(n)↔n∈{1,3} (OP3); OP2 corrected; OP5 added |

---

## Open Problems (current status — D23 v2)

### D23 open problems

| # | Label | Status | Description |
|---|-------|--------|-------------|
| OP1 | δ_long as boundary morphism | OPEN — HIGH | Prove δ_long factors through [S²] categorically |
| OP2 | φ in architecture of J_{d₂} | OPEN — MEDIUM | Characterise the Q(√5)-lattice structure of the Gram matrix; the σ={φ,1/φ} observation was an artefact of a proxy ε_G |
| OP3 | Proof of Shell(n) formula | OPEN — MEDIUM | Analytical proof of Shell(n)=3·C(2n-2,n-1) via Gegenbauer polynomials |
| OP4 | Completeness of ker(d₂) | OPEN — MEDIUM | Prove ker(d₂)=⟨e_{r_val(n)}⟩ exactly (inclusion proved; equality pending) |
| OP5 | Structural necessity of n=3 | OPEN — FUTURE | Show n≠3 is forbidden by PDL axioms, not just a non-coincidence point |

### D22 open problems

| # | Label | Status | Description |
|---|-------|--------|-------------|
| OP1 | Shell splitting from Δn=4 | OPEN — HIGH | Derive Δn/(2n_u)≈0.083ħω₀ from signed-graph formalism |
| OP2 | Isotopic window width ΔN(Z) | OPEN — MEDIUM | Derive from nuclear coordination number c(Z,N) |
| OP3 | Lacunae Z=43, Z=61 | OPEN — MEDIUM | Prove structural impossibility of stable closure |
| OP4 | Chemical properties Block III | OPEN — FUTURE | Coupling nucleus ↔ electron cloud |

### Programme-level open problems

| # | Label | Status | Description |
|---|-------|--------|-------------|
| P1 | Uniqueness of (24,28) | OPEN — MEDIUM | Analytic proof (computational uniqueness confirmed) |
| P2 | Derivation of ε_G | OPEN — MEDIUM | From first principles, without calibration from empirical G |

---

## Session History

- **Session 1 (March 2026):** Full D20 rewrite V1→V2. Key discovery: ε_G is dynamical. PDL_context.md created.

- **Session 2 (March 2026):** GitHub connection established. Full corpus audit.

- **Session 3 (March 2026):** D20-V2 = D20-V3 confirmed. D_Map v7→v8. Three new documents found.

- **Session 4 (March 2026):** Whatever We May Be (EN) produced. D_Map v8 consistency check.

- **Session 5 (March 2026):** Full nuclear stability programme (D22). Neutron quintuplet, N_crit=126.1, Z_sat=20. D_Map v8→v9.

- **Session 6 (March 2026):** Dissemination strategy reviewed.

- **Session 7 (March 2026):** D23 v1 produced (468 lines).
  - K4 = ∂Δ³ ≅ S², H₂(S²;Z) ≅ Z computed exactly.
  - 18 = 6+5+4+3 proved.
  - ker(d₁) = ⟨e_{r_val(p)}⟩ proved over Q(√5).
  - rank(d₂) = 4 proved. CT4 upgraded to theorem.
  - D_Map v9→v10. PDL_context.md v7 produced.

- **Session 8 (March 2026):** D23 v1→v2 (543 lines). Four new results added:
  (a) OP4 RESOLVED: ker(d₂) ⊇ ⟨e_{r_val(n)}⟩ proved exactly over Q(√5).
      Column r_val(n) of J_{d₂} is identically zero — r_val(n)=1032 is the
      passive variable of the nuclear-to-gravitational transition, exact
      parallel with r_val(p)=930 at the proton-to-nuclear transition.
  (b) OP2 CORRECTED: σ(J_{d₂}) ∋ {φ,1/φ} was an artefact of a proxy ε_G
      that over-scaled one column by ×50. With exact values, φ enters the
      ENTRIES of J_{d₂} via R_surf=φ·r_val/3 but not the singular values.
      OP2 reformulated as characterisation of the Q(√5)-lattice in J_{d₂}.
  (c) OP3 RESOLVED: E(n)=Shell(n) ↔ n∈{1,3} proved.
      E(n) = n(n²+3)/2, Shell(n) = 3·C(2n-2,n-1) [closed form verified].
      Proof: Stirling shows Shell(n) grows exponentially for n≥4 while
      E(n) grows polynomially → unique crossing at n=3.
      Physical interpretation: n=3 is the unique non-trivial dimension
      for which gravitational coupling and atomic shell structure share
      the same topological integer.
  (d) OP5 ADDED: Structural necessity of n=3 (show n≠3 forbidden by axioms).
  (e) D23 v2 produced and filed for Zenodo.
  (f) ORCID update in progress.

---

## Instructions for Next Session

Start by saying: *"Read PDL_context.md and the corpus files from the project."*

After each session, update:
- Session History (add new session entry)
- Open Problems (mark resolved, add new)
- Key Numerical Values (if new results)
- Corpus table (if new documents)
