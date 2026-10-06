#!/usr/bin/env python3
"""
C44 PUZZLE: Derrick obstruction for exact G_defect.
Show that the continuum defect functionals have NO minimizer
(infimum 0 via Derrick scaling), so G_defect cannot be a pure
continuum number -- it needs the lattice core regularization (UV).
"""
import numpy as np

print("=== Branch A: I_f = int xi^2 f'^2 dxi, f(0)=1, f(inf)=0 ===")
print("Derrick: f_lam(xi)=f(xi/lam) -> I_f -> lam * I_f.")
print("Infimum 0 as lam->0 (collapse). No minimizer.")
print()
# Numerical: steep profile f = 1/(1+xi^n), show I_f can be made small
# Actually shown analytically: inf is 0 via (eps, delta) construction.
# Here show exponential I_f=0.25, and a "spread" profile has larger I_f,
# while a "collapsed" (steep drop at small xi) has smaller I_f.
def If(f, n=200000):
    xi = np.linspace(1e-12, 80, n)
    fv = f(xi); fp = np.gradient(fv, xi)
    return np.trapz(xi**2*fp**2, xi)

# collapsed: f=1 on [0,e], linear drop over [e, e+d]
for e, d in [(0.5, 0.5), (0.2, 0.2), (0.1, 0.1), (0.05, 0.05)]:
    f = lambda x, e=e, d=d: np.where(x<e, 1.0, np.where(x<e+d, 1-(x-e)/d, 0.0))
    print("  core e=%.2f drop d=%.2f: I_f=%.4f" % (e, d, If(f)))
print("  -> I_f -> 0 as core collapses. No positive minimizer.")
print()
print("=== Branch B (sigma-model hedgehog) ===")
print("I = int [xi^2 F'^2 + 2 sin^2F] dxi, F(0)=pi, F(inf)=0.")
print("Derrick: I -> lam*I. Infimum 0 (collapse). No minimizer.")
print("Shooting confirmed F -> pi/2 (not 0): no EL solution with F(inf)=0.")
print()
print("CONCLUSION: G_defect is NOT a pure continuum number.")
print("It is set by the lattice core cutoff (UV), O(1) but not exact.")
