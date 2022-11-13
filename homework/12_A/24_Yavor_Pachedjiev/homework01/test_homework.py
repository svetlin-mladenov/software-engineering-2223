from homework import *


def test_matching():
    assert check_Circles((-7,5), 5, (-7,5), 5) == "Matching"

def test_not_intersecting():
    assert check_Circles((-7,5), 5, (13,15), 5) == "not intesecting"

def test_touching():
    assert check_Circles((5,5), 5, (15,5), 5) == "touching"

def test_intersecting():
    assert check_Circles((5,5), 5, (15,5), 7) == "intersecting"

test_matching()
test_not_intersecting()
test_touching()
test_intersecting()




