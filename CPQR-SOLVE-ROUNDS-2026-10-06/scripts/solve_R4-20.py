"""R4-20: DM/baryon = 50/9 vs Planck.
Claimed: 5.464+-0.062 -> 1.48 sigma (Planck 2020).
REALITY: 5.464 does not match any Planck release.
  Planck 2018 PR3: 5.364+-0.065 -> 2.96 sigma
  Planck PR4 TTTEEE: 5.337+-0.062 -> 3.51 sigma
  PR4+lensing+nonCMB: 5.291+-0.047 -> 5.69 sigma
The 1.48sigma claim is WRONG. Tension is ~3sigma (not fatal, but not a hit).
Sector assignment (which 3 is baryonic) remains unjustified.
"""
import math
target=50/9
for name,oc,s_oc,ob,s_ob in [
  ("PR3 2018",0.1200,0.0012,0.02237,0.00015),
  ("PR4 TTTEEE",0.1188,0.0012,0.02226,0.00013),
  ("PR4+lensing+nonCMB",0.11804,0.00082,0.02231,0.00012)]:
    r=oc/ob; s=r*math.sqrt((s_oc/oc)**2+(s_ob/ob)**2)
    print(f"{name}: {r:.4f}+-{s:.4f} vs 50/9: {abs(target-r)/s:.2f}sigma")
print("R4-20: 1.48sigma claim REFUTED. Real: ~3sigma. PARTIAL (mechanism interesting, stats wrong).")
