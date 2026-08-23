#!/usr/bin/env python3
# =====================================================================
# D05v2_script1_errata.py
#
# Lockdown script for PDL document D05, version 2:
#   "A Minimal Relational Sketch for the Emergence of the Golden Ratio
#    in PDL (Version 2 - corrected)"
#
# Purpose: independently verify the four errata E1-E4 recorded in
# Section 6 of D05 v2, and verify that the corrected self-similarity
# condition of Section 4 reproduces R_surf = 310*phi exactly.
#
# Every numerical claim made in D05 v2 is recomputed here. Nothing is
# taken from the corpus without being recomputed, and no result of this
# script depends on the Blender realisation.
#
# Dependencies: mpmath (50 decimal places), sympy (exact symbolic).
# Run: python3 D05v2_script1_errata.py
#
# Author: Cedric Laubscher (ORCID 0009-0004-5415-1098)
# PDL framework - https://github.com/laubscher-lab/PDL-framework
# =====================================================================

from math import comb
import mpmath as mp
import sympy as sp

mp.mp.dps = 50

phi = (1 + mp.sqrt(5)) / 2

# ---------------------------------------------------------------------
# Inputs: theorems of C1-C4 only (D16, D16a). Nothing else is assumed.
# ---------------------------------------------------------------------
n_u, n_d = 24, 28
r_u = comb(n_u, 2)              # 276
r_d = comb(n_d, 2)              # 378
r_val = 2 * r_u + r_d           # 930
R_sea = 10087
R_tot = r_val + R_sea           # 11017
r_core = mp.mpf(r_val) / 3      # 310
mu_pe = mp.mpf('1836.15267343')  # proton-electron mass ratio, CODATA
alpha_inv_codata = mp.mpf('137.035999177')

TARGET = 310 * phi               # the value used throughout the corpus

BAR = "=" * 70


def check(label, condition, detail=""):
    condition = bool(condition)   # sympy Booleans -> Python bool
    print(("  PASS  " if condition else "  FAIL  ") + label
          + (("   | " + detail) if detail else ""))
    return condition


results = []

# ---------------------------------------------------------------------
print(BAR)
print("0. INPUTS (theorems of C1-C4; recomputed, not quoted)")
print(BAR)
results.append(check("r_u = C(24,2) = 276", r_u == 276, str(r_u)))
results.append(check("r_d = C(28,2) = 378", r_d == 378, str(r_d)))
results.append(check("r_val = 2*r_u + r_d = 930", r_val == 930, str(r_val)))
results.append(check("R_tot = r_val + R_sea = 11017", R_tot == 11017, str(R_tot)))
results.append(check("r_core = r_val/3 = 310 (exact integer)",
                     r_val % 3 == 0 and r_core == 310, mp.nstr(r_core, 6)))
print(f"  target value used by the corpus: R_surf = 310*phi = "
      f"{mp.nstr(TARGET, 12)}")
print()

# ---------------------------------------------------------------------
print(BAR)
print("E1. DERIVATIVE OF THE TRADE-OFF FUNCTIONAL (D05 v2, Section 3)")
print(BAR)
x, a, b = sp.symbols('x a b', positive=True)
Q = a * x + b / x                      # Q as defined: a*(Rcore/Rsurf) + b*(Rsurf/Rcore)
dQ = sp.simplify(sp.diff(Q, x))
d2Q = sp.simplify(sp.diff(Q, x, 2))
root = sp.solve(sp.Eq(dQ, 0), x)[0]

print("  Definition in D05:  Q = a*(R_core/R_surf) + b*(R_surf/R_core)")
print("  With x = R_core/R_surf, this is  Q(x) = a*x + b/x")
print(f"  Correct derivative       dQ/dx = {dQ}")
print(f"  Correct stationary point x     = {root},  so x^2 = b/a")
print(f"  Second derivative        d2Q   = {d2Q}   -> positive for x,b > 0")
print()
print("  Version 1 wrote:  dQ/dx = -a/x^2 + b = 0  =>  x^2 = a/b")
Q_v1 = a / x + b * x
print(f"  That is the derivative of a/x + b*x, i.e. Q with a and b "
      f"interchanged: {sp.simplify(sp.diff(Q_v1, x))}")
results.append(check("E1 confirmed: v1 stationary point x^2 = a/b is wrong; "
                     "correct is x^2 = b/a",
                     sp.simplify(root**2 - b / a) == 0))
results.append(check("E1 second part: stationary point is a MINIMUM, "
                     "so Q is a cost, not a reward",
                     sp.simplify(d2Q.subs({b: 1, x: 1})) > 0))
print("  Note: a*x + b/x diverges at both ends of (0, inf) and has no")
print("  maximum, so the functional admits no reading as a quantity to")
print("  be maximised.")
print()

# ---------------------------------------------------------------------
print(BAR)
print("E2. PREMATURE DECOMPOSITION (D05 v2, Section 2)")
print(BAR)
print("  Version 1 Section 1 posited:  R_tot = R_core + R_surf + R_sea")
print("  Corpus (D16a):                R_tot = r_val  + R_sea = 11017")
print("  The first requires R_core + R_surf = r_val = 930 exactly.")
sum_cs = r_core + TARGET
residual = mp.mpf(r_val) - sum_cs
print(f"  Under the corrected identification (R_core = 310):")
print(f"     R_core + R_surf = {mp.nstr(sum_cs, 12)}   vs r_val = 930")
print(f"     shortfall       = {mp.nstr(residual, 12)}")
print(f"     310/phi^2       = {mp.nstr(310 / phi**2, 12)}")
results.append(check("E2 confirmed: R_core + R_surf != r_val",
                     abs(sum_cs - r_val) > mp.mpf('1e-6')))
results.append(check("shortfall equals 310/phi^2 exactly",
                     abs(residual - 310 / phi**2) < mp.mpf('1e-40')))
three_way = 310 * phi + 310 + 310 / phi**2
print(f"  Three-way decomposition: 310*(phi + 1 + phi^-2) = "
      f"{mp.nstr(three_way, 20)}")
results.append(check("three-way decomposition equals r_val = 930 exactly",
                     abs(three_way - 930) < mp.mpf('1e-40')))
print("  Proof: phi^-2 = 2 - phi, hence phi + 1 + (2 - phi) = 3. QED")
results.append(check("identity phi^-2 = 2 - phi",
                     abs(1 / phi**2 - (2 - phi)) < mp.mpf('1e-45')))
print()

# ---------------------------------------------------------------------
print(BAR)
print("E3 / E4. ORIENTATION AND IDENTIFICATION (D05 v2, Sections 4-5)")
print(BAR)
print("  The algebra of D05 v1 is CORRECT and is verified first.")
lam = mp.findroot(lambda t: t / (t + 1) - 1 / t, mp.mpf('1.5'))
results.append(check("self-similarity gives lambda^2 = lambda + 1, "
                     "lambda = phi",
                     abs(lam - phi) < mp.mpf('1e-40'), mp.nstr(lam, 15)))
Rs_unit = mp.mpf(1)
Rc_unit = phi * Rs_unit
results.append(check("corollary R_surf/R'_tot = 1/phi^2",
                     abs(Rs_unit / (Rc_unit + Rs_unit) - 1 / phi**2)
                     < mp.mpf('1e-40')))
print("  -> the error of v1 is NOT in the algebra but in the connection.")
print()

print("  Four combinations of orientation and identification:")
print(f"  {'variant':>52s} {'R_surf':>13s} {'= target?':>10s}")
variants = [
    ("v1 as written: R_core=930, R_surf=R_core/phi", mp.mpf(r_val) / phi),
    ("orientation fixed only: R_core=930, R_surf=phi*R_core", phi * r_val),
    ("identification fixed only: R_core=310, R_surf=R_core/phi", r_core / phi),
    ("BOTH fixed: R_core=310, R_surf=phi*R_core", phi * r_core),
]
n_hit = 0
for name, val in variants:
    hit = abs(val - TARGET) < mp.mpf('1e-40')
    n_hit += hit
    print(f"  {name:>52s} {mp.nstr(val, 10):>13s} {str(hit):>10s}")
results.append(check("E3+E4 confirmed: exactly one combination reproduces "
                     "310*phi, and it requires BOTH corrections",
                     n_hit == 1 and abs(variants[3][1] - TARGET)
                     < mp.mpf('1e-40')))
print()

# ---------------------------------------------------------------------
print(BAR)
print("CORRECTED CONDITION, VERIFIED EXACTLY (D05 v2, Eq. 4)")
print(BAR)
R_core = r_core
R_surf = phi * R_core
Rp_tot = R_core + R_surf
lhs = R_surf / Rp_tot
rhs = R_core / R_surf
print("  Condition:  R_surf / R'_tot = R_core / R_surf,  "
      "R'_tot = R_core + R_surf")
print(f"     R_core = {mp.nstr(R_core, 12)}")
print(f"     R_surf = {mp.nstr(R_surf, 12)}")
print(f"     R'_tot = {mp.nstr(Rp_tot, 12)}   ( = 310*phi^2 )")
print(f"     R_surf/R'_tot = {mp.nstr(lhs, 25)}")
print(f"     R_core/R_surf = {mp.nstr(rhs, 25)}")
results.append(check("the two ratios are equal to 40 decimal places",
                     abs(lhs - rhs) < mp.mpf('1e-40')))
results.append(check("common value equals 1/phi",
                     abs(lhs - 1 / phi) < mp.mpf('1e-40'), mp.nstr(1 / phi, 15)))
results.append(check("R'_tot = 310*phi^2",
                     abs(Rp_tot - 310 * phi**2) < mp.mpf('1e-40')))
print()

# ---------------------------------------------------------------------
print(BAR)
print("NUMERICAL CONSEQUENCES (D05 v2, Sections 6-7)")
print(BAR)
print(f"  {'variant':>22s} {'R_surf':>13s} {'alpha^-1':>13s} {'kappa':>14s}")
for name, Rs in [("v1 as written", mp.mpf(r_val) / phi),
                 ("v2 corrected", TARGET)]:
    print(f"  {name:>22s} {mp.nstr(Rs, 10):>13s} "
          f"{mp.nstr(Rs**2 / mu_pe, 9):>13s} {mp.nstr(Rs / R_tot, 10):>14s}")
print(f"  {'CODATA':>22s} {'':>13s} {mp.nstr(alpha_inv_codata, 9):>13s}")
a_inv_v2 = TARGET**2 / mu_pe
a_inv_v1 = (mp.mpf(r_val) / phi)**2 / mu_pe
rel = 100 * (a_inv_v2 - alpha_inv_codata) / alpha_inv_codata
print(f"  relative deviation of the corrected value: {mp.nstr(rel, 6)} %")
results.append(check("v1 value is incompatible with CODATA (>30% off)",
                     abs(a_inv_v1 - alpha_inv_codata)
                     / alpha_inv_codata > mp.mpf('0.3')))
results.append(check("v2 value agrees with CODATA to better than 0.02%",
                     abs(rel) < mp.mpf('0.02')))
print()

print("  Remark 1 of D05 v2: no integer value of R_surf reproduces alpha.")
for v in (501, 502):
    print(f"     R_surf = {v}  ->  alpha^-1 = "
          f"{mp.nstr(mp.mpf(v)**2 / mu_pe, 9)}")
results.append(check("neither 501 nor 502 reproduces CODATA to 0.02%",
                     all(abs(100 * (mp.mpf(v)**2 / mu_pe - alpha_inv_codata)
                             / alpha_inv_codata) > mp.mpf('0.02')
                         for v in (501, 502))))
kappa = TARGET / R_tot
print(f"  kappa = 310*phi/11017 = {mp.nstr(kappa, 12)}")
print()

# ---------------------------------------------------------------------
print(BAR)
print(f"SUMMARY: {sum(results)} / {len(results)} checks passed")
print(BAR)
if all(results):
    print("  All errata of Section 6 are confirmed, and the corrected")
    print("  condition of Section 4 reproduces R_surf = 310*phi exactly.")
else:
    print("  AT LEAST ONE CHECK FAILED - do not deposit without resolving.")
print()
print("  NOTE ON EPISTEMIC STATUS. This script verifies that the corrected")
print("  self-similarity condition is CONSISTENT with R_surf = 310*phi.")
print("  It does NOT derive that condition from axioms C1-C4, and it does")
print("  NOT establish the orientation of the golden section. R_surf")
print("  remains the named hypothesis H-phi. See OP-Hphi-1 to OP-Hphi-4.")
