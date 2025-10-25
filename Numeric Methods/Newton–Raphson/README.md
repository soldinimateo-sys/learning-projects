# Newton–Raphson Method with EOQ Application

**A small, from-scratch implementation of the Newton–Raphson method, applied to the EOQ (Economic Order Quantity) cost model as a practical business example.**
The solution is validated against SciPy and supported by basic unit tests.

This project aims to build a clean and reproducible numerical workflow: starting from a symbolic formulation (SymPy), converting it into a numerical routine, evaluating convergence, and finally interpreting the result in a business context. The notebook documents both the mathematical reasoning and the applied side (inventory optimization), while the Python module and tests focus on correctness and maintainability.

## Overview

- Goal: show math knowledge, practical application, comparison with libraries, and how to test code in a clean, professional presentation.
- Core pieces:
  - A simple Newton–Raphson implementation in Python.
  - EOQ‑style cost optimization as a real‑world example.
  - Comparison with `scipy.optimize.newton`.
  - Reproducible tests via `pytest`.
  - A Jupyter notebook with derivations, visuals, and narrative.

## Math Background (Newton–Raphson)

Given a differentiable function f(x), Newton–Raphson iterates

\[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \]

Key conditions:
- f'(x_n) ≠ 0 at each step.
- A reasonable initial guess x0.
- Function differentiable near the root.

## EOQ Application (Cost Minimization)

We consider a simplified EOQ‑style cost function:

\[ C(L) = \frac{a}{L} + b\,L \]

where L is lot size, a is order/setup related cost, and b is holding cost. The optimal lot size satisfies dC/dL = 0, leading analytically to

\[ L^* = \sqrt{\frac{a}{b}}. \]

In practice, we set f(L) = dC/dL and find f(L) = 0 numerically using Newton–Raphson, then compare to the analytical solution and to SciPy.

## Implementation

- Custom function: `my_newton` in `my_newton.py:5`.
  - Inputs: symbolic expression `f_expr` (SymPy), initial guess `x0`, tolerance `tol`, `max_iter`.
  - Output: list of iterates `[x0, x1, ..., xN]`; the last value is the approximation to the root.
  - Errors: raises `ZeroDivisionError` if derivative is zero; raises `ValueError` if convergence is not reached within `max_iter`.

## Project Structure

- `my_newton.py:5` — Newton–Raphson implementation.
- `newton-0.ipynb` — narrative notebook: theory, EOQ example, plots, and comparisons.
- `test_my_newton.py:7` — pytest suite covering correctness, tolerance behavior, and error cases.
- `README.md` — this documentation.

## Installation

Requirements: Python 3.10+ recommended.

Set up a virtual environment (optional but recommended), then install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Notebook (Recommended for the EOQ story)

- Open `newton-0.ipynb` in Jupyter and run the cells top to bottom to see the theory, EOQ example, visualizations, and comparisons.

### Python API (Quick demo)

```python
import sympy as sp
from my_newton import my_newton

x = sp.Symbol('x')
f = x**2 - 4            # root at x = 2
seq = my_newton(f, x0=3)
approx = seq[-1]
print(approx)            # ~2.0
```

### Comparison With SciPy

```python
import sympy as sp
from scipy.optimize import newton

x = sp.Symbol('x')
f = sp.lambdify(x, x**2 - 4, 'numpy')
fprime = sp.lambdify(x, sp.diff(x**2 - 4, x), 'numpy')

sci = newton(func=f, x0=3, fprime=fprime)
print(sci)               # ~2.0
```

## Testing

Run the test suite with `pytest`:

```bash
pytest -q
```

What’s covered in `test_my_newton.py`:
- `test_quadratic_funct` checks convergence to a known root (`test_my_newton.py:7`).
- `test_tolerance` verifies tolerance effect (`test_my_newton.py:15`).
- `test_raises_when_derivative_zero` ensures derivative‑zero is handled (`test_my_newton.py:24`).
- `test_far_initial_guess` checks non‑convergence from a poor initial guess (`test_my_newton.py:30`).

## Limits and Notes

- Sensitivity to initial guess: far or bad `x0` can cause divergence.
- Derivative must not be zero at iterate points; otherwise the step is undefined.
- For functions with flat regions or discontinuities, consider bracketing methods or safeguards.
- EOQ model here is simplified to highlight the numerical method; real settings add constraints and more terms.

## References

- Numerical Methods textbooks on Newton–Raphson and convergence.
- SymPy: symbolic math in Python.
- SciPy Optimize: `scipy.optimize.newton`.
- EOQ model basics in operations management literature.

## What I Learned and Nexts Steps

As my first GitHub document, the project teach me how to implememt and explain math algorithms, and testing them. As mi profile is oriented to business solutions, I tougth that the EOQ cost was a great example of use. 

I think this was a great first project because teach me the steps of communicating solutions.

## What I Learned and Next Steps

This is my first documented GitHub project, and it helped me learn not only how to implement a numerical method, but how to **present it clearly and test it properly**. I chose EOQ because my long-term interest is connecting math with real decision-making in business settings.

**Key takeaways**
- Starting with a simple case made it easier to focus on testing and correctness.
- Automating the tests gave me confidence in the implementation.
- The method is much easier to understand when connected to a concrete scenario like EOQ.
- Writing documentation forces you to think about *why* the method is useful, not only *how* it works.

**Next steps**
- Go deeper into optimization and nonlinear solvers.
- Extend from 1-variable Newton to systems of nonlinear equations.
- Eventually build a small solver module as part of a growing toolkit for applied math.

This project is my first step toward building tools that create value through applied mathematics and technology.




