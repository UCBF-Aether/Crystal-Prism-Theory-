#!/usr/bin/env python3
"""REP-screening-vacuum: vacuum-structure repair for the self-screening potential.

ORIGINAL: V(x) = +1/2 mu0^2 x e^(-x/L^2), x = A^2 >= 0
  TRUE STRUCTURE: local min at x=0 (V=0), max at x=L^2, V->0+ as x->inf.
  Degenerate minima at 0 and infinity = RUNAWAY. No finite broken vacuum.
  The "SSB new vacuum" was false.

REPAIR (minimal, sign flip): V_rep(x) = -1/2 mu0^2 x e^(-x/L^2)
  - origin unstable: V'(0) = -mu0^2/2 < 0  (genuine SSB)
  - global minimum at x* = L^2, V = -mu0^2 L^2/(2e) < 0
  - V -> 0- at infinity: minimum is GLOBAL, no runaway
  - V''(x*) = mu0^2/(2e L^2) > 0: stable
  - V''(x) -> 0 as x -> inf: mass -> 0 at large A (screening property KEPT)
  - physical mass at vacuum: m^2 = mu0^2/(2e L^2)
  - parameter ID: mu0 ~ 1/xi_coh, L ~ screening scale, VEV A* = L

The Gaussian does double duty: tachyonic at the origin, stabilizing at finite x.
No quartic needed. Next step (not this repair): solve the radial profile
  A'' + (2/r)A' = dV_rep/dA - gJ  for the vortex, replacing the asserted
  V_vortex = V_flat(1 - e^(-r/r_t)).
"""
import math

def check(mu0=1.0, Lam=1.0):
    V  = lambda x: -0.5*mu0**2*x*math.exp(-x/Lam**2)
    dV = lambda x: -0.5*mu0**2*math.exp(-x/Lam**2)*(1-x/Lam**2)
    d2V= lambda x: 0.5*mu0**2*math.exp(-x/Lam**2)*(2-x/Lam**2)/Lam**2
    xs=[i*0.01 for i in range(1,3000)]
    xs_t=min(xs,key=V)
    assert abs(xs_t-Lam**2)<0.02, "min not at L^2"
    assert V(xs_t)<0 and V(1e4)>V(xs_t), "not global"
    assert d2V(xs_t)>0, "not stable"
    assert abs(d2V(1e4))<1e-300, "mass does not vanish at large A"
    assert dV(0)<0, "origin not unstable"
    return {"x*":xs_t, "Vmin":V(xs_t), "m2":d2V(xs_t)}

r=check()
print(f"REPAIRED: x*={r['x*']:.2f}=L^2, Vmin={r['Vmin']:.4f}, m^2={r['m2']:.4f}")
print("SSB genuine, vacuum global, screening (m->0 at large A) preserved.")
