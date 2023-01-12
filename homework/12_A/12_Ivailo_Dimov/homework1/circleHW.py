from math import sqrt

def check_circles(centre1, radius1, centre2, radius2):
    if(centre1 == centre2 and radius1 == radius2):
        return "Matching"

    x1, y1 = centre1
    x2, y2 = centre2
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    radius_sum = radius1 + radius2

    if(distance == radius_sum):
        return "Touching"

    if(distance < radius1 or distance < radius2):
        return "Containing"

    if(distance < radius_sum):
        return "Intercecting"

    if(distance > radius1 + radius2):
        return "No comman"

def test_check_circles_matching():
    assert check_circles((0,0), 5, (0,0), 5) == "Matching"

def test_check_circles_touching():
    assert check_circles((0,0), 5, (10,0), 5) == "Touching"

def test_check_circles_containing():
    assert check_circles((0,0), 10, (0,0), 5) == "Containing"

def test_check_circles_intersecting():
    assert check_circles((0,0), 5, (3,0), 5) == "Intersecting"

def test_check_circles_non_overlapping():
    assert check_circles((0,0), 5, (10,0), 5) == "No common"

def test_check_circles_negative_radius():
    assert check_circles((0,0), -5, (10,0), 5) == "Invalid input"

def test_check_circles_non_numeric():
    assert check_circles((0,0), 'a', (10,0), 5) == "Invalid input"
