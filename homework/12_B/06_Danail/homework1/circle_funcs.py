import math


def isBInsideA(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    return d <= r1 - r2


def isAInsideB(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    return d <= r2 - r1


def areCirclesIntersect(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    return d < r1 + r2


def areCirclesNotTouching(x1, y1, x2, y2, r1, r2):
    return not (isBInsideA(x1, y1, x2, y2, r1, r2) and isAInsideB(x1, y1, x2, y2, r1, r2) and areCirclesIntersect(x1, y1, x2, y2, r1, r2))
