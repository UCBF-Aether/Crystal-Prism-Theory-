"""Worker E (alpha-select): hunt for CPQR-native selection rules for delta.
Geometric exponent sets stated BEFORE searching; exhaustive +-1 combos."""
import math, itertools
PHI=(1+math.sqrt(5))/2
DELTA=137.035999084-137
TOL=DELTA*1e-6
GEO_SETS={
 "tower_rungs": [1,2,3],
 "oct_degrees": [2,4,6],
 "oct_exponents": [1,3,5],
 "power_orders": [2,4,6,8],
 "hidden_coords": [3,7],
 "populations": [6,8,12,24],
}
U=sorted(set().union(*GEO_SETS.values()))
vals={n:PHI**(-n) for n in U}
print(f"delta={DELTA:.10f} tol={TOL:.2e} union={U}")
hits=0
for r in (1,2,3,4):
    for combo in itertools.combinations(U,r):
        for signs in itertools.product((1,-1),repeat=r):
            if abs(sum(s*vals[n] for s,n in zip(signs,combo))-DELTA)<TOL:
                hits+=1; print("HIT",combo,signs)
print("union +-1 hits (<=4 terms):",hits)
# per-component with rigorous 128/8/1 coefficients
hits=0
for a in U:
    for b in U:
        for c in U:
            s=128*vals[a]+8*vals[b]+vals[c]
            if abs(s-DELTA)<TOL: hits+=1; print("HIT",a,b,c)
print("per-component hits:",hits)
# control: GSM exponents, native 240 coefficients
g=vals[7]+vals[14]+vals[16]-vals[8]/240+vals[26]
print(f"GSM-exponents/native-240: {g:.10f} rel.err={abs(g-DELTA)/DELTA:.3e}")
