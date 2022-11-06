from enum import Enum
import math

class Position(Enum):
    pos1 = 'They are equal'
    pos2 = 'They don\'t touch'
    pos3 = 'They touch externally'
    pos4 = 'They touch internally'
    pos5 = 'They intersect at two points'
    pos6 = 'One lying inside other'

class Circle:
    def __init__(self, circle_name, X, Y, radius):
       self.name = circle_name
       self.X = X
       self.Y = Y
       self.radius = radius

def distance_beetween_centers(first, second):
    return math.sqrt(math.pow((second.X - first.X),2) + math.pow((second.Y - first.Y),2))

def mutual_position(first_circle, second_circle):
    radii_sum = first_circle.radius + second_circle.radius
    radii_subtraction = abs(first_circle.radius - second_circle.radius)
    distance = distance_beetween_centers(first_circle, second_circle)

    if distance == radii_subtraction ==  0: 
        return Position.pos1.value
    elif distance > radii_sum: 
        return Position.pos2.value
    elif distance == radii_sum: 
        return Position.pos3.value
    elif distance == radii_subtraction: 
        return Position.pos4.value
    elif radii_subtraction < distance < radii_sum: 
        return Position.pos5.value
    elif distance < radii_subtraction: 
        return Position.pos6.value
    
 
print(f"Input for first circle")
X1 = float(input("X : "))
Y1 = float(input("Y : "))
radius1 = float(input("Radius : ")) 

print(f"Input for second circle")
X2 = float(input("X : "))
Y2 = float(input("Y : "))
radius2 = float(input("Radius : ")) 
    
first_circle = Circle("first circle", X1, Y1, radius1)
second_circle = Circle("second circle", X2, Y2, radius2)
print(mutual_position(first_circle, second_circle))