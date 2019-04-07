import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("Chicago", 50.4, 100.8)
        loc4 = loc1
        loc5 = loc2
        loc6 = loc3
        self.assertEqual(loc1==loc2, True)
        self.assertEqual(loc1==loc3, False)
        self.assertEqual(loc2==loc3, False)
        self.assertEqual(loc1==loc4, True)
        self.assertEqual(loc2==loc4, True)
        self.assertEqual(loc1==loc5, True)
        self.assertEqual(loc1==loc6, False)
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
