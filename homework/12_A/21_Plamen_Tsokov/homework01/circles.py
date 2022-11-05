from math import sqrt

class Circle:
    def __init__(self, circle_name, X, Y, radius):
       self.name = circle_name
       self.X = X
       self.Y = Y
       self.radius = radius

def check_Circles(first_circle, second_circle):

    distance = math.sqrt((first_circle.X-second_circle.X)**2 + (first_circle.Y-second_circle.Y)**2)

    if distance == 0:
        return "MATCHING"
        
    elif distance == first_circle.radius + second_circle.radius:
        return "TOUCHING"
        
    elif distance < first_circle.radius + second_circle.radius:
        if distance > first_circle.radius or distance > second_circle.radius:
            return "CONTAINING"
        else:   
            return "INTERSECTING"
            
    elif distance > first_circle.radius + second_circle.radius:
        return "NOT TOUCHING OR CONTAINIG"
