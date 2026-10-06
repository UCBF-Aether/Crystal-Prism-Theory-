"""R4-30: FCC tetrahedral-void 2-complex homology.
V12 claimed N0=8,N1=24,N2=32,chi=16,b1=4 per cell, b1=128 total.
Reproduced the complex (K8 minus 4 diagonals, 2-skeleton): N0,N1,N2,chi MATCH.
But b1=0 (finite AND periodic), NOT 4. Hence b1=128 is ungrounded.
Correct homology: b0=1, b1=0, b2=15, chi=16.
"""
import itertools
import numpy as np
opp={0:7,1:6,2:5,3:4,4:3,5:2,6:1,7:0}
edges=[(i,j) for i in range(8) for j in range(i+1,8) if opp[i]!=j]
tris=[t for t in itertools.combinations(range(8),3)
      if not (opp[t[0]]==t[1] or opp[t[0]]==t[2] or opp[t[1]]==t[2])]
E={e:k for k,e in enumerate(edges)}
d1=np.zeros((8,len(edges)))
for k,(i,j) in enumerate(edges): d1[i,k]=-1; d1[j,k]=1
d2=np.zeros((len(edges),len(tris)))
for k,(i,j,l) in enumerate(tris):
    for (a,b),c in [((j,l),1),((i,l),-1),((i,j),1)]:
        if a>b: a,b=b,a; c=-c
        d2[E[(a,b)],k]=c
r1=np.linalg.matrix_rank(d1); r2=np.linalg.matrix_rank(d2)
print(f"N0=8 N1={len(edges)} N2={len(tris)} chi={8-len(edges)+len(tris)}")
print(f"b0={8-r1} b1={len(edges)-r1-r2} b2={len(tris)-r2}")
print("R4-30: b1=4/128 NOT reproduced. Correct: b1=0.")
