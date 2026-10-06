"""PART 3: the 6-axis correspondence + t=1 shell inventory, both exact."""
import math, sys
from itertools import combinations
from collections import defaultdict
sys.path.insert(0,'.')
from e8proj import build, at, udirs
PHI=(1+5**0.5)/2
shells,_=build()
# r=1.0 pair centers -> 6 axes?
r1=at(shells,1.0); n=len(r1); used=set(); ctr=[]
for i in range(n):
    if i in used: continue
    j=min((k for k in range(n) if k!=i and k not in used),key=lambda k:round(math.dist(r1[i],r1[k]),9))
    used.add(i); used.add(j); ctr.append(tuple((r1[i][q]+r1[j][q])/2 for q in range(3)))
# axes: pair up antipodal centers
axes=[]; used=set()
for i in range(len(ctr)):
    if i in used: continue
    for j in range(i+1,len(ctr)):
        if j in used: continue
        ci=ctr[i]; cj=ctr[j]
        if abs(sum(ci[q]*cj[q] for q in range(3))+
               math.dist(ci,(0,0,0))*math.dist(cj,(0,0,0)))<1e-9:
            axes.append(ci); used.add(i); used.add(j); break
print("r=1.0: 12 pair-centers ->", len(axes), "axes")
D110=[[v/2**0.5 for v in q] for s1 in(-1.,1.) for s2 in(-1.,1.) for q in((s1,s2,0.),(s1,0.,s2),(0.,s1,s2))]
def mx(A,B):
    def U(p):
        r=math.dist(p,(0.,0.,0.)); return [v/r for v in p]
    A=[U(p) for p in A]; B=[U(p) for p in B]
    return max(abs(sum(a*b for a,b in zip(x,y))) for x in A for y in B)
print("6 axes vs FCC <110>: max|cos| =", round(mx(axes,D110),6))
# five-fold axes (0,+-1,+-phi) -> the same 6 <110> under phi->1: show axis SET equality
ax_phi=[]
for s1 in(-1.,1.):
    for s2 in(-1.,1.):
        ax_phi += [(0.,s1,s2*PHI)]
# normalize pair into 6 axes and compare direction sets
def axis_set(pts):
    S=set()
    for p in pts:
        r=math.dist(p,(0.,0.,0.)); u=tuple(round(v/r,9) for v in p)
        neg=tuple(round(-v,9) for v in u)
        S.add(min(u,neg))
    return S
A1=axis_set(ax_phi)
ax1=[]
for s1 in(-1.,1.):
    for s2 in(-1.,1.):
        ax1 += [(0.,s1,s2*1.0)]
A2=axis_set(ax1); A3=axis_set(axes)
print("5-fold axes -> <110> axes under phi->1: set equal =", A2==axis_set(D110))
print("137 r=1.0 axes == <110> axes: set equal =", A3==axis_set(D110))
# t=1 map shells inventory
d=math.sqrt(2); R=[]
for i,j in combinations(range(8),2):
    for si in(-1.,1.):
        for sj in(-1.,1.):
            x=[0.]*8; x[i]=si; x[j]=sj; R.append(tuple(x))
for b in range(256):
    if bin(b).count('1')%2==0: R.append(tuple(0.5 if (b>>i)&1 else -0.5 for i in range(8)))
P=set()
for x in R:
    P.add((round((x[0]+x[4])/d,9),round((x[1]+x[5])/d,9),round((x[2]+x[6])/d,9)))
P.add((0.,0.,0.)); S=defaultdict(list)
for p in P: S[round(math.dist(p,(0.,0.,0.)),6)].append(p)
print("\nt=1 (1/1) map: shells (r -> n):")
for k in sorted(S): print(f"  {k:.6f} -> {len(S[k])}")
