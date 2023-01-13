from circles import *

def test_circles() : 
    assert circle(Circle(-10, 8, 30), Circle(14, -24, 10)) == "Circles touch to each other"

    assert circle(Circle(10, 20, 3), Circle(-14, -24, 4)) == "Circles don't touch to each other"

    assert circle(Circle(-10, 8, 30), Circle(-10, 8, 2)) == "Circle 2 is inside 1"

    assert circle(Circle(-10, 8, 2), Circle(-10, 8, 30)) == "Circle 1 is inside 2"

    assert circle(Circle(-10, 8, 15), Circle(-10, -4, 10)) == "Circles intersect to each other"