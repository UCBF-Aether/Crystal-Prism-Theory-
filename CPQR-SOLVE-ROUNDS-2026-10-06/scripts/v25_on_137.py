"""V25 defect-continuation rebuilt on CPQR's VERIFIED 137 geometry.

Original: 2026-07-16 E8 TOE MASTER SOLVER V25 (Cory's post, never run).
V25 used its own ad-hoc "golden" projection (102 pts on S^2, incl. 4 NaN
points from roots in the projection nullspace -- RuntimeWarning bug).

This rebuild uses the verified map p=(x_i+phi*x_{i+4})/sqrt(2+phi) -> 137
points (136 nonzero + origin), k=12 nearest-neighbor graph (FCC coordination).

Pipeline: E8 roots -> verified projection -> kNN graph -> Laplacian ->
IPR eigenmode search -> Newton solver H psi + g|psi|^2 psi = mu psi,
sum|psi|^2=1, continuation g in [0,20].

RESULT (solver round 3, 2026-10-06): localized defect branch EXISTS on the
true geometry and is STABLE under nonlinearity (localization sharpens
2.65 -> 2.14 nodes; Newton residual ~1e-14 at every g). Energies mu(g) in
graph-Laplacian units -- physical scale calibration (E_coh per bond) is OPEN.
"""
import numpy as np, itertools, math

phi = (1 + math.sqrt(5)) / 2
D = math.sqrt(2 + phi)

def gen_roots():
    R = []
    for perm in set(itertools.permutations([1, 1, 0, 0, 0, 0, 0, 0])):
        for s in itertools.product([-1, 1], repeat=2):
            r = list(perm)
            ix = [i for i, x in enumerate(r) if x != 0]
            r[ix[0]], r[ix[1]] = s
            R.append(tuple(r))
    for s in itertools.product([-1, 1], repeat=8):
        if sum(1 for x in s if x == 1) % 2 == 0:
            R.append(tuple(x * 0.5 for x in s))
    return list(set(R))

def project_137(roots):
    proj = {}
    for r in roots:
        p = tuple(round((r[i] + phi * r[i + 4]) / D, 12) for i in range(3))
        proj.setdefault(p, []).append(r)
    return np.array(list(proj.keys()))

def knn_graph(pts, k=12):
    N = len(pts)
    d = np.linalg.norm(pts[:, None, :] - pts[None, :, :], axis=2)
    np.fill_diagonal(d, np.inf)
    A = np.zeros((N, N))
    for i in range(N):
        A[i, np.argpartition(d[i], k)[:k]] = 1
    return np.maximum(A, A.T)

def residual(x, g, L):
    mu, u = x[-1], x[:-1]
    return np.append(L @ u + g * u**3 - mu * u, np.sum(u * u) - 1)

def solve_newton(u, g, L, tol=1e-10, itmax=80):
    x = np.append(u, u @ L @ u + g * np.sum(u**4))
    n = len(x)
    for _ in range(itmax):
        F = residual(x, g, L)
        if np.linalg.norm(F) < tol:
            break
        J = np.zeros((n, n))
        for i in range(n):
            xp = x.copy(); xp[i] += 1e-6
            J[:, i] = (residual(xp, g, L) - F) / 1e-6
        x += np.linalg.solve(J, -F)
    return x[:-1], x[-1], np.linalg.norm(residual(x, g, L))

def main():
    pts = project_137(gen_roots())
    assert len(pts) == 137, len(pts)
    A = knn_graph(pts)
    L = np.diag(A.sum(1)) - A
    vals, vecs = np.linalg.eigh(L)
    ipr = np.sum(np.abs(vecs) ** 4, axis=0)
    mode = int(np.argmax(ipr))
    psi = vecs[:, mode] / np.linalg.norm(vecs[:, mode])
    print(f"seed: lambda={vals[mode]:.4f} IPR={np.sum(psi**4):.4f}")
    u = psi.copy()
    print("  g |    mu   |    E    | loc_len |  IPR  | residual")
    for g in np.linspace(0, 20, 21):
        u, mu, res = solve_newton(u, g, L)
        E = u @ L @ u + g / 2 * np.sum(u**4)
        ip = np.sum(u**4)
        print(f"{g:4.1f} {mu:8.4f} {E:8.4f} {1/ip:7.2f} {ip:.4f} {res:.1e}")

if __name__ == "__main__":
    main()
