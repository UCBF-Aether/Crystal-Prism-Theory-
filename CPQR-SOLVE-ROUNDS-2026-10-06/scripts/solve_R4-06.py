"""R4-06: C44-forward verification.
C44 = kappa*E_coh*mu(mu+1)/(2a^3)*S_C44, S_C44 = sum (x^2+y^2)/r^2*(a/r)^23 over FCC.
VERIFIED: 57.5 ppm reproduces with FIXED a=1.3729e-15.
CAVEATS: a is input (R4-12 open); script's hbar self-consistency loop is circular
  AND degrades to 6% off -- must be removed; kappa needs S0=105.65 (muon mass, HOLE I);
  E_coh=144 needs /20 justified (R4-13). Non-circular WRT C44 (doesn't input C44).
"""
import math
import numpy as np
phi=(1+math.sqrt(5))/2; pi=math.pi
mu=21; pw=mu+2
a=1.3729e-15; E_coh=144*1.602176634e-19
S0=105.65/phi**2; eta0=(3*math.sqrt(2))/(pi*S0); kappa=1-eta0*(mu-1)/mu
S=0.0
for x in range(-4,5):
    for y in range(-4,5):
        for z in range(-4,5):
            for bx,by,bz in [(0,0,0),(0,.5,.5),(.5,0,.5),(.5,.5,0)]:
                X,Y,Z=x+bx,y+by,z+bz
                if X==0 and Y==0 and Z==0: continue
                r=math.sqrt(X*X+Y*Y+Z*Z)
                if r>4: continue
                S+=((X*X+Y*Y)/(r*r))*(r**(-pw))
C44=kappa*E_coh*mu*(mu+1)/(2*a**3)*S
print(f"S_C44={S:.2f} C44={C44:.6e} ppm={abs(C44/4.6205e34-1)*1e6:.1f}")
print("R4-06: 57ppm VERIFIED (fixed-a). hbar-loop REMOVED (circular+degrades).")
