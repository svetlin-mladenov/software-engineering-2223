from math import *
from enum import Enum

class Result(Enum):
    SAME_CIRCLES = 3
    ONE_POINT = 1
    TWO_POINTS = 2
    NO_INTERSECTION = 0
    ONE_INSIDE_THE_OTHER = 4
    ERROR = -1

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def __str__(self):
        return "O = (" + str(self.x) + ";" + str(self.y) + ")  radius: " + str(self.r)
    

def circle_relations(a, b):
    if a.r <= 0 or b.r <= 0:
        return Result.ERROR
    if a.r == b.r and a.x == b.x and a.y == b.y:
        return Result.SAME_CIRCLES #same circle
    distance_between_centers =sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    if distance_between_centers == abs(a.r + b.r) or distance_between_centers == abs(a.r - b.r):
        return Result.ONE_POINT#one point of intersection
    if distance_between_centers < abs(a.r + b.r) and distance_between_centers > abs(a.r - b.r):
        return Result.TWO_POINTS #two points of intersection
    if a.r > b.r:
        if distance_between_centers + b.r < a.r:
            return Result.ONE_INSIDE_THE_OTHER #one inside the other
    else:
        if distance_between_centers + a.r < b.r:
            return Result.ONE_INSIDE_THE_OTHER #one inside the other
    return Result.NO_INTERSECTION #no intersection, not inside one another
    

def test_circle_intersection ():
    assert circle_relations(Circle(0, 0, 2),Circle(0, 0, 2)) == Result.SAME_CIRCLES # same circles
    assert circle_relations(Circle(0, 0, 2),Circle(0, 0, 10)) == Result.ONE_INSIDE_THE_OTHER # one inside the other
    assert circle_relations(Circle(1, 0, 1),Circle(0, 0, 2)) == Result.ONE_POINT # one point of intersection
    assert circle_relations(Circle(1, 1, 1),Circle(0, 0, 2)) == Result.TWO_POINTS # two points of intersection
    assert circle_relations(Circle(1, 1, 1),Circle(0, 0, 10)) == Result.ONE_INSIDE_THE_OTHER # one inside the other with different centers
    assert circle_relations(Circle(1, 1, 0),Circle(0, 0, 10)) == Result.ERROR # false data
    assert circle_relations(Circle(5, 5, 1),Circle(0, 0, 2)) == Result.NO_INTERSECTION # no intersection
    
    
    
test_circle_intersection()
