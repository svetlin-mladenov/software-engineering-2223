import pytest
from get_intersections import *

def test_intersections():
    print(get_intersections(0, 0, 10, 5, 5, 10))
    assert get_intersections(0, 0, 5, 2, 2, 5) == (4.391164991562634, -2.3911649915626336, -2.3911649915626336, 4.391164991562634)
    assert get_intersections(0, 0, 3, 0, 0, 5) == None
    assert get_intersections(0, 0, 1, 2, 2, 2) == (0.9557189138830736, 0.2942810861169266, 0.2942810861169266, 0.9557189138830736)
    assert get_intersections(1, 0, 1, 0, 1, 0) == None
    assert get_intersections(0, 0, 1, 0, 0, 1) == None
    assert get_intersections(0, 0, 1, 0, 0, 2) == None
    assert get_intersections(4, 5, 6, 7, 8, 9) == (5.346873642484539, -0.8468736424845402, -1.8468736424845402, 6.346873642484539)
    assert get_intersections(0, 0, 10, 5, 5, 10) == (9.114378277661478, -4.114378277661476, -4.114378277661476, 9.114378277661478)

