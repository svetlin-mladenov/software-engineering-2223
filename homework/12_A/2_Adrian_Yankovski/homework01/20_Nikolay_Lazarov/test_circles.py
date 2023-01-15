from enum import Enum
from tabnanny import check
from circles import CircleStates
from circles import check_circles
from circles import Circle

def test_not_intersekting():
    assert check_circles(Circle(1,1,1),Circle(4,1,1)) == CircleStates.DONTINTERSECT
    assert check_circles(Circle(1,1,2),Circle(4,1,1)) == CircleStates.DONTINTERSECT
    assert check_circles(Circle(1,1,1),Circle(-1,-2,-1)) == CircleStates.DONTINTERSECT
    assert check_circles(Circle(-5,2,3),Circle(-4,-4,2)) == CircleStates.DONTINTERSECT
        

def test_touching():
    assert check_circles(Circle(2,1,1),Circle(4,1,1)) == CircleStates.TOUCHING
    assert check_circles(Circle(1,1,1),Circle(-1,-1,-1)) == CircleStates.TOUCHING
    assert check_circles(Circle(0,0,3),Circle(3,4,2)) == CircleStates.TOUCHING
    assert check_circles(Circle(0,0,3),Circle(-3,-4,2)) == CircleStates.TOUCHING
    
def test_intersecting():    
    assert check_circles(Circle(2,1,1),Circle(3,1,1)) == CircleStates.INTERSECTING
    assert check_circles(Circle(0,0,3),Circle(3,-4,2.5)) == CircleStates.INTERSECTING
    assert check_circles(Circle(0,0,3),Circle(-4,-4,2)) == CircleStates.INTERSECTING
    assert check_circles(Circle(-5,2,3),Circle(-4,-4,3)) == CircleStates.INTERSECTING


    
def test_matching():    
    assert check_circles(Circle(2,1,1),Circle(2,1,1)) == CircleStates.MATCH
    assert check_circles(Circle(2,1,1),Circle(2,1,2)) == CircleStates.MATCH
    
