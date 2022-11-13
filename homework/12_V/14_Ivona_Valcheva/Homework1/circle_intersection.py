import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def circle_intersection(c1:Circle, c2:Circle):
    d = math.sqrt((c1.x - c2.x) * (c1.x - c2.x) + (c1.y - c2.y) * (c1.y - c2.y))
 
    if(d <= c1.r - c2.r):
        return("Circle B is inside A")
    elif(d <= c2.r - c1.r):
        return("Circle A is inside B")
    elif(d < c1.r + c2.r):
        return("Circle intersect to each other")
    elif(d == c1.r + c2.r):
        return("Circle touch to each other")
    else:
        return("Circle not touch to each other")
 