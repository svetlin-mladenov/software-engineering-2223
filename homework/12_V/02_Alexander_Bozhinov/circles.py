import math

class Circle :
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
 
def circle(c1, c2):
    d = math.sqrt((c1.x - c2.x) * (c1.x - c2.x) + (c1.y - c2.y) * (c1.y - c2.y))
 
    if(d <= c1.r - c2.r):
        message = "Circle 2 is inside 1"
    elif(d <= c2.r - c1.r):
        message = "Circle 1 is inside 2"
    elif(d < c1.r + c2.r):
        message = "Circles intersect to each other"
    elif(d == c1.r + c2.r):
        message = "Circles touch to each other"
    else:
        message = "Circles don't touch to each other"

    return message