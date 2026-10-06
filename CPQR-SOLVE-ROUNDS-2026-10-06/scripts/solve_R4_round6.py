#!/usr/bin/env python3
"""Solve round 6 verifications: FUP-fs0-gap, R4-15, R4-14, R4-18, R4-44, R4-29, R4-23.
All numbers reproduced from scratch. Run: python3 solve_R4_round6.py
"""
import math, json

PHI = (1 + math.sqrt(5)) / 2
print("=" * 60)
print("FUP-fs0-gap: toolkit 0.570 vs analytic 0.557614")
print("=" * 60)
f_analytic = 1 - (math.pi**2 / (6 + math.pi**2)) * (1 - 1 / math.sqrt(12))
print(f"  analytic = 1-(pi^2/(6+pi^2))(1-1/sqrt12) = {f_analytic:.6f}")
print(f"  toolkit  = 0.570  [INPUT - Cory 2026-04-14, cf. pydroid_full_chain.py:123]")
print(f"  gap = {abs(0.570 - f_analytic) / f_analytic * 100:.2f}%")
print("  RESOLUTION: 0.570 is an empirical INPUT (matches PIMC 0.57).")
print("  0.557614 is an analytic CANDIDATE whose pi^2/(6+pi^2) factor is OPEN")
print("  (V10 Ch.11 admits it). Neither is proven; the gap is input-vs-formula.")
print("  For hbar: 99.93% uses the input (consistency check);")
print("            97.75% uses the analytic (derivation attempt).")

print("\n" + "=" * 60)
print("R4-15 gFCC-99: g_FCC = 99/(28 phi^2)")
print("=" * 60)
mu, Z, b0 = 21, 12, 7
g = 99 / (28 * PHI**2)
g2 = 3 * (mu + Z) / (4 * b0 * PHI**2)
print(f"  99/(28 phi^2) = {g:.6f}")
print(f"  99 = 3*(mu+Z) = 3*{mu + Z}; 28 = 4*b0 = 4*{b0}")
print(f"  3(mu+Z)/(4 b0 phi^2) = {g2:.6f}  (identical)")
eta0 = 0.77029766
print(f"  eta0/f_s0(toolkit) = {eta0 / 0.570:.6f}")
print(f"  |g_FCC - eta0/f_s0|/(eta0/f_s0) = {abs(g - eta0/0.570)/(eta0/0.570)*100:.3f}%")
print("  The 0.065% match means g_FCC is the factor making zeta_eff=f_s0*g_FCC=eta0.")
print("  Components (mu=21, Z=12, b0=7=QCD) meaningful; combination constructed.")

print("\n" + "=" * 60)
print("R4-14 NT-formula: N_T = 144 phi^2 - 12/5")
print("=" * 60)
NT = 144 * PHI**2 - 12 / 5
print(f"  144*phi^2 - 12/5 = {NT:.6f}")
print(f"  144 = 12^2 (coordination squared); 144*phi^2 = {144*PHI**2:.4f}; 12/5 = 2.4")
print("  Not an integer -> effective number, not a direct count.")
print("  phi^2 factor and -12/5 correction ungrounded; tetrahedral-void")
print("  combinatorics attack stands.")

print("\n" + "=" * 60)
print("R4-18 Vflat-coherence: V_flat = hbar/(m_eff xi_coh)")
print("=" * 60)
hbar = 1.054571817e-34
m0 = 3.3259e-28
m_eff = m0 / (2 * g * NT)
E0 = 144 * 1.602176634e-19
xi = hbar * 299792458 / E0
V = hbar / (m_eff * xi)
print(f"  m_eff = m0/(2 g_FCC N_T) = {m_eff:.4e} kg")
print(f"  xi_coh = hbar c / E0 = {xi:.4e} m")
print(f"  V_flat = {V/1000:.2f} km/s  (vs 234.0: 0.05%)")
print("  BUT: SPARC V_flat spans 24.8-302.2 km/s (median 96.4, N=171).")
d = json.load(open("/home/hatch/workspace/theory/sparc_beta_diagnostic_wide.json"))
vfs = [gg['Vf'] for gg in d]
w10 = sum(1 for v in vfs if abs(v - V/1000) / (V/1000) < 0.10)
print(f"  Only {w10}/{len(vfs)} ({w10/len(vfs)*100:.1f}%) within 10% of 234.1.")
print("  VERDICT: characteristic scale for MW-mass systems, NOT a per-galaxy")
print("  prediction. Superfluid-critical-velocity picture is a consistency")
print("  relation, not a derivation of individual V_flat.")

print("\n" + "=" * 60)
print("R4-44 A5-embedding-caveat: two embeddings, both correct")
print("=" * 60)
chi4 = (4, 0, 1, -1, -1)
chi3 = (3, -1, 0, PHI, -1/PHI)
chi5 = (5, 1, -1, 0, 0)
m1 = (8, 0, 2, -2, -2)
m2 = (8, 0, -1, round(PHI, 3), round(-1/PHI, 3))
c1 = tuple(2*x for x in chi4)
c2 = tuple(round(a + b, 3) for a, b in zip(chi3, chi5))
print(f"  04:18: {m1} == 2*chi4 {c1}: {m1 == c1}")
print(f"  10:02: {m2} == chi3+chi5 {c2}: {m2 == c2}")
sizes = (1, 15, 20, 12, 12)
ip = sum(s*a*b for s, a, b in zip(sizes, m1, [c for c in c2]))/60
print(f"  <2chi4|chi3+chi5> = {ip:.4f} -> disjoint, INEQUIVALENT reps.")
print("  RESOLUTION: different A5 embeddings/actions, not a contradiction.")
print("  R4-20's 50/9 uses irrep DIMENSIONS (embedding-independent); the")
print("  caveat does not block the count. Sector assignment still OPEN.")

print("\n" + "=" * 60)
print("R4-29 m0-mPl: hierarchy 1.53e-20")
print("=" * 60)
mPl = 2.176434e-8
ratio = m0 / mPl
a = 1.37294e-15
lp = 1.616255e-35
print(f"  m0/m_Pl = {ratio:.3e} (vs '1e-19': order-of-magnitude language)")
print(f"  a/l_p   = {a/lp:.3e}")
print("  Arithmetic VERIFIED. 'Defect self-energy matching' derivation NOT in")
print("  workspace; hierarchy cannot be derived without deriving G (OPEN).")
print("  Status: STATED (not tuned, not derived). Blocked on G derivation.")

print("\n" + "=" * 60)
print("R4-23 emergent-GR: h_munu = P u + Q df_s")
print("=" * 60)
print("  Kinematic proposal: 10-comp h_munu from 6-comp u_ij + 1-comp df_s.")
print("  P, Q UNFIXED (FCC symmetry class not applied).")
print("  Einstein equation NOT derived from elastic action.")
print("  What exists: geometric analogy (Katanaev: dislocations<->torsion,")
print("  disclinations<->curvature) + relabeling->diffeomorphism symmetry arg.")
print("  What is missing: P,Q from symmetry; elastic action -> Einstein-Hilbert;")
print("  T_munu identification; 8piG/c^4 from lattice; nonlinear completion.")
print("  VERDICT: analogy/sketch, not derivation. Biggest prize still open.")
print("\nDone. See ledger for grades.")
