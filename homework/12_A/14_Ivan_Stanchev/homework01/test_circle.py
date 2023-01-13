# not intersecting
# touching
# intersecting
# matching

from circle import *

def test_circle_was_created():
    c1 = Circle(0,0,1)
    try:
        c1
    except NameError:
        assert False
    else:
        assert True

def test_circle_parameters_after_creation():
    c1 = Circle(0,0,1)
    check = c1.x == 0 and c1.y == 0 and c1.r == 1
    assert check

def test_circles_comparison():
    c1 = Circle(0,0,0)
    c2 = Circle(0,0,0)
    assert c1 == c2

def test_find_distance_between_centers():
    c1 = Circle(0,0,1)
    c2 = Circle(0,3,2)
    assert (c1.find_distance_between_centers(c2)) == 3

def test_intersection():
    # Not intersecting
    c1 = Circle(0,0,1)
    c2 = Circle(2,2,1)
    assert c1.intersection(c2) == IntersectionState.NotIntersecting

    # Matching
    c1 = Circle(6,6,6)
    c2 = Circle(6,6,6)
    assert c1.intersection(c2) == IntersectionState.Matching

    # Touching
    c1 = Circle(0,0,8)
    c2 = Circle(0,12,4)
    assert c1.intersection(c2) == IntersectionState.Touching

    # Intersecting
    c1 = Circle(0,0,8)
    c2 = Circle(0,12,8)
    assert c1.intersection(c2) == IntersectionState.Intersecting
