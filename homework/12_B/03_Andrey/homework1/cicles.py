from enum import Enum
import math

class CircleValues(Enum):
    DISTANT = "The two cicrcles dont interact"
    TOUCHING = "The two circles touch eachother in one point"
    INTERCEPTING = "The two circles intercept in more than one point" 
    EQUAL = "There is no difference in the two circles"
    CONTAINING = "One of the circles complitely surounds the other"


class Point:

    def __init__(this, x, y):
        this.x = x
        this.y = y

    def __eq__(this, point):

        return this.x == point.x and this.y == point.y
    

class Circle:
    
    def __init__(this, center, radius):
        this.center = center
        this.radius = radius
    
    def __eq__(this, circle):
        return this.radius == circle.radius and this.center == circle.center
        

def check_circles(circle1, circle2):

    if(circle1 == circle2):
        return CircleValues.EQUAL

    center_distance = math.sqrt((circle2.center.x - circle1.center.x)**2 + (circle2.center.y - circle1.center.y)**2)

    if(center_distance > circle1.radius + circle2.radius):
        return CircleValues.DISTANT

    if(center_distance == circle1.radius + circle2.radius 
        or center_distance == max(circle1.radius, circle2.radius) - min(circle1.radius, circle2.radius)):
        return CircleValues.TOUCHING

    if(center_distance < circle1.radius + circle2.radius and 
        max(circle1.radius, circle2.radius) < min(circle1.radius, circle2.radius) + center_distance):
        return CircleValues.INTERCEPTING

    return CircleValues.CONTAINING
