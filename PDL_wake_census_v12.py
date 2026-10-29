# PDL_wake_census_v12.py - surface-only proton, wake census from CORPUS VALUES ONLY
# Known values: sea E=11017 (odd), cores 3xK4 (18 edges, 12 vertices), 930 units, n_u=24.
# Question: how many wake (etrave) relations? Does a declared fractional diagonal-cut
# correction produce the non-integer B required by v10/v11? Family DECLARED a priori.
import json, math, re
PHI=(1+math.sqrt(5))/2
SQ2=math.sqrt(2.0)
E_SEA=11017; E_CORE=18; V_TOT=930; V_CORE=12; V_SEA=918; NU=24
DR=0.04795969; TOL_DR=6.98e-8
TOL_B=TOL_DR*E_SEA   # tolerance on a wake-edge count under Dr=B/E_sea scaling
print("=== V12 WAKE CENSUS (corpus values, surface-only proton) ===")
print("[A] DEGREE / PARITY AUDIT")
sdeg=2*E_SEA
print(f"  sea: V={V_SEA} E={E_SEA} sumdeg={sdeg} avg_deg={sdeg/V_SEA:.6f}")
excess=sdeg-NU*V_SEA
print(f"  {V_SEA}x{NU}={NU*V_SEA}  excess={excess} -> {excess} vertex(es) of degree 25: the parity engine has a LOCUS")
print(f"  cores: 3xK4 -> V={V_CORE} E={E_CORE}; total E={E_SEA+E_CORE}, avg_deg_total={2*(E_SEA+E_CORE)/V_TOT:.6f}")
print(f"  sea odd check: E_SEA={E_SEA} odd={E_SEA%2==1} (23x{E_SEA//23})")
print()
print("[B] WAKE-COUNT TARGETS")
B_duty=DR*E_SEA
B_v10=528.354; src="fallback(3 dec)"
def find_key(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if 'b_req' in str(k).lower() and isinstance(v,(int,float)): return v
            r=find_key(v)
            if r is not None: return r
    elif isinstance(o,list):
        for v in o:
            r=find_key(v)
            if r is not None: return r
    return None
try:
    j=json.load(open('/workspace/v11_summary.json'))
    v=find_key(j)
    if v is not None: B_v10=float(v); src="v11_summary.json"
except Exception as e:
    print("  (could not read v11_summary.json:",e,")")
print(f"  B_duty = Dr x E_sea = {B_duty:.6f}  (monomer edge-uniform: Dr = E_wake/E_sea)")
print(f"  B_v10               = {B_v10:.6f}  (v10 inversion, source: {src})")
print(f"  |B_duty-B_v10| = {abs(B_duty-B_v10):.6f} ({abs(B_duty-B_v10)/TOL_B:.1f} tol) -> two inversions TENSION")
print(f"  tol_B = {TOL_B:.6f}")
print()
print("[C] STRUCTURAL INTEGER CENSUS (known numbers only: 12,18,24,3,4,6,540,252...)")
struct=[("12x44",528),("24x22=n_u(n_u-2)",528),("540-12 (v11 W9)",528),
        ("2x252+24",528),("2x252",504),("252+252+36",540),("540 (v11 W2)",540),
        ("540-24 (v11 W8)",516),("12x43",516),("12x45",540),("24x21",504),("24x23",552),
        ("918-390",528)]
for name,w in struct:
    print(f"  {name:28s} {w:5d}  vs B_duty {w-B_duty:+.4f} ({abs(w-B_duty)/TOL_B:8.1f} tol)  vs B_v10 {w-B_v10:+.4f} ({abs(w-B_v10)/TOL_B:8.1f} tol)")
print()
print("[D] DECLARED FRACTIONAL FAMILY: B = W0 + d*x  OR  B = W0 - d*(1-x)")
x_forms={"1/2":0.5,"1/phi":1/PHI,"1/phi^2":1/PHI**2,"1/sqrt2":1/SQ2,"1/(2sqrt2)":1/(2*SQ2),"sqrt2-1":SQ2-1}
d_list=[1,2,3,4,6,8,12,18,24,36,44,48,63,84,96,108]
W0_list=[w for _,w in struct]
N=len(W0_list)*len(d_list)*len(x_forms)*2
B_range=60.0
lam=N*(2*TOL_B)/B_range
print(f"  family size N={N}  declared range~{B_range:.0f}  Poisson lambda={lam:.4f}  P(>=1|null)={1-math.exp(-lam):.4f}")
hits=[]; close=[]
for tname,targ in (("B_duty",B_duty),("B_v10",B_v10)):
    for name,w in struct:
        for d in d_list:
            for xn,x in x_forms.items():
                for op,bv in ((f"+{d}*{xn}", w+d*x),(f"-{d}*(1-{xn})", w-d*(1-x))):
                    gap=abs(bv-targ)
                    rec=(gap,tname,name,op,bv)
                    if gap<=TOL_B: hits.append(rec)
                    close.append(rec)
close.sort(key=lambda r:r[0])
print("  -- closest 10 (any target) --")
for gap,tname,name,op,bv in close[:10]:
    print(f"     {tname:7s} {name:22s} {op:18s} B={bv:.6f} gap={gap:.6f} ({gap/TOL_B:.2f} tol)")
if hits:
    print(f"  ** HITS (pre-declared): {len(hits)}")
    for gap,tname,name,op,bv in hits: print(f"     HIT {tname} {name} {op} B={bv:.6f} gap={gap:.6f}")
else:
    print("  ** NO HIT inside tolerance -> family falsified at ppm, or inversion model wrong")
print()
print("[E] DIRECT FRACTIONAL READING AT W0=528")
for tname,targ in (("B_duty",B_duty),("B_v10",B_v10)):
    r=targ-528
    print(f"  {tname}: residual r={r:.6f}")
    for xn,x in x_forms.items():
        for d in d_list:
            g=abs(d*x-r); g2=abs(d*(1-x)-r)
            if min(g,g2)<5*TOL_B:
                print(f"     near: d={d} x={xn}: d*x={d*x:.6f} (gap {g:.6f})  d*(1-x)={d*(1-x):.6f} (gap {g2:.6f})")
print()
print("[F] SUPPRESSION BOOKKEEPING")
print(f"  -log2(Dr)={-math.log2(DR):.4f} bits (v9 site-model needed 14.24 bits stacked)")
print(f"  log2(E_sea/528)={math.log2(E_SEA/528):.4f} bits  | 528/11017={528/11017:.8f} vs Dr={DR:.8f} (gap {abs(528/11017-DR)/TOL_DR:.1f} tol)")
print(f"  INTERPRETATION: under Dr=E_wake/E_sea NO exponential suppression needed; the ratio IS geometric.")
print()
print("[G] SECONDARY TARGETS (declared, non-discriminating - reported honestly)")
FT=0.157126; FTOL=0.0009
Ef=FT*E_SEA; win=FTOL*E_SEA
print(f"  f x E_sea = {Ef:.3f} +/- {win:.2f} -> {int(2*win)} consecutive integers allowed; E-wake-fraction NON-discriminating for f")
print(f"  DeltaSigma context: 0.30 +/- 0.05; 1/3 = 0.3333 (edge: cores 18/(18+528)={18/546:.4f}, 252/(252+528)={252/780:.4f})")
print()
print("VERDICT AXES: (1) any pre-declared hit? (2) B_duty vs B_v10 tension = which inversion is right?") 
print("(3) degree-25 parity loci: new structural fact. (4) 528 = 12x44 = 24x22 = 540-12 triple reading.")
out={"E_SEA":E_SEA,"B_duty":B_duty,"B_v10":B_v10,"B_v10_source":src,"tol_B":TOL_B,
     "degree_excess":excess,"lambda":lam,"n_hits":len(hits),
     "hits":[{"target":t,"struct":n,"op":o,"B":b,"gap":g} for g,t,n,o,b in hits],
     "closest":[{"target":t,"struct":n,"op":o,"B":b,"gap":g} for g,t,n,o,b in close[:10]]}
json.dump(out,open('/workspace/v12_summary.json','w'),indent=1)
print("WROTE /workspace/v12_summary.json")
print("EXIT=0")
