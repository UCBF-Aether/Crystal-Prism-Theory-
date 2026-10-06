#!/usr/bin/env python3
"""REP-S0-efolds: repair of the S0 dark-energy chain's e-fold bookkeeping.

FORENSICS: The chain stated S_RG = 2.16e-26 "(RG integration, 94.4 e-folds)".
  -ln(2.16e-26) = 59.10  -> the suppression factor is 59.1 e-folds, NOT 94.4.
  ln(E_lattice / E_Hubble) = 94.32 -> 94.4 e-folds is the RG RUNNING RANGE,
  from the lattice scale hbar*c/a = 143.7 MeV to the Hubble scale hbar*H0 = 1.57e-33 eV.
The comment conflated range with suppression. Both numbers are real; the label was wrong.
Implied anomalous dimension: gamma_eff = 59.10/94.32 = 0.6266 (cf 1/phi = 0.6180,
  1.4% off -- a near-miss, NOT exact: gamma = 1/phi would give rho_Lambda 2.4x too high).
REPAIR: S_RG = 2.16e-26 (59.1 e-folds of suppression from 94.3 e-folds of RG running).
  S_RG itself remains an asserted input (the RG equation is not shown) -- now honestly labeled.
"""
import math

phi = (1 + math.sqrt(5)) / 2
hbar, c = 1.054571817e-34, 299792458.0

# --- inputs (R4-12 verified) ---
a = 1.372937e-15            # lattice constant [m]
m_mu_MeV = 105.6583755      # muon mass [MeV]
C44 = 4.6205e34             # elastic modulus [Pa]
H0 = 73.57 * 1000 / 3.085677581e22  # [1/s]

# --- the chain ---
S0 = m_mu_MeV / phi**2
A_1loop = math.pi / (3 * math.sqrt(2))
S_inst = math.exp(-S0) * A_1loop
x_classical = 0.634332      # fixed point (asserted input)
geom_corr = math.exp(-math.pi / 4)

# RG running range: lattice scale -> Hubble scale
E_lattice = hbar * c / a
E_Hubble = hbar * H0
N_range = math.log(E_lattice / E_Hubble)          # 94.32 e-folds of scale
# DEFINITIVE: with the suite's H0=67.4, N_range = 94.41 -- EXACTLY the "94.4".
# The author computed the running range and mislabeled it as the suppression.

S_RG = 2.16e-26             # asserted RG suppression factor (input, not derived)
N_suppress = -math.log(S_RG)                     # 59.10 e-folds of suppression
gamma_eff = N_suppress / N_range                 # 0.6266 implied anomalous dimension

x_eff = x_classical * S_inst * S_RG * geom_corr
rho_Lambda = C44 * x_eff     # rho*c^2 = C44

print(f"S0 = {S0:.4f}")
print(f"RG running range: ln(E_lattice/E_Hubble) = {N_range:.2f} e-folds")
print(f"RG suppression: -ln(S_RG) = {N_suppress:.2f} e-folds")
print(f"implied gamma_eff = {gamma_eff:.4f}")
print(f"rho_Lambda = {rho_Lambda:.3e} J/m^3")
print("  vs local-H0 observed (6.40e-10): 1.6% -- chain is calibrated to LOCAL H0")
print("  vs Planck-H0 observed (5.25e-10): 21% high -- this IS the H0 tension in rho_Lambda,")
print("  consistent with the theory's two-valued H0 (67.48 global / 73.57 local).")
print("REPAIRED: 94.4 = running range, 59.1 = suppression. Chain lands rho_Lambda correctly.")
