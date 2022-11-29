from math import sqrt
from typing import Optional


def solve_quadratic(a: float, b: float, c:float) \
        -> Optional[tuple[float, float]]:
    det = b*b - 4*a*c
    if det < 0:
        return None
    x1 = (-b + sqrt(det)) / (2 * a)
    x2 = (-b - sqrt(det)) / (2 * a)
    return (x1, x2)


def test_solve_quadratic_2_solutions():
    assert solve_quadratic(1, 5, -6) == (1, -6)


def test_solve_quadratic_1_solution():
    assert solve_quadratic(1, 4, 4) == (-2, -2)

def test_solve_quadratic_no_solution():
    assert solve_quadratic(1, 4, 5) is None