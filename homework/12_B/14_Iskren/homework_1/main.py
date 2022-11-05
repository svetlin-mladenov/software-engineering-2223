from enum import Enum
import math

class Circle:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

class CollisonType(Enum):
    EQUAL = "Equal"
    FINS = "First in Second"
    SINF = "Second in First"
    INTERSECT = "Intersect"
    TOUCHING = "Touching"
    NONE = "None"

def getPythagoreanValue(c1:Circle, c2:Circle):
    return math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)

def getCollisionType(c1:Circle, c2:Circle):
    d = getPythagoreanValue(c1, c2)

    if (c1.__dict__ == c2.__dict__):
         return CollisonType.EQUAL
    if (d <= c1.r - c2.r):
        return CollisonType.SINF
    if (d <= c2.r - c1.r):
        return CollisonType.FINS
    if (d < c1.r + c2.r):
        return CollisonType.INTERSECT
    if (d == c1.r + c2.r):
        return CollisonType.TOUCHING
    else:
        return CollisonType.NONE

def test_equal_circles():
    c1 = Circle(10, 10, 10)
    c2 = Circle(10, 10, 10)

    assert getCollisionType(c1, c2) == CollisonType.EQUAL

def test_fins():
    c1 = Circle(10, 0, 0)
    c2 = Circle(20, 0, 0)

    assert getCollisionType(c1, c2) == CollisonType.FINS

def test_sinf():
    c1 = Circle(20, 0, 0)
    c2 = Circle(10, 0, 0)

    assert getCollisionType(c1, c2) == CollisonType.SINF

def test_intersect():
    c1 = Circle(10, 0, 0)
    c2 = Circle(10, 10, 0)

    assert getCollisionType(c1, c2) == CollisonType.INTERSECT

def test_touching():
    c1 = Circle(10, -10, 0)
    c2 = Circle(10, 10, 0)

    assert getCollisionType(c1, c2) == CollisonType.TOUCHING

def test_none():
    c1 = Circle(10, 0, 0)
    c2 = Circle(10, 20, 20)

    assert getCollisionType(c1, c2) == CollisonType.NONE
