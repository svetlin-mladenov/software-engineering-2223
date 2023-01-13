from circle_funcs import *


def test_circle_funcs():
    assert isAInsideB(0, 0, 0, 0, 1, 2)
    assert not isAInsideB(0, 0, 0, 0, 2, 1)
    assert not isBInsideA(0, 0, 0, 0, 1, 2)
    assert isBInsideA(0, 0, 0, 0, 2, 1)
    assert areCirclesIntersect(0, 0, -3, 0, 3, 3)
    assert not areCirclesIntersect(3, 0, -3, 0, 1, 1)
    assert areCirclesNotTouching(3, 0, -3, 0, 1, 1)
