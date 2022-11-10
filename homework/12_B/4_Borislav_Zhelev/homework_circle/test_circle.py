from are_touching import *
from are_the_same import *
from are_embedded import *
from are_unrelated import *
from circle import *
def test_circle():
    
    assert are_touching(circle(1,1,5),circle(1,7,1))# 1 touching point
    assert are_touching(circle(1,1,5),circle(1,9,6))# two touching points
    assert are_touching(circle(4,4,4),circle(2,4,2))# embedded but touching
    assert are_the_same(circle(1,1,5),circle(1,1,5))
    assert are_embedded(circle(1,1,5),circle(1,1,3))
    assert are_unrelated(circle(1,1,5),circle(100,100,1))
    assert not are_touching(circle(1,1,5),circle(100,100,1))