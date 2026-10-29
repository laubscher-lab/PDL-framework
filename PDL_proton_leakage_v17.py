#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDL_proton_leakage_v17.py - Asymmetry audit of the valence cores (K28/K28/K24)
Question (user, 2026-10-29): the proton cores are canonically 28, 28, 24 relations.
Was the asymmetry preserved in v10-v16? (No - cores were 3 identical K4.)
V17 audits two declared readings:
  H_A: 28/28/24 = INTERNAL core relations  (structural)
  H_B: 28/28/24 = core->sea INTERFACE relations; internal stays K4 (6 each)
Frozen corpus constants: V_mer=918, E_mer=11017=23*479, n_u=930, 3 cores K4 (12 sites, 18 internal).
Targets (pre-registered, unchanged): gap B-528 = 0.35404759 +/- 7.7e-4 (v10 inversion);
f = 0.157126 +/- 9e-4; DeltaSigma = 0.30 +/- 0.05 (EMC).
Stdlib only, Colab-ready. EXIT=0 on completion.
"""
import json, math

sqrt2 = math.sqrt(2.0)
phi = (1.0 + math.sqrt(5.0)) / 2.0

V_MER, E_MER, N_U = 918, 11017, 930
GAP_T, GAP_TOL = 0.35404759, 7.7e-4
F_T, F_TOL = 0.157126, 9e-4
DS_T, DS_TOL = 0.30, 0.05

R = {}

# ---------- V17-A  parity theorem survival (T) ----------
R['V17-A_parity'] = {
    'E_mer': E_MER, 'odd': (E_MER % 2 == 1), 'factorization': '11017 = 23*479',
    'verdict': 'SURVIVES (T): asymmetry at the cores does not touch the sea count; monomer engine intact.'
}

# ---------- V17-B  H_A: internal reading ----------
def min_sites_for_edges(e):
    k = 1
    while k*(k-1)//2 < e:
        k += 1
    return k
k28 = min_sites_for_edges(28)   # 8  (C(8,2)=28)
k24 = min_sites_for_edges(24)   # 8  (C(7,2)=21 < 24)
core_sites = [k28, k28, k24]
tot_sites = sum(core_sites)
R['V17-B_HA'] = {
    'hypothesis': '28/28/24 internal relations per core',
    'min_sites_per_core': core_sites, 'total_core_sites': tot_sites,
    'consequence_1': 'max edges on 4 sites = C(4,2) = 6 < 24,28 -> impossible on K4 sites',
    'consequence_2': 'V_mer + core_sites = %d + %d = %d != n_u = %d, or forces V_mer = %d != 918' % (V_MER, tot_sites, V_MER+tot_sites, N_U, N_U - tot_sites),
    'also_kills': ['144 = 12^2 (f=144/917)', 'B = n_u(n_u-2) = 528', 'delta = 1/C(8,3) = 1/56'],
    'verdict': 'H_A FALSIFIED at fixed n_u=930 / V_mer=918 partition.'
}

# ---------- V17-C  H_B: interface reading ----------
I = [28, 28, 24]
S = sum(I)
pat21 = (I[0] == I[1] and I[2] != I[0])
R['V17-C_HB'] = {
    'hypothesis': '28/28/24 = core->sea interface relations; internal K4 (6 each) preserved',
    'sites_preserved': '918 + 12 = 930 ; 144 = 12^2 ; f = 144/917 survive unchanged',
    'pattern_2plus1': pat21, 'distinguished_core': 'd (24) ; two identical u (28) - the uud shape',
    'spin_reference_core': 'no longer a gauge choice: structurally identified with the d-core (D-level strengthening of v13 Euler localization)',
    'grand_total_relations': E_MER + 18 + S,  # 11115
    'core_associated': 18 + S                 # 98
}

# ---------- V17-D  T1 gap family (declared a priori, N=7, band = value range) ----------
gap_family = {
    '1/(2*sqrt2)': 1.0/(2.0*sqrt2),
    '28/80': 28.0/80.0,
    '24/80': 24.0/80.0,
    '24/76': 24.0/76.0,
    '28/84': 28.0/84.0,
    '24/68': 24.0/68.0,
    '28/72': 28.0/72.0,
}
lo, hi = min(gap_family.values()), max(gap_family.values())
lam = len(gap_family) * (2.0*GAP_TOL)/(hi-lo)
hits = {n: {'value': v, 'gap': abs(v-GAP_T), 'tol': abs(v-GAP_T)/GAP_TOL}
        for n, v in gap_family.items() if abs(v-GAP_T) <= GAP_TOL}
P = 1.0 - math.exp(-lam)  # Poisson P(>=1)
R['V17-D_T1_gap'] = {
    'family_N': len(gap_family), 'band': [lo, hi], 'poisson_lambda': lam,
    'target': GAP_T, 'tol': GAP_TOL, 'hits': hits,
    'P_at_least_1_given_null': P,
    'verdict': ('Only 1/(2*sqrt2) in window; 28/80=0.35 at %.2f tol -> the u-share does NOT replace the Euler diagonal cut.' % (abs(28/80.0-GAP_T)/GAP_TOL))
}

# ---------- V17-E  T2 closed fraction ----------
f_pred = 144.0/917.0
R['V17-E_T2_f'] = {'form': '144/917', 'value': f_pred, 'gap': abs(f_pred-F_T),
    'tol': abs(f_pred-F_T)/F_TOL,
    'verdict': 'UNCHANGED under H_B (sites preserved). PASS.'}

# ---------- V17-F  T3 DeltaSigma family (declared, N=4) ----------
ds_family = {'7/24': 7.0/24.0, '24/80': 24.0/80.0, '1/(2*phi)': 1.0/(2.0*phi), '28/80': 28.0/80.0}
ds_hits = {n: {'value': v, 'gap': abs(v-DS_T), 'tol': abs(v-DS_T)/DS_TOL}
           for n, v in ds_family.items() if abs(v-DS_T) <= DS_TOL}
chain = {'7/24': 'IN-chain (v16)', '24/80': 'IN-chain (interface counts, H_B)',
         '1/(2*phi)': 'OFF-chain (phi, excluded v16)', '28/80': 'IN-chain but 0.35 outside window'}
R['V17-F_T3_DeltaSigma'] = {
    'family_N': len(ds_family), 'window': [DS_T-DS_TOL, DS_T+DS_TOL],
    'hits': ds_hits, 'chain_status': chain,
    'key_finding': '24/80 = 3/10 EXACTLY (0.000 tol): the form v16 excluded as off-chain is now IN-chain via the interface counts; the asymmetry rehabilitates 3/10 structurally.',
    'ambiguity': 'two in-chain forms coexist: 24/80 (exact) vs 7/24 (0.167 tol); selection deferred (spin-surface map under H_B, v18).'
}

# ---------- V17-G  cross-coherence audit ----------
R['V17-G_cross'] = {
    'T1_pair': '(3,8) via delta=1/C(8,3) and gap 1/(2*sqrt2): survives (internal K4 + Euler unchanged)',
    'T3_pair': '(24,80) via 24/(28+28+24): NEW, structurally forced by the asymmetry',
    'f': '144/917: survives',
    'note': 'asymmetry does NOT extend cross-coherence to T1 (28/80 at 5.26 tol) - honest negative.'
}

# ---------- V17-H  verdicts & next step ----------
R['V17-H_verdicts'] = {
    'H_A': 'FALSIFIED',
    'H_B': 'VIABLE and strengthening: preserves every v10-v16 integer result AND the T3 exact form',
    'asymmetry_status': 'rehabilitated as INTERFACE structure (2+1, d distinguished) - matches Turn-20 optimistic reading for T3, not for the T1 gap',
    'next': 'v18: rebuild the full wake census with interface 28/28/24 shared across cores; test whether B=528 survives weighting by interface shares and whether the diagonal-cut fraction coexists with 28/28/24; select 24/80 vs 7/24 via spin-surface map.'
}

with open('/workspace/v17_summary.json', 'w') as fh:
    json.dump(R, fh, indent=2)
print(json.dumps(R, indent=2))
print('EXIT=0')
