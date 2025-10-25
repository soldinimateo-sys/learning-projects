import numpy as np
import sympy as sp

def my_newton(f_expr, x0, tol=1e-6, max_iter=20):
    # Auto-detect variable from the expression
    free_syms = list(getattr(f_expr, 'free_symbols', []))
    x = free_syms[0] if free_syms else sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df = sp.lambdify(x, sp.diff(f_expr, x), 'numpy')

    xn = [x0]

    for _ in range(max_iter):
        if df(xn[-1]) == 0:
            raise ZeroDivisionError("First derivative is zero")
        x_new = xn[-1] - (f(xn[-1]) / df(xn[-1]))
        xn.append(x_new)
        if np.abs(x_new - xn[-2]) < tol:
            return xn

    raise ValueError("Newton method did not converge")
