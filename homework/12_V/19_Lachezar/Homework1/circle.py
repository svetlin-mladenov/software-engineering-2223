import math


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to(self, coordinate):
        return math.sqrt((self.x - coordinate.x)**2 + (self.y-coordinate.y)**2)


class Circle(object):
    def __init__(self, coordinate, radius):
        self.coordinate = coordinate
        self.radius = radius

    def compare_to(self, circle) -> str:
        dist = self.coordinate.get_distance_to(circle.coordinate)
        if self.radius == circle.radius and self.coordinate == circle.coordinate:
            return "equal"
        elif dist <= self.radius-circle.radius:
            return "circumscribed"
        elif dist <= circle.radius-self.radius:
            return "inscribed"
        elif dist < self.radius+circle.radius:
            return "intersected"
        elif dist == self.radius+circle.radius:
            return "contact"
        else:
            return "nil"
