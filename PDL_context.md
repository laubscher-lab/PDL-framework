# PDL Research Context — Cédric Laubscher
*Last updated: March 2026. Read this file at the start of each session.*

---

## Framework Overview

The **Projective Dynamic Logo (PDL)** reconstructs physical reality from relational axioms on finite signed graphs, without presupposing spacetime. Four axioms: minimal binary pulsation, triangular coherence, minimal completeness, logical optimisation. The minimal admissible stationary closure is the (4,6) complete graph (electron prototype). The proton is a hierarchical composite.

---

## Core Integer Architecture (Proton)

| Symbol | Value | Meaning |
|--------|-------|---------|
| n_u | 24 | Up-quark multiplicity |
| n_d | 28 | Down-quark multiplicity |
| r_u | 276 | Internal relations per u-core |
| r_d | 378 | Internal relations for d-core |
| r_val | 930 | Total valence relations |
| R_sea | 10087 | Dynamical sea relations |
| R_tot | 11017 | Total internal relations |
| R_surf | φ × 310 ≈ 501.6 | Active surface (golden ratio) |

---

## Key Derived Results

### Fine-structure constant
α_PDL = μ / R_surf² = μ / (φ² · (r_val/3)²),  α_PDL⁻¹ ≈ 137.02
Agreement with experiment to 10⁻⁴, no free parameters.

### Gravitational bridge formula (D20-V2 — CORRECTED)
Δr_val = ε_G · (R_tot · R_surf / r_val²) · (n_u² - 1) / n_u²

where:
- ε_G = (G·m_p²/ħc)^(1/18) = 0.0075194
- Δr_val = (3/φ)·sqrt(μ/α_exp) − 930 = 0.047960
- Correction factor: (n_u²−1)/n_u² = 575/576 (no-self-loop on up-core)
- Ratio: Δr_val/ε_G = 6.3781
- Structural value R×C = 6.38920 × 0.99826 = 6.3781

### G prediction
G_PDL = 6.67448 × 10⁻¹¹ m³kg⁻¹s⁻²
vs CODATA 2022: 6.67430 × 10⁻¹¹, écart +27 ppm, within experimental uncertainty.

---

## Corpus Status (Documents)

| Doc | Content | Status |
|-----|---------|--------|
| PDL.tex (D1) | Main framework, axioms, proton, α, G, k_B | Reference |
| Combinatorial_Proton_Architecture_PDL_v2.tex | Uniqueness conjecture for (24,28,930,10087,11017) | Solid |
| Emergence_of_the_Golden_Ratio.tex (D18) | Derives φ from self-similarity condition | Sketch — φ not yet derived from axioms |
| Relational_Emergence_of_Born_s_Rule_v2.tex | Born's rule + φ conjecture | Propositional |
| Coherence_Leakage_Exponent_18.tex (D17) | 18 filters structured 6+6+6 | Needs remark on dynamic origin of ε |
| A_Topological_Reformulation.tex | ε as intrinsic probability, topology of coexistence | Conceptual |
| Coherence_Effective_Fields_PDL.tex | Gauss/Faraday discrete, Schrödinger emergence | Programme |
| Schodinger_PDL_v2.tex | Hydrogen compatibility with α_PDL | Consistent |
| Toward_a_Gleason-Type.tex | Born's rule uniqueness for spin-1/2 | Theorem established |
| Towards_Einstein-Dirac_Unification.tex | Dirac+Einstein on PDL substrate | Exploratory |
| Universal_Coherence_Leakage_V2.tex (D20-V2) | Bridge G ↔ α, corrected | PRIMARY RESULT |

---

## D17 Pending Modification

Insert the following remark at the end of Section 2.2, after the existing Remark
("The interpretation of ε is scale-dependent"), before the paragraph
"In the subsequent sections...":

KEY RESULT from computational session March 2026:
The static valence graph admits Γ_min = 0 (Harary balanced assignment with
A={u1,u2}, B={d}, covering all 70,300 triangles of the valence sector).
Therefore ε > 0 must come from pulsation dynamics (transient violations during
update rule F), topological frustration (incompatible surface constraints from
simultaneous coupling to multiple (4,6) blocks), or charge constraint (net
charge +1 may forbid all balanced 2-colourings).

Central conjecture (eq. to add):
  ε = inf_{G ∈ G_p} Γ_cycle(G) = ε_G = (G_N m_p²/ħc)^(1/18) = 0.0075194

where Γ_cycle(G) = (1/2)(Γ(G) + Γ(F(G))) averages violations over a full cycle.

Proof requires: (i) explicit pulsation rule F; (ii) computation of Γ_cycle
for canonical architecture; (iii) verification that minimum equals 0.0075194.

Full LaTeX text for this remark produced in session transcript March 2026.

---

## Open Problems (Priority Order)

1. [CRITICAL] Derive ε_G from pulsation rule
   Specify update rule F for the proton (probably in D1 or D12 full version).
   Compute Γ_cycle. Verify it equals 0.0075194.
   This would connect D17 (combinatorial ε) to D20-V2 (gravitational ε_G).

2. [HIGH] Analytical derivation of the exponent 18
   D17 lists 18 filters named and organized in 3 groups of 6.
   Their mutual independence is NOT proven.
   Minimum: show no subset of 17 filters suffices.

3. [HIGH] Derivation of φ from axioms
   D18 derives φ from a self-similarity condition:
     R_core/R_tot' = R_surf/R_core  →  λ² = λ+1  →  φ
   But this condition itself is NOT derived from Ω.
   Remaining step: show Ω implies self-similarity for all admissible composites.
   D_Born (Relational_Emergence_v2) formulates this as a precise conjecture.

4. [MEDIUM] Analytic uniqueness proof for (24,28)
   Computational search confirms uniqueness in domain n_u,n_d ≤ 56, 233 solutions
   all with identical (n_u,n_d,r_val). Analytic proof pending.

5. [MEDIUM] Series conjecture for bridge formula
   Δr_val/ε_G = R · n_u²/(n_u²+1) = 6.3781 (residual < 0.001%).
   This would be the next-order correction. Not yet derived.

---

## Errors Corrected in D20-V2 (vs D20 original)

| Quantity | Original (wrong) | Corrected |
|----------|-----------------|-----------|
| ε_G | 0.0073891 | 0.0075194 |
| Δr_val | 0.049751 | 0.047960 |
| Bridge formula | 3φ²·ε_G (no structural basis) | ε_G · R · C (derived) |
| G_implied (original) | 4.87 × 10⁻¹¹ (27% off CODATA) | eliminated |

---

## Session History

- March 2026: Full D20 rewrite (6 sections + abstract + intro), .bib cleanup,
  Zenodo description updated, computational proof that Γ_min = 0 for static
  valence graph (key discovery: ε is dynamical not static), D17 remark drafted,
  PDL_context.md created.

---

## Key Numerical Values (All Verified)

ε_G                         = 0.0075194
Δr_val                      = 0.047960
Δr/ε_G (empirical)          = 6.3781
R = R_tot·R_surf/r_val²     = 6.38920
C = (n_u²-1)/n_u²           = 575/576 = 0.99826389
R × C                       = 6.3781 (0.004% residual)
G_PDL                       = 6.67448 × 10⁻¹¹
G_CODATA 2022               = 6.67430 × 10⁻¹¹
Écart G                     = +27 ppm
α_PDL⁻¹                     = 137.022
α_exp⁻¹                     = 137.036
Écart α                     = ~10⁻⁴
Triangles valence sector    = 70,300 (all coherent under Harary assignment)

---

## How to Use This File

At the start of each session, say:
"Please read PDL_context.md from my Google Drive (or upload it)
before we begin."

After each session, update:
- The "Session History" section
- Any resolved open problems
- Any new numerical results
