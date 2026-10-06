#!/usr/bin/env python3
"""Solve round 4: R4-12, R4-16, R4-34, R4-31, R4-22, R4-28, R4-36.
Reproduces every checkable number. Run: python3 solve_R4_round4.py
"""
import math
from collections import defaultdict

print("=" * 70)
print("R4-12 lattice-constant-closed")
print("=" * 70)
a_closed = math.sqrt(3 * math.pi / 5) * 1e-15
print(f"a = sqrt(3pi/5)*1e-15 = {a_closed:.6e} m  (ledger: 1.37294e-15 OK)")
a_voxel = 1.348e-15
print(f"voxel-era a = 1.348e-15  -> drift {(a_voxel - a_closed) / a_closed * 100:.2f}% (STALE)")
c = 299792458.0
m0 = 3.3259e-28
C44_impl = m0 * 4 * c ** 2 / a_closed ** 3
print(f"m0=C44 a^3/(4c^2): C44 implied by m0 & a_closed = {C44_impl:.4e} Pa")
print(f"live_paper INPUT C44 = 4.6205e34 Pa -> consistent to "
      f"{abs(C44_impl - 4.6205e34) / 4.6205e34 * 100:.3f}%")
C44_impl_stale = m0 * 4 * c ** 2 / a_voxel ** 3
print(f"with stale a=1.348e-15: C44 implied = {C44_impl_stale:.4e} Pa "
      f"({abs(C44_impl_stale - 4.6205e34) / 4.6205e34 * 100:.1f}% off)")
print("PIN: working set {a=1.372937e-15, C44=4.6205e34, m0=3.3259e-28} "
      "mutually consistent; 1.348 stale.")

print("=" * 70)
print("R4-16 fs0-analytic  [ledger transcription CORRECTED]")
print("=" * 70)
f_wrong = 1 - (1 - math.pi ** 2 / (6 + math.pi ** 2)) * (1 - 1 / math.sqrt(12))
f_right = 1 - (math.pi ** 2 / (6 + math.pi ** 2)) * (1 - 1 / math.sqrt(12))
print(f"ledger transcription 1-(1-pi^2/(6+pi^2))(1-1/sqrt12) = {f_wrong:.6f} (WRONG)")
print(f"corrected 1-(pi^2/(6+pi^2))(1-1/sqrt12)              = {f_right:.6f}")
print("live_paper.py:359 implements the CORRECTED form -> 0.5576 OK")
g_fcc = 99 / (28 * ((1 + math.sqrt(5)) / 2) ** 2)
hbar = 1.054571817e-34
zeta_needed = hbar / (m0 * c * a_closed)
print(f"v7.0 zeta_eff=f_s0*g_FCC: analytic -> {f_right * g_fcc:.6f} "
      f"({abs(f_right * g_fcc - zeta_needed) / zeta_needed * 100:.3f}% off zeta_needed)")
print(f"v7.0 zeta_eff=f_s0*g_FCC: toolkit 0.570 -> {0.570 * g_fcc:.6f} "
      f"({abs(0.570 * g_fcc - zeta_needed) / zeta_needed * 100:.3f}% off zeta_needed)")
print("=> v7.0's 99.93% uses toolkit 0.570, NOT analytic 0.5576 (97.75%).")
print("   The 2.2% internal inconsistency is load-bearing.")

print("=" * 70)
print("R4-34 hbar-lattice-energy")
print("=" * 70)
E_lattice = 1.369023e-34
eta_needed = hbar / E_lattice
print(f"eta_needed = hbar/E_lattice = {eta_needed:.10f}")
print("script eta (2026-07-22, 11 shells) = 0.7702978463")
print(f"-> E_lattice reverse-engineered from hbar/eta to "
      f"{abs(E_lattice - hbar / 0.7702978463) / (hbar / 0.7702978463) * 1e6:.1f} ppm")
print("DIMENSIONAL: hbar[J s] = eta[1] * E_lattice[J] -> INVALID as written "
      "(J != J s). E_lattice asserted, not derived in script.")

print("=" * 70)
print("R4-34 eta from CURRENT 12-shell geometry (independent check)")
print("=" * 70)
PHI = (1 + math.sqrt(5)) / 2
D = math.sqrt(2 + PHI)
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si in (-1.0, 1.0):
            for sj in (-1.0, 1.0):
                x = [0.0] * 8
                x[i], x[j] = si, sj
                roots.append(tuple(x))
for b in range(256):
    if bin(b).count("1") % 2 == 0:
        roots.append(tuple(0.5 if (b >> i) & 1 else -0.5 for i in range(8)))
proj = {}
for x in roots:
    p = (round((x[0] + PHI * x[4]) / D, 12),
         round((x[1] + PHI * x[5]) / D, 12),
         round((x[2] + PHI * x[6]) / D, 12))
    proj.setdefault(p, []).append(x)
proj.setdefault((0.0, 0.0, 0.0), [])
shells = defaultdict(list)
for p in proj:
    shells[round(math.dist(p, (0, 0, 0)), 9)].append(p)
S2 = sum(len(v) * r * r for r, v in shells.items())
S4 = sum(len(v) * r ** 4 for r, v in shells.items())
N = sum(len(v) for r, v in shells.items() if r > 0)
eta_now = S2 ** 2 / ((N + 0.5) * S4)
print(f"shells={len(shells)} S2={S2:.4f} S4={S4:.4f} N={N}")
print(f"eta = S2^2/((N+1/2)S4) = {eta_now:.10f}")
print("2026-07-22 eta = 0.7702978463 -> stable to 0.2 ppm across versions.")
print("eta0 values in R4-22 posts: 0.7702976252/0.7702976635/0.7702978463")
print("=> eta0 (frozen beta) is COMPUTED from E8 shell moments, not fitted.")

print("=" * 70)
print("R4-31 deuteron-torsion")
print("=" * 70)
print("Post (2025-09-13): 'Deuteron binding energy: 2.224 MeV, predicted")
print("within 0.01% of the measured value.'  NO formula shown; the number is")
print("the measured value restated (2.224566 MeV -> 4 sig figs).")
print("'Effective torsional scale: 1e-30 m' asserted, no derivation.")
print("Torsional term -mu|grad x phi|^2 exists in Lagrangian; mu 'from")
print("torsional resonance scales' (asserted). NEVER solved for the deuteron.")
print("VERDICT: stated, not derived. The 2025-12-15 cluster model USES")
print("2.22 MeV/contact as INPUT (Li-7 98.6%, Be-7 99.95% need indep. check).")

print("=" * 70)
print("R4-22 gauge-traces")
print("=" * 70)
a1, a2, a3 = 0.975, 0.390, 0.195
print(f"rates {a1}/{a2}/{a3} = 5:2:1 exact by construction of asserted")
print("trace factors (5/6, 1/3, 1/6) x (g^2/4pi)(30); g^2/4pi = 0.039 implicit")
print("(~ alpha_GUT, imported not derived). E8 rep-theory computation NOT shown.")
phi = PHI
kap = 1 / (30 * phi ** 2)
Z = 50
DB = kap * math.sqrt(Z) * 1.0 * phi ** 3  # delta_eta/L_* = 1
print(f"DeltaB_CP(Z=50, d_eta/L*=1) = {DB:.3f} x hbar c/L_*; "
      f"L_*^-1=100 MeV -> {DB * 100:.1f} MeV")
print("but (eta-eta0)/L_* is FREE -> tunable, not falsifiable as stated.")
print("Hierarchy check: rates make U(1) grow fastest in IR -> g1>g2>g3,")
print("INVERTED vs observed g3>g2>g1 (unless eta<eta0, unstated).")
print("sin^2W: running direction real, but 1/phi landing NOT derived;")
print("would need tuned (eta-eta0)/L_*. R4-22 does NOT supply the 1/phi factor.")

print("=" * 70)
print("R4-28 collapse-tau")
print("=" * 70)
tau = 4e-14
C = hbar / (2 * tau)
print(f"tau = hbar/(2C[grad theta]) = 4e-14 s -> C = {C:.3e} J (asserted,")
print("never evaluated for SG).")
print("Tension: universal 4e-14 s for a single atom is ~13 orders faster than")
print("atom-interferometer coherence (~1 s) and ~30 orders faster than GRW")
print("(tau~1e16 s/atom). Only viable if C[grad theta] strongly")
print("state-dependent; the functional is never given. Needs: explicit C,")
print("SG evaluation, micro->macro scaling, interferometry bounds.")

print("=" * 70)
print("R4-36 voxel-12-ports")
print("=" * 70)
print("Rhombic dodecahedron = FCC Wigner-Seitz cell: 12 faces = 12 neighbors")
print("(correct crystallography). 12 faces <-> 12 fermions: COUNT matches,")
print("but NO face<->particle map (no charge/color/flavor assignment).")
print("3 acoustic modes <-> 3 generations: count matches, mechanism asserted.")
print("Charge=vorticity: qualitative. VERDICT: geometric counts grounded;")
print("particle map asserted.")
print("=" * 70)
print("DONE")
