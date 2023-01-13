__package__ = "circle"

from enum import Enum, auto
from math import sqrt


class Intersection(Enum):
    NO_POINTS = auto()
    ONE_POINT = auto()
    TWO_POINTS = auto()
    ALL_POINTS = auto()
    UNIDENTIFIED = auto()


class Circle():

    def __init__(self, x: float, y: float, r: float) -> None:
        self.x = x
        self.y = y
        self.r = r

    def __eq__(self, __o: object) -> bool:
        return __o.x == self.x and __o.y == self.y and __o.r == self.r


def circle_intersection(c1: Circle, c2: Circle) -> Intersection:
    dx: float = abs(c1.x - c2.x)
    dy: float = abs(c1.y - c2.y)

    distance: float = sqrt(dx**2 + dy**2)

    match distance:
        case 0 if c1.r == c2.r:
            return Intersection.ALL_POINTS
        case too_far if too_far > c1.r + c2.r:
            return Intersection.NO_POINTS
        case exact_distance if exact_distance == c1.r + c2.r:
            return Intersection.ONE_POINT
        case small_offset if small_offset < c1.r + c2.r:
            return Intersection.TWO_POINTS
        case _:
            print(distance)
            return Intersection.UNIDENTIFIED


