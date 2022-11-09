import math
from enum import Enum


class Result (Enum):
    nonIntersecting = 0,
    sameCircle = 1,
    oneWithinAnother = 2,
    intersecting = 3


def test_get_intersections():
    assert get_intersections(2, 2, 1, 6, 2, 3) == Result.intersecting
    assert get_intersections(2, 2, 1, 6, 2, 4) == Result.intersecting
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
        return Result.intersecting
