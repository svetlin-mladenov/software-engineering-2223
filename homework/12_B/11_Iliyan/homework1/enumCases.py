from enum import Enum
class EnumCases(Enum):
    FAIL = "Invalid circle radius! Circles must have a radius > 0!"
    SAME = "Cirles are the same"
    ONE_INSIDE_TWO = "Circle 1 is inside Circle 2"
    ONE_INSIDE_TWO_SAME_CENTER = "Circle 1 is inside Circle 2 and they share the same center"
    ONE_INSIDE_TWO_TOUCHING = "Circle 1 is inside Circle 2 and are touching from the inside"
    TWO_INSIDE_ONE = "Circle 2 is inside Circle 1"
    TWO_INSIDE_ONE_SAME_CENTER = "Circle 2 is inside Circle 1 and they share the same center"
    TWO_INSIDE_ONE_TOUCHING = "Circle 2 is inside Circle 1 and are touching from the inside"
    TOUCHING = "Cirles are touching from the outside"
    INTERSECTING_LYING_ON_CIRCUMFERENCE = "Circles are intersecting and one of them is lying on the other's circumference"
    INTERSECTING = "Circles are intersecting"
    NOT_INTERACTING = "Circles are not interacting"
