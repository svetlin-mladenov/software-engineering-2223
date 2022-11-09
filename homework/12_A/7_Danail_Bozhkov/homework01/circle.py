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

def test_check_circles():
    c1 = (1,1)
    c2 = (3, 1)
    c1_rad = 1
    c2_rad = 1    
    assert check_circles(c1, c1_rad, c2, c2_rad) == "Touching"
    c11 = (1,1)
    c22 = (-1, -1)
    c11_rad = 1
    c22_rad = 20   
    assert check_circles(c11, c11_rad, c22, c22_rad) == "Containing"
    c111 = (1,1)
    c222 = (-1, -1)
    c111_rad = 1
    c222_rad = 2  
    assert check_circles(c111, c111_rad, c222, c222_rad) == "Intercecting"
    c1111 = (1,1)
    c2222 = (-10, -10)
    c1111_rad = 1
    c2222_rad = 1    
    assert check_circles(c1111, c1111_rad, c2222, c2222_rad) == "No comman"
    c11111 = (1,1)
    c22222 = (1, 1)
    c11111_rad = 1
    c22222_rad = 1    
    assert check_circles(c11111, c11111_rad, c22222, c22222_rad) == "Matching"
