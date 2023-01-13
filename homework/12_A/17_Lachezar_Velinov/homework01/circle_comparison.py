"""Comparing circles
"""
from math import sqrt

from circle import Circle
from circle_intersection_types import CircleIntersectionTypes


def are_circles_intersecting(first: Circle, second: Circle) -> CircleIntersectionTypes:
    """Compares circles
    """
    d = sqrt(pow(first.x_centre - second.x_centre, 2) + pow(first.y_centre - second.y_centre, 2))

    if d <= first.r_length - second.r_length:
        return CircleIntersectionTypes.SECOND_INSIDE_FIRST
    if d <= second.r_length - first.r_length:
        return CircleIntersectionTypes.FIRST_INSIDE_SECOND
    if d <  first.r_length + second.r_length:
        return CircleIntersectionTypes.INTERSECTING
    if d == first.r_length + second.r_length:
        return CircleIntersectionTypes.TOUCHING

    return CircleIntersectionTypes.NOT_TOUCHING
