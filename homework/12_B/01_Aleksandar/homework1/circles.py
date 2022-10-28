from math import *

class Circle:
    def __init__(self, x, y, r):
        self.xx = x
        self.yy = y
        self.rr = r
    def __str__(self):
        return "O = (" + str(self.xx) + ";" + str(self.yy) + ")  radius: " + str(self.rr)
    

def func(a, b):
    if a.rr <= 0 or b.rr <= 0:
        return -1
    if a.rr == b.rr and a.xx == b.xx and a.yy == b.yy:
        return 3 #same circle
    distance_between_centers =sqrt((a.xx - b.xx)**2 + (a.yy - b.yy)**2)
    if distance_between_centers == abs(a.rr + b.rr) or distance_between_centers == abs(a.rr - b.rr):
        return 1 #one point of intersection
    if distance_between_centers < abs(a.rr + b.rr) and distance_between_centers > abs(a.rr - b.rr):
        return 2 #two points of intersection
    if a.rr > b.rr:
        if distance_between_centers + b.rr < a.rr:
            return 4 #one inside the other
    else:#b.rr > a.rr
        if distance_between_centers + a.rr < b.rr:
            return 4 #one inside the other
    return 0 #no intersection, not inside one another
    

c = Circle(0, 0, 2)
d = Circle(0, 0, 2)
e = Circle(0, 0, 10)
f = Circle(1, 0, 1)
g = Circle(1, 1, 1)
h = Circle(1, 1, 0)
j = Circle(5, 5, 1)


assert func(c,d) == 3 # same circles
assert func(g,d) == 2 # two points of intersection
assert func(f,d) == 1 # one point of intersection
assert func(h,e) == -1 # false data
assert func(c,e) == 4 # one inside the other
assert func(g,e) == 4 # one inside the other with different centers
assert func(j,c) == 0 # no intersection


print(c)
