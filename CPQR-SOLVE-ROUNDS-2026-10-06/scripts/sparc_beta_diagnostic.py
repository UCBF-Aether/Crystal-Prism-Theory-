"""R4-26: beta(V_flat) diagnostic -- the Sept-2026 vortex paper's own open problem.
Fit (upsilon_disk, beta) FREE per galaxy (beta in [0.3,1.0]), bin by V_flat,
compare to claimed: 0-40:0.889, 40-60:1.181, 60-90:0.903, 90-130:0.796,
130-180:0.658, 180-400:0.507. Grind froze beta=0.7703 without testing this.
"""
import math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sparc_baseline import (frozen_consts, load_sparc, solve_a_eff, chi2_of,
                            UPS_BULGE, G_PC, G_SI, MSUN, PI, C_SI)

def cpqr_predict_beta(R, Vd, Vb, Vg, ups_d, beta, C):
    Vd_ml = Vd * math.sqrt(max(ups_d, 0.01))
    Vb_ml = Vb * math.sqrt(UPS_BULGE)
    Vg_a = np.abs(Vg)
    Vb2 = Vg_a ** 2 + Vd_ml ** 2 + Vb_ml ** 2
    R_pc = R * 1000.0
    M_bar = max(np.percentile(Vb2 * R_pc, 90) / G_PC, 1e-5)
    V_flat = (C["a0_local"] * G_SI * M_bar * MSUN) ** 0.25 / 1000.0
    with np.errstate(divide="ignore", invalid="ignore"):
        Sigma = np.where(R_pc > 1e-10, Vb2 / (2 * PI * G_PC * R_pc), 0.0)
    _, r_t = solve_a_eff(R, Sigma, V_flat, C["a_base"], C["Sigma_char"])
    x = R / max(r_t, 1e-6)
    V_vortex = V_flat * (1.0 - np.exp(-(x ** beta)))
    return np.sqrt(Vb2 + V_vortex ** 2), V_flat

def nelder_mead_2d(f, x0, step, maxit=300, tol=1e-7):
    # simple 2D Nelder-Mead
    import numpy as np
    x = np.array(x0, float)
    simplex = [x, x + np.array([step[0], 0]), x + np.array([0, step[1]])]
    vals = [f(s) for s in simplex]
    for _ in range(maxit):
        order = np.argsort(vals)
        simplex = [simplex[i] for i in order]; vals = [vals[i] for i in order]
        if abs(vals[0] - vals[-1]) < tol: break
        c = (simplex[0] + simplex[1]) / 2
        xr = c + (c - simplex[2]); vr = f(xr)
        if vr < vals[0]:
            xe = c + 2 * (c - simplex[2]); ve = f(xe)
            simplex[2], vals[2] = (xe, ve) if ve < vr else (xr, vr)
        elif vr < vals[1]:
            simplex[2], vals[2] = xr, vr
        else:
            xc = c + 0.5 * (simplex[2] - c); vc = f(xc)
            if vc < vals[2]:
                simplex[2], vals[2] = xc, vc
            else:
                simplex[1] = (simplex[0] + simplex[1]) / 2; vals[1] = f(simplex[1])
                simplex[2] = (simplex[0] + simplex[2]) / 2; vals[2] = f(simplex[2])
    i = int(np.argmin(vals))
    return simplex[i], vals[i]

def main():
    C = frozen_consts()
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sparc_data")
    gals = load_sparc(data_dir, verbose=False)
    print(f"galaxies: {len(gals)}, frozen beta={C['beta']:.4f}")
    rows = []
    for _name, _g in gals.items():
        gal = dict(_g); gal['name'] = _name
        R, Vo, Ve = gal["R"], gal["Vo"], gal["Ve"]
        Vd, Vb, Vg = gal["Vd"], gal["Vb"], gal["Vg"]
        mask = (Vo > 1.0) & (Ve > 0)
        if mask.sum() < 5: continue
        Vm = Vo[mask]
        e = np.sqrt(Ve[mask] ** 2 + (0.05 * Vm) ** 2)
        def chi2(theta):
            u, b = theta
            if not (0.05 <= u <= 5.0 and 0.05 <= b <= 3.0): return 1e12
            try:
                p, _ = cpqr_predict_beta(R, Vd, Vb, Vg, u, b, C)
            except Exception:
                return 1e12
            if not np.all(np.isfinite(p)): return 1e12
            return float(np.sum(((p[mask] - Vm) / e) ** 2))
        # coarse grid then refine
        best = (None, 1e18)
        for u in (0.2, 0.5, 1.0, 2.0):
            for b in (0.3, 0.6, 0.7703, 1.2, 2.0):
                v = chi2((u, b))
                if v < best[1]: best = ((u, b), v)
        (u0, b0), _ = best
        (u_fit, b_fit), v = nelder_mead_2d(chi2, (u0, b0), (0.2, 0.1))
        _, Vf = cpqr_predict_beta(R, Vd, Vb, Vg, u_fit, b_fit, C)
        n = mask.sum()
        rows.append({"name": gal["name"], "Vf": float(Vf), "beta": float(b_fit),
                     "ups": float(u_fit), "chi2": float(v), "dof": int(n - 2)})
    bins = [(0, 40), (40, 60), (60, 90), (90, 130), (130, 180), (180, 400)]
    claimed = [0.889, 1.181, 0.903, 0.796, 0.658, 0.507]
    print(f"\n{'bin':>12} {'n':>4} {'med_beta':>9} {'mean_beta':>10} {'claimed':>8}")
    all_b = []
    for (lo, hi), cl in zip(bins, claimed):
        bs = [r["beta"] for r in rows if lo <= r["Vf"] < hi]
        all_b += bs
        if bs:
            print(f"{lo:>3}-{hi:<8} {len(bs):>4} {np.median(bs):>9.3f} {np.mean(bs):>10.3f} {cl:>8.3f}")
        else:
            print(f"{lo:>3}-{hi:<8} {0:>4} {'-':>9} {'-':>10} {cl:>8.3f}")
    print(f"\nglobal median beta = {np.median(all_b):.4f} (frozen grind value 0.7703)")
    # boundary pile-up check
    lo_n = sum(1 for b in all_b if b <= 0.301); hi_n = sum(1 for b in all_b if b >= 0.999)
    print(f"at lower bound 0.05: {sum(1 for b in all_b if b<=0.051)}, at upper bound 3.0: {sum(1 for b in all_b if b>=2.999)} (of {len(all_b)})")
    import json
    json.dump([{k: (float(v) if isinstance(v,(int,float)) else v) for k,v in r.items()} for r in rows], open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "sparc_beta_diagnostic_wide.json"), "w"), indent=1)
    print("saved sparc_beta_diagnostic_wide.json")

if __name__ == "__main__":
    main()
