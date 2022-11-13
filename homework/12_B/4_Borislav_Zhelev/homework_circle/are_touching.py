import math
def are_touching(c1,c2):
    d = math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)
    return d <= c1.r + c2.r