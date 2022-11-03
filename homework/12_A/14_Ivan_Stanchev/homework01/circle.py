from enum import Enum
from math import sqrt,pow

class IntersectionState(Enum):
    NotIntersecting = 0
    Touching = 1
    Intersecting = 2
    Matching = 3

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def __eq__(self, c2):
        if(isinstance(c2, Circle)):
            return self.x == c2.x and self.y == c2.y and self.r == c2.r

    def find_distance_between_centers(self,c2):
        distance = sqrt(pow(c2.x - self.x, 2) + (pow(c2.y - self.y, 2)))
        return distance

    def intersection(self, c2):
        distance = self.find_distance_between_centers(c2)
        if (self.r + c2.r) < distance:
            return IntersectionState.NotIntersecting.name
        elif self == c2:
            return IntersectionState.Matching.name
        elif self.r + c2.r == distance:
            return IntersectionState.Touching.name
        elif (self.r + c2.r) > distance:
            return IntersectionState.Intersecting.name
