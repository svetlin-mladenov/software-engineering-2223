from circles_intersection import circles_intersection, Circle, IntersectionType


def test_circles_intersection():
    assert circle_intersection(Circle(1, 1, 1), Circle(3, 3, 1)) == IntersectionType.NOT_INTERSECTING
    assert circle_intersection(Circle(1, 1, 1), Circle(2, 2, 2)) == IntersectionType.INTERSECTING
    assert circle_intersection(Circle(3, 4, 1), Circle(3, 4, 1)) == IntersectionType.MATCHING
    assert circle_intersection(Circle(5, 5, 4), Circle(7, 5, 1)) == IntersectionType.NOT_INTERSECTING
    assert circle_intersection(Circle(7, 6, 3), Circle(12, 6, 4)) == IntersectionType.INTERSECTING
    assert circle_intersection(Circle(-1, -3, 2), Circle(-1, 2, 3)) == IntersectionType.TOUCHING
    assert circle_intersection(Circle(-3, 0, 6), Circle(7, 0, 4)) == IntersectionType.TOUCHING
    assert circle_intersection(Circle(3, 5, 4), Circle(3, 5, 4)) == IntersectionType.MATCHING
    assert circle_intersection(Circle(5, 5, 4), Circle(5, 3, 2)) == IntersectionType.TOUCHING
    assert circle_intersection(Circle(3, 4, 4), Circle(6, 4, 7)) == IntersectionType.TOUCHING
