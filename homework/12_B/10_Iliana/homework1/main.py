from enum import Enum
import math

class Circle:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

class Collison_type(Enum):
    EQUAL = "Equal"
    FINSIDE = "First in Second"
    SINSIDE = "Second in First"
    INTERSECT = "Intersect"
    TOUCHING = "Touching"
    NONE = "None"


def getcollision_type(c1, c2):
    d = math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)

    if (c1.__dict__ == c2.__dict__):
         return collison_type.EQUAL
    if (d <= c1.r - c2.r):
        return collison_type.SINSIDE
    if (d <= c2.r - c1.r):
        return collison_type.FINSIDE
    if (d < c1.r + c2.r):
        return collison_type.INTERSECT
    if (d == c1.r + c2.r):
        return collison_type.TOUCHING
    else:
        return collison_type.NONE

def test_equal_circles():
    c1 = Circle(20, 20, 20)
    c2 = Circle(20, 20, 20)

    assert getcollison_type(c1, c2) == collison_type.EQUAL

def test_FINSIDE():
    c1 = Circle(20, 0, 0)
    c2 = Circle(40, 0, 0)

    assert getcollison_type(c1, c2) == collison_type.FINSIDE

def test_SINSIDE():
    c1 = Circle(40, 0, 0)
    c2 = Circle(20, 0, 0)

    assert getcollison_type(c1, c2) == collison_type.SINSIDE

def test_intersect():
    c1 = Circle(20, 0, 0)
    c2 = Circle(20, 20, 0)

    assert getcollison_type(c1, c2) == collison_type.INTERSECT

def test_touching():
    c1 = Circle(20, -20, 0)
    c2 = Circle(20, 20, 0)

    assert getcollison_type(c1, c2) == collison_type.TOUCHING

def test_none():
    c1 = Circle(20, 0, 0)
    c2 = Circle(20, 40, 40)

    assert getcollison_type(c1, c2) == collison_type.NONE
