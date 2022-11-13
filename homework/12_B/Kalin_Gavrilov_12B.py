import math
def impostor(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d <= r1-r2:
        return 1 #print("C2  is in C1")
    elif d <= r2-r1:
        return 2 #print("C1  is in C2")
    elif d < r1+r2:
        return 3 #print("Circumference of C1  and C2  intersect")
    elif d == r1+r2:
        return 4 #print("Circumference of C1 and C2 will touch")
    else:
        return 5 #print("C1 and C2  do not overlap")
