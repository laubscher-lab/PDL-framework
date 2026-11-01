#!/usr/bin/env python3
"""D72e - sealed predictive pipeline (no measured-G input) + external arbiter.
Reproduces the v53/v54 frozen prediction of the campaign v25-v54."""
import hashlib, json, math

# ---- Sealed predictive block: permitted inputs only ----
# (declared structure, exact constants h and c, measured proton mass m_p)
# FORBIDDEN inside this block: G_CODATA, measured alpha_G, epsilon_rung, delta_rung
alpha_inv = 137 + 33/917          # declared structural form (+0.09 ppm vs CODATA)
alpha = 1/alpha_inv
N = 18                            # rungs of the declared structure
x = 7/12                          # three independent a priori geometric routes (G1, G2, G3)
chord = 2*(1 - math.cos(math.pi/N))   # chord closure, 18 rungs
arc = (math.pi/N)**2                  # arc closure, 18 rungs
delta = (1-x)*chord + x*arc           # 3.04295555 %% bounded by the two closures
eps = alpha*(1+delta)
alpha_G = eps**N
HBAR = 1.054571817e-34            # from exact h
C = 299792458.0                   # exact
MP = 1.67262192369e-27            # measured proton mass
G_pred = alpha_G * HBAR * C / MP**2

predictions = {
  "alpha_inv": alpha_inv,
  "delta_pct": 100*delta,
  "epsilon": eps,
  "alpha_G": alpha_G,
  "G_pred": G_pred,
}
fp = hashlib.sha256(json.dumps(predictions, sort_keys=True).encode()).hexdigest()[:16]

# ---- External arbiter (admitted only after freezing) ----
G_CODATA = 6.67430e-11
ppm = (G_pred/G_CODATA - 1)*1e6
out = dict(predictions)
out.update({"fingerprint": fp, "G_CODATA_arbiter": G_CODATA,
            "arbiter_ppm": ppm, "arbiter_sigma": abs(ppm)/22.0})
print(json.dumps(out, indent=2))
