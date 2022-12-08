from math import sqrt, pow, inf

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def point_distance(p1:Point, p2:Point):
    return sqrt(pow((p2.x - p1.x), 2) + pow((p2.y - p1.y), 2))

class Circle:
    def __init__(self, p:Point, r):
        self.p = p #centre
        self.r = r

def circle_intersection(c1:Circle, c2:Circle):
    d = point_distance(c1.p, c2.p)
    R = c1.r + c2.r
    r = abs(c1.r - c2.r)

    if not d:
        if c1.r == c2.r:
            return inf #congruent
        return 0 #common centre
    elif d < R:
        if d < r:
            return 0 #lying inside
        elif d == r:
            return 1 #touching internally
        return 2 #intersecting
    elif d == R:
        return 1 #touching externally
    return 0 #lying outside

def test():
    c1 = Circle(Point(0, 0), 1)
    c2 = Circle(Point(0, 0), 1)
    assert circle_intersection(c1, c2) == inf
    c1.r = 5
    assert not circle_intersection(c1, c2)
    c2.p = Point(1, 0)
    assert not circle_intersection(c1, c2)
    c2.p = Point(4, 0)
    assert circle_intersection(c1, c2) == 1
    c2.p = Point(5, 0)
    assert circle_intersection(c1, c2) == 2
    c2.p = Point(6, 0)
    assert circle_intersection(c1, c2) == 1
    c2.p = Point(9, 0)
    assert not circle_intersection(c1, c2)
