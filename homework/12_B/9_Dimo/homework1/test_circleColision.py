from CircleColision import Circle, ColisionTypes, circleColide


def test_no_colision():
    c1 = Circle(0,0,5)
    c2 = Circle(10,10,5)
    k = circleColide(c1,c2)
    assert str(k) == str(ColisionTypes.NoCollision(c1,c2))

    c1 = Circle(10,10,1)
    c2 = Circle(10,10,5)
    k = circleColide(c1,c2)
    assert str(k) == str(ColisionTypes.Inside(c1,c2))

def test_colision():
    c1 = Circle(0,0,5)
    c2 = Circle(2,2,5)
    k = circleColide(c1,c2)
    assert str(k) == str(ColisionTypes.ColideTwoPoints(c1,c2))

    c1 = Circle(5,4,3)
    c2 = Circle(5,10,3)
    k = circleColide(c1,c2)
    assert str(k) == str(ColisionTypes.ColideOnePoint(c1,c2))

