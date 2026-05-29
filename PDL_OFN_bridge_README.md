# PDL–OFN Bridge: Numerical Study of β₁ = 3 as a Shared Topological Invariant

**Author:** Cédric Laubscher — Independent Researcher, Switzerland  
**Date:** May 2026  
**Related corpus:** [Projective Dynamic Logo (PDL)](https://cedriclaubscher.ch) — Zenodo community: pdl-framework  
**Related work:** Evdokimov & Ryss, *OFN as a CWS Quantum Code on the Octahedron Graph* (2026), DOI: 10.5281/zenodo.20322830

---

## Context

Two independent pre-geometric frameworks — the **Projective Dynamic Logo (PDL)** and the **Ontological Fundamental Network (OFN)** — independently arrive at β₁ = 3 as a key topological invariant:

- In **PDL**: β₁(K₄) = 3 is the first Betti number of the minimal admissible graph K₄, forced by axioms C1–C4. It gives exactly three independent leakage cycles, whose prime exponents (23, 67, 997) determine the cosmological constant Λ (D51, D52, D53 — DOI: 10.5281/zenodo.20036769).
- In **OFN**: b₁(G_H) = 3 is the first Betti number of the Hamming graph on the vacuum manifold Ω₂₁ ⊂ Q₆. It yields three generations of fermions.

This repository documents a structured numerical investigation of whether this convergence reflects a shared underlying structure, or whether the two frameworks reach the same invariant by genuinely independent routes.

---

## Question

Is the convergence on β₁ = 3 due to:
1. A structural identity between K₄ (PDL) and Q₆ (OFN)?
2. A natural bijection between the two 6-dimensional configuration spaces?
3. A deeper topological property of 6-dimensional binary spaces?

---

## Scripts

All scripts are self-contained, use only the Python standard library, and run directly in Google Colab (no external dependencies).

### Script 1 — Necessity of β₁ = 3 for the PDL cosmological formula

**File:** `script1_beta1_necessity.py`

**What it does:**
- Enumerates all 38 connected graphs on 4 vertices
- Shows that K₄ is the unique one with β₁ = 3
- Computes the PDL cosmological formula C with β₁ = 1, 2, 3 and measures the deviation from C_target in ppm

**Key result:**
| β₁ | Cycles | Deviation from C_target |
|----|--------|------------------------|
| 1  | 1      | 8.2 × 10³⁰ ppm         |
| 2  | 2      | 6.6 × 10⁵ ppm          |
| 3  | 3 (K₄) | **0.41 ppm** ✓         |

β₁ = 3 is a **necessary condition** for the PDL cosmological formula to be compatible with observation.

---

### Script 2 — Orbits of S₄ on signed K₄ configurations

**File:** `script2_S4_orbits.py`

**What it does:**
- Computes all orbits of S₄ on the 64 signed K₄ configurations
- Identifies the 8 balanced configurations (PDL ground states) and their orbit structure
- Compares the natural PDL involution (global sign inversion) with the OFN CP-involution
- Computes characters of the edge permutation representation of S₄

**Key results:**
- S₄ partitions the 64 configurations into **11 orbits** (sizes: 1,1,3,3,4,4,6,6,12,12,12)
- The 8 balanced configurations form **3 orbits** under S₄
- The PDL natural involution has **0 self-conjugate** configurations (all 64 are in crossing pairs)
- The OFN CP-involution has **8 self-conjugate** states in Ω₂₁
- The S₄ decomposition on 6 edges is **1 ⊕ 2 ⊕ 3_std** (confirmed, D36)
- The OFN decomposition under A₅×Z₂ is **8 ⊕ 3 ⊕ 1 ⊕ 1** → SU(3)×SU(2)×U(1)×U(1)′

The symmetry groups, involutions, and decompositions differ structurally.

---

### Script 3 — Bijections between K₄ edges and Q₆ qubits

**File:** `script3_bijection.py`

**What it does:**
- Tests all 720 bijections between the 6 K₄ edges and the 6 Q₆ qubits
- For each bijection, computes the overlap between the 8 balanced PDL configurations and Ω₂₁
- For each bijection, computes β₁ of the preimage of Ω₂₁ in the signed K₄ space
- Samples 2000 random subsets of size 21 in {0,1}⁶ to assess the frequency of β₁ = 3

**Key results:**
- Best overlap balanced PDL ∩ Ω₂₁: **5/8** (no bijection achieves full correspondence)
- Best overlap balanced PDL ∩ self-conjugate OFN: **3/8**
- Preimage of Ω₂₁ has β₁ = 3 for **720/720 bijections** (unconditional)
- ~18% of random size-21 subsets of {0,1}⁶ have β₁ = 3

---

## Conclusions

**What is established:**

1. K₄ is the **unique** connected graph on 4 vertices with β₁ = 3 (exhaustive, 38 graphs).
2. β₁ = 3 is a **necessary condition** for the PDL cosmological formula to be non-degenerate.
3. The convergence on β₁ = 3 is **not** due to a structural identity or natural bijection between K₄ and Q₆.
4. β₁ = 3 is preserved by all 720 bijections for the preimage of Ω₂₁ — this is a property of the **topology of the 6-dimensional binary space**, not an exclusive feature of Ω₂₁ or K₄.

**What this suggests:**

β₁ = 3 appears to be a topological invariant of **minimal relational closures in 6-dimensional binary spaces**, reached independently by PDL and OFN through structurally distinct selections. The convergence is real and non-trivial, but its origin is topological rather than algebraic.

This is the honest starting point for the conjecture: *β₁ = 3 is a necessary condition for any non-trivial relational closure in a 6-dimensional binary space.*

---

## Epistemic status

All results are based on exhaustive enumeration (no sampling except the 2000-subset test in Script 3, which is labelled as an estimate). Every claim is directly reproducible from the scripts.

These results are preliminary. They establish a numerical foundation for a possible joint investigation, not a proof of the conjecture stated above.

---

## References

- PDL corpus (D01–D55): https://zenodo.org/communities/pdl-framework
- PDL cosmological derivation (D51–D53): https://doi.org/10.5281/zenodo.20036769
- PDL synthesis DS01: https://doi.org/10.5281/zenodo.20187274
- OFN CWS paper: https://doi.org/10.5281/zenodo.20322830
- OFN cosmology (Article IV): https://doi.org/10.5281/zenodo.18642431
- PDL website: https://cedriclaubscher.ch
