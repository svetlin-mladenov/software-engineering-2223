"""Circle file
"""
from numbers import Number


class Circle:
    """Circle class
    """
    def __init__(self, x_centre: Number, y_centre: Number, r_length: Number):

        self._x_centre = x_centre
        self._y_centre = y_centre
        self._r_length = r_length

    @property
    def x_centre(self) -> Number:
        return self._x_centre

    @x_centre.setter
    def x_centre(self, x_centre: Number):
        if not isinstance(x_centre, Number):
            raise TypeError(f"Setter expected Number but was given {type(x_centre)} instead.\n")
        self._x_centre = x_centre

    @property
    def y_centre(self) -> Number:
        return self._y_centre

    @y_centre.setter
    def y_centre(self, y_centre: Number):
        if not isinstance(y_centre, Number):
            raise TypeError(f"Setter expected Number but was given {type(y_centre)} instead.\n")
        self._y_centre = y_centre

    @property
    def r_length(self) -> Number:
        return self._r_length

    @r_length.setter
    def r_length(self, r_length: Number):
        if not isinstance(r_length, Number):
            raise TypeError(f"Setter expected Number but was given {type(r_length)} instead.\n")
        if r_length <= 0:
            raise ValueError(f"Setter expected a positive number but was given {r_length} instead\n")
        self._r_length = r_length
