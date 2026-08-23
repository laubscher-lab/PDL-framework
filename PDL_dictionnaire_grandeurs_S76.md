# Dictionnaire des grandeurs PDL et règles de passage entre niveaux

**Session 76 — 23 août 2026. Instrument de travail.**

> **Statut de ce fichier.** Ce n'est **pas un document de corpus** : pas de DOI, pas de dépôt
> Zenodo, pas de citation depuis un document publié. C'est un instrument de navigation, destiné
> à être tenu à jour et à servir de base à l'audit du tableau épistémique de DM v34.
>
> Chaque définition est relevée à sa source. Toute valeur numérique a été recalculée avant
> d'être écrite (arithmétique entière exacte ; `mpmath` à 50 décimales pour $\mathbb{Q}(\sqrt5)$ ;
> `sympy` pour le symbolique exact). Les entrées non trouvées à la source sont marquées
> **[NON LOCALISÉ]** plutôt qu'inférées.

**Garde terminologique appliquée.** $K_4$ au sens littéral de D61 ($\mathrm{Coh}(K_4)\cong\mathbb{Z}_2^3\rtimes V_4$)
désigne **exclusivement l'électron**. Les fermetures nucléoniques composites s'écrivent
**toujours $K_{\mathrm{nuc}}$**, jamais $K_4$ ni $K_4\leftrightarrow K_4$, même par analogie.
$K_{24}$ et $K_{28}$ sont des graphes complets sur 24 et 28 **entités**.

**La géométrie Blender est descendante** : elle réalise ce que le corpus fixe. Aucun résultat
de ce fichier n'est fondé sur elle ; là où elle intervient (§2.6), c'est comme donnée à
expliquer, pas comme preuve.

---

## 1. Échelle des niveaux

| Niveau | Objet | Entités | Relations |
|---|---|---|---|
| L0 sous-électronique | non défini dans le corpus | — | — |
| L1 électronique | $K_4$ | 4 | $R_e = 6$ |
| L2 valence | $K_{24}$, $K_{28}$ | $n_u = 24$, $n_d = 28$ | $r_u = 276$, $r_d = 378$ |
| L3 nucléonique | $K_{\mathrm{nuc}}$ (proton) | **non assigné** | $R_{\mathrm{tot}} = 11017$ |
| L4 macroscopique | assemblages | $N$ nucléons | — |

Le corpus **n'assigne aucun compte d'entités au niveau L3**. C'est le trou de structure le plus
visible du dictionnaire : il rend RP2 (§4) intestable et laisse $n_{\mathrm{sea}}$ sans valeur
directe (I6).

---

## 2. Le dictionnaire

Colonnes : ce qu'elle compte · niveau · statut · extensive (E) / structurelle (S) / mixte ·
source · correspondance de niveau.

### 2.1 Niveau électronique (L1)

| Grandeur | Valeur | Compte | Statut | E/S | Source | Correspondance |
|---|---|---|---|---|---|---|
| $\|V(K_4)\|$ | 4 | entités | théorème | S | D16a ; PDL.tex | — |
| $R_e$ (noté $\Re$) | 6 | **arêtes** de $K_4$ ; $\binom{4}{2}$ | théorème | S | D16a ; DM v33 Thm 2.1 | $R_e = 2c$ (RP1) |
| $\|\mathrm{Coh}(K_4)\|$ | 8 | configurations de signes cohérentes | théorème, vérifié exhaustivement | S | D57 ; D61 ($\cong\mathbb{Z}_2^3$) | — |
| orbites $S_4$ sur $\mathrm{Coh}$ | $1{+}3{+}4$ | classes de configurations | théorème, revérifié | S | D57 | — |
| orbites $V_4$ sur $\mathrm{Coh}$ | **5** ($1{+}1{+}1{+}1{+}4$) | classes de configurations | théorème, revérifié S76 | S | DL03 | voir RN2 |
| $\sin^2\theta_W^{\text{tree}}$ | $1/4=\|V_4\|/16$ | rapport de deux dénombrements | théorème | S | D57, routes A ($192/768$) et B | — |
| $\beta_1(K_4)$ | 3 | cycles indépendants | théorème | S | D51 ; N01 | — |

### 2.2 Niveau valence (L2)

| Grandeur | Valeur | Compte | Statut | E/S | Source | Correspondance |
|---|---|---|---|---|---|---|
| $n_u$ | 24 | **entités** d'un cœur up | théorème (quintuplet) | E | D16a/D16b | chaque entité **est** un $K_4$ en L1 (RP1) |
| $n_d$ | 28 | **entités** d'un cœur down | théorème | E | D16a/D16b | idem |
| $n_{u\text{-cores}}$ | 2 (p) / 1 (n) | **cœurs**, pas entités | théorème | S | D43 | gouverne la parité, voir §5 |
| $\Delta n$ | 4 | **écart** $n_d-n_u$ | théorème (discriminant parfait $149^2$) | **S** | D47 | — |
| $r_u$ | 276 | arêtes de $K_{24}$ ; $\binom{24}{2}$ | **identité**, pas résultat | E | Derivation_alpha_PDL_v2 | — |
| $r_d$ | 378 | arêtes de $K_{28}$ ; $\binom{28}{2}$ | **identité** | E | idem | — |
| $r_{\mathrm{val}}$ | 930 | arêtes des trois cœurs ; $2r_u{+}r_d$ | théorème | E | D05 ; D16a/D16b | $= 3\,r_{\mathrm{core}}$ |
| $r_{\mathrm{core}}$ | 310 | cœur de cohérence **moyen** par quark | définition | S | Derivation_alpha ; D05 v2 éq. 2 | — |
| $n_K$ | 76 | $2n_u{+}n_d$ — **entités des cœurs** *et* **blocs $K_4$** | théorème (dérivé) | E | D43 ; lecture D68 | **doublet de niveau, RP1** |

### 2.3 Interface et bordure

| Grandeur | Valeur | Compte | Statut | E/S | Source | Correspondance |
|---|---|---|---|---|---|---|
| $c$ | 3 | arêtes bloc→mer, par bloc | théorème **sous lecture hiérarchique** ; réalisation **variable** | **S** | D43 ; D68 rem. $c{=}3$ ; S21 ($0,2,3$) | $c = R_e/2$ |
| $n_K c$ | 228 | relations d'interface | théorème dérivé | E | D43 §5 | $76\times3$ |
| $n_K(1{+}c)$ | 304 | interface + 1 arête structurelle/bloc | théorème dérivé | E | D43 ; D68 err. | $=76\times4$ ; voir Q2 |
| $A$ | 55 | arêtes de bordure par cœur up ; $(\Delta n{+}1)(2\Delta n{+}3)$ | théorème | mixte | D43 | **impair** |
| $B$ | 194 | arêtes de bordure par cœur down | théorème | mixte | D43 | **pair** ; $B{-}A=139$ |
| $(\Delta n{+}1)^2$ | 25 | terme d'isospin | théorème | **S** | D43 ; $\Delta n$ de D47 | $=R_{\mathrm{tot}}(p)-R_{\mathrm{tot}}(n)$ |
| $E_{\mathrm{bord}}(p)$ | 329 | arêtes de bordure | théorème inconditionnel | **mixte : 304 (E) + 25 (S)** | D43, OP-A résolu | **impair** |
| $E_{\mathrm{bord}}(n)$ | 468 | idem | théorème | mixte | D43 | **pair** |
| $b = E_{\mathrm{bord}}^{\mathrm{raw}}$ | 204 | **périmètres des trous** ; $2E-4F$ | sortie de simulation → **exprimable dans le quintuplet** (S76) | E | D43 §S21 ; §5 ci-dessous | $\neq 329$, objets distincts |
| $\varepsilon_{\mathrm{geom}}(p)$ | $329/10087 = 47/1441$ | rapport bordure/mer | théorème | rapport | D43 | non réduit dans D43 |
| $\varepsilon_{\mathrm{geom}}(n)$ | $468/9960 = 39/830$ | idem | théorème | rapport | D43 | non réduit dans D43 |

### 2.4 Niveau nucléonique (L3)

| Grandeur | Valeur | Compte | Statut | E/S | Source | Correspondance |
|---|---|---|---|---|---|---|
| $R_{\mathrm{sea}}(p)$ | 10087 | relations dynamiques de la mer | théorème — écrit « $\simeq$ » dans PDL.tex | E | D01/PDL.tex ; D43 ; D63 | **impair** |
| $R_{\mathrm{sea}}(n)$ | 9960 | idem | théorème | E | D22 | **pair** |
| $R_{\mathrm{tot}}$ | 11017 | relations internes ; $r_{\mathrm{val}}+R_{\mathrm{sea}}$ | théorème | E | D05 v2 éq. 1 ; D43 | — |
| $n_{\mathrm{sea}}$ | **jamais assigné** | (faces ou entités de la mer) | **non spécifié** | — | aucune | voir §5 |
| $R_{\mathrm{surf}}$ | $310\varphi \approx 501{,}5905$ | **espérance** du nombre de relations engagées | **hypothèse nommée H$\varphi$** | mixte ($\varphi$ S × $r_{\mathrm{core}}$ E) | **D05 v2** | voir §6 |
| $R_{\mathrm{res}}$ | $310/\varphi^2 \approx 118{,}409$ | défini **par soustraction** | **non interprété** | — | D05 v2 éq. 9 | OP-H$\varphi$-3 |
| $R'_{\mathrm{tot}}$ | $310\varphi^2 \approx 811{,}591$ | $R_{\mathrm{core}}+R_{\mathrm{surf}}$ | **sans référent dans le corpus** | — | D05 v2 §5 | OP-H$\varphi$-3 |
| $\kappa$ | $310\varphi/11017 \approx 0{,}0455288$ | $R_{\mathrm{surf}}/R_{\mathrm{tot}}$ | **théorème sous H$\varphi$** | rapport | D39 ; D42 | $=(\varphi/3)(r_{\mathrm{val}}/R_{\mathrm{tot}})$ |
| $P_1$ | $\varphi/3 \approx 0{,}5393447$ | **probabilité** qu'une relation de valence soit engagée | **sous H$\varphi$** | rapport | D39 | — |

### 2.5 Couplage $K_4 \leftrightarrow$ secteurs de quarks

| Grandeur | Valeur | Compte | Statut | E/S | Source |
|---|---|---|---|---|---|
| $k_1$ | 9 | modes asymétriques ; $\Delta n + (R_e{-}1)$ | théorème | S | D51 |
| $k_2$ | 19 | modes $u$ actifs ; $n_u - R_e + 1$ | théorème (unicité prouvée) | S | D51 ; D55 |
| $k_3$ | 168 | surface de couplage ; $R_e\,n_d$ | théorème | E | D51 |
| $N_{\mathrm{tot}}$ | 119 | pas d'interface ; $(n_d/4)\cdot(r_d{-}r_u)/R_e = 7\times17$ | théorème (Lemme D) | S | D55 |

Relations exactes : $k_1+k_2 = n_d = 28$ ; $k_3/(k_1{+}k_2) = R_e = 6$.

### 2.6 Grandeurs de simulation (Blender, S21) — **descendantes**

| Grandeur | Valeur | Compte | Statut | Source |
|---|---|---|---|---|
| $V_{\mathrm{sea}}$ | 5144 | sommets du maillage | sortie de simulation | D43 §S21 |
| $E_{\mathrm{sea}}$ | 10188 | arêtes du maillage | sortie de simulation | D43 §S21 |
| $F_{\mathrm{sea}}$ | 5043 | faces du maillage | sortie de simulation | D43 §S21 |
| $\chi$ | $-1$ | $V-E+F$ ; sphère à 3 trous | recalculé exact | D43 |
| $930+9859+228$ | 11017 | (valence + mer pure + interface) | **[NON LOCALISÉ]** — l'égalité est exacte, la décomposition n'a pas été retrouvée écrite | — |

**Résultat S76 : ce maillage n'a aucun paramètre propre** — voir §5.

---

## 3. Incohérences relevées — état en fin de Session 76

| # | Objet | État |
|---|---|---|
| I1 | $R_{\mathrm{surf}}$ déclaré cardinalité mais irrationnel | **résolu** — D05 v2, Rem. 1 : espérance, pas cardinal |
| I2 | statut contradictoire de $R_{\mathrm{surf}}$ | **résolu** — hypothèse H$\varphi$ |
| **I3** | **DM v33 : « $\sigma=930$ the active surface »** | **VIVANTE** — la surface active vaut $501{,}59$ ; écart 428,41 |
| **I4** | **DM v33 : « $n_u=24$ = number of u-valence cores »** | **VIVANTE** — fausse deux fois ; rend $n_K=76$ inintelligible |
| I5 | règle $R_{\mathrm{sea}}=2n_{\mathrm{sea}}$ contre 10087 impair | **résolu quant à la nature** — voir §5 |
| I6 | $n_{\mathrm{sea}}$ jamais assigné | ouverte — le niveau L3 n'a aucun compte d'entités |
| I7 | $c=3$ uniforme (théorème) vs variable (S21) | ouverte — **OP-D75-13** ; sans effet sur $E_{\mathrm{bord}}$ |
| I8 | $E_{\mathrm{sea}}=10188$ vs $R_{\mathrm{sea}}=10087$ | expliquée (D68 : $101=76+25$), **non fermée** |
| I9 | erratum D43 : $204+228 = 432 \neq 329$ | **réglé** (D68), à propager |
| **I10** | **DM v33 : « $\kappa=3/\sigma$ » et « H1 : $\kappa=\sigma/R_{\mathrm{tot}}$ »** | **VIVANTE** — donnent $0{,}00323$ et $0{,}08442$ ; $\kappa = 0{,}0455288$ |
| I11 | D05 v1 : quatre erreurs | **résolu** — D05 v2, 10.5281/zenodo.22066454 |
| I12 | $\varepsilon_{\mathrm{geom}}$ non réduit dans D43 | mineure, à signaler dans l'erratum |
| I13 | `unsrt.bst` ignore silencieusement le champ `doi` | **à vérifier sur tout le corpus** |

**Trois incohérences vivantes (I3, I4, I10) sont dans DM v33**, c'est-à-dire dans le document par
lequel un lecteur extérieur entre dans le corpus. Elles ont une cause unique : le glossaire
identifie $\sigma = 930$ à la surface active. Priorité DM v34.

---

## 4. Règles de passage

**RP1 — descendante. Statut : présente au corpus (D68, rem. $c{=}3$), vérifiée sur les nombres exacts.**
« Une entité d'un cœur *est* une fermeture $K_4$ au niveau inférieur. »
- $n_K = 24+24+28 = 76$ est **simultanément** un compte d'entités en L2 et un compte de blocs en L1. **Seul doublet de niveau avéré du corpus.**
- $c = R_e/2 = 3$ : les 6 arêtes de $K_4$ se partagent $3+3$ (trois vers la mer, trois fermant le triangle interne).
- $n_K c = 228$, exactement 3 par bloc.

Cette règle **n'est écrite nulle part comme principe** : D68 la formule comme la lecture qui rend
la justification de D43 correcte. Clarification, pas théorème.

**RP2 — montante. Statut : présente (D42), non testable numériquement.**
« Une relation à un niveau est une entité au niveau supérieur » — les $p_k \in R_{\mathrm{tot}}$
sont des sommets des triangles croisés. Le corpus n'assignant aucun compte d'entités en L3 (I6),
aucun couple de nombres ne permet de la vérifier. Usage définitionnel, pas identité de comptage.

**RN1 — résultat négatif : RP1 et RP2 ne sont pas mutuellement inverses.**
Si elles l'étaient, le nombre d'entités en $L{+}1$ égalerait le nombre de relations en $L$.
- relations en L1 : $R_e = 6$ ; entités en L2 : 24 et 28. $6 \neq 24$, $6 \neq 28$.
- $76 \times 6 = 456$ relations en L1 ; $r_{\mathrm{val}} = 930$ en L2. $456 \neq 930$.

RP1 remplace une entité par un graphe entier ; RP2 promeut une arête en sommet. **Deux sens, mais
pas deux sens de la même flèche.** Toute tentative de règle réversible devra expliquer $456 \neq 930$.

**Q2 — question ouverte, non promue.** $n_K(1{+}c) = 76\times4 = 304$, où $1+c = 4 = |V(K_4)|$.
Exact, mais D43 lit le $+1$ comme « one additional structural edge per block », pas comme un
compte de sommets. Consigné sans statut, parce que c'est une ressemblance de valeur.

---

## 5. La mer : $R_{\mathrm{sea}} = 2n_{\mathrm{sea}}$ (I5), résolu

**Règle localisée à la source.** PDL.tex §« Quantification of the relational sea » :
« characterized by the following counting rule: $R_{\mathrm{sea}} = 2n_{\mathrm{sea}}$ », puis
« $R_{\mathrm{sea}} \simeq 10\,087$ ». Schodinger_PDL_v2.tex : même règle, puis
« $R_{\mathrm{sea}} = 10\,087$ » avec un **égal**. Conflit interne au corpus.

**Théorème** (vérifié sur 11 complexes construits — disques, disques à trous, tores fermés,
tores à trous ; jamais supposé) :
$$E = 2F + \tfrac{b}{2}, \qquad V = F + \tfrac{b}{2} + \chi$$
issus de $4F = 2E - b$ et d'Euler ; **indépendants de la topologie**.

**Conséquence.** $R_{\mathrm{sea}} = 2n_{\mathrm{sea}}$ est le cas $b = 0$ avec $n_{\mathrm{sea}} = F$ :
c'est l'identité d'une mer **fermée**. La mer du proton a trois trous.
**La parité impaire n'est pas une faute de la règle : c'est la signature du bord.**
$E$ impair exige $b \equiv 2 \pmod 4$, réalisable.

**Conjecture (une seule closure ; protocole des deux dénombrements NON satisfait).**
Sous (A) $R_{\mathrm{sea}} = 2F+1$ et (B) $b/2 = n_K + (\Delta n{+}1)^2 + 1$, le maillage S21 se
reconstruit intégralement depuis $(R_{\mathrm{sea}}, n_K, \Delta n, h)$ : $F=5043$, $b=204$,
$E=10188$, $V=5144$, $\chi=-1$. **Aucun paramètre propre au maillage ne subsiste.**

**Identité nouvelle.** $101 = n_K + (\Delta n{+}1)^2$ (D68) et $101 = b/2 - 1$ sont équivalentes, d'où
$$b = 2\bigl(n_K + (\Delta n{+}1)^2 + 1\bigr) = 204 .$$
$b$ était une sortie de simulation ; elle s'exprime dans les entiers du quintuplet.

**Le $+1$ suit l'isospin.** $R_{\mathrm{sea}}(n) = 9960$ est **pair** : la règle est **exacte pour le
neutron** ($n_{\mathrm{sea}} = 4980$) et fautive d'une unité pour le proton seul. $R_{\mathrm{sea}}$
et $E_{\mathrm{bord}}$ ont la même parité dans les deux closures, suivant celle de
$n_{u\text{-cores}}+1$. **Non expliqué, non ajusté.**

> **OP-D75-2 (v3)** — Montrer que $R_{\mathrm{sea}} \equiv E_{\mathrm{bord}} \pmod 2$ est un théorème
> de C1–C4 et non une coïncidence sur deux cas. Prérequis à toute promotion : une seconde closure
> quadrangulée.

---

## 6. $R_{\mathrm{surf}}$ et l'origine de $\varphi$

**Statut : hypothèse nommée H$\varphi$** (D05 v2, 10.5281/zenodo.22066454).
D05 v1 se qualifiait lui-même de *sketch* et d'*informed hypothesis rather than a fully derived
theorem* ; les tables épistémiques de D39 et D43 l'inscrivaient en théorème. **Supersédé.**

**$R_{\mathrm{surf}}$ est une espérance, pas un cardinal.** Aucun entier voisin ne reproduit
$\alpha$ : $501 \to 136{,}699$ ; $502 \to 137{,}246$ ; CODATA $137{,}036$ ; $310\varphi \to 137{,}022$.

**Condition corrigée** (D05 v2, éq. 4), vérifiée à 25 décimales :
$$\frac{R_{\mathrm{surf}}}{R'_{\mathrm{tot}}} = \frac{R_{\mathrm{core}}}{R_{\mathrm{surf}}} = \frac{1}{\varphi},
\qquad R_{\mathrm{core}} = 310, \quad R_{\mathrm{surf}} = 310\varphi .$$

**Décomposition à trois termes** : $r_{\mathrm{val}} = 310(\varphi + 1 + \varphi^{-2}) = 930$, exacte
car $\varphi^{-2} = 2-\varphi$. Le résidu $R_{\mathrm{res}} = 310/\varphi^2$ est **non interprété**.

### Où $\varphi$ ne peut pas venir — résultats négatifs

- **Un invariant topologique est entier** ($\chi$, Betti, rangs d'homologie) : $\sqrt5$ n'en est pas un.
- $\varphi = 2\cos(\pi/5)$ est la signature spectrale de la symétrie d'ordre 5. **Mais les spectres
  de $K_n$ sont $\{n-1,-1,\dots,-1\}$, entièrement entiers.** $K_4$, $K_{24}$, $K_{28}$ ne peuvent
  produire $\sqrt5$.
- **Aucun ordre de groupe du corpus n'est divisible par 5** ($|V_4|=4$, $|S_4|=24$,
  $|\mathrm{Coh}(K_4)|=8$, $|\mathbb{Z}_2^3\rtimes V_4|=32$, $|A_4|=12$, $|S_3|=6$) : par Lagrange,
  aucun élément d'ordre 5. Les cinq $V_4$-orbites n'ont pas d'ordre cyclique naturel.
- **Un dénombrement fini donne un rationnel** — le corpus en est plein : $192/768$, $1/4$,
  $329/10087$, $228/76$. $\varphi/3$ est irrationnel : **aucun tirage indépendant sur un ensemble
  fini ne peut le produire.**

### Où $\varphi$ peut venir — piste ouverte

L'irrationalité quadratique vient de l'**auto-référence** : si le taux d'engagement dépend de ce
qui est déjà engagé, il est un point fixe, non un comptage. Seule la règle de substitution à deux
régimes $S \to S{+}D$, $D \to S$ (matrice $\begin{smallmatrix}1&1\\1&0\end{smallmatrix}$) a pour
discriminant **5** et valeur propre $\varphi$ ; les variantes donnent 8, 9, 13.

**Test contre le corpus : négatif pour la partition globale.**
$r_{\mathrm{val}}/R_{\mathrm{tot}} = 0{,}0844$ contre $1/\varphi^2 = 0{,}382$ attendu ; exposant
$5{,}137$, non entier. Si la règle existe, elle porte sur **engagé/verrouillé au sein de la
valence**, pas sur valence/mer. → **OP-D76-1**.

### RN2 — la piste orbitale du $25$ se ferme

$\mathrm{Coh}(K_4)$ a bien 5 orbites sous $V_4$, et $5^2 = 25$. Mais 5 n'est pas isolé (31 cardinaux
orbitaux pré-enregistrés), **aucun dénombrement ne produit 25** — alors que le $1/4$ de D57 est le
*résultat* de deux dénombrements —, $\Delta n = 4$ vient d'une condition de discriminant (D47) et
non d'une orbite, et OP-D62-5 possède déjà un $5^2$ d'origine algébrique sans rapport.
**La partie structurelle de $E_{\mathrm{bord}}$ n'admet pas de lecture orbitale.**

**Écueil, intact** : $E_{\mathrm{bord}} = 329$ est un théorème, $\varepsilon_{\mathrm{geom}}$ ne dépend
que du total. **L'indétermination de bordure ne touche pas $G$.**

---

## 7. Portée de H$\varphi$

**Conditionnels sous H$\varphi$** : $\kappa$, $\alpha$, $\sigma(N) = 1-(1-\kappa)^N$,
$G_{\mathrm{eff}}$ (Gate 3), la prédiction de Hubble, $\Lambda$.

**Inchangé** : $\varphi$ est un nombre algébrique **fixe**, le $1/3$ compte les trois cœurs.
**Aucun paramètre ajustable n'est introduit** ; l'énoncé « aucun paramètre libre hors
$\Delta m_{\mathrm{iso}}$ » **survit littéralement**. Le programme gagne une hypothèse structurelle
non démontrée, qui se répare par une preuve, pas par un ajustement.

**Intact** : quintuplets proton et neutron, $\Delta n = 4$, $E_{\mathrm{bord}}$,
$\varepsilon_{\mathrm{geom}}$, D43, D44, chaîne de jauge D57–D61. Aucun ne passe par $R_{\mathrm{surf}}$.

**Rappel** : DM v33 affirme la fermeture causale sur **deux** fondements dont aucun ne tient tel
quel — H$\varphi$ et la réouverture d'OP-B par D44v2. DM v34 doit auditer le tableau épistémique
**entrée par entrée**.

---

## 8. Actions

1. **DM v34** — corriger I3, I4, I10 ; « Gate 3 holds without any named hypothesis » devient
   « **under H$\varphi$** » ; auditer le tableau épistémique entrée par entrée contre ce dictionnaire.
2. **D39 et D43** — remplacer « Theorem (D05) » par **H$\varphi$**.
3. **D25** — retirer la phrase affirmant que l'optimisation PDL *sélectionne* $\varphi$ : la
   condition citée est celle d'avant correction et donne 574,77.
4. **D43** — signaler $\varepsilon_{\mathrm{geom}}$ non réduit.
5. **Corpus entier** — vérifier I13 (`unsrt.bst` et le champ `doi`).
6. **RP1** — décider si la lecture hiérarchique mérite un énoncé propre.
