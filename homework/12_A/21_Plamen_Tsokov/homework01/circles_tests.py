import circles 

def test_circle():
    first_circle = circles.Circle("first circle", 2, 4, 2)
    second_circle = circles.Circle("second circle", 2, 4, 15)
    assert circles.mutual_position(first_circle, second_circle) == "CONTAINIG"

def test_circle2():
    first_circle = circles.Circle("first circle", 2, 4, 2)
    second_circle = circles.Circle("second circle", 20, 20, 1)
    assert circles.mutual_position(first_circle, second_circle) == "NOT TOUCHING OR CONTAINIG" 

def test_circle3():
    first_circle = circles.Circle("first circle", 3, 3, 4)
    second_circle = circles.Circle("second circle", 3, 5, 4)
    assert circles.mutual_position(first_circle, second_circle) == "INTERSECTING"    

def test_circle5():
    first_circle = circles.Circle("first circle", 3, 3, 2)
    second_circle = circles.Circle("second circle", 3, 5, 2)
    assert circles.mutual_position(first_circle, second_circle) == "TOUCHING"   

def test_circle6():
    first_circle = circles.Circle("first circle", 1, 3, 1)
    second_circle = circles.Circle("second circle", 1, 3, 1)
    assert circles.mutual_position(first_circle, second_circle) == "MATCHING" 