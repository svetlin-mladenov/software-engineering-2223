"""Enum class
"""
from enum import Enum, auto

class CircleIntersectionTypes(Enum):
    """INTERSECTING\n
    TOUCHING\n
    FIRST_INSIDE_SECOND\n
    SECOND_INSIDE_FIRST\n
    NOT_TOUCHING\n
    """
    INTERSECTING        = auto()
    TOUCHING            = auto()
    FIRST_INSIDE_SECOND = auto()
    SECOND_INSIDE_FIRST = auto()
    NOT_TOUCHING        = auto()
