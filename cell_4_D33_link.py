# ============================================================
# D66 -- CELLULE 4 / 4
# Verification symbolique du lien avec D33: confirmer que la
# distinction "cycle1=classique (carre=+1), cycle2=type-spin
# (carre=-1)" correspond exactement aux operateurs deja construits
# et prouves dans D33 (tau_3 pour gamma^0, T=i*tau_2 pour gamma^i).
# Cellule autonome (sympy).
# ============================================================
import sympy as sp

I2 = sp.eye(2)
tau1 = sp.Matrix([[0, 1], [1, 0]])
tau2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
tau3 = sp.Matrix([[1, 0], [0, -1]])

T = sp.I * tau2   # operateur de pulsation, D33

print("Verification des carres (doit correspondre a D33):")
print("  tau_3^2 =")
sp.pprint(sp.simplify(tau3*tau3))
print("  -> carre = +I : c'est l'operateur 'classique' (cycle 1, condition A)")
print()
print("  T^2 = (i*tau_2)^2 =")
sp.pprint(sp.simplify(T*T))
print("  -> carre = -I : c'est l'operateur 'type-spin' (cycle 2, condition B)")

assert sp.simplify(tau3*tau3 - I2) == sp.zeros(2), "ECHEC: tau_3^2 != I"
assert sp.simplify(T*T + I2) == sp.zeros(2), "ECHEC: T^2 != -I"

print()
print("="*70)
print("CONFIRME: la distinction cycle1(carre+1)/cycle2(carre-1) utilisee")
print("dans la resolution de l'obstruction de parite (cellule 3) n'est")
print("PAS un artifice ad hoc -- ce sont exactement tau_3 (D33, construit")
print("pour gamma^0) et T=i*tau_2 (D33, construit pour gamma^i).")
print("="*70)

print()
print("Rappel du role de ces operateurs dans D33 (pour la redaction):")
print("  gamma^0 = tau_3 (x) I_2   -- carre +1, direction 'temporelle'")
print("  gamma^i = T (x) sigma_i   -- carre -1, direction 'spatiale'")
print("  Cette meme dichotomie +1/-1 est ce qui resout l'obstruction ici.")
