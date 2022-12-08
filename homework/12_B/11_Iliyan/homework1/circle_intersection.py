import math # for square root
from circle import Circle # circle class
from enumCases import EnumCases

def circle_intersection(c1, c2):
  # checking if given circles are valid
  if(c1.r <= 0 or c2.r <= 0):
    return EnumCases.FAIL.value
  
  # distance between two points - dist = sqrt((x1-x2)^2 + (y1-y2)^2)
  dist = math.sqrt((c1.center[0] - c2.center[0])**2 +
                   (c1.center[1] - c2.center[1])**2)
  
  if(dist == 0 and c1.r == c2.r):
    return EnumCases.SAME.value
  elif(dist <= (c2.r - c1.r)):
    if(dist == 0):
      return EnumCases.ONE_INSIDE_TWO_SAME_CENTER.value
    elif(dist == (c2.r - c1.r)):
      return EnumCases.ONE_INSIDE_TWO_TOUCHING.value
    return EnumCases.ONE_INSIDE_TWO.value
  elif(dist <= (c1.r - c2.r)):
    if(dist == 0):
      return EnumCases.TWO_INSIDE_ONE_SAME_CENTER.value
    elif(dist == (c1.r - c2.r)):
      return EnumCases.TWO_INSIDE_ONE_TOUCHING.value
    return EnumCases.TWO_INSIDE_ONE.value
  elif(dist == (c1.r + c2.r)):
    return EnumCases.TOUCHING.value
  elif(dist < (c1.r + c2.r)):
    print(dist, c1.r, c2.r)
    if(dist == c1.r or dist == c2.r):
      return EnumCases.INTERSECTING_LYING_ON_CIRCUMFERENCE.value
    else:
      return EnumCases.INTERSECTING.value
  else: # dist > (c1.r + c2.r)
    return EnumCases.NOT_INTERACTING.value
