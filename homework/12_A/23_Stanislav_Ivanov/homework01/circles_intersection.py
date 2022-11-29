from enum import Enum


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.radius == other.radius)

    def calculate_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class IntersectionType(Enum):
    NOT_INTERSECTING = 0
    TOUCHING = 1
    INTERSECTING = 2
    MATCHING = 10


def circles_intersection(circle1: Circle, circle2: Circle) -> IntersectionType:
    if circle1 == circle2:
        return IntersectionType.MATCHING
    
    distance = circle1.calculate_distance(circle2)

    if distance == circle1.radius + circle2.radius or distance == abs(circle1.radius - circle2.radius):
        return IntersectionType.TOUCHING
    if distance < abs(circle1.radius - circle2.radius) or distance > circle1.radius + circle2.radius:
        return IntersectionType.NOT_INTERSECTING
    return IntersectionType.INTERSECTING
