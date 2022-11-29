from circles import*


def test_circles():
    assert circle_intersection(Circle(0,0,5),Circle(0,0,5)) == Intersection.MATCHING
    assert circle_intersection(Circle(0,0,1),Circle(0,2,1)) == Intersection.TOUCHING # center outside
    assert circle_intersection(Circle(0,0,3),Circle(0,2,1)) == Intersection.TOUCHING # center inside
    assert circle_intersection(Circle(0,0,5),Circle(1,0,6)) == Intersection.TOUCHING # center inside
    assert circle_intersection(Circle(0,0,5),Circle(1,1,6)) == Intersection.INTERSECTING # center inside 
    assert circle_intersection(Circle(0,0,5),Circle(6,6,4)) == Intersection.INTERSECTING # center outside
    assert circle_intersection(Circle(0,0,2),Circle(2,2,1)) == Intersection.INTERSECTING # center outside
    assert circle_intersection(Circle(0,0,1),Circle(2,2,1)) == Intersection.NO_COMMON # center outside
    assert circle_intersection(Circle(0,0,6),Circle(0,0,4)) == Intersection.NO_COMMON # matching centers
    assert circle_intersection(Circle(0,0,2),Circle(4,4,1)) == Intersection.NO_COMMON # center outside
    assert circle_intersection(Circle(0,0,5),Circle(1,1,3)) == Intersection.NO_COMMON # center inside