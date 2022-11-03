from enum import Enum, auto
import math
from turtle import circle

class CircleStates(Enum):
    DONTINTERSECT = auto
    INTERSECTING = auto
    TOUCHING = auto
    MATCH = auto

class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

circle1 = Circle(1,1,1)
circle2 = Circle(4,1,1)

def check_circles(circle1: Circle, circle2: Circle):
    d = math.sqrt((circle1.x - circle2.x) * (circle1.x - circle2.x) + (circle1.y - circle2.y) * (circle1.y - circle2.y))
 
    if(d <= circle1.r - circle2.r):
        print("Circle B is inside A")
        return CircleStates.MATCH
    elif(d <= circle2.r - circle1.r):
        print("Circle A is inside B")
        return CircleStates.MATCH
    elif(d < circle1.r + circle2.r):
        print("Circle intersect to each other")
        return CircleStates.INTERSECTING
    elif(d == circle1.r + circle2.r):
        print("Circle touch to each other")
        return CircleStates.TOUCHING
    else:
        print("Circle not touch to each other")
        return CircleStates.DONTINTERSECT


check_circles(circle1,circle2)