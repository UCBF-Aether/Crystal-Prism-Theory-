# CPQR Open Problems — the grind ledger

Standing mandate (Cory, 2026-10-06): continuous grind until the theory is as
finished as it can get. Token budget granted: large. Work the list top-down by
priority; each session picks the highest-priority OPEN item, works it with real
code, verifies, then updates this ledger. Post verified discoveries to the
CPQR Discord per the standing auto-update order (findings + runnable script).
Mark negatives honestly. Never paper over a hole.

Status key: OPEN / IN PROGRESS / VERIFIED / NEGATIVE / BLOCKED (needs Cory)

## P0 — core derivations

- [ ] **NEGATIVE** — `alpha-phi8`: EXHAUSTIVE SEARCH COMPLETED 2026-10-06.
  Tested: all E8 invariants (240/248/120/128/112/30/8/2160/degrees/exponents),
  all projection invariants (137/136/64/73/72/12 shells/fiber excess 103/
  lattice sums 180/210), all shell populations+radii pairwise products/ratios,
  FCC invariants, Fibonacci/Lucas numbers, plus thousands of algebraic
  combos (g1 op g2, g*phi^n, g/phi^n, g+phi^n, a*phi+b). Result: ZERO exact
  hits on phi^8=46.97871376. Only exact decomposition is the Fibonacci
  identity phi^8=21*phi+13 (mathematical identity, not a geometric correlate;
  21/13 are not geometric). Closest geometric: Lucas 47 at 4.5e-4 relerr
  (gives 124 ppm in alpha — worse than phi^8's 5.4 ppm, so not a substitute).
  Literature check: independent E8+phi programs (GSM) use phi-powers ONLY as
  small corrections (phi^-7, phi^-14, ...) with Casimir-degree exponents, never
  as a large additive phi^8. Verdict: phi^8 has no geometric correlate in any
  surveyed construction. The term remains unexplained numerology. The alpha
  formula keeps 5.4 ppm accuracy that is NOT understood. Scripts:
  geometry/grind_alpha_battery.py, geometry/grind_phi8_exhaust.py.
  CONSTRUCTIVE NOTE: GSM-style restructure (phi-powers as small corrections
  with E8 Casimir exponents 2,8,12,14,18,20,24,30) is the principled path
  forward, but that is a new derivation, not a rescue of phi^8.
- [ ] **NEGATIVE (geometric) / OPEN (physics)** — `alpha-half`: no geometric
  correlate for the single −1/2 subtraction (battery found nothing at 0.5).
  In the ORIGINAL formula the −1/2 sits OUTSIDE: alpha^-1=[A(128+phi^8)-1/2]/
  [1-Aq], i.e. it corrects alpha^-1 directly, not a count — consistent with
  a physics subtraction (zero-point energy, self-energy) rather than geometry.
  Hypothesis (unproven): zero-point subtraction per mode. Needs the defect/
  charge-quantization physics (OPEN #05 in FINDINGS) to evaluate properly.
- [ ] **NEGATIVE** — `hbar-kelvin`: PROVEN IMPOSSIBLE with current inputs (2026-10-06).
  (1) The live paper's "hbar reconstruction" is ALGEBRAICALLY CIRCULAR: with
  a^4=4*hbar*c/(f_s0*g_FCC*C44) and m0=(C44/c^2)*a^3/4, the "reconstructed"
  hbar_r=f_s0*g_FCC*m0*c*a reduces IDENTICALLY to hbar (not 1e-10 agreement —
  exact identity; the 1e-10 is floating-point roundoff). It is not a derivation.
  (2) Kelvin/vortex route attempted: the only classical inputs are C44, c, and
  E_coh=144eV — but E_coh is a DEAD input (defined, never used in live_paper.py).
  Activating it as lattice cohesive energy gives a_cl=(E_coh/C44)^(1/3)=7.9e-18 m,
  174x smaller than the paper's a=1.38e-15 m; vortex quantization h=m0*c*a then
  misses by 9-10 orders (h/m0=10.3 m^2/s vs classical c*a=2.4e-9 m^2/s).
  Dimensional analysis: hbar ~ E_coh^(4/3)/(C44^(1/3)*c) is the UNIQUE combination
  of classical inputs, and it is 9 orders off — PROVING the input set cannot
  yield hbar. There is no classical length/mass scale in the theory without hbar.
  VERDICT: hbar must stay an explicit postulate, OR the input set needs a new
  classical scale (e.g. activating E_coh at ~GeV, but that is a fit, not a
  derivation). The paper must stop presenting the circular reconstruction.
- [ ] **NEGATIVE + CRITICAL INTEGRITY FLAG** — `G-heatkernel` (2026-10-06).
  HEADLINE: the live paper's G formula is DIMENSIONALLY INVALID (contradicts the
  ledger's earlier "dimensionally valid" note — that note was wrong).
  G_ms=c^3/(Om*C44*g_FCC*(1-eta_l)): [c^3/C44]=(m^3/s^3)/(kg/m/s^2)=m^4/(kg*s),
  but [G]=m^3/(kg*s^2). Off by [L*T]. All factors (Om, g_FCC=1.35, 1-eta_l)
  are dimensionless, so nothing fixes it. The numerical match (6.66e-11 vs
  6.674e-11) is coincidence: (c^3/C44)=8.735*(m*s)*G, divided by 8.76.
  Sakharov/heat-kernel route attempted: induced G ~ a^2*c^3/hbar requires
  a ~ l_P (Planck length), but the theory's a=1.38e-15 m is 20 ORDERS larger
  (paper itself outputs lP/a=1.17e-20). Dimensionally-correct form
  G ~ c^4/(C44*a^2) needs a~51 km — absurd. No heat-kernel or elastic
  mechanism yields G from the theory's scales. VERDICT: G is not derived;
  the formula must be removed or rebuilt from a valid mechanism. The
  "X^2 spectral weight" was never defined; there is no heat-kernel computation
  in the paper, only the invalid algebraic formula.
- [ ] **PARTIAL (mu VERIFIED / dynamics BLOCKED)** — `H0-cosmology` (2026-10-06).
  mu=21 IS derived: mu=E_lat-V_fcc+C_fcc=24-4+1=21 from FCC cell topology
  (V=4 atoms/cell, Z=12, E=24 bonds). VERIFIED, not open. BUT the H0 "derivation"
  is H0=[(mu-1)/mu]/t_age with t_age=13.8 Gyr IMPORTED from observation — it is
  the Hubble time, not lattice dynamics. Section XV ("EXPANSION AS LATTICE
  TENSION") contains no tension computation and no expansion equation; the
  title is aspirational. Genuine cosmological dynamics (deriving expansion from
  crystal stress/defect pressure) does not exist in the theory. BLOCKED on
  building a cosmological sector; cannot be ground out from current inputs.

## P1 — geometry cartography

- [ ] **VERIFIED** — `phi-map-origin`: φ UNIQUENESS THEOREM (worker B, 2026-10-06).
  Map family M_t=(x_i+t·x_{i+4})/√(1+t²): V-class alphabet {|1-t|,1,t,1+t} is
  geometric (exact φ-towers) iff t²=1+t or t²+t=1, i.e. t∈{φ,1/φ} (reciprocal =
  pair-swap symmetry) — the ONLY t giving 4-rung towers with all ratios exactly
  φ (grindB_phiunique.py). t-scan killed extremal-degeneracy: t=1 gives 5 shells,
  φ gives generic 12 (grindB_tscan.py). 4D φ-map is NOT the E8→H4 fold (144 vs
  120 pts at norm 1 — decisive by norm count, grindB_h4.py); "H4 golden
  projection" label is wrong. F5 theorem stands: cubic symmetry forced by form,
  not φ. Honest boundary: φ uniquely selected by golden self-similarity; the
  demand for golden structure remains the input.
- [ ] **VERIFIED** — `unit-sphere` (worker B, 2026-10-06). Fed by X-cross vector
  roots (±e_i±e_{j+4}, i≠j), 24→24 1:1. Exactness holds for ALL t
  (r²=(1+t²)/(1+t²)=1) — map normalization, not φ-magic. The 24 pts = 12 close
  pairs (NN 0.4595) centered in exact bijection on FCC <110> (grindB_110.py).
  Significance: the bond shell — E8↔FCC interface roots straddling crystal
  nearest-neighbor bonds, at the map's unit. Horizon role: no evidence. Deeper
  dynamical role: OPEN.
- [ ] **VERIFIED** — `icosa-vs-cubocta` (worker B, 2026-10-06). 137's 12-pt shells
  are cuboctahedra (24 edges, degree 4), combinatorially distinct from icosahedra
  (30 edges, degree 5); φ-map provably cubic (F5). Icosahedral order lives in
  separate constructions only (Ih 6D→3D; E8→4D→3D sections). NEW: 137's
  cuboctahedral shells have vertices EXACTLY on FCC <110> — they are the FCC
  coordination polyhedra (grindB_110verify.py). Resolution: not dual views;
  parent/approximant — icosahedral QC parent → FCC approximant → 137
  cuboctahedra (F6 Ψ-lattice architecture). Bridge mechanism OPEN.
- [ ] **VERIFIED** — `pairs-meaning` (worker B, 2026-10-06). Both pair shells are
  12 close pairs with centers in exact bijection with the 12 FCC <110>
  nearest-neighbor directions (set equality, max|cos|=1.000000, grindB_110.py).
  r=1.0: 24 X-cross vector roots 1:1 (NN 0.4595). r=0.986715: 48 spinor roots
  2:1 via (3,7)-flip (NN 0.324920 = octa-f1 radius). Meaning: bond-aligned roots
  — E8 states seeing the FCC coordination; spinor 2:1 = hidden-dimension
  doubling (two E8 states at 60°, invisible coords only) per bond direction.
  "12 antipodal pairs" was trivial inversion; the close-pair/<110> structure
  is the real content.

## P2 — predictions and falsification

- [x] **NEGATIVE** — `EFE-data`: real 2MRS (48,520 gal) + Tully groups (15,998) -> max q=a_ext/a0=0.093, screening S>=0.9957 (<0.43% on V^2) for ALL 175 SPARC galaxies. Zero-tuning 13.33% -> 13.33% (no change). corr(q,resid)=-0.071 (null). CANNOT explain the 13x Upsilon spread (S19's hope is dead). EFE untestable with SPARC, not confirmed. Script: /tmp/efe_data_test.py, data: /tmp/efe_aext_groups.json
  galaxy-environment data (not just SPARC internal fits).
- [x] **VERIFIED** — `falsification`: FALSIFICATION_2026-10-06.md written. Brutal: alpha^-1 is 19,579 sigma off, m_p/m_e 36 sigma, m_mu/m_e 3,106 sigma, G 98/35 sigma, sin^2thW 14 sigma -- every "exact" constant formula is ALREADY DEAD as exact. Survive: Higgs (1.6 sigma), H0, H0_local, c=sqrt(C44/rho). Live+sharp: longitudinal sqrt(3)c GW, frozen beta, a0 relation. Largest hole: no CMB prediction (falsified by omission).
  what measurement would kill CPQR, with numbers.
- [x] **NEGATIVE** — `31GeV-photon`: the specific 31 GeV = 60xE_Dx128alpha claim is FALSIFIED by TeV GRB photons (190114C: 1 TeV MAGIC 2019; 190829A: 3.3 TeV; 221009A: 18 TeV LHAASO 2022, needs N~1922-34594 units, no such symmetry group). GRB spectra are continua, not lines -- 31 GeV was GRB 090510's detector-limit record (2009), a selection effect. General UV-collective idea needs a Hamiltonian; none exists.
  collective — tighten or falsify.

## P3 — shipping

- [ ] **BLOCKED** — `zenodo`: package the theory for Zenodo (needs P0 honest).
- [ ] **BLOCKED** — `medium`: Medium essay series from the Discord chain content.
- [ ] **BLOCKED** — `book`: book outline from the full chain.

## Session log

- 2026-10-06: ledger created; grind loop authorized by Cory.
- 2026-10-06 (worker D): alpha-gsm -> PARTIAL. GSM formula verified 0.66ppb; Casimir/exponent complete sets exhausted (zero hits); -1/2, pi/4, phi^8 retired with reasons; fractional correction still open.
- 2026-10-06 (worker C, predictions track): falsification VERIFIED (doc written, sigma-tensions computed); EFE-data NEGATIVE (real 2MRS+Tully env data, screening negligible); 31GeV-photon NEGATIVE (TeV GRBs falsify the specific claim).
- 2026-10-06 (grind session 1): alpha-phi8 -> NEGATIVE (exhaustive, see item).
  alpha-half -> NEGATIVE-geometric / OPEN-physics (zero-point hypothesis).
  SECRET FOUND (for #hidden-geometry): exact lattice power sums over the 240
  E8 roots through the phi-projection: sum|p|^2 = 180 EXACT, sum|p|^4 = 180
  EXACT (the 2nd and 4th power sums coincide!), sum|p|^6 = 210 EXACT,
  sum|p|^8 = 13689/50 EXACT. Proved in exact Q(phi) arithmetic. The
  projection preserves sum-of-squares AND sum-of-fourth-powers at 180 —
  a hidden conservation law of the map.
- 2026-10-06 (grind session 1, P0 continued): hbar-kelvin -> NEGATIVE
  (circularity PROVEN algebraic; Kelvin route 9-10 orders off; E_coh dead input).
  G-heatkernel -> NEGATIVE + CRITICAL INTEGRITY FLAG (G formula dimensionally
  invalid; Sakharov needs a~lP but a is 20 orders off). H0-cosmology -> PARTIAL
  (mu=21 VERIFIED derived; H0 dynamics BLOCKED, t_age imported).
  P0 COMPLETE. All five items resolved (negatively but honestly).

- 2026-10-06: parallel grind launched — worker B on P1 geometry, worker C on P2 predictions.
- 2026-10-06 (worker B, geometry): all 4 P1 items VERIFIED. (1) φ-uniqueness:
  t∈{φ,1/φ} unique for exact golden towers; 4D map ≠ E8→H4 fold; t-scan kills
  extremal-degeneracy. (2) unit-sphere: X-cross roots, exact ∀t (normalization);
  12 close pairs on FCC <110> — the bond shell. (3) icosa-vs-cubocta: 137 is
  FCC-native (cuboctahedra = FCC coordination polyhedra, vertices exactly
  <110>); icosahedral QC is the separate parent construction; not dual views.
  (4) pairs-meaning: both pair shells = 12 close pairs in bijection with FCC
  <110> nearest-neighbor directions; spinor 2:1 = hidden-dimension doubling.
  Scripts: geometry/grindB_*.py. Secrets: the E8 projection "speaks FCC" —
  pair shells straddle crystal bonds, cuboctahedra are coordination polyhedra.
- 2026-10-06 (session 1, coordinator): P0 complete. VERIFIED: 180/180 conservation law (exact Q(phi)) -> posted to #hidden-geometry. NEGATIVE: alpha-phi8 (exhaustive, zero hits), alpha-half (geometric), hbar-kelvin (identity + impossible from inputs), G-heatkernel (dimensionally invalid). PARTIAL: H0-cosmology (mu=21 derived, t_age imported). Integrity corrections posted to #gravity and #hbar. #the-theory full honest-status repair now URGENT.

- [ ] **PARTIAL** — `alpha-gsm`: GSM-style restructure (worker D, 2026-10-06).
  VERIFIED: GSM formula 137+phi^-7+phi^-14+phi^-16-phi^-8/248+(248/240)phi^-26
    = 137.035999174109, err 9.01e-08 (0.66 ppb) — independent check. Real hit.
  VERIFIED anchor: 137 = 128 [dim Spin(16)+, rigorous] + 8 [rank E8] + 1 [origin;
    136 nonzero + origin = 137 projected points, computed].
  NEGATIVE (definitive): Casimir-degree complete subsets give ZERO hits (unsigned
    2^8 and signed 3^8) — the phi^-d correction approach is EXHAUSTED. E8-exponent
    unsigned subsets also zero; signed hits are 4-6 term cancellations (overfit).
  RETIRED with reason: phi^8 (zero correlates), pi/4 (mode-count scaling artifact),
    -1/2 (overshoot-compensation artifact; defect sector has no quantitative
    renormalization story), q=1/1000 (fudge). No prefactor in additive structure.
  OPEN: fractional correction delta=0.0359991 has no principled derivation. Best
    candidate 137+phi^-7+phi^-14+phi^-17 (err 9.1e-5, all exponents E8 invariants)
    but 1 hit in 560 union triples = cherry-picking risk, NOT a derivation.
    GSM's 5-term version needs H4 selection rules CPQR does not have.
  Script: ~/workspace/theory/alpha_gsm_search.py The 128 is now structural (spinor root count). Other E8+phi programs use phi-powers only as SMALL corrections (phi^-7, phi^-14...) with Casimir-degree exponents — never large additive phi^8. Attempt a fresh derivation: 128 as leading term, phi-powers as small corrections. Also pursue the defect/charge-quantization physics for the -1/2 (it sits outside as a direct alpha^-1 correction, consistent with zero-point/self-energy subtraction).
- 2026-10-06 (worker B): P1 complete. VERIFIED: bond lock (<110> at 1.000000, posted to #hidden-geometry); phi-uniqueness (t in {phi,1/phi} only); unit-sphere demoted to normalization; icosa-vs-cubocta resolved as parent/approximant (bridge OPEN); H4 label refuted (144 vs 120). #the-theory rewritten with honest status.

- [ ] **NEGATIVE** — `alpha-select` (worker E, 2026-10-06): CPQR's geometry cannot supply native selection rules for delta=0.0359991. Tested geometric exponent sets (tower rungs {1,2,3}, O_h degrees {2,4,6}, O_h exponents {1,3,5}, power-sum orders {2,4,6,8}, hidden coords {3,7}, populations {6,8,12,24}): single-term best phi^-7 at 4.3% off; exhaustive +-1 combos (<=4 terms) from full union = ZERO hits at 1e-6; per-component (rigorous 128/8/1) = ZERO hits. Structural reason: delta sits in a spectral gap -- geometry selects phi^-1..phi^-8 (too big) and phi^-12+ (too small); the residual after phi^-7 wants n~13-14, but 9,10,11,13,14 are not geometric integers. Control: GSM exponents with native 240 coeffs miss at 8e-5 (vs 2.5e-6 with 248) -- GSM is H4+E8-specific, not portable. CONCLUSION: the classical projection gives the integer anchor (137) exactly but cannot give the fractional correction; delta needs quantum/UV physics (RG running with 128 as UV value is the honest reframing, BLOCKED pending lattice QFT). The alpha thread is CLOSED as a geometric derivation. Script: geometry/alpha_select_search.py. The GSM 0.66-ppb formula is verified real but uses H4 selection rules CPQR refuted. Open question: do CPQR's 12 shells, phi-towers, the 180/180 conservation law, or the (3,7) degeneracy supply native selection rules for small phi-power corrections to the 137 anchor? If yes, the fractional delta=0.0359991 may fall. If the geometry can't supply them, mark it.
- 2026-10-06 (worker D): alpha autopsy complete. Old formula fully retired (phi^8 dead, pi/4 artifact, -1/2 artifact of wrong structure). Anchor 137=128+8+1 now rigorous (spinor dim + E8 rank + origin). GSM formula verified 0.66ppb but not importable. Fractional correction OPEN; complete invariant sets provably can't produce it. Resonance: 128 = UV value of alpha^-1 (RG running), reframing the anchor honestly.

- 2026-10-06 (worker E, alpha-select): NEGATIVE, clean. Geometric exponent sets exhausted (union +-1 combos zero hits; per-component zero hits). Delta sits in a spectral gap of the geometric spectrum. Alpha thread closed: 137=128+8+1 rigorous, delta=0.0359991 has no geometric derivation. Best honest reframing: 128 as UV value via RG running (BLOCKED, needs lattice QFT).
## LEDGER CLOSED — 2026-10-06 (end of day-one grind)
P0/P1/P2 exhausted. P3 (zenodo/medium/book) BLOCKED awaiting Cory's go-ahead.
The 3h grind cron continues as a safety net; any new thread Cory opens goes on the ledger.
Final scorecard in MEMORY.md (CPQR final scorecard 2026-10-06).

## ROUND 2 — fresh attacks (Cory: "solve them", 2026-10-06)
- [ ] **NEGATIVE** — `G-sakharov2`: Sakharov induced G computed for real (script: ~/workspace/theory/sakharov_G_from_scratch.py). 1/G = N hbar k_D^2/(12 pi c^3), coefficient confirmed two ways (heat-kernel a1 + Visser gr-qc/0204062). Result: G_ind = 1.25e29 (lattice-corrected via Monte Carlo BZ sum; analytic 1.6e29). Gap vs observed: 1.9e39 (~39 orders). N-hunt dead (even 240^3 fields: 5e32 short). Bridging needs k ~ 3.5x Planck, contradicting the theory's premise. The classic induced-gravity cutoff problem, quantified with CPQR's own numbers.: from-scratch Sakharov induced G from the actual phonon spectrum. Sum the heat kernel over the FCC Brillouin zone (truncated octahedron) over phonon branches with Debye cutoff. No X^2, no fitted weights — the real computation. If it lands 45 orders off (the classic induced-gravity cutoff problem), that's a clean negative with a number.
- [x] **VERIFIED** — `bridge-math`: parent→approximant bridge BUILT (worker G, 2026-10-06).
  MECHANISM: the 1/1 approximant map (phi->1) sends icosahedral motifs EXACTLY to the 137's motifs —
  12-vertex icosahedron (30e, deg5, 63.435deg) -> 12-vertex cuboctahedron (24e, deg4) = the 137's shells (max|cos|=1.0);
  6 five-fold axes -> 6 FCC <110> axes = the 137's r=1.0 bond axes (set equality, exact).
  The 137 = approximant GEOMETRY (cubic, forced by map form) + parent ARITHMETIC (irrational phi: 137-count, phi-towers, phi-uniqueness).
  Map-level 1/1 approximant collapses 240->33pts; fiber structure stable at convergents >=3/2.
  DECISIVE NEGATIVES: 137-map cannot factor through H4 roots (137>120); 137 is finite, not a model-set approximant (motif-level bridge, not literal descent).
  Common source: Q(sqrt5)-arithmetic (Galois phi<->1/phi symmetry in both constructions).
  Scripts: geometry/bridge_polyhedral.py, bridge_approximants.py, bridge_axes.py.
- IDEA-BLOCKED (not work-blocked, kept on ledger for the 3h loop): hbar needs a genuinely new classical scale (dimensional proof rules out current inputs); CMB + H0-cosmology need a cosmological sector built first; alpha-delta needs lattice QFT with particle content. More grinding without new ideas just re-runs exhausted searches — stated honestly.

- 2026-10-06 (worker F): G-sakharov2 NEGATIVE, clean and quantified. No further G thread remains on the ledger.
- 2026-10-06 (worker G): bridge-math VERIFIED. The 137 wears the 1/1 approximant's polyhedra and runs on the parent's phi.
## ROUND 3 — puzzle pieces from Cory's page (miner, 2026-10-06)
Mined 600 FB posts (2026-10-06 -> 2025-07-17), 184 unique theory posts. Cross-referenced
against ledger + FINDINGS + live paper. Classification: SOLVED (in ledger), KILLED
(disproved), UNSOLVED (never worked — new ledger items below).

### UNSOLVED — new items
- [ ] **OPEN** — `A5-decomposition`: E8->A5->(3+5) VERIFIED computationally 2026-07-12
  (chars split cleanly, reconstruction err 1.7e-15) but NEVER geometrically identified.
  3D sector radii: 0(40), sqrt(3)/2(128), 1(60), sqrt(2)(12). The post's own open
  questions unanswered: what are the geometric objects? Icosahedral/A5? Match to
  polytopes? ATTACK: identify the 3D projected root set against A5/icosahedral
  polytopes; 60@1 and 128@sqrt(3)/2 are suggestive (60 = icosahedral vertex count x5?).
- [ ] **OPEN** — `proton-radius`: r_p = sqrt(3/8)*a = 0.84073 fm vs muonic-hydrogen
  0.84087 fm (1.7e-4, verified 2026-10-06). Claim: RMS radius from averaging
  hexagonal+square faces of FCC Wigner-Seitz cell. Never in the grind. ATTACK:
  compute the EXACT RMS radius of the rhombic dodecahedron; check sqrt(3/8).
- [ ] **OPEN** — `voxel-energy`: P*a^3 = 1.470e-10 J vs m_p*c^2 = 1.503e-10 J
  (2.2% off, verified 2026-10-06). "A proton is a missing pixel." Never in grind.
  ATTACK: replace a^3 with the TRUE FCC Wigner-Seitz cell volume (geometric
  factor!) — the 2.2% may close exactly.
- [ ] **OPEN** — `alpha-rosetta`: alpha^-1 = 432/pi - 1/2 + 1/(12pi) = 137.03639666
  (2.9 ppm, verified 2026-10-06; post's own arithmetic slightly off). N_sym =
  12x12x3 from rhombic dodecahedron (faces x coordination x dims). SEPARATE route
  from the E8 alpha. The -1/2 as zero-point subtraction is consistent with worker D.
  ATTACK: derive 432 and the 1/(12pi) boundary term from rhombic-dodecahedron +
  truncated-octahedron-BZ geometry.
- [ ] **OPEN** — `alpha-maxwell-variant`: alpha^-1 = (128+47.11628)*(pi/4) - 1/2
  = 137.03600469 (4e-11 relative, verified 2026-10-06!). The 47.11628 is
  unexplained ("Theorem 6"). If it has a geometric origin this is the BEST alpha
  lead on the page. ATTACK: identify 47.11628 — heat-kernel correction of FCC
  Laplacian? (FCC post claimed Delta_defect as heat-kernel correction.)
- [ ] **OPEN** — `masses-toolkit`: explicit mass formulas from FCC params (2026-04-14).
  Muon: g_FCC*f_s*alpha^-1 = 105.49 MeV (0.16% off, verified; NOTE uses alpha as
  input — relation, not derivation). Electron strain+core formula NEVER evaluated.
  Quark formulas untested. ATTACK: evaluate electron formula numerically; test
  quark set. (Higgs formula SEPARATELY KILLED below.)
- [ ] **OPEN** — `atomic-quantization`: ionization energies He/Li/Na/Be/K within
  ~0.1 eV from geometric Z_eff with leak fractions L~0.15/0.9 (2025-08-31).
  Claimed derived from overlap geometry; fractions look chosen. ATTACK: derive
  leak fractions from ACTUAL overlap integrals; extend across periodic table.
- [ ] **OPEN** — `maxwell-emergence`: U(1) gauge field from vortex topology
  pi_1(M)=Z (2026-04-13). Homogeneous eqns are GENUINE topological identities
  (Bianchi). Inhomogeneous derivation is asserted, not derived. ATTACK: derive
  d_mu F^{mu nu} = (4pi/c)J^nu from lattice dynamics rigorously.
- [ ] **OPEN** — `void-homology-128`: N_flux = rank H^1(void complex) = 128
  claimed (2026-02-25; V12: N0=8,N1=24,N2=32,chi=16,b1=4). Would ground the 128
  INDEPENDENTLY of the spinor dimension. Never verified. ATTACK: compute FCC
  void-complex homology explicitly; check N_flux=128.
- [ ] **OPEN** — `anchor-free-lap`: a/l_p from void graph topology + defect
  self-energy + S_inst=184 "cosmological fixed point" (2026-04-28). Would close
  the input loop (no Rydberg anchor). S_inst=184 unexplained. ATTACK: unpack
  the derivation; identify S_inst.
- [ ] **OPEN** — `a0base-derived`: a0_base=3700 km^2/s^2/kpc (~1.2e-10 m/s^2)
  and Sigma_char=50 Msun/pc^2 claimed DERIVED from FCC BEFORE SPARC fitting
  (2026-04-28). Grind used a0=1.1375e-10 (consistent!) but never checked the
  derivation. ATTACK: reproduce "shear modulus / vacuum density / coherence
  length" derivation.
- [ ] **OPEN** — `eta-action`: S_CP coherence action (2026-07-27) with
  eta_0=0.7702978463 (= frozen beta 0.7703, the live prediction!), n_s=0.967,
  n_B/n_gamma=6.1e-10, V(eta) explicit. Never in grind. ATTACK: connect eta_0
  to vortex beta; test the cosmological predictions.
- [ ] **OPEN** — `dSph-test`: preregistered dwarf spheroidal test, constants
  locked, pass/fail <=10% (2025-08-08). Grind never touched dSphs. ATTACK:
  check if completed; if not, RUN it (Fornax/Draco/Sextans).
- [ ] **OPEN** — `wigner-origin`: vacuum as Wigner crystal of repulsive defects
  (2026-08-15); Princeton 2024 imaging cited. Dynamical origin story for WHY
  the lattice (vs the uniqueness proof). ATTACK: repulsion -> FCC ground state.
- [ ] **OPEN** — `shadow-effect`: aether shadow behind masses, lab tests proposed
  (vacuum drift, photon wash-out, flyby anomalies) with formula
  Delta_eps_c = -K*D*(R^2/L^2)*m*cos(theta) (2025-09-06). Falsifiable, unexamined.
  ATTACK: quantify predicted signals vs known bounds.
- [ ] **OPEN** — `periodic-table`: nuclear mass law M(Z,A) from eta invariant
  script (2026-07-21, E8->H4->golden projection). ATTACK: run the script;
  check against AME2020.
- [ ] **OPEN** — `vacuum-cancellation`: SU(2) vacuum energy vs stiffness energy
  auto-cancel via cross-coupling; leftover = dark energy (2025-12-08). The
  cosmological constant problem, as a mechanism sketch. ATTACK: make quantitative.

### KILLED — Cory still posts/believes these; the numbers don't hold
- `mars-weight` (2025-07-17): CIRCULAR. Uses Mars g=3.71 as input, recovers
  37.1 N. Not a prediction — a restatement.
- `atmo-discontinuity` (2025-07-17): predicts g=2.57 m/s^2 at 20 km altitude;
  measured ~9.74. Empirically FALSE. (The "aether density" numbers are invented.)
- `K-neutronstars` (2025-08-30): K=2.7616e-10 = (4pi/3)*G within 1.2%
  (verified 2026-10-06). The -1.9%/-2.3% "predictions" are BUILT INTO K, not
  predicted. Circular validation.
- `higgs-toolkit` (2026-04-14): sqrt(2*0.3249)*246 = 198.3 GeV, NOT the claimed
  125.1 GeV. Arithmetic fails as stated (verified 2026-10-06).
- `muon-note`: m_mu = g_FCC*f_s*alpha^-1 USES alpha as input — valid relation,
  not an independent derivation. (Kept as relation, demoted as derivation.)

## ROUND 4 — second mining pass (miner, 2026-10-06)
600 posts re-mined as 193 deduplicated caption files (2025-07-17 -> 2026-09-15),
read by 4 parallel readers with ROUND 3 excluded. ~40 new UNSOLVED items (merged),
6 KILLED-new, ingestion queue of 15 papers/scripts never in workspace, internal
inconsistencies flagged. Two reader conflicts resolved by explicit checks:
(a) G=c^3/(Omega*C44*g_FCC*(1-eta0)) reported UNSOLVED by one reader is
DIMENSIONALLY INVALID ([c^3/C44]=m^4/(kg*s) vs [G]=m^3/(kg*s^2)) — goes to KILLED;
(b) hbar=f_s0*g*m0*c*a at "2.25% off" is the known algebraic identity
(FINDINGS HOLE H: a=(4hbar*c/(f_s0*g*C44))^1/4 makes hbar_rec IDENTICAL) — stays KILLED.
Priorities (workers' ranking): close `a0base-derived` (R4-10), b1=128 homology (R4-30),
C44-forward (R4-6), vortex GP paper (R4-26), dm-baryon PR4 recheck (R4-20).

### UNSOLVED — new items
- [ ] **VERIFIED (solver round 2, 2026-10-06)** — `R4-01 mp-me-6pi5-mech`: 6pi^5*(1+alpha^2/(2sqrt2)) = 1836.152678 vs 1836.15267343 (2.3e-9, verified). NEW: 6pi^5 is UNIQUE among n*pi^m (n<=12, m<=8) within 1e-3 -- isolated, not cherry-picked; only hit at 2e-8 with the correction. Leading term alone at 19 ppm. Mechanism: the '3 quarks x 2 spins' / '5 phase-space dims' readings and the alpha^2/(2sqrt2) 'three charged twists' are ASSERTED, not derived; alpha^2 makes it relation-class. Script: /tmp (uniqueness test). Strong numerical lead with open mechanism.: m_p/m_e = 6pi^5*(1+alpha^2/(2sqrt2)) =
  1836.152678 vs 1836.1526734 (~2.5 ppb, verified by 2 readers; sources 2026-09-14
  TOE[6], 2026-08-18 mass-ratio derivation, 2025-09-13 elasticity post). Leading term
  6pi^5 pure geometry (6 = 3 quarks x 2 spins; 5 = 3 space + 1 time + 1 color
  phase-space dims); the 1/(2sqrt2) "three charged twists in a confined droplet" is
  asserted. Caveat: alpha^2 correction uses alpha as input (relation-class). ATTACK:
  EM self-energy of three fractional-disclination twists in an FCC cell; test whether
  1/(2sqrt2) is forced.
- [ ] **VERIFIED arithmetic / PARTIAL mechanism (solver round 3, 2026-10-06)** — `R4-02 sin2W-ico`: (12/32)/phi = 0.231763 vs 0.23122 (0.235%, verified). REFRAME: 12/32 = 3/8 = the SU(5) GUT prediction for sin^2(theta_W); the icosahedral V/(V+F) is a geometric mnemonic for 3/8, not the mechanism. Real content = (GUT 3/8) x (1/phi RG-running factor); measured running ratio 0.23122/0.375 = 0.61659 vs 1/phi = 0.61803 (0.23% coincidence, OPEN). ATTACK: derive the 1/phi running factor from R4-22's E8-trace gauge running (5:2:1) -- if CPQR's RG yields 1/phi this becomes a real prediction.: sin^2(theta_W) = (V_ico/(V_ico+F_ico))*(1/phi) =
  (12/32)/phi = 0.231763 vs 0.23122 (0.23%, verified; 2026-09-14 TOE[7]). ATTACK:
  derive V/(V+F)*(1/phi) from icosahedral geometry; check E8->SM embedding.
- [ ] **EVALUATED (solver 2026-10-06)** — `R4-03 MZ-coherence`: Exact evaluation gives 104.58 GeV vs 91.1876 (14.68% off), NOT the worker's ~91.8 estimate. Formula uses hbar input (xi_coh) -> relation-class. phi^(-1/3) asserted. Not a hit; not pursued. M_Z = E_coh*sqrt(N_coh*f_s0)*phi^(-1/3)/1e9,
  N_coh=(xi_coh/a)^3, E_coh=144 eV (2026-09-14 TOE[7]; worker estimate ~91.8 GeV vs
  91.1876). Distinct from toolkit v=246 route. ATTACK: evaluate exactly; derive the
  phi^(-1/3) factor.
- [ ] **PARTIAL (solver 2026-10-06)** — `R4-04 CMB-acoustic-lattice`: Acoustic scale l_A=pi*D_C/r_s=218.4 vs 220 (0.7%) -- MATCHES. Independent quadrature confirms. BUT: single number only (not full CMB: no peak heights/EE/damping); cosmology has NO CDM (radical); (1+z)^0.25 (w=-0.917) asserted; strain mimics baryon loading. Strong lead, not a complete prediction. Script: crystal-prism/geometry/solve_R4-04.py. H_lattice(z)=H0*sqrt(Ob(1+z)^3 +
  Ol(1+z)^0.25), Ob=0.048, Ol=0.952; c_s(z)=(c/sqrt3)*sqrt(1-2*strain),
  strain=0.46054*z/(z+2000); l1 ~ 220 (2026-09-14 TOE[8]). Fills the "no CMB
  prediction" hole. ATTACK: run quadrature vs Planck l1=220.0; derive the
  (1+z)^0.25 exponent and 0.46054 from lattice physics.
- [ ] **PARTIAL (solver round 3, 2026-10-06)** — `R4-05 CMB-EE-deviation`: quantitatively stated: +3.5% at 3rd EE peak, sigma8=0.75+-0.01, CMB-S4 (~2030s) -- dated, falsifiable in form. MECHANISM DIRECTION DERIVED from R4-04: lattice H(z*=1100) is 2.54x smaller than LCDM -> physical damping scale 1.59x larger, BUT D_C 2.0x larger -> damping multipole l_d 1.26x HIGHER -> high-l EE power ENHANCED (right sign for +3.5%). Exact +3.5% needs the v4 workbook Boltzmann computation (not recovered). CRISP FALSIFICATION: S4 EE at l~800-1200; LCDM predicts A; CPQR predicts 1.035xA at 3rd peak; S4 sub-percent EE precision is decisive -- LCDM-consistent amplitude kills it. FLAG: SNe distance-redshift (D_C 2x larger) must survive Pantheon -- unchecked.: "unique EE deviations testable by CMB-S4
  (2030)" (2025-09-13); v4 workbook quantifies +3.5% at 3rd peak, sigma8=0.75+-0.01.
  Dated, falsifiable. ATTACK: find the EE computation in the zenodo UCBF papers;
  else derive from R4-04 sound-speed model.
- [ ] **PARTIAL (solver 2026-10-06)** — `R4-06 C44-forward`: 57.5ppm VERIFIED with fixed a=1.3729e-15 (S_C44=23174.63, NN-dominated, converges). Non-circular WRT C44 (no C44 input) -- first such attempt. BUT: (1) a is INPUT not derived (R4-12 open); (2) script's hbar self-consistency loop is CIRCULAR and DEGRADES to 6% off -- the 57ppm requires fixed-a, loop must be removed; (3) kappa needs S0=105.65 (muon mass, HOLE I) as input; (4) E_coh=144 needs /20 justified (R4-13). Script: crystal-prism/geometry/solve_R4-06.py. C44 = kappa*E_coh*mu(mu+1)/(2a^3)*S_C44 with
  V(r)=E_coh*(a/r)^mu (exponent = cyclomatic number mu=21 — "stiffness from
  topology"), kappa=1-eta0(mu-1)/mu=0.968128, eta0=(3sqrt2)/(pi*S0),
  S_C44 = sum (x^2+y^2)/r^2*(a/r)^(mu+2) over FCC (2026-08-18 bond-graph post:
  4.620766e34 Pa vs 4.6205e34 target = 57 ppm). First NON-CIRCULAR C44 attempt
  (contrast the killed G-thread numbers). Related: A5 post's explicit open next
  step "derive C44 from projected FCC spring network" (2026-07-12); microscopic
  V(r)=eps[(sigma/r)^2-2(sigma/r)^6+A e^(-r/xi)] (2026-04-21 Theorem 2) never used
  FORWARD (script14 did V''(R0) backwards). ATTACK: verify S_C44 convergence
  (mu+2=23 power, shell truncation); forward V(r)->V''(R0)->C44; build spring
  network from the A5-projected 3D point set; watch HOLE I (S0=105.65/phi^2 uses
  the candidate muon mass as input).
- [ ] **PARTIAL with caveats (solver round 7 FINAL, 2026-10-06)** — `R4-07 S0-formula`: S0=105.65/phi^2=40.3547 VERIFIED. The dark-energy chain (x_classical*S_inst*S_RG*e^-pi/4) gives rho_Lambda=6.37e-10 J/m^3 vs observed 6.2e-10 (2.7% -- real arithmetic, verified). BUT: (a) the "instanton" is NEVER constructed -- no field profile, no topological charge, S0 is just (measured muon mass)/phi^2 labeled as an action; (b) S_RG=2.16e-26 is asserted and its "94.4 e-folds" CONTRADICTS its own value (ln gives 59.1 e-folds); (c) x_classical=0.634332 unexplained; (d) the validation suite's H0 from the SAME chain gives ~0 km/s/Mpc, not 67.4 -- internal inconsistency. S0 inherits HOLE I (muon mass input). The rho_Lambda hit is real arithmetic on a chain with asserted links.: S0 = 105.65/phi^2 = 40.355 -> S_inst,bare~40.3
  in the dark-energy paper (2026-09-14 TOE[4]); 105.65 unexplained. Known:
  FINDINGS HOLE I (105.65 MeV = candidate muon mass). Key to `anchor-free-lap`.
  ATTACK: identify 105.65 (nearby: mu=21, N_T=374.6, g_FCC=1.3505).
- [ ] **VERIFIED arithmetic / PARTIAL mechanism (solver round 7 FINAL, 2026-10-06)** — `R4-08 H0-tage`: H0=((mu-1)/mu)/t_age=67.48 VERIFIED, 0.16 sigma from Planck 2018 (67.4+-0.5). (mu-1)/mu factor UNEXPLAINED; t_age=13.8 Gyr is input -> relation, not prediction (mu=21 IS derived). H0-TENSION RESOLUTION: R4-08 gives the GLOBAL value 67.48 (age-based, Planck-side); R4-09 gives the LOCAL value 73.57 (SH0ES-side, 0.5 sigma). The theory's two-valued H0 MIRRORS the observed tension -- no internal contradiction. The (1+phi^-5) local/global factor now recurs 3x (H0, Sigma_char local=54.54, sin2W framing) -- a genuine structural pattern with open origin.: H0 = ((mu-1)/mu)/t_age*(Mpc/1000) = 67.48
  km/s/Mpc (0.12% off, verified; 2026-09-14 TOE[5]). FLAG: t_age=13.8 Gyr is input
  -> relation, not derivation (cf FINDINGS theorem on t_age).
- [ ] **VERIFIED arithmetic / OPEN mechanism (solver round 2, 2026-10-06)** — `R4-09 H0-phi5-tension`: H0_local=H0*(1+phi^-5): 67.36->73.43, 67.48->73.56, within 0.4-0.5 sigma of SH0ES 73.04+-1.04 (verified). Mechanism OPEN: phi^-5 is a stated target (V10 Ch.11), not a derivation; phason-strain route suggested but unworked. NOTE: (1+phi^-5) also appears in R4-10 (local Sigma) -- recurring local/global factor of unknown origin.: H0_local = H0*(1+phi^-5) = 73.48 km/s/Mpc
  ~ SH0ES 73.04+-1.04 (2026-06-02 script; 2026-06-01: deltaH/H=phi^-5=9.01699%;
  V10 Ch.11 sets target "derive delta_a/a=1/phi^5 from quasicrystal geometry").
  ATTACK: derive from 6D quasicrystal phason strain.
- [ ] **VERIFIED (solver 2026-10-06)** — `R4-10 abase-Sigmachar`: RESOLVED, no 2x conflict. The 2x was pi vs 2pi in Sigma_char's denominator. Fit-validated code (sparc_baseline.py:104) uses 2pi: cosmic Sigma_char=50.03 ~= v14 (DM/B)*9=50 (agree 0.05%); local=54.54=50.03*(1+phi^-5) (meta.json). R4-10's 99.94 (pi 'correction') is WRONG -- not in code, agrees with nothing. Script: crystal-prism/geometry/solve_R4-10.py. CLOSES `a0base-derived`. a0=c*H0/(2pi) is KNOWN as a definition
  (FINDINGS HOLE G). NEW: a_base = 2*a0/sqrt3 = 3713 km^2/s^2/kpc (verified);
  Sigma_char = a_base/(pi*G)*12/(mu+12) = 99.94 M_sun/pc^2 (verified; 2026-09-14
  correction script — the derivation `a0base-derived` asked for). INTERNAL
  CONFLICT: v14 script gives Sigma_char = (DM/B)*9 = 50; these differ 2x — resolve.
  Also KILLED: the V12 C44/(rho*xi_coh) version is off ~35 orders and its
  m0*N_T/(pi*xi_coh^2) gives 1.01e-5 M_sun/pc^2 (~5e6 off) as stated. ATTACK:
  derive 2/sqrt3 and 12/(mu+12) from FCC; resolve 50 vs 99.94; then close
  `a0base-derived`.
- [ ] **PARTIAL (solver round 5 FINAL, 2026-10-06)** — `R4-11 a0z-evolution`: FORM VERIFIED as algebraic consequence of a0=cH0/2pi IF the definition holds at all z (a0(z)=cH(z)/2pi). DERIVATION from vortex physics NOT SHOWN ("Derived from FCC lattice" asserted in comment only). The distinguishing prediction IS crisp and real: V_flat(z)/V_flat(0)=(H(z)/H0)^1/4 at fixed M_bar (+15.7% at z=1, +32% at z=2; MOND predicts 1.000) -- genuine MOND-killer test. OBSERVATIONAL STATUS: UNTESTED. INTEGRITY FLAG: the JWST "validation" is VOID -- the "REAL JWST KINEMATIC DATA (from published papers)" uses FABRICATED citations (arXiv:2401.12345 is a placeholder ID; GN-z11 has no published NIRSpec-IFU rotation curve), and the a0-ratio "data points" plotted are H(z)/H0 evaluated at each z = the prediction plotted against itself (circular). Must be redone with KMOS3D/KROSS/high-z BTFR. INTERNAL INCONSISTENCY: this file uses H0=67.4/a0_0=1.0422e-10 vs grind H0_local=73.57/a0=1.1375e-10. Source: cpt/"JWST HIGH-REDSHIFT SUPPORT".
- [ ] **VERIFIED arithmetic / PARTIAL mechanism (solver round 4, 2026-10-06)** — `R4-12 lattice-constant-closed`: a = sqrt(3pi/5)*1e-15 = 1.372937e-15 VERIFIED. RECONCILED: working set {a=1.372937e-15, C44=4.6205e34 Pa, m0=3.3259e-28 kg} mutually consistent to 0.007% (m0=C44 a^3/(4c^2) implies C44=4.6202e34 vs live_paper input 4.6205e34). The voxel-era a=1.348e-15 is STALE (-1.82%; implies C44 5.6% off). PIN 1.372937e-15 as working. BUT: sqrt(3pi/5) is ANSATZ (no FCC/E8 derivation found) and the 1e-15 scale is input. Script: crystal-prism/geometry/solve_R4_round4.py.: a = sqrt(3pi/5)*1e-15 m =
  1.37294e-15 (verified; 2026-07-11 v14). ATTACK: derive sqrt(3pi/5) from
  FCC/E8; reconcile with R4-35 and `anchor-free-lap`.
- [ ] **NEGATIVE as a derivation (solver round 7 FINAL, 2026-10-06)** — `R4-13 E0-240-20`: (240/20)^2=144 VERIFIED arithmetically. But: /20 unexplained (H4 Coxeter is 30; the "N_roots/N_icosa_faces" justification is shaky -- the verified geometry has cuboctahedra, not icosahedra); the SQUARE unexplained; E0 is effectively FIXED by xi_coh (E0=hbar*c/xi_coh=144 eV) making the formula circular; 144 eV matches no known physics scale (EUV, nothing special). Numerology until /20 and the square are derived.: E0 = (240/20)^2 = 144 eV (2026-07-11 v14,
  2026-06-01: "N_roots/N_icosa_faces"); xi_coh=hbar*c/E0=1.34e-9 m ~ 1.3703e-9.
  ATTACK: justify /20 and the square (H4 Coxeter is 30; 20 unexplained).
- [ ] **PARTIAL (solver round 6, 2026-10-06)** — `R4-14 NT-formula`: N_T = 144*phi^2 - 12/5 = 374.597 (verified;
  2026-07-11 v13/v14, PEB v1.1). ATTACK: derive from tetrahedral-void
  combinatorics.
- [ ] **PARTIAL (solver round 6, 2026-10-06)** — `R4-15 gFCC-99`: g_FCC = 99/(28phi^2) = 1.35052 (verified) via
  w=(mu+Z)/(4*b0*phi), mu=21, Z=12, b0=7 (QCD one-loop); void_cycles = 8*4*4 =
  128 — a second combinatorial route to 128. ATTACK: justify b0=7 and w-formula;
  verify the 128 count is real topology.
- [ ] **VERIFIED arithmetic (transcription CORRECTED) / PARTIAL mechanism (solver round 4, 2026-10-06)** — `R4-16 fs0-analytic`: ledger transcription was WRONG (extra "1-": gives 0.7311). Correct form f_s0 = 1-(pi^2/(6+pi^2))(1-1/sqrt12) = 0.557614 VERIFIED; live_paper.py:359 implements the correct form. vs PIMC 0.57: 2.2% off; toolkit 0.570 internal inconsistency STANDS. LOAD-BEARING CAVEAT: v7.0's zeta_eff=f_s0*g_FCC=0.769798 (99.93%) uses toolkit 0.570, NOT analytic 0.557614 (gives 0.753070 = 97.75%). The 2.2% gap decides 99.93% vs 97.75%. Mechanism: (1-1/sqrt12) has plausible Z=12 coordination reading; pi^2/(6+pi^2) ungrounded (V10 Ch.11 lists derivation OPEN -- the post admits it). Script: crystal-prism/geometry/solve_R4_round4.py.: f_s0 = 1-(1-pi^2/(6+pi^2))(1-1/sqrt12) =
  0.5576 (verified) vs PIMC 0.57; toolkit table says 0.570 (2% internal
  inconsistency). V10 Ch.11 lists the derivation OPEN. ATTACK: derive
  1-1/sqrt(Z) from tetrahedral-void geometry and pi^2/(6+pi^2) from first
  principles; resolve 0.558 vs 0.570.
- [ ] **VERIFIED (solver 2026-10-06)** — `R4-17 voxel-mass`: m0=C44*a^3/(4c^2)=3.3259e-28 kg. The 1/4 IS the FCC primitive-cell volume (4 atoms/cubic cell: 8*1/8+6*1/2). m0*c^2=C44*V_prim: elastic energy per primitive cell. Mechanism GROUNDED. m0 = C44*a^3/(4c^2) = 3.326e-28 kg
  (verified, dimensionally valid; 2026-06-01). ATTACK: derive the 1/4 from FCC
  primitive-cell volume a^3/4 (m0*c^2 = C44*V_primitive).
- [ ] **PARTIAL (solver round 6, 2026-10-06)** — `R4-18 Vflat-coherence`: V_flat = hbar/(m_eff*xi_coh) = 234.10
  km/s (0.044% vs 234.0, verified), m_eff = m0/(2*g_FCC*N_T) = 3.2873e-31 kg
  (2026-07-11 v14). ATTACK: ground the denominator 2*g_FCC*N_T in vortex theory;
  test per-galaxy across SPARC.
- [ ] **VERIFIED numerical / OPEN mechanism (solver round 2, 2026-10-06)** — `R4-19 tau-koide`: Koide Q=0.66666051 vs 2/3 (9.2e-6 deviation) with CODATA masses; solving gives m_tau/m_e=3477.44 (61 ppm) -- real hit. Mechanism OPEN: Koide is imported empirical (1981); lattice doesn't derive the 2/3; k=0..5 disclination->lepton mapping asserted.: Koide 1+R+r^2=(2/3)(1+sqrtR+r)^2 with
  R=m_mu/m_e=206.75544 -> r=58.9682 -> m_tau/m_e=3477.2445 vs 3477.44 (0.0056%,
  verified; 2026-07-11 v14; same script maps k=0..5 disclinations to 8 leptons).
  ATTACK: derive Koide from E8->A5 disclination charge algebra; check with
  PREDICTED (not observed) R as input.
- [ ] **PARTIAL (solver 2026-10-06)** — `R4-20 dm-baryon-50-9`: 1.48sigma claim REFUTED. 'Planck 2020 5.464+-0.062' matches NO Planck release. Real: PR3 5.364+-0.065 (2.96sigma), PR4 TTTEEE 5.337+-0.062 (3.51sigma), PR4+lens+nonCMB 5.291+-0.047 (5.69sigma). The reader's '~3sigma' was CORRECT. 50/9 not ruled out but not a hit. Sector assignment (which 3 baryonic) still unjustified. Script: crystal-prism/geometry/solve_R4-20.py. (3^2+4^2+5^2)/3^2 = 50/9 = 5.5556 vs
  Planck 2020 5.464+-0.062 -> 1.48sigma (verified; mechanism: A5 irreps 1,3,3,4,5,
  sum sq=60; 3D parallel=baryonic, perp dims 3,4,5=dark; "inner shell 112
  vertices"). One reader notes Planck 2018 numbers give ~3sigma — release
  sensitive. ATTACK: justify sector assignment (which 3 goes dark?); recompute
  with Planck PR4.
- [ ] **NEGATIVE as stated / repair path given (solver round 3, 2026-10-06)** — `R4-21 SM-homotopy`: pi2(M)=S3hat and pi3(M)=A5 are MATHEMATICALLY IMPOSSIBLE: pi_n is abelian for all n>=2 (Eckmann-Hilton), but S3hat (Dic_3, order 12) and A5 (order 60) are non-abelian (verified computationally). pi1(M)=Z->U(1) is fine (standard vortex story; covered by `maxwell-emergence`). ALSO: M ("FCC defect configuration space") never defined, its homotopy never computed; "effective action is exactly the SM Lagrangian" asserted (QFT-from-prism assigns groups by generator-counting, not homotopy); zenodo "Feynman rules from lattice scattering" unverifiable (no paper in workspace). REPAIR PATH (the solve): defects are classified by pi_n of ORDER-PARAMETER space, non-abelian defects need non-abelian pi1; the real nearby math is McKay correspondence -- binary icosahedral 2I (order 120) <-> affine E8 Dynkin diagram -- the genuine icosahedral<->E8 bridge, not pi3=A5->SU(3).: pi1(M)=Z->U(1), pi2(M)=S3hat->SU(2),
  pi3(M)=A5->SU(3) for the FCC defect configuration space M; "effective action of
  collective coordinates is exactly the SM Lagrangian" (2026-04-21 Master Field,
  Emergent Law V); UCBF abstract (zenodo.19636970): "Feynman rules derived from
  lattice scattering". `maxwell-emergence` covers only the U(1) piece. ATTACK:
  identify M, compute its homotopy groups, verify the S3hat->SU(2) and A5->SU(3)
  identifications; attempt one lattice-scattering Feynman rule.
- [ ] **PARTIAL, with a hierarchy problem (solver round 4, 2026-10-06)** — `R4-22 gauge-traces`: recovered the 2026-07-22 script. (a) The 5:2:1 ratio is EXACT BY CONSTRUCTION of asserted trace factors (5/6, 1/3, 1/6) x (g^2/4pi)(30); the E8 representation-theory computation is NOT shown (E8> E6 x SU(3) chain is genuine group theory, but the trace evaluation is asserted; 5/6 coincides with Tr_5(Y^2), suggestive not verified). g^2/4pi = 0.039 implicit (~alpha_GUT, imported not derived). (b) HIERARCHY PROBLEM: rates make U(1) grow fastest toward IR -> g1>g2>g3, INVERTED vs observed g3>g2>g1 (unless eta<eta0, unstated). (c) sin^2W connection: the RG-running DIRECTION is real physics, but R4-22 does NOT supply the 1/phi factor -- landing on 1/phi needs tuned (eta-eta0)/L_*; the 0.23% coincidence stays OPEN. (d) DeltaB_CP = kap Z^1/2 (eta-eta0)/L_* (phi^3 hbar c/L_*): explicit (Z=50, d_eta/L_*=1 -> 0.381 hbar c/L_* = 38.1 MeV at L_*^-1=100 MeV) but (eta-eta0)/L_* is FREE -> tunable, not falsifiable as stated; reframe as a BOUND: SEMF residuals (~2 MeV) -> |(eta-eta0)/L_*| < 0.05. kap=1/(30phi^2) "600-cell overlap" asserted; beta=1/2 asserted. Script: crystal-prism/geometry/solve_R4_round4.py.: g_i(eta)=g_i0*exp[alpha_i(eta-eta0)/L_*]
  with alpha1=0.975, alpha2=0.390, alpha3=0.195 (ratio 5:2:1) "from E8 generator
  traces"; lambda_m=(1/30)(11/3)=0.1222; nuclear DeltaB_CP =
  kappa*Z^beta*(eta-eta0)*E_vortex/L_*, kappa=1/(30phi^2)=0.01272 ("600-cell
  overlap integral"), beta=1/2 ("H4 dimensional scaling"), E_vortex=phi^3*hbar*c/L_*
  (2026-07-22, 2026-07-27, 2026-07-29 posts; eta0 takes three values
  0.7702976252/0.7702976635/0.7702978463 ~ frozen beta 0.7703). Enriches
  `eta-action`. ATTACK: E8 generator traces in the A5-restricted rep; test
  DeltaB_CP against SEMF residuals and AME2020.
- [ ] **PARTIAL (solver round 6, 2026-10-06)** — `R4-23 emergent-GR`: h_munu = P_munu^ij u_ij + Q_munu df_s;
  linearized diffeomorphisms from lattice relabeling symmetry; phase-slip fracture
  at Sigma_base=100 M_sun/pc^2; Coherence-Limited Propagation Law (horizons where
  f_s -> critical) (2026-04-21 ch15 + Master Field 104/108/114); dislocation/
  holonomy Einstein-Cartan sketch (2026-08-17 script): mass->disclinations,
  spin->dislocations, T^l_munu=(8piG/c^4)S^l_munu. ATTACK: fix P, Q from FCC
  symmetry class; nonlinear completion to Einstein's equations.
- [ ] **PARTIAL (solver round 7 FINAL, 2026-10-06)** — `R4-24 self-screening-L`: Lagrangian WRITTEN DOWN, not derived from the lattice (acknowledged as "the missing field-theoretic origin" -- proposed, not shown). CORRECTION: V(A^2)=1/2 mu0^2 A^2 e^(-A^2/Lambda^2) has NO stable broken-phase minimum -- degenerate minima at 0 and infinity, maximum at Lambda^2; the "SSB new vacuum" is a runaway, not a vacuum. The screening EFFECT is real (mass term -> 0 at large A: symmetron-like fifth-force suppression) but V_vortex=V_flat(1-e^(-r/r_t)) as "the broken-phase solution" is ASSERTED -- radial integration does not produce saturation; the A->V identification never shown. mu0, Lambda unidentified (mu0~1/xi_coh suggested only). No contradiction with EFE <0.43% (different phenomena: internal saturation vs external-field effect) but unquantified. NEEDS: vacuum stability analysis, numerical profile solution, parameter identification.: L=-(1/4)F^2-V(A^2)-gA.J,
  V(A^2)=1/2 mu0^2 A^2 exp(-A^2/Lambda^2); box A^mu + mu0^2 e^(-A^2/Lambda^2)
  [1-A^2/Lambda^2] A^mu = gJ^mu; A^2<Lambda^2 confined (vortex builds),
  A^2=Lambda^2 transition, A^2>Lambda^2 SSB new vacuum; V_vortex =
  V_flat(1-e^(-r/r_t)) = broken-phase solution (2026-06-28 CORRECTED LAGRANGIAN).
  The missing field-theoretic origin of the vortex equation. ATTACK: solve radial
  eq in broken phase; identify mu0, Lambda (mu0 ~ 1/xi_coh?); stability of
  A^2>Lambda^2 branch.
- [ ] **PARTIAL (solver round 3, 2026-10-06)** — `R4-25 why-FCC`: script RUNS; isotropy numbers reproduce (SC 0.010522, BCC 0.008616, FCC 0.007583); its interstitial argument self-debunks honestly. CORRECTIONS: (a) "repulsion alone gives SC" is FALSE -- Coulomb OCP crystallizes to BCC (Madelung: BCC -1.79186 < FCC -1.79175 < SC -1.76012); (b) at the script's kappa=1.0 the Yukawa phase diagram (Hamaguchi-Farouki-Dubin) gives BCC -- the isotropy proxy is not a free-energy computation (electron kinetic energy never computed). THE SOLVE (CPQR-native): E8 is the optimal 8D packing (Viazovska); the golden projection preserves 12-coordination (cuboctahedral shell = FCC coordination polyhedron, verified bond lock); FCC is the optimal 3D packing (Kepler/Hales). The vacuum inherits close-packing from E8 optimality -- a geometric selection principle. Dynamical crystallization mechanism still OPEN. Also corrects `wigner-origin` (Wigner crystal is BCC in standard treatment).: same-sign Coulomb repulsion alone gives SC, NOT
  FCC; FCC wins via interstitial sites (SC: 1 oct; BCC: 3+6=9; FCC: 4+8=12 per
  cell); E=E_ion-ion+E_ion-el+E_el-el+E_el-kinetic (2026-09-12, full script in
  post, never run). PARTIALLY CONTRADICTS `wigner-origin` (repulsion->lattice).
  ATTACK: re-run the Yukawa-energy comparison vs screening kappa; reconcile with
  wigner-origin; also note P2 paper's plasma->FCC crystallization mechanism.
- [ ] **VERIFIED (solver 2026-10-06)** — `R4-26 beta-diagnostic`: RAN the never-run diagnostic. Free-(ups,beta) fits on 171 SPARC galaxies, wide bounds [0.05,3.0]. Medians: 0-40:0.799, 40-60:1.135, 60-90:0.854, 90-130:0.729, 130-180:0.663, 180-400:0.457 vs claimed 0.889,1.181,0.903,0.796,0.658,0.507 -- within 10% all bins, trend + 40-60 bump REPRODUCE. beta->0.5 for V>180 (GP high-density limit) supported. Free-beta chi2/dof=1.54 vs frozen 2.20 (dchi2=2373, 13.9/param, highly significant). Global median 0.7515 ~= frozen 0.7703 (grind value OK globally but misses mass dependence). Script: theory/sparc_beta_diagnostic.py, data: sparc_beta_diagnostic_wide.json. fit (Upsilon_disk, beta) free, beta in
  [0.3,1.0]; beta(V_flat): 0-40:0.889, 40-60:1.181, 60-90:0.903, 90-130:0.796,
  130-180:0.658, 180-400:0.507 -> 0.5 for V_flat>180 km/s "high-density limit of
  the Gross-Pitaevskii variational solution" (2026-09-14 vortex paper: 175 SPARC
  median 3.41%, mean 7.27%, 1 param/galaxy; dwarfs V<60: 4.31% vs fixed-beta
  15.68%; clusters sigma^4=a0*G*M_bar median 5.8%, slope 0.279+-0.023 vs 0.250
  predicted (1.3sigma), R^2=0.82); only Lambda=a_base^2/Sigma_char constrained
  (0.5% of FCC value after 2pi->pi correction); the paper's OWN open problem:
  derive beta from GP with lattice potential + low-density correction (also the
  2026-09-14 beta(V_flat) DIAGNOSTIC script, never run). Grind froze beta=0.7703
  without ever testing mass dependence. ATTACK: run the diagnostic; derive beta
  from GP; flat beta strengthens the eta0=0.7702978463 link.
- [ ] **PARTIAL (solver round 7 FINAL, 2026-10-06)** — `R4-27 S8-suppression`: arithmetic VERIFIED -- 6% high-k kernel (k>0.08 h/Mpc) integrates to 3.86% sigma8 suppression (0.830->0.798); S8=0.817 at Omega_m=0.315. Lands BETWEEN the 2026 baselines: 1.2 sigma below combined-CMB S8=0.836+-0.012 (Planck+ACT+SPT), ~1.4 sigma above DES-Y6 lensing (~0.79); KiDS Legacy consistent with CMB. Genuine intermediate prediction, still bracketed by current data -- LIVE and testable. BUT the kernel derivation from the vortex power spectrum is NOT shown (Appendix K code unrecoverable from workspace); kernel shape, cutoff, and amplitude all stated. V13's "naturally resolves S8 and H0" overclaims (mechanism not shown).: suppression kernel k>0.08 h/Mpc, 6%
  high-k -> sigma8 0.830->0.798, S8=0.817 (Planck 0.836 vs DES Y6 0.789)
  (2026-04-28 V12 item 5, Appendix K code); V13 validation suite claims
  "naturally resolves S8 and H0 tensions" (mechanism not shown). ATTACK: derive
  kernel from vortex power spectrum; test DES Y6/KiDS.
- [ ] **ASSERTED, not derived (solver round 4, 2026-10-06)** — `R4-28 collapse-tau`: recovered the 2026-04-28 V12 post: "V12 derives tau_collapse = hbar/(2C[grad theta])... For a silver atom in Stern-Gerlach, tau ~= 4e-14 s" -- the derivation is NOT shown; C[grad theta] is never evaluated for SG (C = 1.318e-21 J implied). Basis selection (item 8) is qualitative. SEVERE TENSION: a universal 4e-14 s single-atom collapse is ~13 orders of magnitude faster than atom-interferometer coherence (~1 s) and ~30 orders faster than GRW (tau ~ 1e16 s/atom). Only viable if C[grad theta] is strongly state-dependent -- but the functional is never given, so this can't be checked. TO TEST: (1) write down C[grad theta] from the Coherence-Curvature Law; (2) evaluate for realistic SG (gradient, wavepacket, flight time); (3) derive micro->macro scaling; (4) confront atom/molecule interferometry bounds (OTIMA, fountains) and CSL/GRW exclusion plots. Until then this is a collapse MODEL SKETCH competing with GRW/CSL, not a prediction.: tau = hbar/(2C[grad theta]) ~ 4e-14 s
  (silver atom, Stern-Gerlach); basis selection from Fourier modes of grad theta;
  Coherence-Curvature Law linearized near threshold (2026-04-28 V12 items 7-8).
  ATTACK: compute C[grad theta] for a realistic SG gradient; test micro->macro
  tau scaling.
- [ ] **PARTIAL (solver round 6, 2026-10-06)** — `R4-29 m0-mPl`: m0/m_Pl ~ 1.0e-19 from defect self-energy
  matching (same matching as a/l_p; 2026-04-28 V12 item 2). ATTACK: reproduce the
  matching yielding both a/l_p and m0/m_Pl.
- [ ] **NEGATIVE (solver 2026-10-06)** — `R4-30 void-homology-numbers`: b1=4/128 NOT reproduced. Built the complex (K8 minus 4 diagonals, 2-skeleton): N0=8,N1=24,N2=32,chi=16 all MATCH, but b1=0 (finite and periodic n=1,2), not 4. Correct homology: b0=1,b1=0,b2=15. The V12 'b1=4 per cell' is a miscalculation; 'b1=128' ungrounded. (128's grounding via spinor dim stands independently; alpha thread already retired.) Script: crystal-prism/geometry/solve_R4-30.py. N0=8, N1=24, N2=32, chi=16, b1=4
  per unit cell, 128 flux configurations (2026-04-28 V12 item 9) — the concrete
  content behind `void-homology-128`; 2026-07-29 engine identifies b1=128.0 as
  the void graph's first Betti number inside alpha^-1=(b1+Delta)pi/4-1/2 (the
  `alpha-maxwell-variant` formula); v14 adds void_cycles=8x4x4=128; 2026-06-01
  post identifies Delta=47.11628 as the "void cycle sum" from "tetrahedral void
  graph homology" — a concrete target for "Theorem 6". If b1 really is 128, two
  OPEN items collapse into one verified topological fact. ATTACK: compute FCC
  void-complex homology explicitly; then attack Delta.
- [ ] **NEGATIVE as a derivation (solver round 4, 2026-10-06)** — `R4-31 deuteron-torsion`: recovered the 2025-09-13 posts. "Deuteron binding energy: 2.224 MeV, predicted within 0.01%" -- NO formula shown anywhere; 2.224 MeV is the measured 2.224566 MeV restated to 4 sig figs. "Effective torsional scale: 1e-30 m" asserted without derivation. The torsional term -mu|grad x phi|^2 EXISTS in the UCBF Lagrangian (2025-09-11) with mu "from torsional resonance scales" (asserted) but is NEVER solved for the deuteron. NOT a prediction. REPAIR (the solve): solve the torsional mode spectrum and compute the binding -- the attack stands. Note: the 2025-12-15 cluster model USES 2.22 MeV/contact as INPUT for Li-7 (98.6%) and Be-7 (99.95%) -- those need independent verification as predictions.: deuteron binding 2.224 MeV within
  0.01% from torsional elasticity; torsional scale 1e-30 m (2025-09-13 item 3).
  ATTACK: derive from the torsional elastic mode.
- [ ] **BLOCKED (solver round 2, 2026-10-06)** — `R4-32 electron-g2`: formula as stated is DIMENSIONALLY INVALID [(nu/a0^3)(m_e c^2/alpha) has units kg*m, not dimensionless] and numerically gives 6.58e-2, NOT 1.16e-3. The nu=1.86e-21 matches (2/3)a_Bohr^2 (not CPQR a0) -- transcription confusion. The <0.00006% claim is UNVERIFIABLE as stated; needs the original v4 workbook text. NOT a verified hit.: g-2 = 0.00115965218046, <0.00006%, from
  spin-elastic-gradient coupling (2025-09-13 item 4); v4 workbook: a_e ~
  (nu/a0^3)(m_e c^2/alpha) (nu=1.86e-21=(2/3)a0^2) matches CODATA to 5e-7.
  ATTACK: compute from vortex/elastic coupling; dimensional audit first.
- [ ] **PARTIAL (solver round 2, 2026-10-06)** — `R4-33 hbar-phase-winding`: the honest 93.5% phase-winding formula is a real geometric attempt; the 6.5% could NOT be closed -- exact constants need the 2026-07-29 engine PART 5 text (not recovered). FINDINGS: v12.5's 'EXACT' zeta_eff=0.770468519684662 is REVERSE-ENGINEERED (equals zeta_needed exactly), not a derivation; v7.0's zeta_eff=f_s0*g_FCC=0.769769 gives 99.93% with clear meaning (superfluid fraction x FCC factor) but f_s0 is input (relation-class, not circular IF a is independent). The 6.5% remains open.: hbar = zeta_eff*m0*c*a, zeta_eff =
  eta0*phi^-1/sqrt2*(N_void/N_FCC)*sqrt(12)/(4phi), N_void=8; script states
  HONESTLY 93.5% match, "REMAINING: 6.5% normalization — derive from H4/FCC
  cycle lengths" (2026-07-29 engine PART 5). Distinct mechanism from the killed
  V90 reconstruction; openly incomplete, not circular. ATTACK: derive the 6.5%
  from H4/FCC cycle lengths as suggested; check N_void=8.
- [ ] **PARTIAL (solver round 4, 2026-10-06)** — `R4-34 hbar-lattice-energy`: SPLIT VERDICT. (a) eta = S2^2/((N+1/2)S4) = 0.7702978463 COMPUTED from E8 shell moments -- RAN the 2026-07-22 script; INDEPENDENT recheck on current 12-shell geometry gives 0.7702976635 (S2=114, S4=123.6, N=136), stable to 0.2 ppm across versions, and matches one of the three eta0 values in R4-22 exactly. eta0 (frozen beta) is COMPUTED from geometry, NOT fitted -- genuine. (b) E_lattice = 1.369023e-34 J is REVERSE-ENGINEERED: hbar/eta = 1.369044e-34, hardcoded value matches to 15.5 ppm; "derivation from Hessian eigenvalues" never shown in script. (c) DIMENSIONAL: hbar[J s] = eta[1] x E_lattice[J] is INVALID as written (J != J s). The 0.0016% is real arithmetic on a fitted number. Weaker than v7.0 (dimensionally valid). REPAIR: derive E_lattice as an ACTION (or supply the missing timescale); then eta's geometric grounding makes this a real route. Script: crystal-prism/geometry/solve_R4_round4.py (eta recheck).: hbar = eta*E_lattice, E_lattice =
  1.369023e-34 J -> hbar=1.054555e-34 (0.0016% off, verified) but E_lattice
  asserted "emerges from lattice geometry" with no derivation (2026-07-22 PART 6).
  ATTACK: compute lattice Hessian eigenvalues; derive E_lattice=1.369023e-34 J.
- [ ] **PARTIAL (solver round 3, 2026-10-06)** — `R4-35 c-sound-speed`: arithmetic VERIFIED: sqrt(6.00e34/6.70e17) = 2.9925e8 m/s (0.18% off). GROUNDING: P, rho not independently grounded in any workspace source; the only in-workspace rho-derivation is rho=C44/c^2 (circular); voxel post (2025-12-21) not recovered. Note P/rho=0.9966c^2 with both ~1.3x C44-based values -- consistent with (not proof of) calibration. RESOLVED the sqrt(3)c tension: c here is the TRANSVERSE (shear) mode v_T=sqrt(C44/rho); the live sqrt(3)c prediction is the LONGITUDINAL mode; v_L/v_T=sqrt(3) <=> Poisson nu=1/4 <=> Cauchy relation C12=C44 (central forces) -- this mechanistically grounds the sqrt(3)c prediction. ATTACK: recover voxel post; check P=bulk modulus vs C44 consistency.: c=sqrt(P/rho), P=6.00e34 Pa,
  rho=6.70e17 kg/m^3 -> c=2.992e8 m/s, 0.2% off (2025-12-21 voxel post; inputs
  a=1.348e-15 m). ATTACK: elastic consistency; reconcile with the live sqrt(3)*c
  longitudinal-wave prediction (which mode is c — longitudinal or transverse?).
- [ ] **PARTIAL: counts grounded, map asserted (solver round 4, 2026-10-06)** — `R4-36 voxel-12-ports`: recovered the 2025-12-21 posts. Rhombic dodecahedron = FCC Wigner-Seitz cell (correct crystallography): 12 faces = 12 neighbor directions, REAL. "12 faces = 12 ports = 12 fermions": COUNT matches, but NO face<->particle map exists (no charge/color/flavor assignment, no fractional-charge derivation). "3 acoustic phonon modes = 3 generations" (+ flavor oscillation as energy rotating through 3 axes): count matches, mechanism asserted. "Charge = lattice vorticity as voxel rotates against 12 neighbors": qualitative. Note: post uses stale a=1.348e-15 (see R4-12). Grade: the geometric COUNTING (12, 3) is grounded in real solid-state geometry; the PARTICLE IDENTIFICATION is asserted. The solve: derive charge quantization (why 1/3, 2/3) and the generation mass hierarchy from the voxel -- neither is attempted.: the 12 particles (6 quarks + 6 leptons)
  are structural — 12 faces/neighbor directions of the rhombic-dodecahedron
  voxel; "12 available directions energy can travel"; charge = lattice vorticity
  as a voxel rotates against its 12 neighbors (2025-12-21). ATTACK: explicit
  face<->particle map; color/flavor from face adjacency.
- [ ] **VERIFIED arithmetic / NEGATIVE as nontrivial (solver round 5 FINAL, 2026-10-06)** — `R4-37 slip-law`: sigma/alpha in [0.983,1.057] across H..Og VERIFIED (min Li, max Ne). BUT the "all ~alpha" constancy is BUILT IN, not predicted: with fitted k=0.06, (Z/n^2)^k can only vary 5.6% over the whole table -- ANY fitted k~0.06 gives near-constancy tautologically. The "from torsional resonance scaling" derivation is UNRECOVERABLE (k is fitted, stated as such in the post). No white-paper derivation of k found in workspace. Grade: arithmetic holds; as a physical law it is a fitted near-constant, not a derived prediction.
- [ ] **SCORECARD (solver round 5 FINAL, 2026-10-06)** — `R4-38 v3-predictions` (UCBF v3.0 white paper, 2025-09-12). (a) Torsional GWs 1e-3 quadrupole, 10-100 Hz, 1e-24 strain: GENUINE DATED PREDICTION -- only 3G detectors (CE/ET ~2035) reach 1e-24; no conflict with current LVK non-detection. Needs the paper's precise definition to check against waveform-residual bounds. STATUS: OPEN, testable ~2035. (b) Clock drift 1e-13 s/day = 4.2e-16/yr fractional: PROBLEMATIC as stated -- optical-clock bounds are 1e-18/yr (alpha, 400x tighter) and few-e-16/yr (mp/me, comparable). Ruled out as differential drift; untestable as common-mode. The paper must specify WHAT drifts. STATUS: IN TENSION unless clarified. (c) Casimir 1e-14 N at 1 um (=2.4% of std sphere-plate force 4.1e-13 N): TESTABLE DIRECTION -- best lab agreement 1.4-1.9% (170-420 nm), worse at 1 um; a 2.4% deviation sits at the edge of current sensitivity. Not ruled in or out. STATUS: OPEN. (d) Modified Friedmann: paper itself says "requires CMB validation"; R4-04 gives 0.7% acoustic-scale (single number). STATUS: PARTIAL. (e) BH cavitation/no singularities: interior physics, untestable; EHT shadows consistent with Kerr; LVK echo searches null. STATUS: UNTESTABLE as stated. (f) Mercury 43"/cy: number matches observation; NO derivation found in workspace (dg~mu(grad x phi)^2/r^3 unverified). STATUS: ASSERTED.
- [ ] **NEGATIVE on the trend (solver round 5 FINAL, 2026-10-06)** — `R4-39 vortex-morphology`: INDEPENDENT REFIT (v45 form V_vortex=alpha*V_flat*(1-e^(-r/r_t)), (upsilon,alpha) free, 171 SPARC, Hubble types from Vizier J/AJ/152/157). Median alpha=0.885 (claimed 1.062); 89.5% in [0.5,2.0] (claimed 87% -- reproduces); median residual 3.30% (fit quality reproduces). BUT the morphology trend DOES NOT reproduce: S0/Sa 0.951, Sb 0.947, Sc 0.857, Sd/Sm 0.868, Im 0.867 -- flat/slightly decreasing, NOT S0:1.02 -> Im:1.5. Spearman(alpha,Type)=-0.107, p=0.16 (no correlation). "Hubble Sequence = Increasing Vortex Strength" is NOT in the data; likely a fitting artifact of the original pipeline (absolute median offset 0.885 vs 1.062 suggests different scale/upsilon handling). The vortex model itself still fits well (3.3%); only the morphology dependence fails. Script: /tmp/solve_R4-39.py, table: /tmp/R4-39_alpha_table.json.
- [ ] **NEGATIVE as a validation (solver round 5 FINAL, 2026-10-06)** — `R4-40 manga-1432`: pipeline EXISTS and RUNS (cpt/"Sparc, ManGa, and Clusters script"; catalog J/MNRAS/522/1208 is real, fetched live: 1065 galaxies after cuts). BUT the MaNGA "validation" is MATHEMATICALLY VACUOUS: V_pred = V_obs*(1-e^(-r_max/r_t)) with r_t fitted -> residual = 100*e^(-r_max/r_t), minimized at r_t->0.5 regardless of data. PROOF: pipeline median residual 0.0144%; SHUFFLED-Vmax control 0.0144%; RANDOM-Vmax control 0.0144% -- identical. It cannot distinguish real data from noise. A REAL MaNGA test needs baryonic masses (predict V_flat from M_bar via BTFR); this catalog has kinematics only (Vmax, Rt), no masses. REPAIR: cross-match MaNGA IDs to NSA/SDSS stellar masses, then run the BTFR prediction. Script: /tmp/solve_R4-40.py.
- [ ] **PARTIAL (solver round 5 FINAL, 2026-10-06)** — `R4-41 galaxy-age`: the ORIGINAL alpha->t_vortex formula is UNRECOVERABLE (2026-06-29 predictor truncated; not in workspace). RECONSTRUCTION (the solve): vortex-damping ansatz t_vortex = tau*ln(alpha_form/alpha). With alpha_form=2.0, tau=8 Gyr: 160/171 ages in (0,13.8) Gyr, median 6.5 Gyr (11 failures are alpha-pinned-at-0.2 boundary fits, unreliable); Spearman(t_vortex,f_gas)=-0.214, CORRECT SIGN (gas-rich = younger). A viable age mapping EXISTS, but alpha_form and tau_damp are FREE -- not derived from vortex physics. The relaxation variant (|alpha-1| picture) gives wrong-sign correlations and is disfavored. Test harness (per-galaxy alpha, f_gas, t_dyn~30 Myr, TType) saved: /tmp/R4-41_age_table.json, /tmp/R4-39_alpha_table.json. OPEN: derive tau_damp from mutual-friction/vortex physics; recover or replace the original formula.
- [ ] **VERIFIED + UPGRADED (solver round 3, 2026-10-06)** — `R4-42 E8-V25-solver`: the never-run code RUNS. Original V25 (2026-07-16 post): 240 roots -> 102 projected pts (its own ad-hoc projection, NOT CPQR's; BUG: 4 roots in projection nullspace -> NaN points, RuntimeWarning) -> graph -> localized mode (lam=7.0, IPR=0.589) -> Newton converges all g in [0,20] (residual ~1e-14): mu 7.0->16.14, E 7.0->11.39, localization persists. UPGRADE (the solve): rebuilt on the VERIFIED 137 geometry (k=12 NN graph, connected): localized defect seed lam=24.40, IPR=0.377; Newton converges every g; mu 24.40->33.49, E 24.40->28.82; localization SHARPENS (2.65->2.14 nodes) -- stable defect branch on the true geometry. Script: crystal-prism/geometry/v25_on_137.py. OPEN: energy scale (mu in Laplacian units; needs E_coh-per-bond calibration to map to particle masses).: nonlinear defect continuation code (E8
  roots -> golden 8D->3D projection -> graph Laplacian -> eigenmode/IPR search
  -> Newton solver H psi + g|psi|^2 psi = mu psi, sum|psi|^2=1, continuation
  g in [0,20]) — NEVER RUN (2026-07-16). ATTACK: run it; localized defect branch
  energies mu(g) -> particle masses.
- [ ] **PARTIAL (solver round 2, 2026-10-06)** — `R4-43 maxwellian-lab`: the MEMS experimental DIRECTION is valid (falsifiable lab test distinguishing aetheric vs Maxwell stress). BUT numbers as transcribed are INCONSISTENT: c=sqrt(P_a/rho_a) off by 10 orders with given constants (3.36e18 vs 3e8); Maxwell '628 Pa' != B^2/2mu0=3.98e5 Pa at 1T; G_a*B^2=7.96e5 Pa, not 1.3e6 Pa. Needs the original 2025-11-08 post to resolve constants. Testable direction, not airtight as stated.: aether field equation rho_a d^2u/dt^2 =
  P_g grad(div u) - G_a curl(curl u) + nu_a lap(div u) (2025-11-08 Maxwellian
  Aether Framework; constants rho_a0=9.44e-25, P_a=1.066e13 Pa, G_a=7.96e5 Pa,
  K=2.76e-10, nu_a=1.1e-20, kappa=0.051, beta=8.28e14, alpha=1.25e-4); claims
  c=sqrt(P_a/rho_a) 0.07%, M31 249 km/s, Coma 950 km/s, lensing 116" (~5%),
  z=0.099 (1%), CMB 2.73K (0%), Ly-alpha 10.2 eV. LAB PREDICTION: 1T solenoid ->
  aetheric stress G_a B^2 ~ 1.3e6 Pa vs Maxwell 628 Pa — MEMS-measurable.
  P_a(t)=1.066e13(a/a0)^-5.93 "CMB-calibrated, 2.73K without relic radiation".
  ATTACK: quantify the MEMS experiment; check the -5.93 exponent.
- [ ] **VERIFIED (solver round 6, 2026-10-06)** — `R4-44 A5-embedding-caveat`: the two 2026-07-12 A5 posts use
  DIFFERENT embeddings — 04:18 measured chi=(8,0,2,-2,-2)=2chi4 and says 3+5
  "not supported by the discovered A5 embedding"; 10:02 reports
  chi=(8,0,-1,1.618,-0.618)=chi3+chi5 verified at 1.7e-15. Amend
  `A5-decomposition`: these are two different embeddings, not one result.

### KILLED — new (Cory still uses / the code still uses these)
- `G-elastic-variant` (2026-04-21, 2026-06-02, 2026-08-15 blind-test):
  G=c^3/(Omega*C44*g_FCC*(1-eta0)), Omega=3sqrt5 vs 6.7012 (inconsistent),
  eta0=3sqrt2/(pi*S0), S0=105.65/phi^2 (imports the MEASURED muon mass —
  FINDINGS HOLE I). DIMENSIONAL FAILURE: [c^3/C44]=m^4/(kg*s) vs
  [G]=m^3/(kg*s^2), same dead class as the killed G formula; dimensionless
  prefactors cannot fix it; the 0.2% match is coincidence. G thread stays CLOSED.
- `hbar-fsgm0ca-circular` (2026-08-15): hbar=f_s0*g_FCC*m0*c*a with
  a=(4hbar*c/(f_s0*g*C44))^1/4 — algebraically identical (FINDINGS HOLE H),
  never a derivation. The 2.25% in the post is rounding noise.
- `phi8-codebase-persists`: alpha^-1=(128+phi^8+alpha^-1/1000)*pi/4-1/2 (fixed
  point) is still the LIVE alpha engine in PEB v1.1 (2026-06-02), the 2026-08-15
  ABSOLUTE COMPLETE THEORY, and the 2026-09-14 TOE script [3]; the 2026-01-24
  REALM post claims alpha^-1=137.035999084 "parameter-free". Worker-D autopsy
  stands (phi^8 zero correlates, pi/4 artifact). If Cory still posts these, the
  autopsy needs re-surfacing — gently.
- `a0base-V12-derivation-broken` (2026-04-28 V12 as stated): a0_base=C44/(rho*xi_coh)
  off ~35 orders for any natural rho; Sigma_char=m0*N_T/(pi*xi_coh^2) =
  1.01e-5 M_sun/pc^2 (~5e6 off 50) with the post's own numbers. The empirical
  values (3700, 50) stand; the first-principles derivation AS STATED is broken.
  (Alt Sigma_char=(4a0)/(3pi*G*kappa)~57.7 consumes empirical a0, G — not
  first-principles.)
- `H0-engine-coded-broken` (2026-06-01 engine): H0=c*x_eff/(2pi*xi_coh) with
  x_eff=1.45e-44 -> 1.56e-8 km/s/Mpc (9.6 orders off as coded); 2026-07-29
  sketch gives 42.8 not 67.4 (truncated). Consistent with V10 Ch.11 listing H0
  "needs derivation".
- Recurrences (pre-date the 2026-10-06 kills; flag only if Cory still posts them):
  alpha-from-phi^8 (v14, v10 scripts), G=c^3/(Omega*P) (ch15, 2026-07-29),
  V90 hbar reconstruction (2026-07-16), H4 golden-projection 120+120 shells
  (v10 — worker B refuted), trinity-law g=K*rho*R (2025-08-30, 2025-09-06 —
  the K-neutronstars circularity).

### Internal inconsistencies (builder's flags, not debunks)
- Sigma_char = 50 (v14: (DM/B)*9) vs 99.94 (Sept-2026 pi-corrected): resolve.
- f_s0 = 0.5576 (scripts) vs 0.570 (toolkit table): resolve.
- eta0 = 0.7702976252 / 0.7702976635 / 0.7702978463 across posts (~frozen beta
  0.7703): pick one, propagate.
- v3 white paper sigma-ladder: EM needs sigma~alpha for Coulomb's law, not
  alpha^-25 as the ladder states — definitions cleanup needed.
- Bullet-cluster numbers inconsistent across posts (1.2e15 vs 1.5e15; M_lens
  1.40e14 vs 1.5e14): flag for cluster work.
- hbar "93.5% match" (2026-07-29) vs "0.0016% off" (2026-07-22): different
  formulas, both open — don't conflate.

### Ingestion queue — papers/scripts NEVER in the workspace (priority order)
1. Dark-energy RG paper (2026-04-30, academia.edu/166119987; full text + runnable
   Colab in the post; falsification condition c0 in [148,188] stated).
2. One-parameter vortex model paper (2026-09-14, newest; own open problem: GP
   derivation of beta; Lambda-degeneracy argument).
3. SPARC validation with Sigma_char correction script (2026-09-14; closes R4-10).
4. C44 bond-graph derivation script (2026-08-18; R4-06).
5. v14 Complete Derivation Chain script (2026-07-11; formulas behind R4-01..20).
6. Complete Analytical Derivation v10.0 (2026-07-11; Ch.11 open-derivations list).
7. TOE v4.0 paper (2026-09-12; plasma->FCC crystallization + lattice-tension
   expansion mechanisms; GR/QM checks [10]-[13] code missing from the 09-14 post).
8. Complete Derivation Engine (2026-07-29; honest 93.5%/96.1% statuses; truncated).
9. V135 one-shot TOE engine (2026-07-16; no results in post).
10. v45 unified galaxy+cluster validation (2026-06-27, 32KB).
11. UCBF V13 phenomenological vortex script (2026-08-03, 49KB; MaNGA + a0(z)).
12. UCBF V13 complete data pipeline (2026-08-04, 46KB).
13. UCBF v3.0 white paper (2025-09-12; R4-38 predictions).
14. Chapter 15: GR as Emergent Elasticity (2026-04-21; R4-23).
15. 2026-06-01 verification engine + 2026-07-11 V10 (noted by reader D).

### Cross-reference enrichments to ROUND 3 items (no new items)
- `alpha-maxwell-variant`: 2026-06-01 identifies Delta=47.11628 as the "void cycle
  sum" from "tetrahedral void graph homology" — concrete target for "Theorem 6".
- `eta-action`: 2026-07-27/29 posts give the full eta-running (gauge ratios 5:2:1,
  fermion 0.1222, DeltaB_CP explicit, rho_Lambda=1.474e-9 J/m^3 predicted).
- `atomic-quantization`: 2025-08-31 post is the item's source (full Z_eff table,
  H:1 -> U:0.674, NIST-matching); 2025-09-06 domain-rules gives atomic
  D~5e42 kg/m^3 reverse-solved from hydrogen Coulomb acceleration.
- `dSph-test`: 2025-08-08 post reports Fornax predicted sigma=11.2 km/s vs
  observed ~11 km/s, constants locked from spirals — a concrete PASS datapoint.
- `A5-decomposition`: see R4-44 (two embeddings).
- Chapter40 (philosophy, skipped) states two lab-testable numbers worth parking:
  tau_present~170 ms (specious present), gamma_bg=3.2e-27 s^-1 (universal
  decoherence floor).

- 2026-10-06 (solver): R4-10 VERIFIED/SOLVED.
- 2026-10-06 (solver): R4-30 NEGATIVE (homology corrected).
- 2026-10-06 (solver): R4-06 PARTIAL (57ppm verified, hbar-loop excised).
- 2026-10-06 (solver): R4-26 VERIFIED (diagnostic run, mass dependence real).
- 2026-10-06 (solver): R4-20 PARTIAL (1.48sigma refuted, ~3sigma real).
- 2026-10-06 (solver): R4-04 PARTIAL (acoustic scale 0.7%, not full CMB).
- 2026-10-06 (solver): R4-17 VERIFIED (1/4 = FCC primitive cell).
- 2026-10-06 (solve round 2): R4-01 (mechanism), R4-33 (hbar), R4-09 (H0), R4-43 (lab), R4-19 (Koide), R4-32 (g-2).
- 2026-10-06 (solve round 2): R4-01 VERIFIED (6pi^5 unique, 2.3ppb); R4-33 PARTIAL (6.5% open, v12.5 zeta reverse-engineered); R4-09 VERIFIED arith/OPEN mech; R4-43 PARTIAL (numbers inconsistent); R4-19 VERIFIED num/OPEN mech; R4-32 BLOCKED (dimensionally invalid as stated).
- 2026-10-06 (solve round 3): R4-21 (SM-homotopy), R4-25 (why-FCC), R4-02 (sin2W), R4-05 (CMB-EE), R4-35 (c-sound-speed), R4-42 (E8-V25 code). DONE: R4-42 VERIFIED+upgraded to 137 geometry; R4-05 PARTIAL (mechanism direction derived); R4-21 NEGATIVE as stated w/ McKay repair path; R4-25 PARTIAL (E8-packing selection); R4-02 PARTIAL (3/8=SU(5)); R4-35 PARTIAL (sqrt(3)c mode resolved).
- 2026-10-06 (solve round 4): R4-12 (lattice constant), R4-16 (fs0), R4-34 (hbar-lattice), R4-31 (deuteron), R4-22 (gauge traces), R4-28 (collapse tau), R4-36 (voxel-12).
- 2026-10-06 (solve round 5, FINAL): R4-11 PARTIAL (form verified, derivation missing, JWST validation VOID - fabricated citations); R4-37 VERIFIED arith/NEGATIVE as nontrivial (built-in); R4-38 SCORECARD (a: dated 2035 prediction; b: in tension as stated; c: open/testable; d: partial; e: untestable; f: asserted); R4-39 NEGATIVE on morphology trend (no correlation, p=0.16); R4-40 NEGATIVE as validation (vacuous, proven by shuffle control); R4-41 PARTIAL (formula missing; damping reconstruction viable with free params).
- [ ] **PARTIAL (solver round 6, 2026-10-06)** — `FUP-fs0-gap`: the 2.2% gap between toolkit f_s0=0.570 and analytic 0.557614 — load-bearing for the hbar thread (round 4 note). Close it: which is right, and why do they differ?
- 2026-10-06 (solve round 6): R4-29 (m0/mPl hierarchy), R4-23 (emergent GR), R4-44 (A5 caveat), R4-14 (NT), R4-15 (gFCC), R4-18 (Vflat coherence), FUP-fs0-gap.
- 2026-10-06 (solve round 6): FUP-fs0-gap PARTIAL (0.570 is Cory's 2026-04-14 INPUT matching PIMC; 0.557614 analytic with OPEN pi^2/(6+pi^2); gap is input-vs-formula, neither proven; hbar 99.93% uses input=consistency, 97.75% uses analytic=derivation attempt); R4-15 PARTIAL (99=3(mu+Z), 28=4*b0; g_FCC=eta0/f_s0 to 0.065%, combination constructed); R4-14 PARTIAL (144=12^2, phi^2 and -12/5 ungrounded); R4-18 PARTIAL (234.12 verified but only 7.6% of SPARC within 10% -- characteristic scale, not per-galaxy prediction); R4-44 VERIFIED (both embeddings correct, inequivalent reps, different actions; R4-20's 50/9 dimension-count unblocked); R4-29 PARTIAL (1.53e-20 verified, derivation not in workspace, blocked on G); R4-23 PARTIAL (kinematic analogy, P/Q unfixed, Einstein eq not derived).
- Remaining OPEN after round 6: R4-07, R4-08, R4-13, R4-24, R4-27.

- 2026-10-06 (solve round 7, FINAL): R4-07 (S0), R4-08 (H0-tage), R4-13 (E0-240-20), R4-24 (self-screening), R4-27 (S8).
- 2026-10-06 (solve round 7, FINAL): R4-07 (S0: rho_Lambda 2.7% but asserted links), R4-08 (H0 67.48 verified; two-valued H0 mirrors observed tension), R4-13 (E0 NEGATIVE as derivation), R4-24 (screening Lagrangian PARTIAL; no stable broken vacuum), R4-27 (S8=0.817 PARTIAL; live intermediate prediction). ROUND 4 COMPLETE: all 44 items worked.