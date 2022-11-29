import math
from enum import Enum
class ColisionType:
    def __init__(self, c1,c2, value):
        self._circle1 = c1
        self._circle2 = c2
        self._value = value
    def getValue(self):
        return self._value

class ColisionTypes(Enum):
    INSIDE = "Circle is in"
    NOCOLISION = "No collision"
    COLIDETWOPOINTS = "Colision at two points"
    COLIDEONEPOINT =  "Colision at one point"
    SAME = "Circles are the same"



class Circle:
    def __init__(self,x,y,r) -> None:
        self.x = x
        self.y = y 
        self.r = r
    def __str__(self) -> str:
        return "Circle at x:"+str(self.x)+" and y:"+str(self.y)+" and radius:"+str(self.r)
    def circleColide(self,c2) ->ColisionType:

        d = math.sqrt((self.x-c2.x)**2 + (self.y-c2.y)**2)
        if(self.r == c2.r and d == 0):
            return ColisionTypes.SAME.value
        if d <= self.r-c2.r:
            return ColisionTypes.INSIDE.value
        elif d <= c2.r-self.r:
            return ColisionTypes.INSIDE.value
        elif d < self.r+c2.r:
            return ColisionTypes.COLIDETWOPOINTS.value
        elif d == self.r+c2.r:
            return ColisionTypes.COLIDEONEPOINT.value
        else:
            return ColisionTypes.NOCOLISION.value

def circleColide(c1:Circle,c2:Circle):
    return c1.circleColide(c2)
