# PDL Framework — Projective Dynamic Logo

**Author:** Cédric Laubscher — Independent Researcher, Switzerland
**Site:** [cedriclaubscher.ch](https://cedriclaubscher.ch)
**Zenodo community:** [pdl-framework](https://zenodo.org/communities/pdl-framework)

## Licence
Unless otherwise stated, the textual content of this repository
(including notes, articles, and figures) is licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International Licence](https://creativecommons.org/licenses/by-sa/4.0/).

© 2026 Cédric Laubscher

**Status:** Programme closed at D55 (May 2026) — synthesis document DS01 available

***

## For the critical reader

If you have arrived here to evaluate, challenge, or falsify the programme, start with:

1. `IMRad_PDL.pdf` — a self-contained IMRaD-structured summary of the framework, its claims, and its limitations (recommended entry point for reviewers).
2. `DS01_programme_closure_at_D55.tex` — synthesis document listing all results, their epistemic status (unconditional theorem / structured conjecture / open problem), and the three experimentally testable predictions.
3. `PDL Global Mapping of Structures Results and Open Problems_v16.tex` — full dependency map of the corpus.

Every result in this corpus carries an explicit epistemic label. Negative results are documented with the same rigour as positive ones. Questions and objections are welcome — the most useful question is: *which step in the chain C1–C4 → G do you find least convincing?*

***

## What is PDL?

The **Projective Dynamic Logo (PDL)** framework derives the principal constants of physics from four combinatorial axioms C1–C4 on finite signed graphs, with a single irreducible external parameter: the up–down quark mass difference $\Delta m_{\rm iso} = m_d - m_u$.

At D55 (May 2026), the following results are established as unconditional theorems of C1–C4:

| Result | Value / Statement | Document |
|---|---|---|
| Fine-structure constant | $\alpha_{\rm PDL} = 1/137.036$ | D25 |
| Newton's constant | $G_{\rm PDL}$ within 17 ppm of CODATA | D44 |
| Cosmological constant | $\Lambda_{\rm PDL}$ within 0.17% of observation | D51–D53 |
| Bekenstein–Hawking $\tfrac{1}{4}$ | $S_{BH} = k_B A / (4\ell_P^2)$ | D50 |
| Nuclear magic numbers | $\{2,8,20,28,50,82,126\}$ derived | D47 |
| Periodic table $Z \leq 82$ | Valley of stability, 31/31 sub-shells | D47 |
| Weinberg angle | $\theta_W = 19\pi/119$, $\sin^2\theta_W = 0.231196$ (0.48$\sigma$ PDG 2024) | D55 |
| Born rule | $P = |\psi|^2$ via Gleason + Hopf fibration | D34, D46 |
| Schrödinger equation | From $K_4$ pulsation | D32 |
| Dirac equation | $T^2 = -I_2$ from $K_4$ | D33 |
| Einstein equation | $\sigma(N)$-modified coupling | D35 |
| London equation | From coherence graph pulsation | D49 |

***

## Recommended Reading Order

The corpus is organised into ten phases. Reading in order is strongly recommended, as each document builds on the previous ones.

### Phase 0 — Introduction
| File | Description |
|---|---|
| `PDL.tex` | Narrative introduction to the PDL framework |
| `IMRad_PDL.tex` | IMRaD-structured summary (recommended entry point for reviewers) |

### Phase 1 — Axiomatic Foundations (C1–C4)
| File | Description |
|---|---|
| `LDP.tex` | The four axioms C1–C4 and the minimal admissible closure |
| `A_Topological_Reformulation_in_the_Projective_Dynamic_Logo_Framework.tex` | Topological reformulation |

### Phase 2 — The Proton Quintuplet
| File | Description |
|---|---|
| `Combinatorial_Proton_Architecture_PDL.tex` / `_v2` | Derivation of the proton quintuplet $(24,28,930,10087,11017)$ |
| `On the Combinatorial Selection and Local Uniqueness of the PDL Proton Architecture.tex` | Uniqueness proof |
| `Minimal Stationary Closures in the PDL Framework Necessity of the 4-6 Block.tex` | Necessity of the 4-6 block |

### Phase 3 — Fundamental Constants
| File | Description |
|---|---|
| `Derivation_alpha_PDL.tex` / `_v2` | Derivation of $\alpha = 1/137.036$ |
| `A Parameter-Free Structural Bridge between the Fine-Structure Constant and Newton's Gravitational Constant.tex` | Bridge $\alpha \to G$ |
| `D44-Closure_of_OP-B.tex` | Newton's constant |
| `D51_leakage_constant.tex` | Cosmological constant (step 1) |
| `D52_leakage_bases.tex` | Cosmological constant (step 2) |
| `D53_causal_closure_Lambda.tex` | Causal closure for $\Lambda$ |

### Phase 4 — Quantum Mechanics from C1–C4
| File | Description |
|---|---|
| `D43_causal_chain.tex` | Full causal chain diagram |
| `D42v3_Derivation_of_H3_from_C1_C4.tex` | Equiparticipation Lemma (24 576 cases, 0 violations) |
| `Dirac Equation from the SL(2,C) Pulsation of K_4 in the PDL Framework.tex` | Dirac equation |
| `Born Rule from (A)∧(B)-Admissible Amplitudes in the PDL Framework.tex` | Born rule Level 1 |
| `D46 — Born's Rule Level 2.tex` | Born rule Level 2 (Hopf fibration) |
| `D48v3_coherence_tensor.tex` | Coherence tensor |
| `D49_london_equation.tex` | London equation (superconductivity) |

### Phase 5 — Electroweak and Gravitational Sector
| File | Description |
|---|---|
| `D35_Einstein_PDL.png` | Einstein equation ($\sigma(N)$-modified coupling) |
| `D50 — BH Quarter.tex` | Bekenstein–Hawking entropy |
| `D55_Weinberg_angle.tex` | Weinberg angle $\theta_W = 19\pi/119$ |

### Phase 6 — Nuclear and Atomic Structure
| File | Description |
|---|---|
| `Nuclear Stability PDL.tex` | Nuclear stability framework |
| `D47 -- Shell Filling.tex` | Magic numbers and periodic table (31/31 sub-shells, $Z=1$–82) |
| `D41 pdl island of inversion.tex` | Island of inversion (confrontation Ha et al., *Nature Comm.* 2025) |

### Phase 7 — Cosmology and Black Holes
| File | Description |
|---|---|
| `Closure-Density Dependence of the Effective Gravitational Coupling and the Structural Origin of the Hubble Tension.tex` | Hubble tension |
| `D45 pbh threshold.tex` | Primordial black hole threshold (+11.89% vs GR, testable via Fermi-LAT) |
| `D54_equation_of_state.tex` | Equation of state $w = -1$ |

### Phase 8 — Coherence Leakage and Exponent 18
| File | Description |
|---|---|
| `Coherence Leakage Hierarchical Filtering and the Exponent 18 in the PDLogo Framework_v2.tex` | Exponent 18 derivation |
| `Coherence_Effective_Fields_Gauss_Faraday_Structure_Triangle_Counts_Schrödinger_Dynamics_PDL_Framework.tex` | Effective fields |

### Phase 9 — Global Mapping and Open Problems
| File | Description |
|---|---|
| `PDL Global Mapping of Structures Results and Open Problems_v16.tex` | Latest global map (v16) |
| `DS01_programme_closure_at_D55.tex` | **Synthesis document DS01** — programme closure, open problems, experimental frontiers |

### Phase 10 — PDL-V: Extensions to Biology (DL series)
| File | Description |
|---|---|
| `DL01 — From Axioms to Life.tex` | Self-replication thresholds from C1–C4 |
| `DL02 — Existence Separation.tex` | Existence separation theorem |

***

## Falsifiable Predictions

Three predictions are at or approaching experimental testability:

| Prediction | PDL Value | Current Data | Horizon |
|---|---|---|---|
| $\Delta m_{\rm iso}$ (D30) | 2.532 MeV | FLAG 2024: $2.52 \pm 0.08$ MeV | 3–5 yr (±0.04 MeV) |
| $\Delta m_{\rm iso}$ (D55) | 2.446 MeV | Within current interval | 3–5 yr |
| PBH threshold (D45) | +11.89% vs GR | Fermi-LAT pending | Indeterminate |
| Magic numbers near $N=82,126$ (D47) | Specific deviations | FRIB/RIKEN pending | Indeterminate |

***

## Computational Verification

| Document | Verification | Cases |
|---|---|---|
| D29 | Exhaustive check of Gate 1 amplitude 155/11017 | 768 configurations |
| D42 | Equiparticipation Lemma | 24 576 cases, 0 violations |
| D50 | Statistical independence | 30 720 cases |
| D55 | `PDL_D55_Colab_OP10a.py` | Numerical Weinberg angle check |

***

## Repository Structure

All documents are in the root directory. Each numbered derivation `DXX` is provided as:
- `DXX_title.tex` — LaTeX source (compilable in Overleaf, British English)
- `DXX___title.pdf` — compiled output
- `DXX_references.bib` — bibliography (when applicable)

Supporting figures are provided as `.png` or `.pdf` named after their parent document. Multiple versions (`_v2`, `_v3`) reflect iterative refinements; the highest-numbered version is always current.

***

## Contact

Cédric Laubscher — [cedriclaubscher.ch](https://cedriclaubscher.ch)
