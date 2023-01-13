# Nikola Milkov 12v №22

from enum import Enum
import math


class Circles(Enum):
    Circle_A_and_circle_B_are_the_same = 1
    Circle_B_is_inside_circle_A_and_they_do_not_intersect = 2
    Circle_B_is_inside_circle_A_and_they_touch_to_each_other_in_one_point = 3
    Circle_A_is_inside_circle_B_and_they_do_not_intersect = 4
    Circle_A_is_inside_circle_B_and_they_touch_to_each_other_in_one_point = 5
    Circles_intersect_in_two_points = 6
    Circles_touch_to_each_other_in_one_point = 7
    Circles_do_not_touch_to_each_other_and_they_do_not_intersect = 8


# circle1(x1, y1, r1)
# circle2(x2, y2, r2)
# d = distance between the centre of circle1 and the centre of circle2

# Function to check if two circles intersect/touch to each other and how
def circles(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    if r1 == r2 and x1 == x2 and y1 == y2:
        return 1
    elif d < r1 - r2:
        return 2
    elif d == r1 - r2:
        return 3
    elif d < r2 - r1:
        return 4
    elif d == r2 - r1:
        return 5
    elif d < r1 + r2:
        return 6
    elif d == r1 + r2:
        return 7
    else:
        return 8


def test_circles():
    # tests same circles
    assert circles(0, 0, 5, 0, 0, 5) == 1
    assert circles(0, -2, 4, 0, -2, 4) == 1
    assert circles(-3, 14, -2, -3, 14, -2) == 1

    # tests for circle B inside circle A
    assert circles(0, 0, 10, 5, 0, 4) == 2
    assert circles(0, 0, 10, 5, 0, 5) == 3
    assert circles(-5, 0, 6, -1, 0, 1) == 2

    # tests for circle A inside circle B
    assert circles(0, 0, 5, 6, 0, 12) == 4
    assert circles(0, 0, 5, 6, 0, 11) == 5
    assert circles(0, 0, 2, -1, 0, 4) == 4

    # tests for circle A intersecting circle B in two points
    assert circles(0, 0, 5, 10, 0, 6) == 6
    assert circles(0, 0, 5, 0, 10, 6) == 6
    assert circles(-3, 0, 5, 0, -5, 10) == 6

    # tests for circle A touching to circle B in one points
    assert circles(0, 0, 5, 10, 0, 5) == 7
    assert circles(0, 0, 5, 0, 10, 5) == 7
    assert circles(-3, 0, 5, 3, 0, 1) == 7

    # tests for circle A not intersecting circle B
    assert circles(0, 0, 5, 10, 0, 4) == 8
    assert circles(0, 0, 5, 0, 10, 4) == 8
    assert circles(-3, 0, 4, 3, 0, 1) == 8
