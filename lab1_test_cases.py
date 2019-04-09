import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        blist = [1,0,2,5,3,4]
        clist = []
        dlist = [1,1,1,1,1,1]
        elist = [1,0,0,2]
        flist = [9]
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter(blist), 5)
        self.assertEqual(max_list_iter(clist), None)
        self.assertEqual(max_list_iter(dlist), 1)
        self.assertEqual(max_list_iter(elist), 2)
        self.assertEqual(max_list_iter(flist), 9)
		
    def test_reverse_rec(self):
        
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([3,2,1]), [1,2,3])
        self.assertEqual(reverse_rec([4,3,2,1]), [1,2,3,4])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1,2,3,4,5]), [5,4,3,2,1])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), None)
        

if __name__ == "__main__":
        unittest.main()

    
