"""R4-10 resolution: Sigma_char 50 vs 99.94.
The 2x is pi vs 2pi in the denominator. The FIT-VALIDATED code uses 2pi.
Cosmic Sigma_char = 50.03 ~= (DM/B)*9 = 50 (v14). Local = 54.54 (SPARC fits).
R4-10's 99.94 (pi version) is erroneous -- not in the code, agrees with nothing.
"""
import math
C=2.99792458e8; PI=math.pi; G=6.674e-11
PC=3.085677581e16; MSUN=1.98847e30; PHI=(1+math.sqrt(5))/2
t_age=13.8e9*365.25*24*3600; H0=((21-1)/21)/t_age
def sig(a0, denom_pi):
    ab=2*a0/math.sqrt(3)
    return (ab/(denom_pi*G))*(12/33)*PC**2/MSUN
a0_cos=C*H0/(2*PI); a0_loc=a0_cos*(1+PHI**-5)
print("cosmic, 2pi (CODE):", round(sig(a0_cos,2*PI),4), "vs v14 (DM/B)*9 = 50")
print("local,  2pi (CODE):", round(sig(a0_loc,2*PI),4), "vs meta.json 54.5376")
print("cosmic, pi (TEXT): ", round(sig(a0_cos,PI),2), "<- R4-10's 99.94: WRONG")
print("R4-10 RESOLVED: no 2x conflict; 99.94 was an erroneous pi-correction.")
