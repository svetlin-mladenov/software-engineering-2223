import unittest
from homework import check_circles

class TestCircles(unittest.TestCase):
    def test_check_matching(self):
        self.assertEqual(check_circles((1, 1), 1, (1, 1), 1), "MATCHING")
    
    def test_check_containing(self):
        self.assertEqual(check_circles((0, 0), 8, (1, 1), 5), "CONTAINING")
    
    def test_check_intersecting(self):
        self.assertEqual(check_circles((2, 2), 4, (4, 4), 4), "INTERSECTING")
        
    def test_check_touching(self):
        self.assertEqual(check_circles((8, 9), 2, (4, 6), 3), "TOUCHING")

    def test_check_no_common(self):
        self.assertEqual(check_circles((1, 2), 3, (15, 27), 6), "NO_COMMON")
