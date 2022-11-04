import math
import re


def find_relative_position(x1, y1, r1, x2, y2, r2):
    centers_distance = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    if centers_distance == r1 + r2:
        print("Circle A touches circle B in one mutual point on their borders")
        return 0
    elif centers_distance > r1 + r2:
        print("The circles don't touch")
        return 1
    elif centers_distance == r1 - r2:
        print("The circles touch each other internally")
        return 2
    elif centers_distance < r1 - r2:
        print("One of the circles is located inside the other")
        return 3
    elif r1 - r1 < centers_distance < r1 + r2:
        print("The circles intersect each other at two points")
        return 4
    else:
        return 5


#find_relative_position(1, 1, 2, 6, 1, 3)
find_relative_position(2, 2, 4, 1, 1, 1)