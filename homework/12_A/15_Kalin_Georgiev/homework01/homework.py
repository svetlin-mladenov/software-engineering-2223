import math

def check_circles(c1_center, c1_radius, c2_center, c2_radius):

    (x1, y1) = c1_center
    (x2, y2) = c2_center
    distance_from_centers = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    sum_of_radiuses = c1_radius + c2_radius
    


#checks if the circles match each other
    if distance_from_centers == 0 and c1_radius == c2_radius:
        return "MATCHING"


#checks if the circles are touching each other
    if distance_from_centers == sum_of_radiuses:
        return "TOUCHING"


#checks if one circle contain the other other
    elif  distance_from_centers + c2_radius <= c1_radius or distance_from_centers + c1_radius <= c2_radius:
        return "CONTAINING"


#checks if circles are touching in two points 
    elif distance_from_centers < sum_of_radiuses:
        return "INTERSECTING"


#then circles have no common points
    else:
        return "NO_COMMON"



#print(check_circles((8, 9), 2, (4, 6), 3))