from math import sqrt
from typing import Final, Literal, Optional

def quadratic_solve(a: float, b: float, c: float) \
        -> Optional[tuple[float, float]]:
    d: Final = b**2 - 4*a*c
    if d < 0:
        return None
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    return x1, x2

def test_quadratic_solve():
    assert quadratic_solve(1, 5, -6) == (1, -6)

def test_quadratic_solve_1_solution():
    assert quadratic_solve(1, 4, 4) == (-2, -2)

def test_quadratic_solve_no_solutions() -> None:
    assert quadratic_solve(1, 4, 5) is None
    assert quadratic_solve(1, 2, "3") is None

def my_tuple() -> list[int]:
    return [1, 2, 3.14]

def my_dict() -> dict[str, int]:
    return {
        "gosho": 20,
        18: "pesho"
    }

def my_dict2() -> dict[str, list[int]]:
    return {
        "gosho": [4, 5],
        "pesho": [6, 7],
    }


def intcmp(a: int, b: int) -> Literal[-1, 0, 1]:
    if a < b:
        return -1
    if a > b:
        return 1
    return 0