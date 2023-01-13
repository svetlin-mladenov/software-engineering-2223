import math

def areColliding(x1, y1, x2, y2, r1, r2):

    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
 
    if( d == r1+r2 or 
        d < r1+r2 or
        d <= r2-r1 or
        d <= r1-r2):
        return True

    return False

def test_are_circles_coliding():
    assert areColliding(-10,8,14, -24, 30, 10)
    assert areColliding(4, 3, 12, 3, 4, 4)
    assert areColliding(4, 3, 12, 3, 5, 5)
    assert areColliding(4, 3, 12, 3, 3, 6)
    assert areColliding(4, 3, 12, 3, 6, 3)
    assert not areColliding(-10,8,14, -24, 10, 10)
    assert not areColliding(4, 3, 13, 3, 4, 4)

 