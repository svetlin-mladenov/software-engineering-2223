import circles


def test_no_common():
    # Example of two circles that have nothing in common
    assert circles.checkCircles([-5, 0], 1, [2, 0], 4) == circles.CircleState.NO_COMMON

def test_matching():
    # Example of two matching circles
    assert circles.checkCircles([1, 2], 3, [1, 2], 3) == circles.CircleState.MATCHING

def test_intersecting():
    # Example of two intersecting circles
    assert circles.checkCircles([0, 1], 2, [2, 1], 3) == circles.CircleState.INTERSECTING

def test_touching():
    # Example of two touching circles
    assert circles.checkCircles([-2, 0], 2, [1, 0], 1) == circles.CircleState.TOUCHING

def test_containing():
    # Example of a containing circle
    assert circles.checkCircles([0, 2], 4, [2, 0], 1) == circles.CircleState.CONTAINING

def test_contained():
    # Example of a contained circle
    assert circles.checkCircles([0, 2], 1, [0, 0], 5) == circles.CircleState.CONTAINED
