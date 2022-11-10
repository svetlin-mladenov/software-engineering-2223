from circle import *

circle1: Circle = Circle(Coordinate(0, 0), 1)
circle2: Circle = Circle(Coordinate(3, 3), 1)
circle3: Circle = Circle(Coordinate(0, 0), 2)
circle4: Circle = Circle(Coordinate(4, 0), 2)
circle5: Circle = Circle(Coordinate(3, 0), 2)
circle6: Circle = Circle(Coordinate(0.5, 0.5), 0.1)
circle7: Circle = Circle(Coordinate(0, 0), 100)

coordinate1: Coordinate = Coordinate(0, 0)
coordinate2: Coordinate = Coordinate(0, 1)


def test_get_distance_to():
    assert 1 == coordinate1.get_distance_to(coordinate2)
    assert 0 == coordinate1.get_distance_to(coordinate1)


def test_circle():
    assert "nil" == circle1.compare_to(circle2)
    assert "inscribed" == circle1.compare_to(circle3)
    assert "nil" == circle2.compare_to(circle1)
    assert "intersected" == circle3.compare_to(circle5)
    assert "contact" == circle3.compare_to(circle4)
    assert "circumscribed" == circle7.compare_to(circle6)
    assert "equal" == circle1.compare_to(circle1)
