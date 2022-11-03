from cicles import *

def test_point_eq():
    Point1 = Point(0,0)
    Point2 = Point(0,0)
    Point3 = Point(1,0)

    #1 point 1 and 2 are equal
    assert (Point1 == Point2)
    #2 point 2 and 3 are NOT equal
    assert not (Point2 == Point3)

def test_circle_eq():
    circle1 = Circle(Point(0,0),0)
    circle2 = Circle(Point(0,0),0)
    circle3 = Circle(Point(0,0),1)
    
    #1 circle 1 and 2 are equal
    assert (circle1 == circle2)
    #2 circle 2 and 3 are NOT equal
    assert not (circle2 == circle3)

def test_circle_compare():
    circle1 = Circle(Point(0,0), 5)
    circle2 = Circle(Point(0,0), 10)
    circle3 = Circle(Point(0,0), 10)
    circle4 = Circle(Point(1,0), 5)
    circle5 = Circle(Point(6,0), 5)
    circle6 = Circle(Point(11,0), 5)
    circle7 = Circle(Point(5,0), 5)

    #1,2 circcles 2 and 3 are equal
    assert (check_circles(circle2, circle3) is CircleValues.EQUAL)
    assert (check_circles(circle3, circle2) is CircleValues.EQUAL)

    #3,4 circle 2 contains circle 1
    assert (check_circles(circle2, circle1) is CircleValues.CONTAINING)
    assert (check_circles(circle1, circle2) is CircleValues.CONTAINING)

    #5,6 circle 1 is distant with circle 6
    assert (check_circles(circle6, circle1) is CircleValues.DISTANT)
    assert (check_circles(circle1, circle6) is CircleValues.DISTANT)

    #7,8 circle 4 touches circle 6
    assert (check_circles(circle4, circle6) is CircleValues.TOUCHING)
    assert (check_circles(circle6, circle4) is CircleValues.TOUCHING)

    #9,10 circle 4 intercepts with circle 5
    assert (check_circles(circle4, circle5) is CircleValues.INTERCEPTING)
    assert (check_circles(circle5, circle4) is CircleValues.INTERCEPTING)

    #11,12 circle 5 intercepts with circle 2 from within
    assert (check_circles(circle5, circle2) is CircleValues.INTERCEPTING)
    assert (check_circles(circle2, circle5) is CircleValues.INTERCEPTING)

    #12,13 circle 7 touches circle 2 from within
    assert (check_circles(circle7, circle2) is CircleValues.TOUCHING)
    assert (check_circles(circle2, circle7) is CircleValues.TOUCHING)