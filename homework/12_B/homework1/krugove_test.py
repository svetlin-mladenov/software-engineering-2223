from krugove import Circle,circlesColide
def test_in():

    c1=Circle(0,0,5)
    c2 = Circle(5,5,3)
    assert circlesColide(c1,c2)

    c1=Circle(0,0,4)
    c2 = Circle(5,5,4)
    assert circlesColide(c1,c2)

def test_out():

    c1=Circle(0,0,4)
    c2 = Circle(6,6,4)
    assert not circlesColide(c1,c2)
    c1=Circle(0,0,4.485)
    c2 = Circle(6,6,4)
    assert not circlesColide(c1,c2)
#BUG ne raboti detekciqta ok
