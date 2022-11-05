import math

class ColisionType:
    def __init__(self, c1,c2, value):
        self._circle1 = c1
        self._circle2 = c2
        self._value = value
    def getValue(self):
        return self._value

class ColisionTypes:
    class Inside(ColisionType):
        def __init__(self, c1, c2):
            super().__init__(c1, c2, -1)
        def __str__(self) -> str:
            return str(self._circle1)+" is in "+str(self._circle2)
    class NoCollision(ColisionType):
        def __init__(self, c1, c2):
            super().__init__(c1, c2, 0)
        def __str__(self) -> str:
            return str(self._circle1)+" does not collide with "+str(self._circle2)

    class ColideTwoPoints(ColisionType):
        def __init__(self, c1, c2):
            super().__init__(c1, c2, 1)
        def __str__(self) -> str:
            return str(self._circle1)+" collides with "+str(self._circle2) +" at two points"

    class ColideOnePoint(ColisionType):
        def __init__(self, c1, c2):
            super().__init__(c1, c2, 2)
        def __str__(self) -> str:
            return str(self._circle1)+" touches with "+str(self._circle2)



class Circle:
    def __init__(self,x,y,r) -> None:
        self.x = x
        self.y = y 
        self.r = r
    def __str__(self) -> str:
        return "Circle at x:"+str(self.x)+" and y:"+str(self.y)+" and radius:"+str(self.r)
    def circleColide(self,c2) ->ColisionType:
        d = math.sqrt((self.x-c2.x)**2 + (self.y-c2.y)**2)
        if d <= self.r-c2.r:
            return ColisionTypes.Inside(c2,self)
        elif d <= c2.r-self.r:
            return ColisionTypes.Inside(self,c2)
        elif d < self.r+c2.r:
            return ColisionTypes.ColideTwoPoints(self,c2)
        elif d == self.r+c2.r:
            return ColisionTypes.ColideOnePoint(self,c2)
        else:
            return ColisionTypes.NoCollision(self,c2)

def circleColide(c1:Circle,c2:Circle):
    return c1.circleColide(c2)
