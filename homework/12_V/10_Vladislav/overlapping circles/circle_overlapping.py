import math
def circle_overlapping(x1,y1,r1,x2,y2,r2):
  d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  if x1 == x2 and y1 ==y2 and r1 == r2:
    return "Same circle"
  elif d <= r1-r2:
    return "Second circle is in the first one"
  elif d <= r2-r1:
    return "First circle is in the second one"
  elif d < r1+r2:
    return "Circles overlap partially"
  elif d == r1+r2:
    return "Circles are touching in one point"
  else:
    return "Circles not overlapping"