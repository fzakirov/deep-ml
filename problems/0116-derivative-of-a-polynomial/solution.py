def poly_term_derivative(c: float, x: float, n: float) -> float:
    c*(x**n)
    result = c*n*(x**(n-1))
    return result