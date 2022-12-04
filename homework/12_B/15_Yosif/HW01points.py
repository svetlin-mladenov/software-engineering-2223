import math

def interface(a):
	if(len(a)==6):
		return check_case(a[0],a[1],a[2],a[3],a[4],a[5])
	else:
		return 100

def check_case(x1,y1,r1,x2,y2,r2):

	if(x1==x2 and y1==y2 and r1==r2):
		# съвпадат
		return "same"

	distance = math.sqrt(abs(x1-x2)*abs(x1-x2)+abs(y1-y2)*abs(y1-y2))
	if(distance<abs(r1-r2)):
		# едното в другото
		return "in"
	if(distance<r1+r2):
		# print("d and r1+r2")
		# print(distance)
		# print(r1+r2)
		# пресичат се 
		return "intersect"
	if(abs(distance-(r1+r2))<0.0001):
		# допират се
		return "touch"
	# нито едно от предходните
	return "none"

def main():
	same1 = [0,0,1,0,0,1]
	same2 = [1,1,10,1,1,10]
	in1 = [0,0,1,0,0,2]
	in2 = [0,0,1,1,1,5]
	in3 = [1,5,10,0,0,2]
	in4 = [0,0,2,0,0,1]
	intersect1 = [0,0,2,2,2,2]
	intersect2 = [10,10,2,11,11,3.4]
	touch1 = [0,0,1,2,0,1]
	touch2 = [3,6,2,6,3,2.2426]
	no = [0,0,1,3,3,1]
	cases = [same1,same2,in1,in2,in3,in4,intersect1,intersect2,touch1,touch2,no]

	for i in cases:
		print(interface(i))

main()