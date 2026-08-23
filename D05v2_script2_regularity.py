#!/usr/bin/env python3
# =====================================================================
# D05v2_script2_regularity.py
#
# Lockdown script for PDL document D05, version 2, Remark 4
# ("A candidate regularity criterion, post hoc").
#
# Purpose: verify the three arithmetical claims made in that remark:
#   (i)   under the adopted orientation, the three parts of r_val are
#         integer powers of phi times the mean core, exponents (1,0,-2);
#         under the opposite orientation they are not;
#   (ii)  imposing the form x + 1 + x^-2 = 3 forces x = phi, apart from
#         the degenerate root x = 1;
#   (iii) among integer triples with -12 <= c < b < a <= 12 satisfying
#         phi^a + phi^b + phi^c = 3, exactly two occur, and the second
#         is excluded because none of its parts equals the mean core.
#
# IMPORTANT. This script verifies arithmetic only. The criterion it
# tests was formulated AFTER the target value was known. It carries no
# evidential weight and is recorded in D05 v2 as a lead, not as proof.
# See OP-Hphi-2.
#
# Dependencies: mpmath (50 decimal places), sympy (exact symbolic).
# Run: python3 D05v2_script2_regularity.py
#
# Author: Cedric Laubscher (ORCID 0009-0004-5415-1098)
# PDL framework - https://github.com/laubscher-lab/PDL-framework
# =====================================================================

import mpmath as mp
import sympy as sp

mp.mp.dps = 50
phi = (1 + mp.sqrt(5)) / 2
r_val = mp.mpf(930)
r_core = r_val / 3               # 310
TOL = mp.mpf('1e-35')

BAR = "=" * 70
results = []


def check(label, condition, detail=""):
    print(("  PASS  " if condition else "  FAIL  ") + label
          + (("   | " + detail) if detail else ""))
    return condition


def phi_exponent(value):
    """Return the exponent k such that value = r_core * phi^k, and
    whether k is an integer."""
    ratio = value / r_core
    k = mp.log(ratio) / mp.log(phi)
    return k, abs(k - mp.nint(k)) < mp.mpf('1e-30')


# ---------------------------------------------------------------------
print(BAR)
print("(i) THE THREE PARTS OF r_val, UNDER BOTH ORIENTATIONS")
print(BAR)
print("  r_val = 930 = 3 * 310 (three valence cores; theorem, D43).")
print("  The self-similarity condition fixes R_core and R_surf;")
print("  the residual is then determined: R_res = r_val - R_core - R_surf.")
print()

orientations = [
    ("A  surface is the LARGER part (adopted in D05 v2)", phi * r_core),
    ("B  surface is the smaller part (D05 v1)", r_core / phi),
]

integer_flags = {}
for name, R_surf in orientations:
    R_core = r_core
    R_res = r_val - R_core - R_surf
    print(f"  {name}")
    all_int = True
    for label, value in (("R_surf", R_surf), ("R_core", R_core),
                         ("R_res ", R_res)):
        k, is_int = phi_exponent(value)
        all_int &= is_int
        print(f"     {label} = {mp.nstr(value, 12):>14s}   "
              f"= 310 * phi^({mp.nstr(k, 8)})   integer exponent: {is_int}")
    integer_flags[name[0]] = all_int
    print(f"     -> all three exponents integer: {all_int}")
    print()

results.append(check("orientation A: all three exponents are integers",
                     integer_flags['A']))
results.append(check("orientation B: NOT all exponents are integers",
                     not integer_flags['B']))
results.append(check("orientation A exponents are exactly (1, 0, -2)",
                     all(abs(phi_exponent(v)[0] - e) < mp.mpf('1e-30')
                         for v, e in ((phi * r_core, 1), (r_core, 0),
                                      (r_val - r_core - phi * r_core, -2)))))
print("  Exact identity: phi^1 + phi^0 + phi^-2 = phi + 1 + (2 - phi) = 3,")
print("  since phi^-2 = 2 - phi. Hence 310 * 3 = 930. QED")
lhs = phi**1 + phi**0 + phi**-2
results.append(check("phi^1 + phi^0 + phi^-2 = 3 to 40 decimal places",
                     abs(lhs - 3) < mp.mpf('1e-40'), mp.nstr(lhs, 25)))
print()

# ---------------------------------------------------------------------
print(BAR)
print("(ii) DOES THE FORM x + 1 + x^-2 = 3 FORCE x = phi?")
print(BAR)
x = sp.symbols('x')
eq = sp.Eq(x + 1 + 1 / x**2, 3)
poly = sp.simplify(sp.expand(x**3 - 2 * x**2 + 1))
print(f"  x + 1 + 1/x^2 = 3   <=>   x^3 - 2x^2 + 1 = 0")
print(f"  factorisation: {sp.factor(poly)}")
roots = sp.solve(poly, x)
print("  roots:")
for r in roots:
    rv = complex(sp.N(r, 30))
    print(f"     {sp.simplify(r)}   =  {rv.real:.15f}")
gold = [r for r in roots if abs(complex(sp.N(r, 30)).real
                                - float(phi)) < 1e-12]
results.append(check("the polynomial factors as (x-1)(x^2-x-1)",
                     sp.simplify(sp.factor(poly)
                                 - (x - 1) * (x**2 - x - 1)) == 0))
results.append(check("phi is a root", len(gold) == 1))
above_one = [r for r in roots
             if complex(sp.N(r, 30)).real > 1.0000001]
results.append(check("phi is the ONLY root exceeding unity",
                     len(above_one) == 1
                     and abs(complex(sp.N(above_one[0], 30)).real
                             - float(phi)) < 1e-12))
print("  x = 1 is the degenerate uniform partition (three equal parts).")
print()

# ---------------------------------------------------------------------
print(BAR)
print("(iii) ISOLATION TEST: INTEGER TRIPLES WITH phi^a + phi^b + phi^c = 3")
print(BAR)
LO, HI = -12, 12
sols = []
for a in range(LO, HI + 1):
    for b in range(LO, a):
        for c in range(LO, b):
            if abs(phi**a + phi**b + phi**c - 3) < TOL:
                sols.append((a, b, c))
n_tested = sum(1 for a in range(LO, HI + 1)
               for b in range(LO, a) for c in range(LO, b))
print(f"  Range: {LO} <= c < b < a <= {HI}   ({n_tested} ordered triples)")
print(f"  Solutions found: {sols}")
results.append(check("exactly two integer triples satisfy the identity",
                     len(sols) == 2))
results.append(check("(1, 0, -2) is among them", (1, 0, -2) in sols))
print()
print("  Parts generated by each solution (in units of 310):")
for t in sols:
    parts = [310 * phi**e for e in t]
    has_core = any(abs(p - 310) < mp.mpf('1e-30') for p in parts)
    print(f"     {str(t):>12s} -> "
          f"({', '.join(mp.nstr(p, 8) for p in parts)})"
          + ("   contains the mean core 310"
             if has_core else "   NO part equals the mean core 310"))
excluded = [t for t in sols if 0 not in t]
results.append(check("the second solution contains no part equal to 310, "
                     "and is therefore excluded by the corpus definition "
                     "of the mean core",
                     len(excluded) == 1 and excluded[0] != (1, 0, -2)))
results.append(check("under the constraint that one part equals the mean "
                     "core, (1,0,-2) is unique in this range",
                     [t for t in sols if 0 in t] == [(1, 0, -2)]))
print()

# ---------------------------------------------------------------------
print(BAR)
print(f"SUMMARY: {sum(results)} / {len(results)} checks passed")
print(BAR)
if all(results):
    print("  All three arithmetical claims of Remark 4 are confirmed.")
else:
    print("  AT LEAST ONE CHECK FAILED - do not deposit without resolving.")
print()
print("  NOTE ON EPISTEMIC STATUS. The regularity criterion tested here")
print("  was formulated after the target value 310*phi was known. It is")
print("  NOT derived from axioms C1-C4 and does NOT establish the")
print("  orientation of the golden section independently. It is recorded")
print("  in D05 v2 as a lead only. Establishing or refuting it is")
print("  OP-Hphi-2. Furthermore, R_res = 310/phi^2 is defined by")
print("  subtraction and has no relational interpretation in the corpus;")
print("  see OP-Hphi-3.")
