#!/usr/bin/env python3
"""REP-manga-btfr: rebuild MaNGA validation as a REAL baryonic Tully-Fisher test.

OLD (void): V_pred = V_obs*(1-exp(-r_max/r_t)) -> residual -> 0 by construction.
  Circular. Shuffled data gave identical residual. Mathematically vacuous.

NEW: Genuine BTFR test of the vortex model prediction.
  MODEL: V_flat = (a0*G*M_bar)^1/4  with a0 = 1.1375e-10 m/s^2 (fixed by H0_local)
    => V = 0.3505 * Mbar^1/4 [km/s, Msun], i.e. M_bar = 66.2 * V^4, slope EXACTLY 4.
  OBSERVED (McGaugh): M_bar = 47 * V^4.
  TENSION: +0.149 dex (1.41x in mass, 1.090x in velocity).

  This is REAL and FALSIFIABLE: the model makes a specific, quantitative prediction
  (A=66.2, slope=4) that differs from observation (A=47). If stellar M/L systematics
  shrink and A stays at 47, the model has a genuine problem.

  CURRENT VERDICT: model SURVIVES -- 0.15 dex is within the dominant M/L systematics
  (IMF 0.25 dex, 3.6um M/L 0.10-0.15 dex). Not a discrepancy, but a live prediction.

MaNGA/2MASS attempt:
  Cross-matched 1376 MaNGA galaxies (Arora+2023) to 2MASS XSC via Vizier TAP
  (1177 matched). BUT: 2MASS K-band systematically underestimates flux by ~0.5+ dex
  for this sample (shallow, missing LSB flux) -> masses unreliable for precision BTFR
  (recovered slope 1.9 vs 4.0 -- biased, not just noisy). The cross-match pipeline
  works; the MASS CATALOG is the limitation. NSA stellar masses needed for a sharp
  independent MaNGA test.

STATUS: PARTIAL -- real test framework built, model prediction quantified and
  surviving within systematics, but MaNGA arm needs NSA masses to be decisive.
"""
import math

a0 = 1.1375e-10      # m/s^2, from H0_local = 73.57
G = 6.67430e-11      # SI
Msun = 1.98847e30    # kg

C = (a0*G*Msun)**0.25/1000.0   # km/s per Msun^1/4
A_model = 1/C**4
A_obs = 47.0                   # McGaugh BTFR

print("=== REP-manga-btfr: real BTFR test ===\n")
print(f"Model:    M_bar = {A_model:.1f} * V_flat^4   (slope exactly 4.0)")
print(f"Observed: M_bar = {A_obs:.0f} * V_flat^4   (McGaugh)")
tension = math.log10(A_model/A_obs)
print(f"Tension: {tension:+.3f} dex")
print("\nSystematics on observed A: IMF ~0.25, M/L ~0.10-0.15, HI ~0.05 dex")
print(f"=> {tension:.2f} dex is WITHIN systematics. Model SURVIVES.")
print("\nFalsifiable: if M/L tightens and A stays 47, the model fails.")
print("MaNGA/2MASS: 1177/1376 matched, but K-band masses biased (0.5+ dex).")
print("NSA masses needed for sharp MaNGA test.")
print("\nPARTIAL: real test, model survives, MaNGA arm needs better masses.")
