import math
import pytest


def intersections(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    if d <= r1 - r2:
        result = "Circle B is inside Circle A"
    elif d <= r2 - r1:
        result = "Circle A is inside Circle B"
    elif d < r1 + r2:
        result = "The circles intersect"
    elif d == r1 + r2:
        result = "The circles touch each other"
    else:
        result = "The circles do not touch each other"

    return result


def test_intersections():
    assert intersections(-10, 8, 14, -24, 30, 10) == ("The circles touch each other")
    assert intersections(5, 19, 5, 19, 10, 20) == ("Circle A is inside Circle B")
    assert intersections(5, 19, 5, 19, 30, 20) == ("Circle B is inside Circle A")
    assert intersections(10, 12, 10, 70, 85, 80) == ("The circles intersect")
    assert intersections(3, 4, 14, 18, 5, 8) == ("The circles do not touch each other")
    assert intersections(3, 4, 34, 18, 50, 8) == ("Circle B is inside Circle A")