import math

def circle(x1, y1, x2, y2, r1, r2):
	d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

	if d == r1 + r2:
		return("Circumference of C1 and C2 will touch") 
	elif d < r1 + r2:
		return("Circumference of C1  and C2  intersect")
	elif d <= r2 - r1:
		return("C1  is in C2") 
	elif d <= r1 - r2:
		return("C2  is in C1")
	elif (x1 == x2 and y1 == y2 and r1 == r2):
		return("They are the same circle!")
	else:
		return("C1 and C2  do not overlap")
		

