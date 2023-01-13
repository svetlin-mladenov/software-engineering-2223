import pytest
from circle_overlapping import *

def test_overlapping():
    assert circle_overlapping(5, 4, 2, 3, 9, 2) == "Circles not overlapping"
    assert circle_overlapping(5, 4, 3, 5, 10, 3) == "Circles are touching in one point"
    assert circle_overlapping(6, 4, 3, 10, 4, 2) == "Circles overlap partially"
    assert circle_overlapping(5, 4, 3, 5, 4, 2) == "Second circle is in the first one"
    assert circle_overlapping(5, 4, 2, 5, 4, 3) == "First circle is in the second one"
    assert circle_overlapping(5, 4, 3, 5, 4, 3) == "Same circle"



