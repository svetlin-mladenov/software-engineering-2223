from main import *
def testCircleIntersection():
    assert circle_intersection(Circle(-10, 8), Circle(14, -24), 30, 10)
    assert not circle_intersection(Circle(0, 8), Circle(14, -24), 3, 10)
    assert not circle_intersection(Circle(-10, 1000), Circle(14, -24), 30, 10)
    assert not circle_intersection(Circle(-10, 111), Circle(14, -24), 30, 10)
    assert not circle_intersection(Circle(-10, 822), Circle(14, -24), 30, 10)