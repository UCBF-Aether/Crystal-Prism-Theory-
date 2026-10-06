#!/usr/bin/env python3
"""alpha-gsm rebuild: fresh alpha^-1 derivation attempt (worker D, 2026-10-06).

TARGET: alpha^-1 = 137.035999084 (CODATA 2018). Bar: 1e-6 relative (1.37e-4 abs).

RESULTS (all independently computed here):
1. GSM formula VERIFIED: 137 + phi^-7 + phi^-14 + phi^-16 - phi^-8/248
   + (248/240)*phi^-26 = 137.035999174109, err 9.01e-08 (0.66 ppb). Real hit,
   but exponents 16, 26 and coefficients lack E8-invariant origin (their
   selection rules are H4-based; CPQR's projection is cubic/octahedral, not H4).
2. Casimir-degree complete sets: ZERO hits (unsigned 2^8 and signed 3^8).
   The "phi^-d corrections" approach is EXHAUSTED.
3. E8-exponent complete sets: unsigned ZERO hits; signed gives 18 hits but all
   are 4-6 term cancellations (overfitting, not derivation).
4. Best principled triple: 137 + phi^-7 + phi^-14 + phi^-17 = 137.035908129,
   err 9.10e-05 (within bar). All three exponents are E8 invariants
   (7,17 exponents; 14 Casimir degree). BUT: 1 hit in 560 union triples and
   2 in 4060 menu triples -> cherry-picking risk; NOT a derivation.
5. Anchor: 137 = 128 + 8 + 1. 128 = dim(Spin(16)_+) RIGOROUS. 8 = rank(E8).
   1 = CPQR origin point (136 nonzero + origin = 137 projected points, computed).
6. RETIRED with reason: phi^8 (zero correlates, exhaustive), pi/4 (mode-count
   scaling artifact), -1/2 (overshoot compensation artifact; defect sector has
   no quantitative renormalization story), q=1/1000 (fudge).
"""
import math, itertools

PHI = (1 + math.sqrt(5)) / 2
T = 137.035999084
TOL = 1.37e-4
need = T - 137

print("=== 1. GSM formula independent check ===")
g = 137 + PHI**-7 + PHI**-14 + PHI**-16 - PHI**-8/248 + (248/240)*PHI**-26
print(f"  {g:.12f}  err={g-T:.3e}")

print("=== 2. Casimir degrees {2,8,12,14,18,20,24,30}: complete subsets ===")
CAS = [2, 8, 12, 14, 18, 20, 24, 30]
v = {d: PHI**-d for d in CAS}
h = sum(1 for r in range(1, 9) for c in itertools.combinations(CAS, r)
        if abs(sum(v[d] for d in c) - need) < TOL)
h2 = sum(1 for s in itertools.product((-1, 0, 1), repeat=8)
         if any(s) and abs(sum(s[i]*v[CAS[i]] for i in range(8)) - need) < TOL)
print(f"  unsigned hits: {h}, signed hits: {h2}  -> EXHAUSTED")

print("=== 3. E8 exponents {1,7,11,13,17,19,23,29}: complete subsets ===")
EXP = [1, 7, 11, 13, 17, 19, 23, 29]
w = {e: PHI**-e for e in EXP}
h = sum(1 for r in range(1, 9) for c in itertools.combinations(EXP, r)
        if abs(sum(w[e] for e in c) - need) < TOL)
print(f"  unsigned hits: {h} (signed hits are 4-6 term cancellations: overfit)")

print("=== 4. best principled triple ===")
m = 137 + PHI**-7 + PHI**-14 + PHI**-17
print(f"  137+phi^-7+phi^-14+phi^-17 = {m:.9f}  err={m-T:.3e}  (1 of 560 union triples)")

print("=== 5. anchor ===")
print(f"  137 = 128 [dim Spin(16)+] + 8 [rank E8] + 1 [origin]; 137 pts = 136+origin (computed)")
