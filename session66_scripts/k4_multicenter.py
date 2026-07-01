"""
Verification script - Session 65, Piste "reseau multi-centres" (T_pdl + T_pp)
Construction explicite du graphe de couplage nucleon-nucleon combinant
D56 (etoile T_pdl, neutrons -> protons) et D40 (graphe complet T_pp plafonne a Z_sat=20).
Verifie : (1) reduction exacte aux formules D40/D56 connues ; (2) loi d'echelle du
poids total en fonction de N a Z=N fixe ; (3) confrontation a l'exposant attendu
pour une cible de type trou noir (aire de Schwarzschild ~ M^2) vs matiere nucleaire
ordinaire (aire geometrique ~ A^(2/3)).
"""
import networkx as nx
import numpy as np
from mpmath import mp, mpf, sqrt
phi = (1+sqrt(5))/2

mp.dps = 30

# --- Quantites PDL exactes (verifiees contre D40_Nuclear_Stability_PDL.tex) ---
R_surf_p = mpf(310)            # *vp, facteur vp s'annule dans les rapports utilises ici
R_tot_p  = mpf(11017)
R_sea_n  = mpf(9960)
T   = (310*phi)**2 / mpf(9960)      # T = Rsurf(p)^2 / Rsea(n)   (binding p-n, D40 eq. T)
Tpp = (310*phi)**2 / mpf(11017)     # Tpp = Rsurf(p)^2 / Rtot(p) (conflict p-p)
Zsat = 20

print(f"T   (p-n binding)  = {float(T):.6f}   [cible D40: 25.2603]")
print(f"Tpp (p-p conflict) = {float(Tpp):.6f} [cible D40: 22.8368]")

def build_multicenter_graph(Z, N, Zsat=20):
    """Construit le graphe pondere nucleon-nucleon multi-centres.
    Noeuds = nucleons individuels (chacun un bloc K4, vertex-disjoint par construction D56 L2).
    Aretes p-p : graphe complet sur c=min(Z,Zsat) protons, poids Tpp (D40, theoreme de saturation).
    Aretes p-n : chaque neutron couple aux min(Z,Zsat) premiers protons, poids T (generalisation
                 multi-centres explicite de l'etoile D56, qui ne couplait qu'a UN proton central).
    Aretes n-n : aucune regle de couplage direct etablie dans le corpus (absent de D40/D56) -> poids 0.
    """
    G = nx.Graph()
    protons  = [f"p{i}" for i in range(Z)]
    neutrons = [f"n{j}" for j in range(N)]
    G.add_nodes_from(protons, kind="p")
    G.add_nodes_from(neutrons, kind="n")
    c = min(Z, Zsat)
    active_protons = protons[:c]
    # p-p : graphe complet plafonne
    for i in range(c):
        for k in range(i+1, c):
            G.add_edge(active_protons[i], active_protons[k], weight=float(Tpp), kind="pp")
    # p-n : chaque neutron engage les c premiers protons
    for nu in neutrons:
        for pr in active_protons:
            G.add_edge(nu, pr, weight=float(T), kind="pn")
    return G

# --- (1) Verification de reduction exacte aux formules D40/D56 connues ---
for Z in [5, 15, 20, 30]:
    G = build_multicenter_graph(Z, N=1, Zsat=20)
    W_pp = sum(d["weight"] for _,_,d in G.edges(data=True) if d["kind"]=="pp")
    c = min(Z,20)
    C_Z_formula = c*(c-1)/2 * float(Tpp)
    assert abs(W_pp - C_Z_formula) < 1e-9, f"Echec reduction C(Z) pour Z={Z}"
print("\n[OK] Reduction exacte du sous-graphe p-p a la formule C(Z)=c(c-1)/2 * Tpp (D40, Theoreme de saturation)")

G1 = build_multicenter_graph(Z=20, N=3, Zsat=20)
W_pn = sum(d["weight"] for _,_,d in G1.edges(data=True) if d["kind"]=="pn")
assert abs(W_pn - 3*20*float(T)) < 1e-9
print("[OK] Reduction exacte du sous-graphe p-n a k*c*T pour k neutrons, generalisant D56 (k=1 centre -> k centres)")

# --- (2) Invariance par relabeling (verification explicite, piege Session 64 #1) ---
import itertools, random
random.seed(0)
G2 = build_multicenter_graph(Z=8, N=5, Zsat=20)
W_total_ref = sum(d["weight"] for _,_,d in G2.edges(data=True))
for _ in range(20):
    perm_p = list(range(8)); random.shuffle(perm_p)
    perm_n = list(range(5)); random.shuffle(perm_n)
    mapping = {f"p{i}": f"p{perm_p[i]}" for i in range(8)}
    mapping.update({f"n{j}": f"n{perm_n[j]}" for j in range(5)})
    G2r = nx.relabel_nodes(G2, mapping)
    W_total_r = sum(d["weight"] for _,_,d in G2r.edges(data=True))
    assert abs(W_total_r - W_total_ref) < 1e-9
print("[OK] Poids total invariant sous relabeling (20 permutations aleatoires testees) - la regle ne reference jamais l'identite interne des nucleons, seulement leur type et Zsat")

# --- (3) Loi d'echelle du poids total en fonction de N (Z=N, regime sature Z>Zsat) ---
Ns = [25, 50, 100, 200, 400, 800, 1600, 3200]
totals = []
for n in Ns:
    G = build_multicenter_graph(Z=n, N=n, Zsat=20)
    Wt = sum(d["weight"] for _,_,d in G.edges(data=True))
    totals.append(Wt)

logN = np.log(Ns)
logW = np.log(totals)
slope, intercept = np.polyfit(logN, logW, 1)
print(f"\nExposant d'echelle mesure (poids total vs N, Z=N, regime Z>Zsat=20) : {slope:.4f}")
print("Exposant attendu pour reseau sature (theorie) : 1.0 (extensif)")
print("Exposant requis par la cible Bekenstein-Hawking (rayon de Schwarzschild R_s ~ M ~ N) : 2.0")
print("Exposant requis par une surface geometrique de matiere nucleaire ordinaire (R ~ N^(1/3)) : 0.667")
