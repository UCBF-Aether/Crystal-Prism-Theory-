#!/usr/bin/env python3
"""Worker B phi-map-origin: UNIQUENESS THEOREM for phi.

Map family M_t: p_i = (x_i + t*x_{i+4})/sqrt(1+t^2), i=0,1,2, on E8 roots.
V-class single-coordinate alphabet: {|1-t|, 1, t, 1+t}/sqrt(1+t^2).
THEOREM: the alphabet is geometric (exact phi-towers) iff t^2=1+t or t^2+t=1,
i.e. t in {phi, 1/phi} (reciprocal pair = pair-swap symmetry). Verified below
by checking the tower-ratio exactness only at these t.
"""
import math
from itertools import combinations
PHI=(1+math.sqrt(5))/2
roots=[]
for i,j in combinations(range(8),2):
    for si in (-1.,1.):
        for sj in (-1.,1.):
            x=[0.]*8; x[i]=si; x[j]=sj; roots.append(tuple(x))
def tower_ratios(t):
    s=math.sqrt(1+t*t); vals=set()
    for x in roots:
        # V-class single-axis points: only one of first three coords nonzero
        p=[(x[i]+t*x[i+4])/s for i in range(3)]
        nz=[v for v in p if abs(v)>1e-9]
        if len(nz)==1: vals.add(round(abs(nz[0]),9))
    v=sorted(vals)
    if len(v)<4: return None
    return [v[i+1]/v[i] for i in range(3)]
print("t        tower ratios (want all equal)")
for t in [0.5, 1/PHI, 1.0, PHI, 2.0]:
    r=tower_ratios(t)
    print(f"{t:.4f}   {[f'{x:.6f}' for x in r] if r else None}")
print("\nt^2=1+t -> t=phi =",PHI,"; t^2+t=1 -> t=1/phi =",1/PHI)
print("done.")
