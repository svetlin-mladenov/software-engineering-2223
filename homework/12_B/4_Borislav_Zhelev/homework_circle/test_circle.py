from are_touching import *
from are_the_same import *
from are_embedded import *
from are_unrelated import *
from circle import *
def test_circle():
    c1 = circle(1,1,5)
    c2 = circle(1,9,6)
    c3 = circle(1,1,3)
    c4 = circle(100,100,1)
    c5 = circle(1,1,5)

    assert are_touching(c1,c2)
    assert are_the_same(c1,c5)
    assert are_embedded(c1,c3)
    assert are_unrelated(c1,c4)
    assert not are_touching(c1,c4)