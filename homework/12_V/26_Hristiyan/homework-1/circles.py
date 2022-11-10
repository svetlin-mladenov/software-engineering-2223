import math


def circles(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # (5 - 1)** 2 + (4 - 1)**2 = 25
    # d = 5
    if d <= r1 - r2:
        return "C2 is in C1"
    elif d <= r2 - r1:
        return "C1 is in C2"
    elif d < r1 + r2:
        return "Circumference of C1 and C2 intersect"
    elif d == r1 + r2:
        return "Circumference of C1 and C2 will touch"
    else:
        return "C1 and C2 do not overlap"

def test_circles():
    assert circles(4, 4, 1, 0, 0, 1) == "C1 and C2 do not overlap"
    assert circles(1, 1, 1, 0, 0, 1) == "Circumference of C1 and C2 intersect"
    assert circles(5, 4, 2, 1, 1, 3) == "Circumference of C1 and C2 will touch"
    assert circles(0, 0, 1, 0, 0, 3) == "C1 is in C2"
    assert circles(0, 0, 3, 0, 0, 1) == "C2 is in C1"
    
    

