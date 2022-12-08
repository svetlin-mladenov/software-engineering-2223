from circle import circle_intersection, Circle, Intersection

def test_circle_intersection_all_points():
    c1: Circle = Circle(x=0, y=0, r=10)
    c2: Circle = Circle(x=0, y=0, r=10)
    assert circle_intersection(c1, c2) == Intersection.ALL_POINTS;

    c3: Circle = Circle(x=0, y=0, r=9)
    assert not circle_intersection(c1, c3) == Intersection.ALL_POINTS;

def test_circle_intersection_one_point():
    c1: Circle = Circle(x=0, y=0, r=5)
    c2: Circle = Circle(x=15, y=0, r=10)

    assert circle_intersection(c1, c2) == Intersection.ONE_POINT

def test_circle_intersection_two_points():
    c1: Circle = Circle(x=0, y=0, r=5)
    c2: Circle = Circle(x=10, y=0, r=10)
    assert circle_intersection(c1, c2) == Intersection.TWO_POINTS

def test_circle_intersection_no_points():
    c1: Circle = Circle(x=0, y=0, r=5)
    c2: Circle = Circle(x=150, y=0, r=10)
    assert circle_intersection(c1, c2) == Intersection.NO_POINTS
