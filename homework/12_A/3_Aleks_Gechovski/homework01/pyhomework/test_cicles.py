from circles import *

def test_containing():
    a_c = (2,0) 
    b_c = (0,0)

    a_r = 3
    b_r = 1

    assert check_circles(a_c, a_r, b_c, b_r) == "Containing!"

def test_matching():
    a_c = (0,0) 
    b_c = (0,0)

    a_r = 3
    b_r = 3

    assert check_circles(a_c, a_r, b_c, b_r) == "Matching!"

def test_intercepting():
    a_c = (2,0) 
    b_c = (0,0)

    a_r = 3
    b_r = 3

    assert check_circles(a_c, a_r, b_c, b_r) == "Intercepting!"