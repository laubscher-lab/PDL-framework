# PDL — Project Context and Session Memory
# Last updated: Session 8 (March 2026)

---

## Programme Identity

**PDL** = Projective Dynamic Logo (English) = **LDP** = Logo Dynamique Projectif (French)
Author: Cédric Laubscher, independent researcher, Switzerland
Contact: cedric.laubscher@gmail.com
Repository: https://github.com/laubscher-lab/PDL-framework
Zenodo: search "Cédric Laubscher"

---

## Core Integers (never change these)

| Symbol | Value | Role |
|--------|-------|------|
| n_u | 24 | Up-core valence multiplicity |
| n_d | 28 | Down-core valence multiplicity |
| r_val(p) | 930 | Proton total stationary valence |
| R_sea(p) | 10087 | Proton dynamical sea |
| R_tot(p) | 11017 | Proton total relational budget |
| R_surf | 310φ ∈ Q(√5) | Proton active surface |
| r_val(n) | 1032 | Neutron total stationary valence |
| R_sea(n) | 9960 | Neutron dynamical sea |
| R_tot(n) | 10992 | Neutron total relational budget |
| N_crit | 126.1 | Maximum stable neutron number |
| Z_sat | 20 | Saturation threshold (valley of stability) |

---

## Key Numerical Values

| Quantity | Value | Status |
|----------|-------|--------|
| φ (golden ratio) | (1+√5)/2 = 1.61803... | Exact |
| ε_G | 0.0075197 | Derived via bridge formula from α_exp |
| α_PDL^{-1} | 137.022 | Derived, no free param, dev 1.0×10⁻⁴ |
| G_PDL | 6.67448×10⁻¹¹ m³kg⁻¹s⁻² | Derived, dev 27 ppm vs CODATA 2022 |
| Δr_val | 0.047960 | EM valence surplus |
| R = R_tot·R_surf/r_val² | ≈ 6.3892 | Amplification factor |
| C = n_u²/(n_u²-1) | 576/575 | Up-core coherence correction |
| R·C | ≈ 6.4003 | Bridge product |
| κ = R_surf/R_tot | 310φ/11017 ≈ 0.04553 ∈ Q(√5) | Surface engagement coefficient |
| 18κ | ≈ 0.8195 ∈ Q(√5) | Gravitational amplification of κ |
| σ_loc (Hubble) | ≈ 0.211 | Constrained by H0_local/H0_CMB |

---

## Corpus Documents

| File | Label | Description | Status |
|------|-------|-------------|--------|
| PDL.tex | D1 | Main technical article: axioms, (4,6), proton, constants | Published Zenodo |
| PDL_intro / PDL_Intro_2026 | D2 | Accessible introduction EN | Published Zenodo |
| PDL_position / Position_paper_PDL.tex | D3 | Position paper: status, open problems, TO interface | Published Zenodo |
| TO-PDL.tex | D_TO | Interface with Theory of Objectivity | Published Zenodo |
| Towards_Einstein-Dirac_Unification_PDL.tex | D_ED | Einstein–Dirac unification sketch | Published Zenodo |
| A_Topological_Reformulation...tex | D_Top | Leakage as probability, coexistence topology | Published Zenodo |
| Derivation_alpha_PDL_v2.tex | D_Alpha / D5 | Structural derivation of α (v2) | Published Zenodo |
| Relational_Emergence_of_Born... | D_Born / D6 | Born's rule + golden ratio active surface (v2) | Published Zenodo |
| Coherence_Leakage...Exponent_18...v2.tex | D17 | Hierarchical filtering, exponent 18 (v2) | Published Zenodo |
| Universal_Coherence_Leakage...V3.tex | D20-V3 | Bridge G ↔ α — PRIMARY RESULT | CURRENT VERSION |
| Existence_as_Pulsating_Closure...tex | D_Exist | Ontological meditation on PDL | Philosophical |
| Whoever_We_May_Be...v2.tex | D_Who_v2 | Philosophical synthesis, article format | Philosophical |
| Whoever_we_may_be — LDP_v2.tex | D_Who_book | Same themes, book format FR | Published Zenodo |
| Whatever_We_May_Be...v2.tex | D_Who_book_EN | Popular introduction EN | Published Zenodo |
| Quoi_que_nous_soyons...v2.tex | D_Who_book_FR | Popular introduction FR | Published Zenodo |
| Discrete_Cavity_Modes...tex | D19 | PDL cavity, density of states ρ(ν)∝ν² | Published Zenodo |
| PDL_Nuclear_Stability_Skeleton.tex | D22 | Nuclear stability, neutron quintuplet, N_crit=126 | Published Zenodo |
| PDL___Topological_Origin_of_the_Exponent_18_v2.tex | D23 | Topological origin of exponent 18: K₄=∂Δ³≅S², 18=6+5+4+3 | Published Zenodo |
| PDL_Bridge_G_Alpha_v2.tex | D24 | **NEW** Paper 1: parameter-free bridge α–G | Ready for Zenodo/arXiv |
| PDL_Hubble_tension.tex | D25 | **NEW** Paper 2: Hubble tension from closure density | Ready for Zenodo/arXiv |

---

## D20 Version History

| Version | Status | Key change |
|---------|--------|-----------|
| V1 (original) | SUPERSEDED | ε_G=0.0073891 (wrong), bridge formula 3φ²ε_G (no structural basis) |
| V2 | SUPERSEDED (label) | Corrected ε_G, corrected bridge formula |
| V3 | CURRENT | Scientifically identical to V2 — confirmed in Session 3 |

---

## Open Problems (current status)

1. [RESOLVED — Session 7] Topological proof of exponent 18 (D23)
   - K₄ = ∂Δ³ ≅ S², H₂(S²;Z) ≅ Z, generator [S²] = (-1,+1,-1,+1)ᵀ
   - Decomposition 18 = 6+5+4+3 proved analytically over Q(√5)
   - rank(d₀)=6, rank(d₁)=5 with ker=⟨e_{r_val(p)}⟩, rank(d₂)=4

2. [OPEN — HIGH] Formal categorical identification of δ_long (OP1 in D23)
   - Bridge formula δ_long: C₁→C₃ conjectured to factor through [S²]∈H₂(∂Δ³;Z)
   - Would complete interpretation of all 3 boundary morphisms as realisations
     of the single generator of H₂(S²;Z)

3. [OPEN — MEDIUM] Golden ratio in algebraic structure of J_{d₂} (OP2 in D23)
   - φ enters every entry of J_{d₂} via R_surf = φ·r_val/3
   - Characterise the φ-structured lattice in the space of PDL transition amplitudes

4. [OPEN — MEDIUM] Closed-form proof of Shell(n) = 3·C(2n-2,n-1) (OP3 in D23)
   - Verified computationally for n=1..8; analytical proof via Gegenbauer polynomials pending

5. [OPEN — MEDIUM] ker(d₂) = ⟨e_{r_val(n)}⟩ exact (OP4 in D23)
   - Numerical confirmation done; exact proof over Q(√5) not yet complete

6. [OPEN — FUTURE] Structural necessity of n=3 (OP5 in D23)
   - E(3)=Shell(3)=18 proved; showing n≠3 is forbidden by PDL axioms remains open
   - Would constitute a derivation of 3-dimensionality from coherence axioms

7. [OPEN — HIGH] Derivation of ε_G from first principles (OP1 in D24)
   - ε_G currently determined via bridge formula from α_exp
   - Need: explicit graph-theoretic computation of minimal frustration density
     η(G_{p*}) on the proton constraint graph at p*
   - Resolving this makes G a fully predicted constant with no empirical input
   - SAME COMPUTATION needed to derive ρ₀ in D25 (OP1 in D25)

8. [OPEN — HIGH] Global uniqueness of proton quintuplet (OP2 in D24)
   - Local rigidity under ±1 perturbation of any integer: confirmed computationally
   - Formal proof of global uniqueness within all PDL-admissible configurations: pending
   - Blocks upgrade of Theorems in D24 from "tightly constrained" to "proved"

9. [OPEN — MEDIUM] Higher-order corrections to bridge formula (OP3 in D24)
   - Residual 0.34% in bridge Δr_val = ε_G·R·C
   - Conjecture: series in 1/n_u² converges; next term ≈ R·C·n_u²/(n_u²+1) ≈ 6.3781
   - Would reduce residual below 0.001%

10. [OPEN — MEDIUM] Categorical proof of δ_long as long morphism (OP4 in D24)
    - Bridge formula is the algebraic realisation of δ_long: C₁→C₃
    - Proof that it factors through [S²] would place G–α connection on topological footing

11. [OPEN — MEDIUM] Parameter-free derivation of k_B (OP5 in D24 / OP5 in D25)
    - Current: order-of-magnitude consistency via k_B^PDL ~ ℏω_p·ε_G^12
    - Need: precise structural identification of the thermodynamic ensemble in PDL

12. [OPEN — HIGH] Derivation of saturation density ρ₀ (OP1 in D25)
    - ρ₀ = density at which ⟨N⟩ = 1/κ (each surface relation engaged once)
    - Requires computing the "volume" of N(P₀) in the coherence-cost pseudometric d
    - SAME COMPUTATION as OP1 in D24 (derivation of ε_G from first principles)

13. [OPEN — MEDIUM] Exact treatment of engagement correlations (OP2 in D25)
    - Theorem 3.1 (D25) assumes independence of engagement events across neighbours
    - Correction of order κ·σ_loc ≈ 0.01: within current uncertainties
    - Full treatment requires pair-correlation function on J(P₀,Pᵢ)∩J(P₀,Pⱼ)

14. [OPEN — MEDIUM] Quantitative prediction of σ_loc from LSS data (OP3 in D25)
    - Current: σ_loc ≈ 0.211 consistent with known LSS; not derived from it
    - Need: integrate closure-density field ρ_cl(r) from DESI/Euclid catalogues
    - Would transform P1–P3 predictions from structural to quantitative

15. [OPEN — MEDIUM] Higher-order corrections in κ to Hubble formula (OP4 in D25)
    - Leading term: 18κ·σ_loc ≈ 0.173
    - Next order: C(18,2)κ²·σ_loc² ≈ 0.014 (1.4% of tension amplitude)
    - Detectable at DESI precision (0.5%)

16. [OPEN — MEDIUM] Shell splitting from Δn=4 (OP1 in D22)
    - Mechanism identified: Δn/(2n_u) = 1/12 ≈ 0.083 ℏω₀
    - Combinatorial derivation from signed-graph formalism: not yet done

17. [OPEN — MEDIUM] Isotopic window width ΔN(Z) (OP2 in D22)

18. [OPEN — MEDIUM] Lacunae Z=43, Z=61 (OP3 in D22)

19. [OPEN — FUTURE] Chemical properties via Block III (OP4 in D22)

---

## Epistemic Status Summary (D24 + D25 results)

| Result | Status |
|--------|--------|
| K₄ unique minimal PDL closure | Structural theorem (D23) |
| n_u=24 from quadratic, unique | Proved (D23, D24) |
| R_surf = 310φ ∈ Q(√5) | Structural definition |
| α_PDL^{-1} = φ²r_val²/(9μ), no free param | Derived (D24) |
| α_PDL^{-1} = 137.022, dev 10⁻⁴ | Verified vs CODATA 2022 |
| Bridge Δr_val = ε_G·R·C, 0.34% residual | Tightly constrained (D24) |
| G_PDL = 6.67448×10⁻¹¹, dev 27 ppm | Verified vs CODATA 2022 (D24) |
| κ = R_surf/R_tot ∈ Q(√5), no free param | Derived (D25) |
| p_e = κ (engagement probability) | Proved (D25, Lemma 3.1) |
| σ(N) = 1-(1-κ)^N, exact | Proved (D25, Theorem 3.1) |
| σ(x) = 1-e^{-x}, continuum limit | Proved (D25, Proposition 3.1) |
| G_eff(ρ_cl) ≈ G₀(1+18κ·σ), leading order | Derived (D25, Theorem 4.1) |
| σ_loc ≈ 0.211 from H0_local/H0_CMB | Constrained (D25) |
| Predictions P1, P2, P3 (Hubble) | Structural, falsifiable (D25) |

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

- **Session 8 (March 2026):** PDL Hubble tension programme.

  Theoretical developments:
  (a) Formal derivation of δ(ρ_cl) from graph combinatorics:
      - Lemma: p_e = κ = R_surf/R_tot ∈ Q(√5) from uniform relational budget
      - Theorem (exact): σ(N) = 1-(1-κ)^N, no free parameter
      - Proposition: continuum limit σ(x) = 1-e^{-x}, error bounded at ≤0.5%
      - Key: exponential form derived, not postulated
  (b) Density-dependent G_eff(ρ_cl) = G₀(1+18κ·σ(ρ_cl/ρ₀)) derived
  (c) Hubble tension identified as observational signature of κ-mechanism:
      σ_loc ≈ 0.211 consistent with LSS data
  (d) Three falsifiable predictions P1–P3 formulated for DESI/Euclid/SKA

  Productions:
  - D24: PDL_Bridge_G_Alpha_v2.tex + PDL_Bridge_references.bib
    Paper 1 (British English, Theorem/Proof style, Q(√5) arithmetic)
    α–G bridge: α at 10⁻⁴, G at 27 ppm, from single ε_G = 0.0075197
    Target journal: Foundations of Physics or IJMPA
  - D25: PDL_Hubble_tension.tex + PDL_Hubble_references.bib
    Paper 2 (British English, same style as D24)
    σ(N)=1-(1-κ)^N derived; Hubble tension as structural prediction
    Target journal: JCAP or Universe (MDPI)

  Epistemic assessment:
  - D24 is ready for arXiv + Zenodo submission
  - D25 is ready for arXiv + Zenodo submission, with ρ₀ as single free parameter
  - Critical path: OP1 (D24) = OP1 (D25) = derivation of ε_G/ρ₀ from first principles
    Resolving this single problem would make G a fully derived constant and
    would simultaneously determine ρ₀, making D25 parameter-free as well

---

## Dependency Map (critical path)

```
Proton quintuplet (24,28,930,10087,11017)
    ├── α (Theorem, D5/D24) ──────────────────────── no free param
    ├── Δr_val (Proposition, D24) ─────────────────── from α_exp
    │        └── Bridge R·C (Theorem, D24) ──────── G at 27 ppm
    │                 └── ε_G = 0.0075197
    │                          ├── G_PDL (D24) ─── 27 ppm CODATA 2022
    │                          └── k_B (order of magnitude, D1)
    ├── κ = R_surf/R_tot (D25) ────────────────────── exact Q(√5)
    │        └── σ(N) = 1-(1-κ)^N (D25) ──────────── proved
    │                 └── G_eff(ρ_cl) (D25) ────── Hubble tension
    ├── Exponent 18 (Theorem, D23) ─────────────── topological necessity
    │        └── 18κ = 0.8195 (D25) ──────────── amplification
    └── Nuclear stability (D22) ─────────────────── N_crit=126.1
```

**OPEN GATE:** derivation of ε_G from η(G_{p*}) (OP1/D24 = OP1/D25)
- If proved: G becomes parameter-free, ρ₀ determined, D25 becomes parameter-free
- This is the highest-priority open problem in the programme

---

## Next Actions (priority order)

1. **[IMMEDIATE]** Publish D24 and D25 on Zenodo and arXiv (hep-th + gr-qc)
2. **[IMMEDIATE]** Update D_Map to v11 integrating D24 and D25
3. **[HIGH]** Tackle OP1 (D24): compute η(G_{p*}) = minimal frustration density
   of the proton constraint graph by explicit graph-theoretic enumeration
4. **[HIGH]** Contact DESI data team re: σ_loc computation from galaxy catalogues
   (OP3 in D25) — this could provide observational confirmation of P2
5. **[MEDIUM]** Complete ker(d₂) = ⟨e_{r_val(n)}⟩ exact over Q(√5) (OP4 in D23)
6. **[MEDIUM]** Higher-order bridge correction: verify R·C·n_u²/(n_u²+1) conjecture

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
