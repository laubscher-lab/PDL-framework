# D68 — Zenodo deposit sheet

Everything below is ready to paste. Fields follow the Zenodo upload form order.

---

## 1. Files to upload (8 files)

Filenames follow the corpus convention already visible in the registry
(`D66_parity_obstruction.pdf`, `D67_metric_and_coherence_tensor.pdf`).
They are the names a peer will see after download, so they must remain
meaningful on their own and must not carry drafting artefacts.

| # | File | Role | MD5 |
|---|------|------|-----|
| 1 | `D68_pulsation_bipartition.pdf` | **Main document** (27 pp.) — upload first | `1bb0b61b6a5274b9c402a22f1e38b43e` |
| 2 | `D68_pulsation_bipartition.tex` | LaTeX source | `d39dcb11631564d0bafaeec0c62dc056` |
| 3 | `D68_references.bib` | Bibliography source | `f49e71b1e68c30db47f2d38c8b70c722` |
| 4 | `PDL_pulsation_regimes_script1.py` | Verification script 1 | `fa86890b3483d79b8ea8e21e39b29f79` |
| 5 | `PDL_pulsation_regimes_script2.py` | Verification script 2 | `70d8a1273a9b0acbcbd34fa2c9962b68` |
| 6 | `PDL_pulsation_regimes_script3.py` | Verification script 3 | `a46fd4c9032cb5588640903e6cc62e6d` |
| 7 | `PDL_pulsation_regimes_script4.py` | Verification script 4 | `f15dd2592e9ecf979086b621cc83d220` |
| 8 | `PDL_pulsation_regimes_script5.py` | Verification script 5 | `f7a7c6c691ef75fb2f6bf9bc4110eb93` |

The `.tex` calls `\bibliography{D68_references}`, so the bibliography file
must keep exactly the name `D68_references.bib` for a peer to recompile.
The whole set has been rebuilt and recompiled under these filenames:
four passes, zero errors, zero unresolved references, zero placeholders.

Scripts 6–15 of the session belong to **D69**, not here.

---

## 2. Resource type

**Publication → Preprint**

---

## 3. Title

```
The Pulsation as a Bipartition: Complete Classification of C1-Admissible Dynamical Laws, and a Singleton Obstruction Theorem for Frustration-Based Selection (Projective Dynamic Logo Framework — Document D68)
```

---

## 4. Creators

```
Laubscher, Cédric
```
- Affiliation: `Independent Researcher, Switzerland`
- ORCID: `0009-0004-5415-1098`

---

## 5. Description

```
The founding question of the PDL programme — what distinguishes something that exists from something that does not — is answered in axiom C1 by the postulate of a repeatable, non-trivial binary alternation. The corpus has never argued for C1; it has only assumed it. This document supplies the missing argument, quarantined in an appendix as motivation rather than proof, and then determines exhaustively what C1 can and cannot mean.

Three results are established as unconditional theorems of C1–C4. First, a C2-admissible sign configuration on a complete signed graph is exactly a bipartition of its vertices, and the pulsation is exactly a switching by a fixed vertex subset: an involution, hence a two-cycle by construction. Second, the pulsation laws compatible with C1 are completely classified. On n entities there are exactly 2(2^n − 2) admissible laws, falling into exactly two families and no third, and generating exactly 2^(n−1) − 1 distinct relational dynamics — in bijection with the non-trivial coherent configurations. In particular, a strictly universal simultaneous inversion of every entity is the trivial element: it is not incoherent but empty, being the exact gauge redundancy already identified as the U(1) global phase in D46. What survives is a partition of the entities into two phase classes, all entities sharing one period and differing only by a binary offset, each changing state exactly once per relational cycle. Third, the set of frustrated triangles is pointwise invariant under every switching, so the classification is independent of frustration and is not a property of the balanced idealisation.

Two negative results follow, both first-class. C4 is blind to the pulsation: the frustration count is identical across all 2^(n−1) − 1 candidate bipartitions, so no minimisation of leakage can select one. And the natural refinement that does select — minimising the frustration carried across the pulsating boundary — always selects a cut of size one, that is, a single privileged entity, which is inadmissible in a relational theory. This last statement is proved here as a theorem for all n and all cut sizes; the proof turns entirely on the two-graph parity condition, and is reproduced exactly on the extremal family. A corollary excludes every functional built from frustration and group size alike.

Section 10 carries every object of the paper through explicitly on K4, configuration by configuration, so that the results can be checked by hand before any script is run. Three errata are recorded: two in D46, verified against its source, and one in D43, where an arithmetic bridge between simulation and theorem does not close; correcting the latter shows that the excess of 101 which the corpus has carried unexplained is exactly n_K + (Δn+1)² = 76 + 25. A divergence between D46's definition of the pulsation and the one derived here is recorded as an open problem. Five verification scripts, exhaustive up to n = 7, are deposited with this document.
```

---

## 6. Publication date

Today's date (deposit date).

---

## 7. Keywords / subjects

```
Projective Dynamic Logo
PDL
signed graphs
switching classes
two-graphs
Harary balance
combinatorial foundations of physics
pulsation
gauge redundancy
parity obstruction
foundations of physics
discrete structures
```

---

## 8. Language

```
English
```

---

## 9. Version

```
v1
```
(Internally the source is marked Version 4; that numbering is a drafting trace, not a publication history. This is the first deposited version.)

---

## 10. Related identifiers

Use **"is new version of"** only if you decide to supersede something — you should not, D68 is new.

Add the following as **"references"** (cites):

| Relation | DOI |
|---|---|
| references | `10.5281/zenodo.18462686` (D01) |
| references | `10.5281/zenodo.18463130` (D02) |
| references | `10.5281/zenodo.18664995` (D08) |
| references | `10.5281/zenodo.18832953` (D16) |
| references | `10.5281/zenodo.19307249` (D33) |
| references | `10.5281/zenodo.19678389` (D43) |
| references | `10.5281/zenodo.19956932` (D46) |
| references | `10.5281/zenodo.20639684` (D60) |
| references | `10.5281/zenodo.20645713` (D61) |
| references | `10.5281/zenodo.21351177` (D66) |
| references | `10.5281/zenodo.21382362` (D67) |

D46 and D43 additionally deserve the relation **"is supplement to"** is *not* right — the correct extra relation for a document carrying errata is:

| Relation | DOI | Why |
|---|---|---|
| corrects (or, if unavailable in the form, "references") | `10.5281/zenodo.19956932` (D46) | Errata 1 and 2 |
| corrects (or "references") | `10.5281/zenodo.19678389` (D43) | Erratum 3 |

Zenodo's relation vocabulary does not always expose "corrects"; if it is absent, use "references" and rely on the errata being explicit in the text.

---

## 11. Community

```
pdl-framework
```

---

## 12. Licence

Match the rest of the corpus. If previous documents used **Creative Commons Attribution 4.0 International (CC BY 4.0)**, use the same.

---

## 13. Post-deposit checklist

1. Copy the new DOI into `10.5281zenodo.txt` with the block format used throughout:
   ```
   D68
   https://doi.org/10.5281/zenodo.XXXXXXXX
   The Pulsation as a Bipartition: Complete Classification of C1-Admissible Dynamical Laws, and a Singleton Obstruction Theorem for Frustration-Based Selection (Projective Dynamic Logo Framework — Document D68)
   D68_pulsation_bipartition.pdf
   ```
2. Fill the D68 DOI into `D69_references.bib`, which currently carries a placeholder in the `note` field of the `D68` entry, then recompile D69.
3. Update `PDL_context.md`: change the D68 line in the DOI index from *(à réserver)* to the actual DOI, and mark the Session 76 priority 1 as done.
4. Push the `.tex`, `.bib` and the five scripts to `laubscher-lab/PDL-framework`.
5. Update `cedriclaubscher.ch`.

---

## 14. Two registry discrepancies to settle (independent of this deposit)

- **DM v32.** The registry lists `21520303` against the title "Global Mapping … (Version 32)"; the working notes carried `21411025`. One of the two is wrong. Not cited in D68, so it does not block the deposit.
- **D42.** The registry lists `20041348` with the v1 title, while the source file in circulation is `D42v3`. Worth checking whether v3 was ever deposited.

---

## 15. What is deliberately published as unresolved

Stating this plainly so the decision is conscious rather than accidental:

- **OP-D68-1** — a second extremal family at n = 6 (30 classes of minimal gap against the 15 the single-negative-edge family accounts for) is unidentified. It does not affect Theorem 9.5, whose proof does not rely on identifying the extremal families.
- **OP-D68-7** — D46 defines the pulsation as the global edge reversal, D68 derives it as a switching; the two give different values for the ratio P₂/P₁, which feeds the (A)∧(B) criterion of D29 and thence D50 and D64. Publishing this states publicly that part of the corpus awaits clarification. That is the honest position, but it is a choice.
