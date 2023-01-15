import math
def are_embedded(c1,c2):
    d = math.sqrt((c1.x - c2.x) * (c1.x - c2.x) + (c1.y - c2.y) * (c1.y - c2.y))
    return d <= c1.r - c2.r or d <= c2.r - c1.r 
