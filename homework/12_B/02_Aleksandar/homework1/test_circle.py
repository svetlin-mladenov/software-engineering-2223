from circle import *

C1 = Circle(3,4,5)
C2 = Circle(14,18,8) # NOT TOUCHING
C3 = Circle(8,4,5) # INTERSECT
C4 = Circle(2,2,2) # INSIDE
C5 = Circle(-7,4,5) # TOUCHING
C6 = Circle(3,4,5) #SAME
C7 = Circle(1,2,0) # INVALID CIRCLE
# https://www.desmos.com/calculator/6sntulfbz2

def test_intersect():
    assert C1.check(C3) == 'INTERSECT'

def test_inside():
    assert C1.check(C4) == 'INSIDE'

def test_touching():
    assert C1.check(C5) == 'TOUCHING'

def test_nottouching():
    assert C1.check(C2) == 'NOTTOUCHING'

def test_same():
    assert C1.check(C6) == 'SAME'

def test_invalid():
    assert C1.check(C7) == 'INVALID'