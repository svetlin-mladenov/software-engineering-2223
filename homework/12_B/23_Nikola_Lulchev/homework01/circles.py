import math

def check(x1, y1, r1, x2, y2, r2):

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if x1 == y1 and x2 == y2 and r1 == r2:
        return 1 # The two circles are the same
    elif d <= r1-r2:
        return 2 # Circle 2 is in Circle 1
    elif d <= r2-r1:
        return 3 # Circle 1 is in Circle 2
    elif d < r1+r2:
        return 4 # The two circles cross each other
    elif d == r1+r2:
        return 5 # The two circles are touching
    else:
        return 6 # They are not crossing or touching each other
