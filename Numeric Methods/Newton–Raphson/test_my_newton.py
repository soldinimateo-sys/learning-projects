import pytest
import numpy as np
import sympy as sp
from my_newton import my_newton
from scipy.optimize import newton

def test_quadratic_funct():
    x = sp.Symbol('x')
    f_expr = x**2 - 4
    x0 = 3
    real_root = 2
    result = my_newton(f_expr, x0)
    assert np.isclose(result[-1], real_root, atol=1e-6)
    
@pytest.mark.parametrize("tol", [1e0, 1e-2, 1e-8, 1e-12], ids=["1","1e-2","1e-8","1e-12"])
def test_tolerance(tol):
    x = sp.Symbol('x')
    f_expr = x**2 - 4
    x0 = 3
    real_root = 2
    result = my_newton(f_expr, x0, tol=tol, max_iter=200)
    assert np.isclose(result[-1], real_root, atol=tol)
    
def test_raises_when_derivative_zero():
    x = sp.Symbol('x')
    f_expr = sp.Integer(2)  # Constant function -> derivative = 0
    with pytest.raises(ZeroDivisionError):
        my_newton(f_expr, 1)
        
def test_far_initial_guess():
    x = sp.Symbol('x')
    f_expr = x**3
    x0 = 1000
    with pytest.raises(ValueError):
        my_newton(f_expr, x0)