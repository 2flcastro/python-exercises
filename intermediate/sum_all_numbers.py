# ----------------------------------
# Sum all Numbers in a Range
# ----------------------------------
# You will recieve a list of two numbers. Return the sum of those two numbers
# and all the numbers between them.
#
# The lowsest number will not always come firt.
# ----------------------------------

import unittest

def sum_all(lst):
    return total


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Sum_All(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_all([1, 4]), 10)

    def test_2(self):
        self.assertEqual(sum_all([4, 1]), 10)

    def test_3(self):
        self.assertEqual(sum_all([5, 10]), 45)

    def test_4(self):
        self.assertEqual(sum_all([10, 5]), 45)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
