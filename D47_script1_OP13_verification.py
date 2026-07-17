"""
D47_script1_OP13_verification.py
=============================================================================
Verification independante d'OP13 (D47, Theorem OP13) :

  L'equation de quasi-completude 3*n_u^2 + (2*Delta_n-3)*n_u
  + Delta_n*(Delta_n-1) - 1860 = 0 a un discriminant (en n_u) qui est un
  carre parfait UNIQUEMENT pour Delta_n = 4, parmi Delta_n in {0,4,...,32},
  et vaut alors 149^2 = 22201.

Ce script ne depend d'aucune donnee externe. A executer tel quel dans
Colab ou en local.

Statut de ce script : verification de premier passage, independante du
corpus. N'engage aucune modification du corpus tant que Cedric n'a pas
relu ce resultat.
=============================================================================
"""

import math

def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n

print("Verification d'OP13 : unicite de Delta_n = 4")
print("=" * 70)
print(f"{'Delta_n':>8} {'discriminant':>14} {'carre parfait ?':>17} {'racine':>8}")

results = []
for delta_n in range(0, 33, 4):
    a, b, c = 3, (2 * delta_n - 3), delta_n * (delta_n - 1) - 1860
    disc = b * b - 4 * a * c
    sq = is_perfect_square(disc)
    root = math.isqrt(disc) if disc >= 0 else None
    results.append((delta_n, disc, sq, root))
    print(f"{delta_n:>8} {disc:>14} {str(sq):>17} {str(root) if sq else '-':>8}")

squares = [r for r in results if r[2]]
print()
print(f"Nombre de solutions carrees parfaites : {len(squares)}")
if len(squares) == 1:
    dn, disc, _, root = squares[0]
    print(f"Solution unique : Delta_n = {dn}, discriminant = {disc} = {root}^2")
    if dn == 4 and root == 149:
        print("CONCLUSION : conforme a l'enonce de D47 (Delta_n=4, racine=149).")
        print("OP13 : CONFIRME par verification independante.")
    else:
        print("ATTENTION : la solution unique ne correspond pas exactement a "
              "l'enonce de D47 (attendu Delta_n=4, racine=149). A verifier.")
else:
    print("ATTENTION : plusieurs solutions ou aucune solution carree parfaite "
          "trouvee. Ceci contredirait l'enonce de D47 -- a verifier en priorite "
          "avant toute publication d'errata sur ce point.")

print()
print("Valeur induite du splitting spin-orbite s = Delta_n / (2*n_u), avec "
      "n_u = 24 (force separement par la contrainte C2 et la table du "
      "quintuplet du proton -- non re-derive ici) :")
if len(squares) == 1 and squares[0][0] == 4:
    s = 4 / (2 * 24)
    from fractions import Fraction
    print(f"s = 4/48 = {Fraction(4, 48)} = {s}")
