import math
from enum import Enum


class Result (Enum):
    nonIntersecting = 0,
    sameCircle = 1,
    oneWithinAnother = 2,
    onePointInt = 3,
    twoPointsInt = 4


def test_get_intersections():
    assert get_intersections(2, 2, 1, 6, 2, 3) == Result.onePointInt
    assert get_intersections(2, 2, 1, 6, 2, 4) == Result.twoPointsInt
    assert get_intersections(2, 2, 1, 6, 2, 1) == Result.nonIntersecting
    assert get_intersections(2, 2, 1, 2, 2, 1) == Result.sameCircle
    assert get_intersections(6, 2, 3, 6, 2, 2) == Result.oneWithinAnother
    assert get_intersections(6, 2, 2, 6, 2, 3) == Result.oneWithinAnother


def get_intersections(x0, y0, r0, x1, y1, r1):
    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
    if d > r0 + r1:
        return Result.nonIntersecting
    if d == 0 and r0 == r1:
        return Result.sameCircle
    if d < abs(r0 - r1):
        return Result.oneWithinAnother
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        if x3 == x4 and y3 == y4:
            return Result.onePointInt
        else:
            return Result.twoPointsInt

