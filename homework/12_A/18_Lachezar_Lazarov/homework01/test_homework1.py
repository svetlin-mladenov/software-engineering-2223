from math import sqrt

def checkCircle(c1_center, c1_rad, c2_center, c2_rad):
    if (c1_center == c2_center and c1_rad == c2_rad):
	    return "Matching"

    c1_x, c1_y = c1_center
    c2_x, c2_y = c2_center

    dist = sqrt((c1_x - c2_x)**2+(c1_y - c2_y)**2)
    sum_rad = c1_rad + c2_rad 

    if (dist < sum_rad):
        return "Intersecting"
    if (dist >sum_rad):
        return "Not intersecting"
    
    if(c1_rad + dist == c2_rad or c2_rad + dist == c1_rad):
        return "Containing!"

    if(dist == sum_rad):
        return "Touching"
    
def test_checkCircle():
    assert checkCircle((-7,5), 5, (-7,5), 5) == "Matching"
    assert checkCircle((-7,5), 5, (13,15), 5) == "Not intersecting"
    assert checkCircle((5,5), 5, (15,5), 5) == "Touching"
    assert checkCircle((5,5), 5, (15,5), 7) == "Intersecting"
