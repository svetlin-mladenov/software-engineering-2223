from enum import Enum
from math import sqrt
from typing import Final, Literal, Optional, Union

# def fun(arg1: Type1, arg2: Type2) -> ReturnType:
#     body

def quadratic_solve(a: float, b: float, c: float) \
        -> Union[tuple[float, float], tuple[float], tuple]:
    d: Final = b*b - 4*a*c
    if d < 0:
        return ()
    x1 = (-b + sqrt(d)) / (2 * a)
    if d == 0:
        return (x1,)
    x2 = (-b - sqrt(d)) / (2 * a)
    return x1, x2

def test_quadratic_solve():
    assert quadratic_solve(1, 5, -6) == (1, -6)

def test_quadratic_solve_1_solution():
    assert quadratic_solve(1, 4, 4) == (-2,)

def test_quadratic_solve_no_solution():
    assert quadratic_solve(1, 4, 5) is ()

# def test_quadratic_solve_generic_call():
#     a = ...
#     b = ...
#     c == ...
#     res = quadratic_solve(a, b, c)
#     if isinstance(res, tuple):
#         # 2
#     if res is not None
#         # 1
#     else:
#         # 0

def intcmp(a: int, b: int) -> Literal[-1, 0, 1]:
    if a > b:
        return 1
    if a < b:
        return -1
    return 0

# v2

class Result(Enum):
    LESS = -1
    MORE = 1
    EQUAL = 0

def intcmp(a: int, b: int) -> Result:
    if a > b:
        return Result.MORE
    if a < b:
        return Result.LESS
    return Result.EQUAL

def my_list() -> list[int]:
    return [1, 2, 3]

def my_dict() -> dict[str, int]:
    # return {}  # empty dict
    return {
        "stefan": 12,
        "pesho": 20,
        20: "gosho",
    }