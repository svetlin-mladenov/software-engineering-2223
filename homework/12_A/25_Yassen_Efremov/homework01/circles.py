import math
from enum import Enum
 

class CircleState(Enum):
	NO_COMMON = 1
	MATCHING = 2
	TOUCHING = 3
	CONTAINING = 4
	CONTAINED = 5
	INTERSECTING = 6

# A function that returns information about two given circles in a cartesian coordinate system
def checkCircles(c1_center, c1_radius, c2_center, c2_radius):

	# Calculate the distance here because we use it a lot later
	center_distance = math.sqrt((c2_center[0] - c1_center[0])**2 + (c2_center[1] - c1_center[1])**2)

	# No common
	if center_distance > c1_radius + c2_radius:
		return CircleState.NO_COMMON

	elif center_distance < c1_radius + c2_radius:
		# Matching
		if not center_distance and c1_radius == c2_radius: return CircleState.MATCHING
		# Touching (from the inside)
		if c1_radius == center_distance + c2_radius or c2_radius == center_distance + c1_radius: return CircleState.TOUCHING
		# Containing
		if c1_radius > center_distance + c2_radius: return CircleState.CONTAINING
		if c2_radius > center_distance + c1_radius: return CircleState.CONTAINED
		# Intersecting
		return CircleState.INTERSECTING

	else:	# Touching
		return CircleState.TOUCHING
