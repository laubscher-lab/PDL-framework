# PDL_pulsation_regimes_script5.py
# ============================================================
# Verification script -- Is PARITY the cause? The singleton
# obstruction for v_cross
# PDL Framework -- preliminary to a possible document D68
#
# RETRACTION CARRIED FORWARD:
#   In session discussion I asserted "no quantity built from C2 and
#   C4 can select a pulsation bipartition". That is FALSE and I
#   produced the counterexample myself: v_cross is built purely from
#   the violated triangles (C4) and selects perfectly, 1243/1243.
#   What killed it is not failure to discriminate but the FORM of
#   what it selects: always a cut of size 1, i.e. a single
#   privileged entity, inadmissible in a relational theory.
#
# STATEMENT UNDER TEST (conjecture, corroborated, NOT a theorem):
#   (P)  For every non-empty two-graph Delta on n vertices, the
#        minimum of v_cross over all proper cuts is attained at a
#        cut of size 1 -- and, empirically, ONLY at cuts of size 1.
#
# THE IDENTITY THAT MAKES IT READABLE:
#   A triangle is internal to a cut S iff it lies entirely inside S
#   or entirely inside its complement. Hence
#        v_cross(S) = v - mono(S),  mono(S) = #{T subset S}
#                                            + #{T subset V\S}
#   Minimising v_cross  <=>  MAXIMISING the number of monochromatic
#   violated triangles. Since v is constant across cuts, any
#   functional a*v_cross + b*v ranks exactly as v_cross does: this
#   is the clean proof that composite criteria built from tension
#   and group size cannot rank differently from v_cross alone.
#
# PROVED BY HAND (verified here):
#   - mono(S) <= C(k,3) + C(n-k,3) for |S| = k, maximal at k = 1;
#   - for k <= 2 no triangle fits inside S, so v_cross(S) counts the
#     violated triangles meeting S, monotone under inclusion; hence
#     the minimum over size-2 cuts is >= the minimum over singletons.
#   The case k >= 3 is NOT proved: triangles can then fit inside S.
#
# THE DECISIVE POINT:
#   A naive counterexample exists as a HYPERGRAPH. On n = 6 with
#   violated set { {0,1,2}, {3,4,5} }, the 3|3 cut gives v_cross = 0
#   while every singleton gives 1. Statement (P) would be false.
#   BUT that set is not a two-graph: the 4-subset {0,1,2,3} contains
#   exactly ONE violated triangle, an odd number. Violated sets of
#   signed complete graphs are two-graphs -- every 4-subset contains
#   an EVEN number of violated triangles -- so the configuration is
#   not a realisable PDL universe.
#
#   CONJECTURED MECHANISM: it is the PARITY CONDITION, and nothing
#   else, that forces the selection onto singletons. This script
#   tests that attribution directly.
#
# METHOD -- why the contrast must be SIZE-MATCHED:
#   Comparing two-graphs against uniformly random hypergraphs would
#   be confounded: two-graphs do not have the size distribution of
#   random hypergraphs. If violations occurred only at sizes
#   two-graphs cannot reach, parity would be credited with a mere
#   size effect. Hypergraphs are therefore sampled at EXACTLY the
#   sizes two-graphs attain, size by size.
#
# REPRESENTATION:
#   Triangles are indexed; a triangle set is an integer bitmask.
#   mono(S) = popcount(Delta & monomask[S]). Parity is checked with
#   quadmask[Q] over all 4-subsets. Exact integer arithmetic only.
#
# Standard library only: itertools, random.
#
# PDL verrouillage protocol: execute independently in Google Colab
# and return the full output BEFORE any LaTeX drafting.
#
# Author: Cedric Laubscher
# Date:   August 2026
# ============================================================

import itertools
import random
from itertools import combinations

print("=" * 70)
print("PDL_pulsation_regimes_script5.py")
print("Is PARITY the cause? The singleton obstruction for v_cross")
print("=" * 70)
print()

try:
    (1).bit_count()
    def pc(x):
        return x.bit_count()
except AttributeError:
    def pc(x):
        return bin(x).count("1")


# ============================================================
# Setup
# ============================================================

def build(n):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    eidx = {e: k for k, e in enumerate(edges)}
    tris = list(combinations(range(n), 3))
    tidx = {T: k for k, T in enumerate(tris)}

    # cuts modulo complementation, proper and non-empty
    cuts = []
    for k in range(1, n // 2 + 1):
        for c in combinations(range(n), k):
            S = frozenset(c)
            if 2 * k == n and 0 not in S:
                continue
            cuts.append(S)

    monomask = {}
    for S in cuts:
        mask = 0
        for T in tris:
            inside = sum(1 for v in T if v in S)
            if inside == 0 or inside == 3:
                mask |= 1 << tidx[T]
        monomask[S] = mask

    quadmasks = []
    for Q in combinations(range(n), 4):
        mask = 0
        for T in combinations(Q, 3):
            mask |= 1 << tidx[T]
        quadmasks.append(mask)

    return edges, eidx, tris, tidx, cuts, monomask, quadmasks


def eid(eidx, a, b):
    return eidx[(a, b)] if a < b else eidx[(b, a)]


def violated_mask(s, tris, tidx, eidx):
    m = 0
    for T in tris:
        if s[eid(eidx, T[0], T[1])] * s[eid(eidx, T[0], T[2])] \
                * s[eid(eidx, T[1], T[2])] == -1:
            m |= 1 << tidx[T]
    return m


def class_reps(n, edges, eidx):
    """One representative per switching class: edges at vertex 0 positive."""
    free = [k for k, (i, j) in enumerate(edges) if i != 0]
    for bits in itertools.product([1, -1], repeat=len(free)):
        s = [1] * len(edges)
        for k, b in zip(free, bits):
            s[k] = b
        yield tuple(s)


def is_two_graph(D, quadmasks):
    return all(pc(D & q) % 2 == 0 for q in quadmasks)


def argmin_sizes(D, cuts, monomask):
    """Sizes of the cuts attaining min v_cross (= max mono)."""
    best, arg = -1, []
    for S in cuts:
        mv = pc(D & monomask[S])
        if mv > best:
            best, arg = mv, [S]
        elif mv == best:
            arg.append(S)
    n_all = max(max(S) for S in cuts) + 1
    sizes = sorted({min(len(S), n_all - len(S)) for S in arg})
    return sizes, len(arg), best


# ============================================================
# PART 1 -- Violated sets of switching classes ARE two-graphs
# ============================================================
print("PART 1 -- Violated-triangle sets of switching classes = two-graphs")
print("-" * 70)

TWOGRAPHS = {}
for n in range(4, 8):
    edges, eidx, tris, tidx, cuts, monomask, quadmasks = build(n)
    seen = set()
    for s in class_reps(n, edges, eidx):
        seen.add(violated_mask(s, tris, tidx, eidx))
    all_parity = all(is_two_graph(D, quadmasks) for D in seen)
    expected = 2 ** ((n - 1) * (n - 2) // 2)
    TWOGRAPHS[n] = (sorted(seen), build(n))
    print(f"  n = {n}: distinct violated sets = {len(seen):6d}  "
          f"(expected 2^C(n-1,2) = {expected:6d})  match = "
          f"{len(seen) == expected}")
    print(f"         all satisfy the 4-subset parity condition: {all_parity}")
print()
print("  This is the classical two-graph correspondence. It is the ONLY")
print("  constraint distinguishing realisable violated sets from")
print("  arbitrary triangle sets.")
print()


# ============================================================
# PART 2 -- Statement (P) on all two-graphs
# ============================================================
print("PART 2 -- (P): is min v_cross attained at a singleton, for every")
print("         non-empty two-graph?")
print("-" * 70)
print(f"  {'n':>3s} {'two-graphs':>11s} {'non-empty':>10s} "
      f"{'min at size 1':>14s} {'ONLY size 1':>12s} {'violations':>11s}")

for n in range(4, 8):
    Ds, (edges, eidx, tris, tidx, cuts, monomask, quadmasks) = TWOGRAPHS[n]
    ne = [D for D in Ds if D != 0]
    at1, only1, viol = 0, 0, []
    for D in ne:
        sizes, _, _ = argmin_sizes(D, cuts, monomask)
        if 1 in sizes:
            at1 += 1
        if sizes == [1]:
            only1 += 1
        else:
            viol.append((D, sizes))
    print(f"  {n:3d} {len(Ds):11d} {len(ne):10d} {at1:14d} {only1:12d} "
          f"{len(ne) - only1:11d}")
    TWOGRAPHS[n] = (Ds, (edges, eidx, tris, tidx, cuts, monomask, quadmasks))
    if viol:
        print(f"        FIRST VIOLATIONS (D, argmin sizes): {viol[:3]}")
print()
print("  If 'ONLY size 1' equals 'non-empty' for every n, statement (P)")
print("  holds in the strong form on the whole tested range.")
print()


# ============================================================
# PART 3 -- SIZE-MATCHED contrast: two-graphs vs free hypergraphs
# ============================================================
print("PART 3 -- Size-matched contrast. Does removing PARITY create")
print("         violations at the SAME sizes?")
print("-" * 70)

random.seed(20260811)
SAMPLES = 4000

for n in (5, 6, 7):
    Ds, (edges, eidx, tris, tidx, cuts, monomask, quadmasks) = TWOGRAPHS[n]
    ntri = len(tris)
    sizes_present = sorted({pc(D) for D in Ds if D != 0})
    print(f"  --- n = {n}: {ntri} triangles, two-graph sizes "
          f"{sizes_present} ---")
    print(f"      {'|D|':>5s} {'two-graphs':>11s} {'tg violating':>13s} "
          f"{'free sampled':>13s} {'free violating':>15s} {'rate':>8s}")
    for v in sizes_present:
        tg = [D for D in Ds if pc(D) == v]
        tgv = 0
        for D in tg:
            sizes, _, _ = argmin_sizes(D, cuts, monomask)
            if sizes != [1]:
                tgv += 1
        fv, ns = 0, min(SAMPLES, 4000)
        for _ in range(ns):
            idxs = random.sample(range(ntri), v)
            D = 0
            for i in idxs:
                D |= 1 << i
            sizes, _, _ = argmin_sizes(D, cuts, monomask)
            if sizes != [1]:
                fv += 1
        print(f"      {v:5d} {len(tg):11d} {tgv:13d} {ns:13d} {fv:15d} "
              f"{100.0 * fv / ns:7.1f}%")
    print()

print("  READING: if the 'tg violating' column is 0 everywhere while")
print("  'free violating' is substantial AT THE SAME SIZES, then parity")
print("  -- not size -- is what forces the selection onto singletons.")
print("  If free hypergraphs also almost never violate, then parity is")
print("  NOT the mechanism and the conjectured proof strategy is wrong.")
print()


# ============================================================
# PART 4 -- Do violating hypergraphs always fail parity?
# ============================================================
print("PART 4 -- Every violating hypergraph must fail the parity condition")
print("-" * 70)

for n in (5, 6):
    Ds, (edges, eidx, tris, tidx, cuts, monomask, quadmasks) = TWOGRAPHS[n]
    ntri = len(tris)
    if ntri > 20:
        continue
    tot, viol, viol_parity_ok = 0, 0, 0
    minimal = []
    for D in range(1, 2 ** ntri):
        tot += 1
        sizes, _, _ = argmin_sizes(D, cuts, monomask)
        if sizes != [1]:
            viol += 1
            if is_two_graph(D, quadmasks):
                viol_parity_ok += 1
            if len(minimal) < 3 and pc(D) <= 3:
                Ts = [tris[i] for i in range(ntri) if (D >> i) & 1]
                odd = [Q for Q, q in zip(combinations(range(n), 4), quadmasks)
                       if pc(D & q) % 2 == 1]
                minimal.append((Ts, sizes, odd[:2]))
    print(f"  n = {n}: all {tot} non-empty triangle sets enumerated")
    print(f"         violating (min not exclusively at singletons): {viol}")
    print(f"         of which ALSO two-graphs: {viol_parity_ok}")
    print(f"         CHECK -- no violating set is a two-graph: "
          f"{viol_parity_ok == 0}")
    for Ts, sizes, odd in minimal:
        print(f"         example {Ts} -> argmin sizes {sizes}; "
              f"odd 4-subsets e.g. {odd}")
print()


# ============================================================
# PART 5 -- The proved case k <= 2, and the gap at k >= 3
# ============================================================
print("PART 5 -- Proved case (k <= 2) and the unproved case (k >= 3)")
print("-" * 70)

for n in (5, 6, 7):
    Ds, (edges, eidx, tris, tidx, cuts, monomask, quadmasks) = TWOGRAPHS[n]
    ne = [D for D in Ds if D != 0]
    ok2, gaps = 0, {}
    for D in ne:
        m1 = max(pc(D & monomask[S]) for S in cuts if len(S) == 1)
        big = [S for S in cuts if 3 <= len(S) <= n - 3]
        if not big:
            ok2 += 1
            continue
        m3 = max(pc(D & monomask[S]) for S in big)
        g = m1 - m3
        gaps[g] = gaps.get(g, 0) + 1
        if g > 0:
            ok2 += 1
    print(f"  n = {n}: two-graphs where singletons STRICTLY beat all cuts")
    print(f"         of size >= 3 : {ok2} / {len(ne)}")
    if gaps:
        print(f"         gap (best singleton - best large cut) -> count: "
              + ", ".join(f"{k}->{gaps[k]}" for k in sorted(gaps)))
print()
print("  A gap that is always strictly positive is the quantitative")
print("  content of the missing proof. A gap of 0 anywhere marks the")
print("  exact configurations the proof must handle.")
print()

print("=" * 70)
print("WHAT THIS SCRIPT DECIDES")
print("=" * 70)
print("  Part 1: the two-graph correspondence, verified.")
print("  Part 2: statement (P) on every two-graph up to n = 7.")
print("  Part 3: SIZE-MATCHED attribution of the effect to parity.")
print("  Part 4: exhaustive check that no violating set is a two-graph.")
print("  Part 5: the numerical gap the general proof must reproduce.")
print()
print("  If Part 3 shows free hypergraphs violating at the same sizes")
print("  where two-graphs never do, the proof strategy is confirmed and")
print("  the theorem should be provable from parity alone.")
print("=" * 70)
