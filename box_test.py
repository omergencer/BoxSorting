import unittest
import time
from box_fin import *

class StackTest(unittest.TestCase):
    def test_int(self):
        test = run_("2,3")
        print("2,3",test)
        self.assertIsNotNone(test)
    def test_float(self):
        test = run_("2.6,3575.4646")
        print("2.6,3575.4646",test)
        self.assertIsNotNone(test)
    def test_intfloat(self):
        test = run_("2,3.7")
        print("2,3.7",test)
        self.assertIsNotNone(test)
    def test_wrong_type(self):
        test = run_("2.5,'hello'")
        print("2.5,'hello'",test)
        self.assertIsNotNone(test)
    def test_empty(self):
        test = run_('')
        print('',test)
        self.assertIsNotNone(test)
    
    
        
if __name__ == "__main__":
    unittest.main()
