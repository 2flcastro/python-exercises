# ----------------------------------
# Smallest Commom Multiple
# ----------------------------------
# Find the smallest common multiple of the provided parameters that can be
# evenly divided by both, as well as by all sequential numbers in the range
# between these parameters.
#
# The range will be a list of two numbers that will not necessarily be in
# numerical order.
#
# e.g. for 1 and 3, find the lowest common multiple of both 1 and 3 that is
# evenly divisible by all numbers BETWEEN 1 and 3.
#
# Helpful Links:
# - https://www.mathsisfun.com/least-common-multiple.html
# - https://www.artofproblemsolving.com/wiki/index.php/Least_common_multiple
# ----------------------------------

import unittest

def smallest_common(lst):
    return scm


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Smallest_Common(unittest.TestCase):
    def test_1(self):
        self.assertEqual(smallest_common([1, 5]), 60)

    def test_2(self):
        self.assertEqual(smallest_common([5, 1]), 60)

    def test_3(self):
        self.assertEqual(smallest_common([1, 13]), 360360)

    def test_4(self):
        self.assertEqual(smallest_common([23, 18]), 6056820)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
