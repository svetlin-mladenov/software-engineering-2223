import math


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def circle_intersection(arg1, arg2, r1, r2):
    d = math.sqrt((arg1.x - arg2.x) * (arg1.x - arg2.x) + (arg1.y - arg2.y) * (arg1.y - arg2.y))

    if d <= r1 - r2:
        print("Circle B is inside A")
        return False
    elif d <= r2 - r1:
        print("Circle A is inside B")
        return False
    elif d < r1 + r2:
        print("Circle intersect to each other")
        return True
    elif d == r1 + r2:
        print("Circle touch to each other")
        return True
    else:
        print("Circle not touch to each other")
        return False


c1 = Circle(-10, 8)
c2 = Circle(14, -24)
r1, r2 = 30, 10

circle_intersection(c1, c2, r1, r2)
