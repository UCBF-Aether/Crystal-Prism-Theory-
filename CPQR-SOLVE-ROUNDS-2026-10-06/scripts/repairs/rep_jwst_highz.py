#!/usr/bin/env python3
"""REP-jwst-highz: rebuild the high-z validation for the a0(z) prediction with REAL data.

PREDICTION: V_flat(z)/V_flat(0) = (H(z)/H0)^(1/4) at fixed M_bar
  -> +15.7% at z=1, +32% at z=2. MOND predicts exactly 1.000.

OLD (void): cited placeholder arXiv IDs, plotted prediction against itself.
NEW: KROSS (Harrison+2017, J/MNRAS/467/1965, 429 rotation-dominated galaxies at z~0.85)
  + KMOS3D literature (Ubler+2017).

TEST: KROSS M* TFR zero-point evolution is -0.41+/-0.08 dex (at fixed V, less M* at z~1).
  Convert to baryonic: dlogM_bar = -0.41 + log10[(1+fz)/(1+f0)]  (gas correction)
  CPQR predicts: dlogM_bar = -log10(H(z)/H0), and for M*:
    dlogM* = log10(1+f0) - log10(H(z)/H0) - log10(1+fz)

RESULT: with standard gas fractions (fz~0.5-1.2 at z~1, f0~0.1-0.3 locally),
  CPQR predicts -0.29 to -0.53 dex; observed -0.41+/-0.08. CONSISTENT.
  KMOS3D bTFR literature is mixed (-0.44 at z~0.9 vs -0.23 predicted;
  -0.27 at z~2.3 vs -0.54 predicted) -- sample-selection sensitive.

VERDICT: PARTIAL. The test is now REAL (not fabricated) and falsifiable.
  KROSS supports the prediction within gas systematics; KMOS3D is mixed.
  The prediction stands, awaiting sharper data (direct high-z HI, larger samples).
"""
import math

def H_ratio(z, Om=0.315):
    return math.sqrt(Om*(1+z)**3 + (1-Om))

print("=== REP-jwst-highz: a0(z) vs real high-z kinematics ===\n")

# CPQR prediction at fixed M_bar
for z in [0.9, 1.0, 2.0, 2.3]:
    boost = H_ratio(z)**0.25
    print(f"z={z}: V(z)/V(0) = {boost:.3f} (+{(boost-1)*100:.1f}%), "
          f"dlogM_bar = {-math.log10(H_ratio(z)):+.3f} dex")

print("\n--- KROSS (Harrison+2017), 429 rot-dom galaxies, z_med~0.85 ---")
print("Observed M* TFR zero-point evolution: -0.41 +/- 0.08 dex")
z=0.9; lh=math.log10(H_ratio(z))
print(f"CPQR predicted M* offset for (fz, f0):")
for fz, f0 in [(0.8,0.2),(1.0,0.2),(0.5,0.3),(1.2,0.1)]:
    d=math.log10(1+f0)-lh-math.log10(1+fz)
    ok="MATCH" if abs(d+0.41)<0.08 else ("close" if abs(d+0.41)<0.16 else "off")
    print(f"  fz={fz}, f0={f0}: {d:+.3f} dex  [{ok}]")

print("\n--- KMOS3D (Ubler+2017) bTFR literature ---")
for z, obs in [(0.9,-0.44),(2.3,-0.27)]:
    pred=-math.log10(H_ratio(z))
    print(f"  z~{z}: observed {obs:+.2f} dex, CPQR {pred:+.3f} dex")

print("\nVERDICT: PARTIAL -- real test, KROSS consistent within gas systematics,")
print("KMOS3D mixed. Prediction falsifiable, not ruled out, not yet sharp.")
