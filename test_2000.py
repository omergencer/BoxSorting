import unittest
import time
from box_fin import *

class StackTest(unittest.TestCase):
    def test_100(self):
        test = run_('',rcount = 2000)
        self.assertIsNotNone(test)

if __name__ == "__main__":
    unittest.main()

