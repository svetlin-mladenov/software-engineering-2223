import unittest
from circles import circle_check


class TestCircles(unittest.TestCase):

    def test_circles_matching(self):
        self.assertEqual(circle_check(radius1=1, radius2=1,
                         center_1=(0, 0), center_2=(0, 0)), 360)

    def test_circles_touching(self):
        self.assertEqual(circle_check(radius1=3, radius2=2,
                         center_1=(1, 1), center_2=(5, 4)), 1)

    def test_circles_intersecting(self):
        self.assertEqual(circle_check(radius1=1, radius2=5,
                         center_1=(1, 2), center_2=(4, 5)), 2)

    def test_circles_containing(self):
        self.assertEqual(circle_check(radius1=1, radius2=5,
                         center_1=(1, 1), center_2=(1, 1)), 0)

    def test_circles_no_common(self):
        self.assertEqual(circle_check(radius1=1, radius2=5,
                         center_1=(1, 1), center_2=(11, 11)), -1)


if __name__ == '__main__':
    unittest.main()
