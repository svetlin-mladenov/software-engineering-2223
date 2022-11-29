import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def intersects(self, other):
        if(math.ceil(self.distance_to(other)) < self.r + other.r):
            return True
        return False
    def touches(self, other):
        if(math.ceil(self.distance_to(other)) == self.r + other.r):
            return True
        return False
    def remote(self, other):
        if(math.ceil(self.distance_to(other)) >  self.r + other.r):
            return True
        return False
    
def test_intersect():
    assert Circle(0, 0, 5).intersects(Circle(0, 6, 4))
    assert Circle(0, 0, 4).intersects(Circle(0, 10, 7))

def test_touch():
    assert Circle(0, 0, 3).touches(Circle(0, 5, 2))

def test_remote():
    assert Circle(-5, -5, 5).remote(Circle(5, 5, 5))