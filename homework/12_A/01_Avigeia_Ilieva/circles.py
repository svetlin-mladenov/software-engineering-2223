import math 
from enum import Enum, auto


class Intersection(Enum):
    NO_COMMON = auto()
    TOUCHING = auto()
    INTERSECTING = auto()   
    MATCHING = auto()

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def circle_intersection(c1:Circle, c2:Circle):
    if c1.r <= 0 or c2.r <= 0:
        return Exception ("Radius must be possitive number") 

    distance = math.sqrt((c1.x-c2.x)**2 + (c1.y-c2.y)**2)

    if distance == 0 and c1.r == c2.r:
        return Intersection.MATCHING
        
    if distance == c1.r + c2.r or distance == abs(c1.r - c2.r):
        return Intersection.TOUCHING
    
    if distance < c1.r + c2.r and distance > abs(c1.r - c2.r):
        return Intersection.INTERSECTING

    else:
        return Intersection.NO_COMMON