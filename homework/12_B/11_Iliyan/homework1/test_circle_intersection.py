from circle import Circle
from circle_intersection import circle_intersection
from enumCases import EnumCases

def test_circle_intersection():
    #1 Fail case (radius <= 0)
    assert circle_intersection(Circle((0, 0), 0), Circle((0, 0), -1)) == EnumCases.FAIL.value

    #2 Same circle case
    assert circle_intersection(Circle((-5, 6), 5), Circle((-5, 6), 5)) == EnumCases.SAME.value
    assert circle_intersection(Circle((0, 0), 10), Circle((0, 0), 10)) == EnumCases.SAME.value

    #3 Circle 1 inside Circle 2 (not same center) case
    assert circle_intersection(Circle((29, 30), 5), Circle((0, 0), 50)) == EnumCases.ONE_INSIDE_TWO.value

    #4 Circle 1 inside Circle 2 (same center) case
    assert circle_intersection(Circle((0, 0), 5), Circle((0, 0), 10)) == EnumCases.ONE_INSIDE_TWO_SAME_CENTER.value

    #5 Circle 1 inside Circle 2 (touching) case
    assert circle_intersection(Circle((-10, -12), 10), Circle((-10, 8), 30)) == EnumCases.ONE_INSIDE_TWO_TOUCHING.value
    assert circle_intersection(Circle((5, 0), 5), Circle((0, 0), 10)) == EnumCases.ONE_INSIDE_TWO_TOUCHING.value

    #6 Circle 2 inside Circle 1 (not same center) case
    assert circle_intersection(Circle((10, 0), 50), Circle((-10, 0), 5)) == EnumCases.TWO_INSIDE_ONE.value

    #7 Circle 2 inside Circle 1 (same center) case
    assert circle_intersection(Circle((10, 0), 10), Circle((10, 0), 5)) == EnumCases.TWO_INSIDE_ONE_SAME_CENTER.value
    assert circle_intersection(Circle((0, 0), 10), Circle((0, 0), 5)) == EnumCases.TWO_INSIDE_ONE_SAME_CENTER.value    

    #8 Circle 2 inside Circle 1 (touching) case
    assert circle_intersection(Circle((-10, 8), 30), Circle((-10, -12), 10)) == EnumCases.TWO_INSIDE_ONE_TOUCHING.value    
    assert circle_intersection(Circle((0, 0), 10), Circle((5, 0), 5)) == EnumCases.TWO_INSIDE_ONE_TOUCHING.value
    
    #9 Circles touching from the outside case
    assert circle_intersection(Circle((0, 0), 5), Circle((10, 0), 5)) == EnumCases.TOUCHING.value
    assert circle_intersection(Circle((-10, 8), 30), Circle((14, -24), 10)) == EnumCases.TOUCHING.value
    assert circle_intersection(Circle((11, 0), 5), Circle((1, 0), 5)) == EnumCases.TOUCHING.value
    assert circle_intersection(Circle((1, 0), 5), Circle((11, 0), 5)) == EnumCases.TOUCHING.value

    #10 Circles intersecting
    assert circle_intersection(Circle((-10, 8), 30), Circle((-10, -26), 10)) == EnumCases.INTERSECTING.value
    assert circle_intersection(Circle((0, 0), 5), Circle((6, 0), 5)) == EnumCases.INTERSECTING.value
    assert circle_intersection(Circle((0, 0), 5), Circle((3, 0), 5)) == EnumCases.INTERSECTING.value
    assert circle_intersection(Circle((-10, 8), 30), Circle((-10, -14), 10)) == EnumCases.INTERSECTING.value
    assert circle_intersection(Circle((6, 0), 5), Circle((0, 0), 10)) == EnumCases.INTERSECTING.value
    assert circle_intersection(Circle((0, 0), 10), Circle((6, 0), 5)) == EnumCases.INTERSECTING.value

    #11 Circles intersecting and one of them is lying on the other's circumference
    assert circle_intersection(Circle((-10, 8), 30), Circle((20, 8), 10)) == EnumCases.INTERSECTING_LYING_ON_CIRCUMFERENCE.value
    assert circle_intersection(Circle((1, 0), 5), Circle((6, 0), 5)) == EnumCases.INTERSECTING_LYING_ON_CIRCUMFERENCE.value
    assert circle_intersection(Circle((6, 0), 5), Circle((1, 0), 5)) == EnumCases.INTERSECTING_LYING_ON_CIRCUMFERENCE.value

    #13 Circles not interacting case
    assert circle_intersection(Circle((0, 1), 2), Circle((10, 10), 5)) == EnumCases.NOT_INTERACTING.value
    assert circle_intersection(Circle((0, 0), 5), Circle((11, 0), 5)) == EnumCases.NOT_INTERACTING.value
    assert circle_intersection(Circle((11, 0), 5), Circle((0, 0), 5)) == EnumCases.NOT_INTERACTING.value
