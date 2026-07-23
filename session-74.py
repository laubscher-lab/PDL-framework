# Session 74 — Tous les scripts, format Colab (cellules # %%)
# A utiliser avec : session-74.md (resultats) et session-74-arg.md (cheminement)
# Chaque bloc porte le numero de section du document principal auquel il correspond.

# %% [markdown]
# ## Installation (si necessaire dans un nouvel environnement Colab)
# %%
# !pip install networkx sympy --quiet

# %% [markdown]
# ## §1 — Alphabet de l'electron (K4 sous V4) — 5 lettres, structure [1,1,1,1,4]
# Voir session-74-arg.md §2 : faux depart sous S4 complet (3 orbites, pauvre),
# corrige en trouvant V4 (D60/D61) comme le bon groupe.
# %%
import itertools

def coherent_K4_configs():
    edges = list(itertools.combinations(range(4), 2))
    configs = []
    for bits in itertools.product([1, -1], repeat=len(edges)):
        s = dict(zip(edges, bits))
        def sgn(i, j, s=s):
            return s[(i, j)] if (i, j) in s else s[(j, i)]
        coherent = all(sgn(a,b)*sgn(a,c)*sgn(b,c)==1 for a,b,c in itertools.combinations(range(4),3))
        if coherent:
            configs.append(tuple(bits))
    return configs, edges

COH, edges = coherent_K4_configs()
E_IDX = {e:i for i,e in enumerate(edges)}
def eidx(u,v): return E_IDX.get((u,v), E_IDX.get((v,u)))

V4_local = [{0:0,1:1,2:2,3:3},{0:1,1:0,2:3,3:2},{0:2,1:3,2:0,3:1},{0:3,1:2,2:1,3:0}]
def local_act(p, cfg):
    ns=[0]*6
    for (u,v),k in E_IDX.items(): ns[eidx(p[u],p[v])]=cfg[k]
    return tuple(ns)
def letter(cfg): return min(local_act(g,cfg) for g in V4_local)

letters = {c: letter(c) for c in COH}
orbit_sizes = {}
for c,l in letters.items():
    orbit_sizes[l] = orbit_sizes.get(l,0)+1
print(f"|Coh(K4)| = {len(COH)}")
print(f"Nombre de lettres distinctes (orbites) = {len(set(letters.values()))}")
print(f"Tailles d'orbites : {sorted(orbit_sizes.values())}")

# %% [markdown]
# ## §2 — Racine combinatoire commune (r_u, r_d) : parite, vecteurs, angles
# Identite algebrique exacte reliant les deux branches (lineaire et quadratique).
# %%
import math

n_u, n_d = 24, 28
r_u = n_u*(n_u-1)//2
r_d = n_d*(n_d-1)//2
print(f"r_u = C(24,2) = {r_u},  r_d = C(28,2) = {r_d}")
print(f"  r_u mod 4 = {r_u%4},  r_d mod 4 = {r_d%4}")

r_val_p = 2*r_u + r_d
r_val_n = r_u + 2*r_d
v_p_sq = 2*r_u**2 + r_d**2
v_n_sq = 2*r_d**2 + r_u**2

lhs = v_p_sq - v_n_sq
rhs = (r_val_p - r_val_n) * (r_u + r_d)
print(f"\n|v_p|^2 - |v_n|^2 = {lhs}")
print(f"(r_val(p)-r_val(n))*(r_u+r_d) = {rhs}")
print(f"Identite exacte verifiee : {lhs == rhs}")

# %% [markdown]
# ## §2 (suite) — Racine plus profonde : n_u, n_d mod 8 expliquent le mod-4 de r_u, r_d
# %%
print("Verification exhaustive de C(n,2) mod 4 selon n mod 8 :")
for nmod8 in range(8):
    vals = set()
    for k in range(50):
        n = 8*k + nmod8
        if n < 2: continue
        c = n*(n-1)//2
        vals.add(c % 4)
    print(f"  n ≡ {nmod8} (mod 8)  ->  C(n,2) mod 4 ∈ {sorted(vals)}")

# %% [markdown]
# ## §3 — Traduction du neutron et du proton (2 lettres chacun)
# Stabilisateur du vecteur (r_d,r_d,r_u) ou (r_u,r_u,r_d) sous S3.
# %%
v_p = (r_u, r_u, r_d)   # proton : 2 up, 1 down
v_n = (r_d, r_d, r_u)   # neutron : 1 up, 2 down
S3 = list(itertools.permutations([0,1,2]))

def stabilizer(v):
    return [p for p in S3 if tuple(v[p[i]] for i in range(3))==v]

stab_p = stabilizer(v_p)
stab_n = stabilizer(v_n)
print(f"Stabilisateur proton : {len(stab_p)} elements -> {stab_p}")
print(f"Stabilisateur neutron : {len(stab_n)} elements -> {stab_n}")

def special_axis(v):
    vals = list(v)
    counts = {x: vals.count(x) for x in set(vals)}
    minority_val = min(counts, key=lambda x: counts[x])
    return [i for i,x in enumerate(vals) if x==minority_val]

print(f"Axe special proton (minoritaire) : {special_axis(v_p)}")
print(f"Axe special neutron (minoritaire) : {special_axis(v_n)}")

# %% [markdown]
# ## §5 — Resultat negatif : test du cycle de pulsation (spin) comme source des 3 axes
# %%
import numpy as np

sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
T = np.array([[0,-1],[1,0]], dtype=complex)  # operateur de pulsation D33/D66

psi0 = np.array([1,0], dtype=complex)
states = [psi0]
for k in range(1,4):
    states.append(T @ states[-1])

print("Direction de spin pour chaque etat de pulsation :")
for k, psi in enumerate(states):
    Sx = 0.5*np.real(psi.conj() @ sx @ psi)
    Sy = 0.5*np.real(psi.conj() @ sy @ psi)
    Sz = 0.5*np.real(psi.conj() @ sz @ psi)
    print(f"  psi_{k}: (Sx,Sy,Sz) = ({Sx:+.3f}, {Sy:+.3f}, {Sz:+.3f})")
print("-> Un seul axe realise (Sz), jamais 3 -- le cycle de pulsation seul ne suffit pas.")

# %% [markdown]
# ## §5 — Resultat negatif : "cout combinatoire faible = sens physique spontane"
# %%
r_val_p_v = 930  # deja etabli, r_val(p)
r_val_n_v = 1032
R_sea_p, R_sea_n = 10087, 9960
R_tot_p = r_val_p_v + R_sea_p
R_tot_n = r_val_n_v + R_sea_n

p_to_n = r_val_p_v * R_tot_n / 4
n_to_p = r_val_n_v * R_tot_p / 4
print(f"p->n (capture electronique) = {p_to_n}")
print(f"n->p (desintegration beta)  = {n_to_p}")
print("Fait physique : m_n > m_p => n->p SPONTANEE (energetiquement favorable)")
print(f"Hypothese 'cout faible=spontane' predirait p->n (plus petit={p_to_n<n_to_p})")
print(">>> CONTRADICTION -- hypothese rejetee (melange de registres combinatoire/energie)")

# %% [markdown]
# ## §5 — Nouvelle incoherence de corpus : formule N_min(Z) testee contre donnees reelles
# A SIGNALER A CEDRIC — voir session-74.md §5 et §18.
# %%
ratio = 9960/11017  # R_sea(n)/R_tot(p)

real_Nmin = {
    1:0, 2:1, 3:3, 4:5, 5:5, 6:6, 7:7, 8:8, 9:10, 10:10,
    11:12, 12:12, 13:14, 14:14, 15:16, 16:16, 17:18, 18:18, 19:20, 20:20,
    21:24, 22:24, 23:28, 24:26, 25:30, 26:28, 27:32, 28:30,
}
print(f"{'Z':>3} {'N_min PDL':>10} {'N_min reel':>11} {'ecart relatif':>14}")
errs = []
for Z, Nreal in real_Nmin.items():
    Npred = Z*(Z-1)/2 * ratio
    rel_err = (Npred-Nreal)/Nreal*100 if Nreal>0 else float('nan')
    if Nreal>0: errs.append(abs(rel_err))
    print(f"{Z:>3} {Npred:>10.2f} {Nreal:>11} {rel_err:>13.1f}%")
print(f"\nErreur relative moyenne : {sum(errs)/len(errs):.1f}%  (annonce du corpus : 15%)")
print(">>> INCOHERENCE CONFIRMEE -- l'accord de 15% ne se reproduit pas.")

# %% [markdown]
# ## §6 — Formalisme L_k et famille des hypercubes (Moteur 1)
# Verification : Q2=5, Q3=30, Q4=2288 -- croissance accelerante.
# %%
import networkx as nx

def balanced_configs_efficient(G):
    nodes = list(G.nodes()); n = len(nodes); edges = list(G.edges())
    E_IDX = {e:i for i,e in enumerate(edges)}
    def eidx(u,v): return E_IDX.get((u,v), E_IDX.get((v,u)))
    configs = []
    for bits in itertools.product([0,1], repeat=n-1):
        part = {nodes[0]:0}
        for i,b in enumerate(bits): part[nodes[i+1]] = b
        cfg = tuple(1 if part[u]==part[v] else -1 for u,v in edges)
        configs.append(cfg)
    return configs, edges, E_IDX, eidx

def hypercube(k):
    G = nx.hypercube_graph(k)
    G = nx.convert_node_labels_to_integers(G, label_attribute='orig')
    orig = nx.get_node_attributes(G, 'orig')
    bits_of = {i: orig[i] for i in G.nodes()}
    idx_of = {v:k for k,v in bits_of.items()}
    return G, bits_of, idx_of

for k in [2,3,4]:
    G, bits_of, idx_of = hypercube(k)
    n = G.number_of_nodes()
    configs, edges, E_IDX, eidx = balanced_configs_efficient(G)
    flips = []
    for b in itertools.product([0,1], repeat=k):
        perm = {}
        for v in G.nodes():
            vb = bits_of[v]
            nb = tuple(x^y for x,y in zip(vb,b))
            perm[v] = idx_of[nb]
        flips.append(perm)
    def act(p, s, E_IDX=E_IDX, eidx=eidx, edges=edges):
        ns=[0]*len(edges)
        for (u,v),i in E_IDX.items(): ns[eidx(p[u],p[v])]=s[i]
        return tuple(ns)
    visited=set(); ORBITS=[]
    for s in configs:
        if s not in visited:
            orb = frozenset(act(p,s) for p in flips)
            ORBITS.append(orb); visited|=orb
    sizes = sorted(len(o) for o in ORBITS)
    print(f"Q{k} ({n} sommets) -> L_k = {len(ORBITS)}  tailles={dict((x,sizes.count(x)) for x in sorted(set(sizes)))}")

# %% [markdown]
# ## §7 — Pont K4 <-> C4 : tous deux graphes de Cayley sur Z2 x Z2
# %%
Z2xZ2 = list(itertools.product([0,1], repeat=2))
def xor(a,b): return tuple(x^y for x,y in zip(a,b))

def cayley(generators):
    G = nx.Graph()
    G.add_nodes_from(Z2xZ2)
    for g in Z2xZ2:
        for gen in generators:
            h = xor(g,gen)
            if g!=h: G.add_edge(g,h)
    return G

nonzero = [g for g in Z2xZ2 if g!=(0,0)]
unit_gens = [(1,0),(0,1)]

G_full = cayley(nonzero)
G_unit = cayley(unit_gens)
print(f"Cayley(Z2xZ2, tous generateurs) isomorphe a K4 ? {nx.is_isomorphic(G_full, nx.complete_graph(4))}")
print(f"Cayley(Z2xZ2, generateurs poids 1) isomorphe a C4 ? {nx.is_isomorphic(G_unit, nx.cycle_graph(4))}")

# %% [markdown]
# ## §7 — Classification exhaustive des 6 graphes connexes a 4 sommets
# Seuls K4 et C4 reussissent le test regulier+fixant.
# %%
def order_of(p, ident, n):
    cur=dict(p); k=1
    while cur!=ident:
        cur={i:p[cur[i]] for i in range(n)}; k+=1
        if k>30: return None
    return k
def compose(p,q,n): return {i:p[q[i]] for i in range(n)}

def coherent_configs_general(G):
    edges = list(G.edges())
    E_IDX = {e:i for i,e in enumerate(edges)}
    def eidx(u,v): return E_IDX.get((u,v), E_IDX.get((v,u)))
    cycles = nx.cycle_basis(G)
    def is_balanced(s):
        for cyc in cycles:
            prod=1
            for i in range(len(cyc)):
                u,v=cyc[i],cyc[(i+1)%len(cyc)]
                prod*=s[eidx(u,v)]
            if prod!=1: return False
        return True
    ALL = list(itertools.product([1,-1], repeat=len(edges)))
    return [s for s in ALL if is_balanced(s)], edges, E_IDX, eidx

def act_g(p, s, E_IDX, eidx):
    ns=[0]*len(E_IDX)
    for (u,v),k in E_IDX.items(): ns[eidx(p[u],p[v])]=s[k]
    return tuple(ns)

def test_graph_V4(G, name):
    n=4
    COH, edges, E_IDX, eidx = coherent_configs_general(G)
    GM = nx.algorithms.isomorphism.GraphMatcher(G,G)
    AUT = list(GM.isomorphisms_iter())
    ident = {i:i for i in range(n)}
    order2 = [p for p in AUT if order_of(p,ident,n)==2]
    visited=set(); ORBITS=[]
    for s in COH:
        if s not in visited:
            orb = frozenset(act_g(p,s,E_IDX,eidx) for p in AUT)
            ORBITS.append(list(orb)); visited|=orb
    aut_sizes = sorted(len(o) for o in ORBITS)
    for a,b in itertools.combinations(order2,2):
        ab = compose(a,b,n)
        if ab==ident or order_of(ab,ident,n)!=2: continue
        grp=[ident,a,b,ab]
        if len(set(tuple(sorted(g.items())) for g in grp))!=4: continue
        if not all(compose(x,y,n) in grp for x in grp for y in grp): continue
        for orb in ORBITS:
            if len(orb)!=4: continue
            all_imgs = set(act_g(g, orb[0], E_IDX, eidx) for g in grp)
            if len(all_imgs)!=4: continue
            others = [o for o in ORBITS if o is not orb]
            if all(act_g(g,s,E_IDX,eidx)==s for o in others for s in o for g in grp):
                visited2=set(); V4_ORBITS=[]
                for s in COH:
                    if s not in visited2:
                        o2=frozenset(act_g(g,s,E_IDX,eidx) for g in grp)
                        V4_ORBITS.append(o2); visited2|=o2
                sizes = sorted(len(o) for o in V4_ORBITS)
                return f"{name}: |E|={G.number_of_edges()} orbites(Aut)={aut_sizes} -> V4-OK L_k={len(V4_ORBITS)} tailles={sizes}"
    return f"{name}: |E|={G.number_of_edges()} orbites(Aut)={aut_sizes} -> pas de V4 regulier+fixant"

graphs_4v = {
    "P4 (chemin)": nx.path_graph(4),
    "K_{1,3} (etoile)": nx.star_graph(3),
    "C4 (cycle)": nx.cycle_graph(4),
    "paw": nx.Graph([(0,1),(1,2),(0,2),(2,3)]),
    "diamond (K4-1arete)": (lambda g:(g.remove_edge(0,1),g)[1])(nx.complete_graph(4)),
    "K4": nx.complete_graph(4),
}
for name, G in graphs_4v.items():
    print(test_graph_V4(nx.convert_node_labels_to_integers(G), name))

# %% [markdown]
# ## §7 — Moteur 2 : mecanisme antipodal sur les cycles pairs (C4,C6,C8,C10 marchent, C12 casse)
# %%
def act_cycle(perm, s, edges, E_IDX, eidx):
    ns=[0]*len(edges)
    for (u,v),k in E_IDX.items(): ns[eidx(perm[u],perm[v])]=s[k]
    return tuple(ns)

for n_cycle in [4,6,8,10,12]:
    G = nx.cycle_graph(n_cycle)
    configs, edges, E_IDX, eidx = balanced_configs_efficient(G)
    antipode = {v:(v+n_cycle//2)%n_cycle for v in range(n_cycle)}
    GM = nx.algorithms.isomorphism.GraphMatcher(G,G)
    AUT = list(GM.isomorphisms_iter())
    visited=set(); ORBITS=[]
    for s in configs:
        if s not in visited:
            orb = frozenset(act_cycle(p,s,edges,E_IDX,eidx) for p in AUT)
            ORBITS.append(orb); visited|=orb
    small = [o for o in ORBITS if len(o) < n_cycle]
    big = [o for o in ORBITS if len(o) == n_cycle]
    fixes_small = all(act_cycle(antipode,s,edges,E_IDX,eidx)==s for o in small for s in o)
    free_on_big = all(act_cycle(antipode,s,edges,E_IDX,eidx)!=s for o in big for s in o) if big else None
    print(f"C{n_cycle:>2}: antipodale fixe petites orbites={fixes_small}, libre sur grandes={free_on_big}")

# %% [markdown]
# ## §8 — Transmission de signal : relais rigide (4 ponts), information mutuelle parfaite
# %%
def build_chain_dense(N, n_bridges=4):
    G = nx.Graph()
    for i in range(N):
        offset = 4*i
        G.add_edges_from((offset+a, offset+b) for a,b in itertools.combinations(range(4),2))
    bridge_edges=[]
    for i in range(N-1):
        o1,o2 = 4*i, 4*(i+1)
        for v in range(n_bridges):
            e=(o1+v,o2+v); G.add_edge(*e); bridge_edges.append(e)
    return G, bridge_edges

N=4
G, bridges = build_chain_dense(N,4)
configs, edges, E_IDX, eidx = balanced_configs_efficient(G)
bridge_idx=[eidx(a,b) for a,b in bridges]
first_idx=[eidx(a,b) for a,b in itertools.combinations(range(4),2)]
last_off=4*(N-1)
last_idx=[eidx(last_off+a,last_off+b) for a,b in itertools.combinations(range(4),2)]

from collections import defaultdict
by_bcfg = defaultdict(lambda: defaultdict(int))
for s in configs:
    bcfg = tuple(s[i] for i in bridge_idx)
    l1 = tuple(s[i] for i in first_idx)
    l2 = tuple(s[i] for i in last_idx)
    by_bcfg[bcfg][(l1,l2)] += 1

example_bcfg = list(by_bcfg.keys())[0]
jd = by_bcfg[example_bcfg]
tot = sum(jd.values())
m1=defaultdict(int); m2=defaultdict(int)
for (a,b),c in jd.items(): m1[a]+=c; m2[b]+=c
H1 = -sum((c/tot)*math.log2(c/tot) for c in m1.values())
H12 = -sum((c/tot)*math.log2(c/tot) for c in jd.values())
H2 = -sum((c/tot)*math.log2(c/tot) for c in m2.values())
MI = H1+H2-H12
print(f"N={N} blocs, distance {N-1} : Information mutuelle = {MI:.3f} bits (max={H1:.3f})")
print(f"Fraction transmise : {MI/H1*100:.1f}%")

# %% [markdown]
# ## §8 — Richesse par repetition : 8^N exact (produit parfait)
# %%
N=5
G, bridges = build_chain_dense(N, 4)
configs, edges, E_IDX, eidx = balanced_configs_efficient(G)
block_values = [set() for _ in range(N)]
for s in configs:
    for i in range(N):
        idx = [eidx(4*i+a,4*i+b) for a,b in itertools.combinations(range(4),2)]
        block_values[i].add(tuple(s[j] for j in idx))
joint_words = set()
for s in configs:
    word = tuple(tuple(s[eidx(4*i+a,4*i+b)] for a,b in itertools.combinations(range(4),2)) for i in range(N))
    joint_words.add(word)
product_indiv = 1
for bv in block_values: product_indiv *= len(bv)
print(f"Mots globaux distincts = {len(joint_words)}, produit individuel = {product_indiv}")
print(f"Rapport = {len(joint_words)/product_indiv:.4f}  (1.0 = repetition pure)")

# %% [markdown]
# ## §8 — Goulot d'etranglement : maillon pauvre (K3) borne le signal transmis
# %%
G2 = nx.Graph()
G2.add_edges_from(itertools.combinations(range(4),2))          # gauche K4
G2.add_edges_from(itertools.combinations(range(4,7),2))        # milieu K3 (pauvre)
G2.add_edges_from((7+a,7+b) for a,b in itertools.combinations(range(4),2))  # droit K4
bridges2 = []
for v in range(3):
    e1, e2 = (v, 4+v), (4+v, 7+v)
    G2.add_edge(*e1); G2.add_edge(*e2)
    bridges2 += [e1, e2]

nodes2 = list(G2.nodes()); edges2 = list(G2.edges())
E_IDX2 = {e:i for i,e in enumerate(edges2)}
def eidx2(u,v): return E_IDX2.get((u,v),E_IDX2.get((v,u)))
configs2=[]
for bits in itertools.product([0,1], repeat=len(nodes2)-1):
    part={nodes2[0]:0}
    for i,b in enumerate(bits): part[nodes2[i+1]]=b
    cfg=tuple(1 if part[u]==part[v] else -1 for u,v in edges2)
    configs2.append(cfg)

left_idx = [eidx2(a,b) for a,b in itertools.combinations(range(4),2)]
right_idx = [eidx2(7+a,7+b) for a,b in itertools.combinations(range(4),2)]
bridge_idx2 = [eidx2(a,b) for a,b in bridges2]
# IMPORTANT : conditionner sur la config des ponts, pas marginaliser (sinon la
# correlation reelle s'efface artificiellement -- meme piege que la chaine a 2 ponts).
by_bcfg2 = defaultdict(lambda: defaultdict(int))
for s in configs2:
    bcfg = tuple(s[i] for i in bridge_idx2)
    l_left = tuple(s[i] for i in left_idx)
    l_right = tuple(s[i] for i in right_idx)
    by_bcfg2[bcfg][(l_left,l_right)] += 1
max_MIb = 0
for bcfg, jd in by_bcfg2.items():
    m1b=defaultdict(int); m2b=defaultdict(int)
    for (a,b),c in jd.items(): m1b[a]+=c; m2b[b]+=c
    totb=sum(jd.values())
    H1b=-sum((c/totb)*math.log2(c/totb) for c in m1b.values())
    H2b=-sum((c/totb)*math.log2(c/totb) for c in m2b.values())
    H12b=-sum((c/totb)*math.log2(c/totb) for c in jd.values())
    MIb=H1b+H2b-H12b
    max_MIb=max(max_MIb,MIb)
print(f"Information mutuelle (conditionnelle aux ponts) a travers le maillon K3 = {max_MIb:.3f} bits (max possible=3.000)")
print(f"Fraction transmise malgre le maillon pauvre : {max_MIb/3.0*100:.1f}%")

# %% [markdown]
# ## §8 — Instructions : 8 fonctions distinctes, forment (Z2)^3 -- MAIS non forcees (voir cellule suivante)
# %%
G3 = nx.Graph()
G3.add_edges_from(itertools.combinations(range(4),2))
G3.add_edges_from((4+a,4+b) for a,b in itertools.combinations(range(4),2))
bridges3 = [(v,4+v) for v in range(4)]
G3.add_edges_from(bridges3)
configs3, edges3, E_IDX3, eidx3 = balanced_configs_efficient(G3)
A_idx=[eidx3(a,b) for a,b in itertools.combinations(range(4),2)]
C_idx=[eidx3(4+a,4+b) for a,b in itertools.combinations(range(4),2)]
bridge_idx3=[eidx3(a,b) for a,b in bridges3]

by_bcfg3 = defaultdict(dict)
for s in configs3:
    bcfg = tuple(s[i] for i in bridge_idx3)
    lA=tuple(s[i] for i in A_idx); lC=tuple(s[i] for i in C_idx)
    by_bcfg3[bcfg][lA]=lC

all_letters = sorted(set(next(iter(by_bcfg3.values())).keys()))
letter_idx = {l:i for i,l in enumerate(all_letters)}
distinct_funcs = {}
for bcfg, fmap in by_bcfg3.items():
    sig = tuple(letter_idx[fmap[a]] for a in all_letters)
    distinct_funcs[sig] = bcfg
print(f"{len(distinct_funcs)} fonctions A->C distinctes trouvees (sur 16 instructions possibles)")

perms = list(distinct_funcs.keys())
def compose_p(p,q): return tuple(p[q[i]] for i in range(len(q)))
identity_p = tuple(range(8))
def order_of_p(p):
    cur=p; k=1
    while cur!=identity_p:
        cur=compose_p(p,cur); k+=1
        if k>20: return None
    return k
orders = sorted(order_of_p(p) for p in perms)
print(f"Ordres des elements : {orders}  (tous 2 -> structure (Z2)^3)")

# %% [markdown]
# ## §8 — Correction cruciale (symptome 1) : le groupe (Z2)^3 n'est PAS force
# Seule l'identite (sur 24 puis 120 correspondances testees) ferme un groupe coherent.
# %%
def test_sigma(sigma, n_verts=4):
    Gt = nx.Graph()
    Gt.add_edges_from(itertools.combinations(range(n_verts),2))
    Gt.add_edges_from((n_verts+a,n_verts+b) for a,b in itertools.combinations(range(n_verts),2))
    bridges_t = [(v, n_verts+sigma[v]) for v in range(n_verts)]
    Gt.add_edges_from(bridges_t)
    configs_t, edges_t, E_IDX_t, eidx_t = balanced_configs_efficient(Gt)
    A_idx_t=[eidx_t(a,b) for a,b in itertools.combinations(range(n_verts),2)]
    C_idx_t=[eidx_t(n_verts+a,n_verts+b) for a,b in itertools.combinations(range(n_verts),2)]
    bridge_idx_t=[eidx_t(a,b) for a,b in bridges_t]
    by_bcfg_t = defaultdict(dict)
    for s in configs_t:
        bcfg = tuple(s[i] for i in bridge_idx_t)
        lA=tuple(s[i] for i in A_idx_t); lC=tuple(s[i] for i in C_idx_t)
        by_bcfg_t[bcfg][lA]=lC
    all_letters_t = sorted(set(next(iter(by_bcfg_t.values())).keys()))
    letter_idx_t = {l:i for i,l in enumerate(all_letters_t)}
    distinct_t = {}
    for bcfg, fmap in by_bcfg_t.items():
        sig = tuple(letter_idx_t[fmap[a]] for a in all_letters_t)
        distinct_t[sig] = bcfg
    perms_t = list(distinct_t.keys())
    def compose_t(p,q): return tuple(p[q[i]] for i in range(len(q)))
    perm_set = set(perms_t)
    closed = all(compose_t(p,q) in perm_set for p in perms_t for q in perms_t)
    return closed

results_sigma = {}
for sigma in itertools.permutations(range(4)):
    results_sigma[sigma] = test_sigma(sigma)
good = [s for s,c in results_sigma.items() if c]
print(f"Correspondances testees : {len(results_sigma)} (=4!)")
print(f"Fermees (structure de groupe) : {len(good)}  -> {good}")
print(">>> Seule l'identite ferme un groupe -- le (Z2)^3 est un artefact de convention, pas force.")

# %% [markdown]
# ## §9 — Convergence a trois voies sur n=4 : verification algebrique exacte
# %%
from sympy import symbols, factor, solve, Eq, expand, div

n = symbols('n')
poly1 = expand(n*(n-1)*(n-2) - 24)   # DL01/DL02 : C(n,3)=4
poly2 = expand(n*(n-1) - 2*(2*n-2))  # resolution de spin : 2n-2 = C(n,2)

print(f"Equation 1 (DL01/DL02) factorisee : {factor(poly1)}")
print(f"Equation 2 (spin) factorisee : {factor(poly2)}")
q1, r1 = div(poly1, n-4, n)
q2, r2 = div(poly2, n-4, n)
print(f"Poly1 / (n-4) = {q1}, reste = {r1}")
print(f"Poly2 / (n-4) = {q2}, reste = {r2}")
print(">>> Les deux equations partagent EXACTEMENT le facteur (n-4).")

# %% [markdown]
# ## §9 — Le 3e critere (V4 regularite) : recherche exhaustive, n=4 seule solution
# %%
from math import comb

exact_matches = []
for nn in range(2, 29):
    for kk in range(0, nn//2 + 1):
        size = comb(nn,kk) if kk != nn-kk else comb(nn,kk)//2
        if size == 4:
            exact_matches.append((nn,kk,size))
print(f"Paires (n,k) donnant une orbite de taille EXACTEMENT 4 (n=2..28) : {exact_matches}")
print(">>> n=4 (k=1) est la SEULE solution -- convergence a 3 voies confirmee.")

# %% [markdown]
# ## §9 — Z4 (cyclique) vs V4 (Klein) : seul V4 fixe ponctuellement
# %%
Z4 = [{0:0,1:1,2:2,3:3},{0:1,1:2,2:3,3:0},{0:2,1:3,2:0,3:1},{0:3,1:0,2:1,3:2}]
COH2, edges2b = coherent_K4_configs()
E_IDX2b = {e:i for i,e in enumerate(edges2b)}
def eidx2b(u,v): return E_IDX2b.get((u,v),E_IDX2b.get((v,u)))
def act2b(perm, s):
    ns = {}
    for (i,j),k in E_IDX2b.items():
        ns[(perm[i],perm[j]) if perm[i]<perm[j] else (perm[j],perm[i])] = s[(i,j)] if isinstance(s,dict) else s[E_IDX2b[(i,j)]]
    return tuple(ns[e] for e in edges2b)

# (reutilise directement le calcul de §1 pour l'orbite de taille 4 et les petites orbites)
S4 = [dict(zip(range(4),p)) for p in itertools.permutations(range(4))]
def act_full(perm, cfg):
    ns=[0]*6
    for (u,v),k in E_IDX2b.items(): ns[eidx2b(perm[u],perm[v])]=cfg[k]
    return tuple(ns)
visited=set(); ORBITS_full=[]
for c in COH2:
    if c not in visited:
        orb = set(act_full(p,c) for p in S4)
        ORBITS_full.append(orb); visited|=orb
big_orbit = [o for o in ORBITS_full if len(o)==4][0]
small_orbits = [o for o in ORBITS_full if len(o)!=4]

s0 = list(big_orbit)[0]
images_z4 = set(act_full(g,s0) for g in Z4)
print(f"Z4 sur orbite-4 -> {len(images_z4)} images distinctes (regularite si =4)")
fixed_ok_z4 = all(act_full(g,s)==s for o in small_orbits for s in o for g in Z4)
print(f"Z4 fixe les petites orbites ? {fixed_ok_z4}")
print(">>> Z4 est regulier mais NE FIXE PAS -- seul V4 (Klein) reussit les deux conditions.")

# %% [markdown]
# ## §11 — Recherche de L(K24), L(K28) : aucune orbite exacte en puissance de 2
# %%
for n_test in [24, 28]:
    print(f"\nOrbites de K_{n_test} sous S_{n_test} complet :")
    pow2_found = []
    for k in range(0, n_test//2+1):
        size = comb(n_test,k) if k != n_test-k else comb(n_test,k)//2
        if size>1 and (size & (size-1))==0:
            pow2_found.append((k,size))
    print(f"  Puissances de 2 exactes (hors k=0) : {pow2_found}")

# %% [markdown]
# ## §11 — Meilleure approximation puissance de 2 (K24 : 1.19%, K28 : 10.30%)
# %%
for n_test in [24,28]:
    best = None
    for k in range(1, n_test//2+1):
        size = comb(n_test,k) if k != n_test-k else comb(n_test,k)//2
        p = round(math.log2(size))
        nearest = 2**p
        rel_err = abs(size-nearest)/size*100
        if best is None or rel_err < best[1]:
            best = (k, rel_err, size, nearest, p)
    print(f"K{n_test} : meilleure approx k={best[0]}, taille={best[2]}, 2^{best[4]}={best[3]}, ecart={best[1]:.2f}%")

# %% [markdown]
# ## §11 — Hypothese du sous-ensemble communicant : K16 (=Q4), 2288 orbites
# %%
G16, bits_of16, idx_of16 = hypercube(4)  # Q4 = K16 avec generateurs XOR-translation
configs16, edges16, E_IDX16, eidx16 = balanced_configs_efficient(G16)
flips16 = []
for b in itertools.product([0,1], repeat=4):
    perm = {}
    for v in G16.nodes():
        vb = bits_of16[v]
        nb = tuple(x^y for x,y in zip(vb,b))
        perm[v] = idx_of16[nb]
    flips16.append(perm)
def act16(p, s):
    ns=[0]*len(edges16)
    for (u,v),i in E_IDX16.items(): ns[eidx16(p[u],p[v])]=s[i]
    return tuple(ns)
visited16=set(); ORBITS16=[]
for s in configs16:
    if s not in visited16:
        orb = frozenset(act16(p,s) for p in flips16)
        ORBITS16.append(orb); visited16|=orb
print(f"K16 (groupe Z2^4) : {len(ORBITS16)} orbites -- identique a Q4 (meme groupe, meme resultat)")
L_candidate = len(ORBITS16)
print(f"Candidat retenu : L(K24) = L(K28) ~= {L_candidate}")

# %% [markdown]
# ## §12 — Formule d'identite du tableau periodique : L^(3A) x 5^Z, preuve d'unicite
# %%
L = 2288

def compo(Z, N):
    K24 = 2*Z + 1*N
    K28 = 1*Z + 2*N
    return K24, K28

def signature(Z, N):
    A = Z+N
    return L**(3*A) * 5**Z

seen = {}
collisions = 0
for Z in range(1, 31):
    for N in range(0, 41):
        sig = signature(Z,N)
        if sig in seen:
            collisions += 1
        else:
            seen[sig] = (Z,N)
print(f"{len(seen)+collisions} combinaisons testees (Z=1..30, N=0..40)")
print(f"Collisions trouvees : {collisions}  -> unicite {'CONFIRMEE' if collisions==0 else 'VIOLEE'}")

print("\nCartes d'identite H et He :")
for name,(Z,N) in [('1H',(1,0)),('2H(D)',(1,1)),('3H(T)',(1,2)),
                     ('3He',(2,1)),('4He',(2,2))]:
    K24,K28 = compo(Z,N)
    A=Z+N
    log2_orbite = 3*A*math.log2(L) + Z*math.log2(5)
    print(f"  {name:<8} {K24}xK24+{K28}xK28+{Z}e | orbite={log2_orbite:.1f} bits")

# %% [markdown]
# ## §13 — Raffinement valence electronique : l'helium perd tout son signal (gaz noble)
# %%
valence = {1:1, 2:0, 6:4, 7:5, 8:6, 15:5, 16:6}  # He : couche pleine -> valence=0

def carte_valence(Z, N, nom):
    K24, K28 = compo(Z,N)
    A = Z+N
    v = valence[Z]
    log2_ancien = 3*A*math.log2(L) + Z*math.log2(5)
    log2_valence = 3*A*math.log2(L) + (v*math.log2(5) if v>0 else 0)
    print(f"{nom:<6} Z={Z:<2} valence={v:<2} | ancien={log2_ancien:.1f} bits | valence-seule={log2_valence:.1f} bits | retire={log2_ancien-log2_valence:.1f} bits")

for nom,Z,N in [('1H',1,0),('4He',2,2),('12C',6,6),('14N',7,7),('16O',8,8)]:
    carte_valence(Z,N,nom)
print(">>> He (gaz noble) : signal retire = signal total -- coherent avec son inertie chimique.")

# %% [markdown]
# ## §14 — Decouverte : code lineaire, distance minimale 3, 100% phonemique
# %%
COH3, edges3b = coherent_K4_configs()
COH3_set = set(COH3)

def mult(c1,c2): return tuple(a*b for a,b in zip(c1,c2))
closed_lin = all(mult(c1,c2) in COH3_set for c1 in COH3 for c2 in COH3)
print(f"Code lineaire (ferme sous multiplication elt-par-elt) ? {closed_lin}")

weights = [sum(1 for x in c if x==-1) for c in COH3]
print(f"Poids des mots-code : {sorted(weights)}")
print(f"Distance minimale = poids minimal non-nul = {min(w for w in weights if w>0)}")

def hamming(c1,c2): return sum(1 for a,b in zip(c1,c2) if a!=b)
E_IDX3b = {e:i for i,e in enumerate(edges3b)}
def eidx3b(u,v): return E_IDX3b.get((u,v),E_IDX3b.get((v,u)))
def act3b(p,cfg):
    ns=[0]*6
    for (u,v),k in E_IDX3b.items(): ns[eidx3b(p[u],p[v])]=cfg[k]
    return tuple(ns)
letters3 = {c: min(act3b(g,c) for g in V4_local) for c in COH3}

pairs_d3 = [(c1,c2) for c1 in COH3 for c2 in COH3 if c1<c2 and hamming(c1,c2)==3]
phon = sum(1 for c1,c2 in pairs_d3 if letters3[c1]!=letters3[c2])
print(f"\nPaires minimales (distance 3) : {len(pairs_d3)}")
print(f"  PHONEMIQUES : {phon}/{len(pairs_d3)} ({phon/len(pairs_d3)*100:.0f}%)")

# %% [markdown]
# ## §15 — Test de bijectivite (aller-retour statique, pas encore une conversation dynamique)
# %%
example_bcfg2 = list(by_bcfg3.keys())[0]
fmap2 = by_bcfg3[example_bcfg2]
inverse = defaultdict(set)
for a,c in fmap2.items(): inverse[c].add(a)
is_bijective = all(len(v)==1 for v in inverse.values()) and len(fmap2)==len(inverse)
print(f"Fonction A->C bijective (donc C->A tout aussi deterministe) ? {is_bijective}")
print(">>> Aller-retour MATHEMATIQUE confirme -- pas encore une conversation DYNAMIQUE (pas de temps modelise).")

# %% [markdown]
# ## §16 — Correction : tension globale (facteur 16) vs repertoire local (inchange)
# %%
def coherent_hub_only():
    edges_h = list(itertools.combinations(range(4),2))
    E_IDX_h = {e:i for i,e in enumerate(edges_h)}
    def eidx_h(u,v): return E_IDX_h.get((u,v),E_IDX_h.get((v,u)))
    ALL = list(itertools.product([1,-1], repeat=len(edges_h)))
    def is_bal(s):
        return all(s[eidx_h(a,b)]*s[eidx_h(a,c)]*s[eidx_h(b,c)]==1 for a,b,c in itertools.combinations(range(4),3))
    return [s for s in ALL if is_bal(s)]

seul = set(coherent_hub_only())
print(f"Repertoire LOCAL du hub, seul : {len(seul)} configs")
print(f"Repertoire LOCAL du hub, avec satellite connecte : {len(seul)} configs (identique, verifie plus tot)")
print()
print(f"MAIS la richesse TOTALE DU SYSTEME :")
print(f"  Proton seul (H)              : |Coh| = 2^(4-1)  = {2**3}")
print(f"  Proton + neutron connecte (D) : |Coh| = 2^(8-1) = {2**7}")
print(f"  Rapport = {2**7//2**3}  -- la vraie tension est ICI, pas dans le repertoire local.")

# %% [markdown]
# ## §18 — Table du tableau periodique (36 premiers elements) + colonne entites pulsantes
# Formule L^(3A) x 5^Z (ou 5^valence pour le raffinement), plus la couche electronique
# de la derniere couche (x4 car un electron = K4 = 4 entites pulsantes).
# %%
L = 2288

def compo(Z, N):
    K24 = 2*Z + 1*N
    K28 = 1*Z + 2*N
    return K24, K28

derniere_couche = {
    1:1, 2:2, 3:1, 4:2, 5:3, 6:4, 7:5, 8:6, 9:7, 10:8,
    11:1, 12:2, 13:3, 14:4, 15:5, 16:6, 17:7, 18:8,
    19:1, 20:2, 21:2, 22:2, 23:2, 24:1, 25:2, 26:2, 27:2, 28:2,
    29:1, 30:2, 31:3, 32:4, 33:5, 34:6, 35:7, 36:8,
}

elements = [
    ("H",1,0),("He",2,2),("Li",3,4),("Be",4,5),("B",5,6),("C",6,6),("N",7,7),
    ("O",8,8),("F",9,10),("Ne",10,10),("Na",11,12),("Mg",12,12),("Al",13,14),
    ("Si",14,14),("P",15,16),("S",16,16),("Cl",17,18),("Ar",18,22),("K",19,20),
    ("Ca",20,20),("Sc",21,24),("Ti",22,26),("V",23,28),("Cr",24,28),("Mn",25,30),
    ("Fe",26,30),("Co",27,32),("Ni",28,30),("Cu",29,34),("Zn",30,34),("Ga",31,39),
    ("Ge",32,41),("As",33,42),("Se",34,45),("Br",35,44),("Kr",36,48),
]

print(f"{'Elt':<4} {'Z':>3} {'N':>3} {'A':>3} {'comptage(n-1)':>14} {'orbite(bits)':>13} {'e- derniere couche':>19} {'entites pulsantes':>18}")
for name,Z,N in elements:
    K24,K28 = compo(Z,N)
    A = Z+N
    n_entities = K24*24+K28*28
    axe_comptage = n_entities - 1
    axe_orbite = 3*A*math.log2(L) + Z*math.log2(5)
    e_derniere = derniere_couche[Z]
    entites_pulsantes = e_derniere * 4
    print(f"{name:<4} {Z:>3} {N:>3} {A:>3} {axe_comptage:>14} {axe_orbite:>13.1f} {e_derniere:>19} {entites_pulsantes:>18}")

# %% [markdown]
# ## §18 — Preuve que le comptage SEUL ne peut jamais identifier un atome (structurel, pas 76/80)
# %%
print("Verification exhaustive de la periodicite du comptage seul (Z=1..30, N=0..40) :")
seen_comptage = {}
collisions_comptage = 0
for Z in range(1, 31):
    for N in range(0, 41):
        comptage = 76*Z + 80*N - 1
        if comptage in seen_comptage:
            collisions_comptage += 1
        else:
            seen_comptage[comptage] = (Z,N)
print(f"Collisions sur le comptage seul : {collisions_comptage}")

print("\nCaractere structurel (pas specifique a 76/80) -- teste sur des poids arbitraires :")
for w1t, w2t in [(76,80),(3,5),(10,7),(100,99)]:
    gt = math.gcd(w1t,w2t)
    print(f"  poids ({w1t},{w2t}) : pgcd={gt} -> periode exacte delta_Z={w2t//gt}, delta_N=-{w1t//gt}"
          f"  (verif: {w1t}*{w2t//gt} == {w2t}*{w1t//gt} -> {w1t*(w2t//gt)==w2t*(w1t//gt)})")

# %% [markdown]
# ## §18 — Resultat negatif : l'affinite combinatoire (5^v) est trop plate pour un gradient chimique
# %%
valence_test = {1:1, 2:0, 3:1, 6:4, 7:5, 8:6, 9:7, 11:1, 17:7}

def signal_valence(Z, N, v_override=None):
    K24, K28 = compo(Z,N)
    A = Z+N
    v = valence_test[Z] if v_override is None else v_override
    return 3*A*math.log2(L) + (v*math.log2(5) if v>0 else 0)

print(f"{'Element':<8} {'Z':>3} {'valence':>8} {'gain si +1e':>14} {'perte si -1e':>14}")
for name,Z,N in [('H',1,0),('Li',3,4),('C',6,6),('N',7,7),('O',8,8),('F',9,10),('Na',11,12),('Cl',17,18)]:
    v = valence_test[Z]
    base = signal_valence(Z,N)
    gain_capture = signal_valence(Z,N,v_override=v+1) - base
    perte_cession = base - signal_valence(Z,N,v_override=max(v-1,0))
    print(f"{name:<8} {Z:>3} {v:>8} {gain_capture:>14.3f} {perte_cession:>14.3f}")
print("\n>>> Gain/perte IDENTIQUE (log2(5)~2.322) pour tout element -- le modele 5^v est")
print(">>> trop plat pour capturer un gradient d'electronegativite reel (pas de notion de")
print(">>> proximite a une couche pleine/vide). Resultat negatif honnete, pas cache.")

# %% [markdown]
# ## §19 — Recherche de points fixes (Von Neumann) parmi les 16 instructions
# Auto-replication = une instruction qui laisse une lettre EXACTEMENT inchangee.
# %%
by_bcfg_vn = defaultdict(dict)
for s in configs3:
    bcfg = tuple(s[i] for i in bridge_idx3)
    lA=tuple(s[i] for i in A_idx); lC=tuple(s[i] for i in C_idx)
    by_bcfg_vn[bcfg][lA]=lC

print(f"{'Instruction (pont)':<20} {'points fixes ?':<16} {'nb lettres fixees'}")
n_with_fixed = 0
for bcfg, fmap in by_bcfg_vn.items():
    fixed = [a for a,c in fmap.items() if a==c]
    if fixed: n_with_fixed += 1
    print(f"{str(bcfg):<20} {'OUI' if fixed else 'non':<16} {len(fixed)}")
print(f"\n{n_with_fixed}/16 instructions ont au moins un point fixe.")

# %% [markdown]
# ## §19 — Verification : les points fixes sont-ils un vrai mouvement, ou un artefact de jauge ?
# %%
nodes8 = list(range(8))
edges8 = list(itertools.combinations(range(4),2)) + \
         [(4+a,4+b) for a,b in itertools.combinations(range(4),2)] + \
         [(v,4+v) for v in range(4)]

def config_from_bipartition(part):
    return {e: (1 if part[e[0]]==part[e[1]] else -1) for e in edges8}

part1 = {i:0 for i in range(8)}  # tout dans le meme groupe -> instruction (1,1,1,1)
part2 = {i:(0 if i<4 else 1) for i in range(8)}  # satellite entier bascule -> instruction (-1,-1,-1,-1)
cfg1 = config_from_bipartition(part1)
cfg2 = config_from_bipartition(part2)

print("Instruction (1,1,1,1)   : hub interne =", [cfg1[e] for e in itertools.combinations(range(4),2)])
print("Instruction (-1,-1,-1,-1) : hub interne =", [cfg2[e] for e in itertools.combinations(range(4),2)],
      "(identique -- rien ne bouge, juste un renommage du cote de la bipartition)")

# %% [markdown]
# ## FIN — Recapitulatif des sections couvertes
# %%
print("""
Sections de session-74.md couvertes par ce notebook :
  §1  Alphabet electron (K4/V4)
  §2  Racine combinatoire (r_u, r_d)
  §3  Traduction neutron/proton
  §5  Resultats negatifs (spin, cout/direction, N_min(Z))
  §6  Formalisme L_k, hypercubes
  §7  Moteurs 1 et 2, classification 4 sommets
  §8  Transmission, goulot, instructions (+ correction symptome 1)
  §9  Convergence a 3 voies sur n=4
  §11 Recherche L(K24)/L(K28), hypothese sous-ensemble communicant
  §12 Formule d'identite du tableau periodique
  §13 Raffinement valence electronique
  §14 Code lineaire, distance minimale 3
  §15 Test de bijectivite
  §16 Correction tension globale/repertoire local
  §18 Table 36 elements + entites pulsantes, preuve structurelle (comptage seul),
      resultat negatif de l'affinite combinatoire
  §19 Recherche de points fixes (Von Neumann), verification qu'ils sont des artefacts de jauge

Non couvert (constructions abandonnees, non concluantes, ou hors registre calculable,
voir session-74-arg.md §1-26 pour le cheminement complet) :
  - Tentatives de couplage K4-K4 symetrique (10+2, toutes negatives)
  - Superposition de couches, mode "multiplication"
  - Recherche du critere complet succès/echec (octaedre, prisme, K4,4)
  - Test electron mobile (§17, symetrique, non concluant par construction)
  - Toute la discussion philosophique (nous, porteur, McTaggart) : voir D19ad_*.tex,
    pas ce notebook -- registre conceptuel, non calculable.
  - Production et debogage des documents D19ad/DL03 : voir les .tex/.bib eux-memes.
""")

