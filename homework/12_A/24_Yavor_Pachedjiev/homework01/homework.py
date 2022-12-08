from math import sqrt

def check_Circles(c1_center, c1_rad, c2_center, c2_rad):
    if(c1_center == c2_center and c1_rad == c2_rad):
        return "Matching"
    c1_x, c1_y = c1_center
    c2_x, c2_y = c2_center

    distance = sqrt((c2_y - c1_y)**2 + (c2_x - c1_x)**2)
    rad_sum = c1_rad + c2_rad
    if(rad_sum < distance):
        return "not intesecting"
    if(rad_sum == distance):
        return "touching"
    if(rad_sum > distance):
        return "intersecting"
