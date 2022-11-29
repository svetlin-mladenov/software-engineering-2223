from CircleColision import Circle, ColisionTypes, circleColide


def test_no_colision():
    c1 = Circle(0,0,5)
    c2 = Circle(10,10,5)
    k = circleColide(c1,c2)
    assert k == ColisionTypes.NOCOLISION.value

    c1 = Circle(10,10,1)
    c2 = Circle(10,10,5)
    k = circleColide(c1,c2)
    assert k == ColisionTypes.INSIDE.value
    
    c1 = Circle(10,10,5)
    c2 = Circle(10,10,5)
    k = circleColide(c1,c2)
    assert k == ColisionTypes.SAME.value

def test_colision():
    c1 = Circle(0,0,5)
    c2 = Circle(2,2,5)
    k = circleColide(c1,c2)
    assert k == ColisionTypes.COLIDETWOPOINTS.value

    c1 = Circle(5,4,3)
    c2 = Circle(5,10,3)
    k = circleColide(c1,c2)
    assert str(k) == ColisionTypes.COLIDEONEPOINT.value

