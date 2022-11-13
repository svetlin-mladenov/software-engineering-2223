
import math
 
# definirane na tochkite okrujnosti i dali ima vruzka mejdu tqh
def circles(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    
    if(d <= r2 - r1):
        print("Okrujnost 1 e w 2")
    elif(d <= r1 - r2):
        print("Okrujnost 2 e w 1")
    elif(d == r1 + r2):
        print("Okrujnostite se dopirat") 
    elif(d < r1 + r2):
        print("Circle intersect to each other")
    else:
        print("Nqma vruzka i dopir")
 

#cqlata informaciq za okrujnostite 
x1, y1 = -10, 8
x2, y2 = 14, -24
r1, r2 = 30, 10
 
#vikane na funksiqta
circles(x1, y1, x2, y2, r1, r2)
 