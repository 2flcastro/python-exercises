# Unit Tests: Factorialize A Number
# -----------------------------------
import sys
sys.path.append(sys.path[0] + '/../../beginner')

import unittest
from factorializeNumber import factorialize

class TestFactorializeNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorialize(5), 120)
        
    def test_2(self):
        self.assertEqual(factorialize(10), 3628800)
        
    def test_3(self):
        self.assertEqual(factorialize(20), 2432902008176640000)
        
    def test_4(self):
        self.assertEqual(factorialize(0), 1)


# Run Tests
if __name__ == '__main__':
    unittest.main()