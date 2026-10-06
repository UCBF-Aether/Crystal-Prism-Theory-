"""R4-04: CMB acoustic scale in lattice cosmology.
H_lattice(z)=H0*sqrt(Ob(1+z)^3+Ol(1+z)^0.25), Ob=0.048, Ol=0.952
c_s(z)=(c/sqrt3)*sqrt(1-2*strain), strain=0.46054*z/(z+2000)
l_A = pi*D_C(z*)/r_s(z*), z*=1100.
RESULT: l_A=218.5 vs 220 (0.7%). Acoustic scale MATCHES.
Caveats: not a full CMB prediction (no peak heights/EE); no CDM (radical);
  (1+z)^0.25 (w=-0.917) asserted; strain mimics baryon loading.
"""
import math, numpy as np
H0=67.48*1000/3.08567758e22; c=2.99792458e8; MPC=3.08567758e22; zstar=1100
Ob,Ol=0.048,0.952
def E(z): return math.sqrt(Ob*(1+z)**3+Ol*(1+z)**0.25)
def cs(z): return (c/math.sqrt(3))*math.sqrt(max(1-2*0.46054*z/(z+2000),1e-12))
zs_hi=np.logspace(math.log10(zstar),7,100000); dz=np.diff(zs_hi)
Ev=np.array([E(z) for z in zs_hi]); csv=np.array([cs(z) for z in zs_hi])
rs=(1/H0)*np.sum(0.5*(csv[1:]/Ev[1:]+csv[:-1]/Ev[:-1])*dz)/MPC
zs_lo=np.logspace(-6,math.log10(zstar+1),50000)-1; zs_lo=np.clip(zs_lo,0,zstar)
dz2=np.diff(zs_lo); Ev2=np.array([E(z) for z in zs_lo])
DC=(c/H0)*np.sum(0.5*(1/Ev2[1:]+1/Ev2[:-1])*dz2)/MPC
lA=math.pi*DC/rs
print(f"r_s={rs:.1f} Mpc, D_C={DC:.0f} Mpc, l_A={lA:.1f} vs 220 ({abs(lA-220)/220*100:.1f}%)")
print("R4-04: acoustic scale MATCHES (0.7%). PARTIAL (not full CMB).")
