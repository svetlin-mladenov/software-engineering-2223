import circles 

def test_circle():
    first_circle = circles.Circle("first circle", -2.45, 1.9, 3.38)
    second_circle = circles.Circle("second circle", -2.53, 2.64, 15.52)
    assert circles.mutual_position(first_circle, second_circle) == "One lying inside other"

def test_circle2():
    first_circle = circles.Circle("first circle", 1, 1, 1)
    second_circle = circles.Circle("second circle", 6, 7, 1)
    assert circles.mutual_position(first_circle, second_circle) == "They don't touch" 
    
def test_circle3():
    first_circle = circles.Circle("first circle", -3.61, 5.06, 3.75)
    second_circle = circles.Circle("second circle", -1.22, 4.13, 3.88)
    assert circles.mutual_position(first_circle, second_circle) == "They intersect at two points"    

def test_circle4():
    first_circle = circles.Circle("first circle", -5, 3, 1)
    second_circle = circles.Circle("second circle", -3, 3, 1)
    assert circles.mutual_position(first_circle, second_circle) == "They touch externally" 

def test_circle5():
    first_circle = circles.Circle("first circle", 6, 2.5, 1)
    second_circle = circles.Circle("second circle", 6, 2, 0.5)
    assert circles.mutual_position(first_circle, second_circle) == "They touch internally"   
    
def test_circle6():
    first_circle = circles.Circle("first circle", 6, 5, 1)
    second_circle = circles.Circle("second circle", 6, 5, 1)
    assert circles.mutual_position(first_circle, second_circle) == "They are equal"         