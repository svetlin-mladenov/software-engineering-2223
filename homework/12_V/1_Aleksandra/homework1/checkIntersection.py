import math

def test_get_intersections():
    assert get_intersections(2, 2, 1, 6, 2, 3) == (3, 2)
    assert get_intersections(2, 2, 1, 6, 2, 4) == (2.125, 1.0078432583507784, 2.125, 2.9921567416492216)
    assert get_intersections(2, 2, 1, 6, 2, 1) == 0
    assert get_intersections(2, 2, 1, 2, 2, 1) == 1
    assert get_intersections(6, 2, 3, 6, 2, 2) == 2
    assert get_intersections(6, 2, 2, 6, 2, 3) == 2


def get_intersections(x0, y0, r0, x1, y1, r1):
    # distance between the two circles' centers
    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    # non intersecting
    if d > r0 + r1:
        print("The two circles aren't intersecting!")
        return 0
    # One circle within other
    if d < abs(r0 - r1):
        print("One of the circles is in the other one.")
        return 2
    # coincident circles
    if d == 0 and r0 == r1:
        print("The two circles coincident!")
        return 1
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        if x3 == x4 and y3 == y4:
            print("Point of intersection is " + str(x3) + " " + str(y3))
            return x3, y3
        else:
            print("Points of intersection are [" + str(x3) + " " + str(y3) + "] and [" + str(x4) + " " + str(y4) + "]")
            return x3, y3, x4, y4

