"""PART 2: rational approximants t=p/q of the 137 map M_t.
Convergents of phi: 1/1, 2/1, 3/2, 5/3, 8/5, 13/8 -> phi.
For each t: image of 240 E8 roots, # distinct points, shell count.
Also: 6 five-fold axes under t -> check vs <110> and vs 137's r=1.0 pair axes.
"""
import math
from itertools import combinations
from collections import defaultdict
from fractions import Fraction
def build_map(t):
    d=math.sqrt(1+t*t)  # normalization analogous to sqrt(2+phi)
    R=[]
    for i,j in combinations(range(8),2):
        for si in (-1.,1.):
            for sj in (-1.,1.):
                x=[0.]*8; x[i]=si; x[j]=sj; R.append(tuple(x))
    for b in range(256):
        if bin(b).count('1')%2==0:
            R.append(tuple(0.5 if (b>>i)&1 else -0.5 for i in range(8)))
    P=set()
    for x in R:
        P.add((round((x[0]+t*x[4])/d,9),round((x[1]+t*x[5])/d,9),round((x[2]+t*x[6])/d,9)))
    P.add((0.,0.,0.))
    S=defaultdict(list)
    for p in P: S[round(math.dist(p,(0.,0.,0.)),6)].append(p)
    return P,S
print("t        #pts  #shells")
for t in [1.0, 2.0, 1.5, 5/3, 8/5, 13/8, (1+5**0.5)/2]:
    P,S=build_map(t)
    print(f"{t:.6f}  {len(P):4d}  {len(S):3d}")
# five-fold axes under t
print("\n6 five-fold axes (0,1,t)-type under t -> vs FCC <110>:")
D110=[[v/2**0.5 for v in q] for s1 in(-1.,1.) for s2 in(-1.,1.) for q in((s1,s2,0.),(s1,0.,s2),(0.,s1,s2))]
def mx(A,B):
    def U(p):
        r=math.dist(p,(0.,0.,0.)); return [v/r for v in p]
    A=[U(p) for p in A]; B=[U(p) for p in B]
    return max(abs(sum(a*b for a,b in zip(x,y))) for x in A for y in B)
for t in [1.0, (1+5**0.5)/2]:
    ax=[]
    for s1 in(-1.,1.):
        for s2 in(-1.,1.):
            ax += [(0.,s1,s2*t),(s1,s2*t,0.),(s1*t,0.,s2)]
    # 12 axis endpoints -> 6 axes; just check the 12 directions
    print(f"  t={t:.4f}: max|cos| vs <110> = {mx(ax,D110):.6f}")
