import math
from enum import Enum


class Result(Enum):
    EQUAL = "EQUAL"
    CIRCUMSCRIBED = "CIRCUMSCRIBED"
    INSCRIBED = "INSCRIBED"
    INTERSECTED = "INTERSECTED"
    CONTACT_INSIDE = "CONTACT_INSIDE"
    CONTACT_OUTSIDE = "CONTACT_OUTSIDE"
    NIL = "NIL"


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
            return Result.EQUAL
        if dist == abs(self.radius - circle.radius):
            return Result.CONTACT_INSIDE

        if dist < self.radius - circle.radius:
            return Result.CIRCUMSCRIBED
        if dist < circle.radius - self.radius:
            return Result.INSCRIBED
        if dist < self.radius + circle.radius:
            return Result.INTERSECTED
        if dist == self.radius + circle.radius:
            return Result.CONTACT_OUTSIDE

        return Result.NIL
