from math import sqrt
from sympy import srepr, symbols, Eq, solve

class Circle:
    x = 0
    y = 0
    rad = 0
    def __init__(self,x:int,y:int,rad:int):
        self.x = x
        self.y =y
        self.rad = rad

    def __str__(self):
        return "(Ball with x:"+self.x+" and y:"+self.y+" and rad:"+self.rad+")"

def circlesColide(c1:Circle,c2:Circle):
    return abs((c2.x-c1.x)**2 + (c2.y-c1.y)**2) <= abs((c1.rad+c2.rad)**2)



