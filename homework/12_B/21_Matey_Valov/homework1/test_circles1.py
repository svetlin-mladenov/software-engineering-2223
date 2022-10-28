from enum import Enum
import math

class Output(Enum):
    NoIntersect = 1
    Touch       = 2
    Intersect   = 3
    OneInOther  = 4
    Same        = 5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r
        
def circle_intersection(a, b):
    if(a.center.x == b.center.x) and (a.center.y == b.center.y) and (a.r == b.r):
        return Output.Same.value
    
    d = math.sqrt((a.center.x - b.center.x) * (a.center.x - b.center.x) + (a.center.y - b.center.y) * (a.center.y - b.center.y))
    
    if(d <= a.r - b.r) or (d <= b.r - a.r):
        return Output.OneInOther.value
    if(d < a.r + b.r):
        return Output.Intersect.value
    if(d == a.r + b.r):
        return Output.Touch.value
    
    return Output.NoIntersect.value

circle1 = Circle(Point(0, 0), 5)
circle2 = Circle(Point(10, 0), 5)
circle3 = Circle(Point(9, 0), 5)
circle4 = Circle(Point(11, 0), 5)
circle5 = Circle(Point(0, 0), 4)

def test_same_circle():
    assert circle_intersection(circle1, circle1) == Output.Same.value
    
def test_one_circle_in_other():
    assert circle_intersection(circle1, circle5) == Output.OneInOther.value

def test_circles_intersecting():
    assert circle_intersection(circle1, circle3) == Output.Intersect.value
    assert circle_intersection(circle2, circle3) == Output.Intersect.value
    assert circle_intersection(circle2, circle4) == Output.Intersect.value
    
def test_circles_touching():
    assert circle_intersection(circle1, circle2) == Output.Touch.value

def test_no_intersection():
    assert circle_intersection(circle1, circle4) == Output.NoIntersect.value
    assert circle_intersection(circle5, circle2) == Output.NoIntersect.value
    

