import pytest

from circle_intersection import *

def test_circle_intersection():
    assert circle_intersection(Circle(5, 4, 3), Circle(5, 4, 2)) == "Circle B is inside A"
    assert circle_intersection(Circle(5, 4, 2), Circle(5, 4, 3)) == "Circle A is inside B"
    assert circle_intersection(Circle(6, 4, 3), Circle(10, 4, 2)) == "Circle intersect to each other"
    assert circle_intersection(Circle(5, 4, 3), Circle(5, 10, 3)) == "Circle touch to each other"
    assert circle_intersection(Circle(5, 4, 3), Circle(3, 9, 2)) == "Circle not touch to each other"
    