from circleComparison import circle

def test_circle():
	#circle(x1, y1, x2, y2, r1, r2)
	assert "C1 and C2  do not overlap" == circle(5, 4, 3, 9, 2, 2)
	assert "Circumference of C1 and C2 will touch" == circle(5, 4, 5, 10, 3, 3)
	assert "Circumference of C1  and C2  intersect" == circle(6, 4, 10, 4, 3, 2)
	assert "C2  is in C1" == circle(5, 4, 5, 4, 3, 2)
	#assert "C1  is in C2" == circle(5, 4, 5, 4, 2, 3)
	#assert "They are the same circle!" == circle(5, 4, 5, 4, 3, 3) 
