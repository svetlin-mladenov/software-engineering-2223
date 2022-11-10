from cicles import *

def test_point_eq():

    #1 point 1 and 2 are equal
    assert Point(0,0) == Point(0,0)
    #2 point 2 and 3 are NOT equal
    assert not Point(0,0) == Point(1,0)


def test_circle_eq():
    
    #1 circle 1 and 2 are equal
    assert Circle(Point(0,0),0) == Circle(Point(0,0),0)
    #2 circle 2 and 3 are NOT equal
    assert not Circle(Point(0,0),0) == Circle(Point(0,0),1)


def test_circle_compare():

    #1,2 circcles 2 and 3 are equal
    assert check_circles(Circle(Point(0,0), 10), Circle(Point(0,0), 10)) is CircleValues.EQUAL
    assert check_circles(Circle(Point(0,0), 10), Circle(Point(0,0), 10)) is CircleValues.EQUAL

    #3,4 circle 2 contains circle 1
    assert check_circles(Circle(Point(0,0), 10), Circle(Point(0,0), 5)) is CircleValues.CONTAINING
    assert check_circles(Circle(Point(0,0), 5), Circle(Point(0,0), 10)) is CircleValues.CONTAINING

    #5,6 cicle 1 is distant with circle 6
    assert check_circles(Circle(Point(11,0), 5), Circle(Point(0,0), 5)) is CircleValues.DISTANT
    assert check_circles(Circle(Point(0,0), 5), Circle(Point(11,0), 5)) is CircleValues.DISTANT

    #7,8 cicle 4 touches circle 6
    assert check_circles(Circle(Point(1,0), 5), Circle(Point(11,0), 5)) is CircleValues.TOUCHING
    assert check_circles(Circle(Point(11,0), 5), Circle(Point(1,0), 5)) is CircleValues.TOUCHING

    #9,10 crcle 4 intercepts with circle 5
    assert check_circles(Circle(Point(1,0), 5), Circle(Point(6,0), 5)) is CircleValues.INTERCEPTING
    assert check_circles(Circle(Point(6,0), 5), Circle(Point(1,0), 5)) is CircleValues.INTERCEPTING

    #11,12 ircle 5 intercepts with circle 2 from within
    assert check_circles(Circle(Point(6,0), 5), Circle(Point(0,0), 10)) is CircleValues.INTERCEPTING
    assert check_circles(Circle(Point(0,0), 10), Circle(Point(6,0), 5)) is CircleValues.INTERCEPTING

    #12,13 circle 7 touches circle 2 from within
    assert check_circles(Circle(Point(5,0), 5), Circle(Point(0,0), 10)) is CircleValues.TOUCHING
    assert check_circles(Circle(Point(0,0), 10), Circle(Point(5,0), 5)) is CircleValues.TOUCHING
    assert check_circles(Circle(Point(0,0), 10), Circle(Point(9,0), 1)) is CircleValues.TOUCHING
