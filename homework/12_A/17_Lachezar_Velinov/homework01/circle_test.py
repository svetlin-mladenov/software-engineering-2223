"""Testing
"""
import pytest
import circle_comparison
from circle_intersection_types import CircleIntersectionTypes
from circle import Circle


@pytest.mark.parametrize("x1, y1, r1, x2, y2, r2, result",[
    (5, 4, 2, 3,  9,  2, CircleIntersectionTypes.NOT_TOUCHING),
    (5, 4, 3, 5,  10, 3, CircleIntersectionTypes.TOUCHING),
    (6, 4, 3, 10, 4,  2, CircleIntersectionTypes.INTERSECTING),
    (5, 4, 3, 5,  4,  2, CircleIntersectionTypes.SECOND_INSIDE_FIRST),
    (5, 4, 2, 5,  4,  3, CircleIntersectionTypes.FIRST_INSIDE_SECOND)
])
def test_circle(x1, y1, r1, x2, y2, r2, result):
    """tests circles
    """
    assert circle_comparison.are_circles_intersecting(
        Circle(x1, y1, r1), Circle(x2, y2, r2)) == result
