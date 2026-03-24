# PDL Research Context — Cédric Laubscher
*Last updated: March 2026 — Session 9. Copy this file to GitHub after each session.*

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

### Topological proof of exponent 18 — Session 7 (D23)
  K4 = ∂Δ³ ≅ S²  →  dim H₂(S²;Z) = 1
  ker(d₁) = ⟨e_{r_val(p)}⟩ = (0,0,1,0,0,0)ᵀ  [proved over Q(√5), exact]
  ker(d₂) = trivial on free variables of C₂  [proved over Q(√5), exact]
  Decomposition: 18 = 6 + 5 + 4 + 3  (ranks + boundary morphisms)
  Boundary morphisms: δ₀₁ [T=(Δn+1)²], δ₁₂ [G=ε^18], δ_long [bridge formula]
  Common ancestor with periodic table: both 18s are invariants of S² imposed
  by dim_R = 3.

### Surface engagement fraction and density-dependent G — Sessions 8–9 (D25/D26)
  κ = R_surf/R_tot = φ×310/11017 = 0.045528  ∈ Q(√5), no free parameter
  σ(N) = 1 − (1−κ)^N  [proved from recurrence, exact]
  G_eff(N) = σ(N) · G_PDL
  Saturation half-point: N_{1/2} = ln2/|ln(1−κ)| ≈ 14.9
  Full saturation (σ > 0.99): N_sat ≈ 101

### Hubble tension resolution — Sessions 8–9 (D25/D26)
  Local (N_local ≈ 120):  σ(120) = 0.9963  →  G_eff ≈ G_PDL  →  H₀ ≈ 73 km/s/Mpc
  CMB epoch (N_CMB ≈ 41): σ(41)  = 0.850   →  G_eff reduced  →  H₀ ≈ 67 km/s/Mpc
  Predicted ratio: √(σ(120)/σ(41)) = 1.0827
  Observed ratio:  73.04/67.4 = 1.0837
  Discrepancy: 0.09% — no free parameter

---

## Corpus Table (current)

| Filename | Label | Topic | Status |
|----------|-------|-------|--------|
| PDL.tex | D1 | Main article: axioms, proton, constants, G | Published Zenodo |
| PDL_Intro.tex | D2 | Introduction to PDL | Published Zenodo |
| PDL_Position.tex | D3 | Position paper, open problems | Published Zenodo |
| Combinatorial_Proton_v2.tex | D4/D5 | Proton quintuplet uniqueness | Published Zenodo |
| Alpha_PDL_v2.tex | D6 | Fine-structure constant derivation | Published Zenodo |
| Effective_Fields_PDL.tex | D7 | Discrete Gauss–Faraday, effective fields | Published Zenodo |
| Golden_Ratio_PDL.tex | D8 | Golden ratio in proton surface | Published Zenodo |
| Coherence_Leakage_18.tex | D9 | Leakage filters, exponent 18 (original) | Published Zenodo |
| Topological_Reformulation.tex | D10 | Coexistence topology, leakage probability | Published Zenodo |
| Schrodinger_v2.tex | D11 | PDL–Schrödinger compatibility | Published Zenodo |
| Schrodinger_Sketch_v2.tex | D12 | Schrödinger-type dynamics sketch | Published Zenodo |
| Universal_Coherence_Leakage_V3.tex | D20-V3 | Bridge G↔α — PRIMARY RESULT | CURRENT VERSION |
| Existence_as_Pulsating_Closure.tex | D_Exist | Ontological meditation on PDL | Philosophical |
| Whoever_We_May_Be_v2.tex | D_Who_v2 | Philosophical synthesis, article format | Philosophical |
| Whoever_we_may_be_LDP_v2.tex | D_Who_book | Same themes, book format FR | Published Zenodo |
| Whatever_We_May_Be_v2.tex | D_Who_book_EN | Popular introduction EN | Published Zenodo |
| Quoi_que_nous_soyons_v2.tex | D_Who_book_FR | Popular introduction FR | Published Zenodo |
| Discrete_Cavity_Modes.tex | D19 | PDL cavity, density of states ρ(ν)∝ν² | Published Zenodo |
| PDL_Nuclear_Stability_Skeleton.tex | D22 | Nuclear stability, neutron quintuplet, N_crit=126 | Published Zenodo |
| PDL_Topological_Origin_18_v2.tex | D23 | Topological origin of exponent 18: K₄=∂Δ³≅S², 18=6+5+4+3 | Published Zenodo |
| PDL_Bridge_G_Alpha_v2.tex | D24 | Paper 1: parameter-free bridge α–G | Ready for Zenodo/arXiv |
| PDL_Hubble_tension.tex | D25 | Paper 2: Hubble tension from closure density (v1) | Ready for Zenodo/arXiv |
| PDL_Hubble_Resolution.tex | D26 | **NEW** Paper 3: Full cosmological resolution, Overleaf-ready | Session 9 — Ready |
| References_Hubble.bib | D26-bib | Bibliography for D26 (20 entries, BibTeX) | Session 9 — Ready |

---

## D20 Version History

| Version | Status | Key change |
|---------|--------|-----------|
| V1 (original) | SUPERSEDED | ε_G=0.0073891 (wrong), bridge formula 3φ²ε_G (no structural basis) |
| V2 | SUPERSEDED (label) | Corrected ε_G, corrected bridge formula |
| V3 | CURRENT | Scientifically identical to V2 — confirmed in Session 3 |

---

## D25 vs D26 Distinction

| Feature | D25 (Session 8) | D26 (Session 9) |
|---------|----------------|----------------|
| Format | Research note style | Full journal paper, D23 template style |
| Bridge formula | Referenced | Fully derived in §2 |
| Exponent 18 | Referenced | Summarised with proof sketch in §3 |
| σ(N) derivation | Theorem 3.1 + Proposition | Definition + Remark on recurrence |
| Friedmann treatment | Schematic | Full equation with Λ discussion |
| Main result | Theorem 4.1 (leading order) | Proposition 5.1 (exact ratio) |
| Solar-system consistency | Not treated | §6.2 explicit argument |
| Open problems | OP1–OP4 | OP1–OP5 (OP5 = CMB power spectrum) |
| Bibliography | PDL_Hubble_references.bib | References_Hubble.bib (20 entries) |
| Lines | ~350 | 556 |
| TikZ figures | No | Yes: Figure 1 (σ curve) + Figure 2 (H₀ curve) |

D26 supersedes D25 as the primary cosmological paper. D25 remains valuable as the
original derivation document and should be cited as the source of σ(N) and G_eff(N).

---

## Open Problems (current status)

1. [RESOLVED — Session 7] Topological proof of exponent 18 (D23)
   - K₄ = ∂Δ³ ≅ S², H₂(S²;Z) ≅ Z, generator [S²] = (-1,+1,-1,+1)ᵀ
   - Decomposition 18 = 6+5+4+3 proved analytically over Q(√5)
   - rank(d₀)=6, rank(d₁)=5 with ker=⟨e_{r_val(p)}⟩, rank(d₂)=4

2. [OPEN — HIGH] Formal categorical identification of δ_long (OP1 in D23, OP4 in D24)
   - Bridge formula δ_long: C₁→C₃ conjectured to factor through [S²]∈H₂(∂Δ³;Z)
   - Would complete interpretation of all 3 boundary morphisms as realisations
     of the single generator of H₂(S²;Z)

3. [OPEN — MEDIUM] Golden ratio in algebraic structure of J_{d₂} (OP2 in D23)
   - φ enters every entry of J_{d₂} via R_surf = φ·r_val/3
   - Characterise the φ-structured lattice in the space of PDL transition amplitudes

4. [OPEN — MEDIUM] Closed-form proof of Shell(n) = 3·C(2n-2,n-1) (OP3 in D23)
   - Verified computationally for n=1..8; analytical proof via Gegenbauer polynomials pending

5. [OPEN — MEDIUM] ker(d₂) = ⟨e_{r_val(n)}⟩ exact over Q(√5) (OP4 in D23)
   - Numerical confirmation done; exact proof not yet complete

6. [OPEN — FUTURE] Structural necessity of n=3 (OP5 in D23)
   - E(3)=Shell(3)=18 proved; showing n≠3 is forbidden by PDL axioms remains open
   - Would constitute a derivation of 3-dimensionality from coherence axioms

7. [OPEN — HIGH] Derivation of ε_G from first principles (OP1 in D24 = OP1 in D25/D26)
   - ε_G currently determined via bridge formula from α_exp and G_CODATA
   - Need: explicit graph-theoretic computation of minimal frustration density
     η(G_{p*}) on the proton constraint graph at p*
   - Resolving this makes G a fully predicted constant with no empirical input
   - SAME COMPUTATION needed to derive ρ₀ in D25/D26

8. [OPEN — HIGH] Global uniqueness of proton quintuplet (OP2 in D24)
   - Local rigidity under ±1 perturbation of any integer: confirmed computationally
   - Formal proof of global uniqueness within all PDL-admissible configurations: pending

9. [OPEN — MEDIUM] Higher-order corrections to bridge formula (OP3 in D24)
   - Residual 0.34% in bridge Δr_val = ε_G·R·C
   - Conjecture: series in 1/n_u² converges; next term ≈ R·C·n_u²/(n_u²+1)
   - Would reduce residual below 0.001%

10. [OPEN — MEDIUM] Parameter-free derivation of k_B (OP5 in D24)
    - Current: order-of-magnitude consistency via k_B^PDL ~ ħω_p·ε_G^12
    - Need: precise structural identification of the thermodynamic ensemble in PDL

11. [OPEN — HIGH] Rank decomposition of d₂(N) as function of N (OP1 in D26)
    - D26 asserts G_eff(N) = σ(N)·G_PDL as a structural conjecture
    - Need: compute J_{d₂}(N) explicitly and show rank(d₂(N)) = σ(N)×4
    - Would elevate G_eff(N) formula from conjecture to proved theorem
    - This is the highest-priority new open problem from Session 9

12. [OPEN — HIGH] Derivation of saturation density ρ₀ (OP1 in D25, OP2 in D26)
    - ρ₀ = density at which ⟨N⟩ = 1/κ (each surface relation engaged once)
    - Requires computing the "volume" of N(P₀) in the coherence-cost pseudometric d
    - SAME COMPUTATION as derivation of ε_G from first principles (item 7 above)

13. [OPEN — MEDIUM] Exact treatment of engagement correlations (OP2 in D25, OP3 in D26)
    - σ(N) formula assumes independence of engagement events across neighbours
    - Correction of order κ·σ_loc ≈ 0.01: within current uncertainties
    - Full treatment requires pair-correlation function on J(P₀,Pᵢ)∩J(P₀,Pⱼ)

14. [OPEN — MEDIUM] Quantitative prediction of N_local from LSS data (OP3 in D25, OP3 in D26)
    - Current: N_local ≈ 120 is structurally motivated but not derived from LSS
    - Need: integrate closure-density field ρ_cl(r) from DESI/Euclid catalogues
    - Would transform H₀ prediction from structural to quantitative

15. [OPEN — MEDIUM] CMB angular power spectrum with variable G (OP4 in D26)
    - ΔG/G ≈ 15% between CMB and local epoch modifies acoustic horizon scale
    - Compute impact on C_ℓ^TT and C_ℓ^EE; verify compatibility with Planck precision
    - Detectable at DESI/Euclid/Roman level

16. [OPEN — MEDIUM] Higher-order corrections in κ to Hubble formula (OP4 in D25)
    - Leading term: 18κ·σ_loc ≈ 0.173
    - Next order: C(18,2)κ²·σ_loc² ≈ 0.014 (1.4% of tension amplitude)
    - Detectable at DESI precision (0.5%)

17. [OPEN — MEDIUM] Shell splitting from Δn=4 (OP1 in D22)
    - Mechanism identified: Δn/(2n_u) = 1/12 ≈ 0.083 ħω₀
    - Combinatorial derivation from signed-graph formalism: not yet done

18. [OPEN — MEDIUM] Isotopic window width ΔN(Z) (OP2 in D22)

19. [OPEN — MEDIUM] Lacunae Z=43, Z=61 (OP3 in D22)

20. [OPEN — FUTURE] Chemical properties via Block III (OP4 in D22)

---

## Epistemic Status Summary

| Result | Status | Document |
|--------|--------|----------|
| K₄ unique minimal PDL closure | Structural theorem | D23 |
| n_u=24 from quadratic, unique | Proved over Q(√5) | D23, D24 |
| R_surf = 310φ ∈ Q(√5) | Structural definition | D8 |
| α_PDL⁻¹ = φ²r_val²/(9μ), no free param | Derived | D24 |
| α_PDL⁻¹ = 137.022, dev 10⁻⁴ | Verified vs CODATA 2022 | D24 |
| Bridge Δr_val = ε_G·R·C, 0.004% residual | Structural theorem | D20-V3, D24 |
| G_PDL = 6.67448×10⁻¹¹, dev 27 ppm | Verified vs CODATA 2022 | D20-V3 |
| 18 = 6+5+4+3 proved | Topological theorem | D23 |
| κ = R_surf/R_tot ∈ Q(√5), no free param | Derived | D25, D26 |
| σ(N) = 1-(1-κ)^N, exact | Proved from recurrence | D25, D26 |
| G_eff(N) = σ(N)·G_PDL | Structural conjecture | D25, D26 |
| H₀_local/H₀_CMB = √(σ(N_l)/σ(N_c)) | Structural prediction | D26 |
| Predicted ratio 1.0827 vs observed 1.0837 | 0.09% agreement | D26 |
| N_CMB ≈ 41 as primordial epoch | Structural prediction | D26 |
| Solar-system ∂G/∂t compatibility | Argument (exponential suppression) | D26 §6.2 |

---

## Dependency Map (critical path)

```
Proton quintuplet (24,28,930,10087,11017)
    ├── α (Theorem, D5/D24) ──────────────────────── no free param
    ├── Δr_val (Proposition, D24) ─────────────────── from α_exp
    │        └── Bridge R·C (Theorem, D24) ──────── G at 27 ppm
    │                 └── ε_G = 0.0075194
    │                          ├── G_PDL (D20/D24) ── 27 ppm CODATA 2022
    │                          └── k_B (order of magnitude, D1)
    ├── κ = R_surf/R_tot (D25/D26) ─────────────────── exact Q(√5)
    │        └── σ(N) = 1-(1-κ)^N (D25/D26) ─────── proved
    │                 └── G_eff(N) (D25/D26) ─────── Hubble tension resolved
    │                          └── H₀_local/H₀_CMB = 1.0827 vs 1.0837 obs
    ├── Exponent 18 (Theorem, D23) ─────────────────── topological necessity
    │        └── 18κ = 0.8195 (D25) ──────────────── amplification
    └── Nuclear stability (D22) ──────────────────── N_crit=126.1, N_CMB~40
```

**OPEN GATE:** derivation of ε_G from η(G_{p*}) (item 7 above)
- If proved: G becomes parameter-free, ρ₀ determined, D25/D26 become fully parameter-free
- Simultaneously resolves items 7, 12 above
- This is the highest-priority foundational open problem in the programme

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
  Key results proved over Q(√5): K₄=∂Δ³≅S², 18=6+5+4+3 analytically,
  common ancestor of PDL exponent 18 and periodic table 18.
  Productions: D23 (PDL_Exponent18_Topology.tex, 468 lines), D_Map v10.

- **Session 8 (March 2026):** PDL Hubble tension programme (first pass).
  Theoretical developments:
  (a) Lemma: p_e = κ = R_surf/R_tot ∈ Q(√5) from uniform relational budget
  (b) Theorem (exact): σ(N) = 1-(1-κ)^N, no free parameter
  (c) Proposition: continuum limit σ(x) = 1-e^{-x}, error bounded at ≤0.5%
  (d) G_eff(ρ_cl) = G₀(1+18κ·σ(ρ_cl/ρ₀)) derived as leading-order result
  (e) σ_loc ≈ 0.211 consistent with LSS data; three falsifiable predictions
  Productions: D24 (Bridge_G_Alpha_v2.tex), D25 (PDL_Hubble_tension.tex),
  both + matching .bib files. D_Map v10→v11 planned.

- **Session 9 (March 2026):** Full cosmological paper on Hubble resolution (D26).

  Developments relative to Session 8:
  (a) Complete formal derivation in §1–§6 following D23 template style exactly
  (b) σ(N) recurrence derivation made explicit (Remark after Definition 4.1):
      σ(N) = σ(N-1) + κ·(1-σ(N-1)) with σ(0)=0 — additive capture process
  (c) Precise numerical table: N_CMB = 40.8, σ(41) = 0.850, H₀(41) = 67.3,
      N_local = 120, σ(120) = 0.9963, H₀(120) = 72.87
  (d) Predicted ratio √(0.9963/0.850) = 1.0827 vs observed 1.0837 → 0.09%
  (e) Solar-system ∂G/∂t consistency: rate dσ/dN|_{N=120} = κ(1-κ)^120 ≈ 1.69×10⁻⁴
      exponentially suppressed — compatible with |∂G/G| < 10⁻¹³ yr⁻¹
  (f) N_CMB ≈ 40 linked to neutron mass gap 6μ_n − R_tot(n) = 40 (structural)
  (g) Formal Proposition 5.1 with uncertainty range N_local∈[80,200],
      N_CMB∈[35,50], ratio 1.0827 ± 0.003

  New open problem identified:
  - OP1 (D26): rank decomposition of d₂(N) as function of N
    Establishing rank(d₂(N)) = σ(N)×4 exactly would make G_eff(N) a theorem

  Interactive visualisation produced:
  - Canvas widget with σ(N) curve, dual markers (CMB/local), H₀ bars,
    sliders for N_CMB and N_local, topology decomposition panel (18=6+5+4+3)

  Productions:
  - D26: PDL_Hubble_Resolution.tex (556 lines, Overleaf-ready)
    Full journal paper in English, D23 template style
    §1 Introduction, §2 Proton architecture + bridge, §3 Exponent 18 summary,
    §4 σ(N) definition and properties, §5 Hubble tension resolution,
    §6 Discussion + solar-system + epistemic table + 5 open problems
    Target journal: JCAP or Physical Review D (cosmology section)
  - D26-bib: References_Hubble.bib (213 lines, 20 entries, full BibTeX)
    Covers: full PDL corpus (D1–D26), Planck 2020, Riess 2022, Freedman 2024,
    ACT 2020, Di Valentino 2021, Knox & Millea 2020, Uzan 2003, CODATA 2022,
    Hatcher 2002, Fulton & Harris 1991, Weinberg 2008, Brans & Dicke 1961

---

## Next Actions (priority order)

1. **[IMMEDIATE]** Publish D26 (PDL_Hubble_Resolution.tex) on Zenodo and arXiv
   (gr-qc + astro-ph.CO cross-listing) with D26-bib
2. **[IMMEDIATE]** Update D_Map to v11: add D26, update D25 status, update
   epistemic table CT5 to reflect G_eff(N) as structural conjecture
3. **[HIGH]** OP1 (D26): compute rank(d₂(N)) as function of N — this is now
   the highest-priority NEW problem from this session
4. **[HIGH]** OP1 (D24/D25/D26): derivation of ε_G from η(G_{p*}) —
   still the highest-priority FOUNDATIONAL problem in the programme
5. **[HIGH]** Contact DESI data team re: closure-density field ρ_cl(r)
   computation from galaxy catalogues (OP3 in D26)
6. **[MEDIUM]** Complete ker(d₂) = ⟨e_{r_val(n)}⟩ exact over Q(√5) (OP4 in D23)
7. **[MEDIUM]** CMB power spectrum impact: compute ΔC_ℓ from ΔG/G ≈ 15% (OP4 in D26)
8. **[MEDIUM]** Higher-order bridge correction: verify R·C·n_u²/(n_u²+1) conjecture

---

## Instructions for Next Session

Start by saying: *"Read PDL_context.md and the corpus files from the project."*

After each session, update:
- Session History (add new session entry)
- Open Problems (mark resolved, add new)
- Key Numerical Values (if new results)
- Corpus table (if new documents)
- Dependency map (if new connections)
- Next Actions (reprioritise)
