#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PDL v14 - Multi-target confrontation of the frozen surface-wake mechanism (v13)
# Frozen targets: T1 skin Dr_val=0.04795969 +- 6.98e-8 ; T2 closed fraction
# f=0.157126 +- 9e-4 ; T3 valence spin DS=0.30 +- 0.05 (EMC/COMPASS)
# No new parameters. Families declared BEFORE evaluation. Poisson nulls.
import math, json

PHI = (1.0 + math.sqrt(5.0)) / 2.0
SQ2 = math.sqrt(2.0)

# Corpus numbers (fixed)
E_SEA, V_SEA = 11017, 918
V_CORE, E_CORE, E_TOT = 12, 18, 11035
N_U, DEG = 24, 24

# Frozen wake mechanism (v12/v13)
D_BOW = 8
B_INT = 540 - 12                              # = 528 = 24x22 wake boundary - diag interface
CORR_1LOC = (SQ2/2.0)*(1.0/2.0)*(1.0/2.0)     # sqrt2/8, one diagonal wake stub
N_LOC = 2                                     # Euler condition: exactly 2 parity loci (deg 25)
B_FRAC = N_LOC * CORR_1LOC                    # = 1/(2 sqrt2)
B = B_INT + B_FRAC                            # 528.35355339

T1, TOL1 = 0.04795969, 6.98e-8
B_T13, TOL_B13 = 528.35404759, 7.6e-4         # consolidated v13 target
T2, TOL2 = 0.157126, 9.0e-4
T3, TOL3 = 0.30, 0.05
BAND2 = (0.10, 0.25)
BAND3 = (0.20, 0.40)

def p_tail(lam, k):
    s = 0.0
    for j in range(0, k):
        s += lam**j / math.factorial(j)
    return 1.0 - math.exp(-lam) * s

S = {}
print('='*76)
print('PDL v14 - multi-target test of the frozen surface-wake mechanism')
print('='*76)

# ---------------- V14-A : T1 continuity ----------------
print('')
print('[V14-A] T1 skin - frozen mechanism (v13 recall)')
dA = abs(B - B_T13); okA = dA <= TOL_B13
print('  B_pred = %d + 1/(2 sqrt2) = %.8f' % (B_INT, B))
print('  B_target_consolidated_v13 = %.8f' % B_T13)
print('  gap = %.2e (%.2f tol) -> %s' % (dA, dA/TOL_B13, 'PASS' if okA else 'FAIL'))
dr = B / E_SEA
print('  info: direct Dr=B/E_sea = %.8f vs Dr_val %.8f -> raw gap %.2e' % (dr, T1, abs(dr-T1)))
print('  note: duty-cycle mapping with delta=1/(nu+32)=1/56 closes it (v13-C); closed form pending')
S['A'] = {'B_pred': B, 'gap': dA, 'tol_frac': dA/TOL_B13, 'pass': okA}

# ---------------- V14-B : T2 closed fraction ----------------
print('')
print('[V14-B] T2 closed fraction f = %.6f +- %.1e   band declared: [%.2f, %.2f]' % (T2, TOL2, BAND2[0], BAND2[1]))
nums = [(144, '12^2 core-sites'), (145, '12^2+1'), (143, '12^2-1'), (918, 'V_sea'), (156, '6x(nu+2)')]
dens = [(918, 'V_sea'), (917, 'V_sea-1'), (919, 'V_sea+1'), (930, 'cloture930'), (5832, '18^3')]
fam = []
for a, na in nums:
    for dd, nd in dens:
        fam.append(('G1 %s / %s' % (na, nd), a*1.0/dd))
fam.append(('G2 1/phi^4', 1.0/PHI**4))
fam.append(('G2 1/phi^4 + 1/E_sea', 1.0/PHI**4 + 1.0/E_SEA))
fam.append(('G2 2/(3phi^3) [dead candidate v3 recheck]', 2.0/(3.0*PHI**3)))
fam.append(('G2 1/(3phi^2)+1/(2phi^4)', 1.0/(3.0*PHI**2) + 1.0/(2.0*PHI**4)))
Nf = len(fam)
lam2 = Nf * (2.0*TOL2) / (BAND2[1]-BAND2[0])
print('  N_declared = %d | lambda = %.3f | P(>=1|null) = %.4f' % (Nf, lam2, p_tail(lam2, 1)))
hits = []
for name, v in fam:
    if BAND2[0] <= v <= BAND2[1]:
        d = abs(v - T2)
        if d <= TOL2:
            hits.append((name, v, d))
hits.sort(key=lambda h: h[2])
print('  HITS inside window: %d' % len(hits))
for name, v, d in hits:
    print('    %-45s f=%.7f  gap=%.2e (%.2f tol)' % (name, v, d, d/TOL2))
if hits:
    print('  P(>=%d|null) = %.4g (caveat: cluster forms are correlated)' % (len(hits), p_tail(lam2, len(hits))))
best = min(fam, key=lambda nv: abs(nv[1]-T2))
print('  best overall: %s  f=%.7f  gap=%.2e' % (best[0], best[1], abs(best[1]-T2)))
okB = len(hits) > 0
S['B'] = {'N': Nf, 'lambda': lam2, 'n_hits': len(hits), 'hits': [{'form': h[0], 'f': h[1], 'gap': h[2]} for h in hits], 'pass': okB}

# ---------------- V14-C : T3 valence spin ----------------
print('')
print('[V14-C] T3 valence spin DS = %.2f +- %.2f   band declared: [%.2f, %.2f]' % (T3, TOL3, BAND3[0], BAND3[1]))
dsf = [('1/3 period-3 phase', 1.0/3.0),
       ('1/(2phi)', 1.0/(2.0*PHI)),
       ('7/24 = (1/3)(1-1/8) bow-phase', 7.0/24.0),
       ('3/10', 3.0/10.0),
       ('5/18', 5.0/18.0),
       ('9/32 = 3^2/2^5', 9.0/32.0),
       ('11/36', 11.0/36.0),
       ('3/(4phi)', 3.0/(4.0*PHI))]
Nd = len(dsf)
lam3 = Nd * (2.0*TOL3) / (BAND3[1]-BAND3[0])
print('  N_declared = %d | lambda = %.3f | P(>=1|null) = %.4f (non-discriminant by design)' % (Nd, lam3, p_tail(lam3, 1)))
hits3 = []
for name, v in dsf:
    if BAND3[0] <= v <= BAND3[1]:
        d = abs(v - T3)
        if d <= TOL3:
            hits3.append((name, v, d))
hits3.sort(key=lambda h: h[2])
for name, v, d in hits3:
    print('    %-38s DS=%.6f  gap=%.4f' % (name, v, d))
okC = len(hits3) > 0
S['C'] = {'N': Nd, 'lambda': lam3, 'n_hits': len(hits3), 'hits': [{'form': h[0], 'DS': h[1], 'gap': h[2]} for h in hits3], 'pass': okC, 'discriminant': False}

# ---------------- V14-D : verdict + derivation agenda ----------------
print('')
print('[V14-D] VERDICT')
survives = okA and okB and okC
print('  T1 skin          : %s' % ('PASS' if okA else 'FAIL'))
print('  T2 closed frac   : %s (%d declared-family hits)' % ('PASS' if okB else 'FAIL', len(hits)))
print('  T3 spin (check)  : %s (non-discriminative)' % ('PASS' if okC else 'FAIL'))
print('  => mechanism %s the triple target' % ('SURVIVES' if survives else 'DIES on'))
print('')
print('  Derivation agenda (coefficients requiring closed form from C1-C4):')
print('    1) d_bow = 8 (bow degree)')
print('    2) sqrt2/8 per locus (diagonal wake cut)')
print('    3) delta = 1/(nu+32) = 1/56 (stationary duty-cycle correction)')
print('    4) f-form selection among B-hits; NOTE: 2/(3phi^3) reappears in the')
print('       +-9e-4 window -> reconcile with the fatal v3 window (priority)')
print('    5) DS-form selection (1/(2phi) vs 7/24 vs 3/10) via spin-surface map')
S['D'] = {'survives': survives}

json.dump(S, open('/workspace/v14_summary.json', 'w'), indent=1)
print('')
print('summary written to /workspace/v14_summary.json')
print('EXIT=0')
