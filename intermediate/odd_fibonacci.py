# ----------------------------------
# Sum All Odd Fibonacci Numbers
# ----------------------------------
# Given a positive integer "num", return the sum of all odd Fibonacci numbers
# that are less than or equal to "num".
#
# The first two numbers in the Fibonacci sequence are 1 and 1. Every additional
# number in the sequence is the sume of the two previous numbers. The first six
# numbers of the Fibonacci sequence are 1, 1, 2, 3, 5, and 8.
#
# For example, sum_fibs(10) should return 10 because all odd Fibonacci numbers
# less than 10 are 1, 1, 2, 3, 5, and 8.
# ----------------------------------

import unittest

def sum_fibs(num):
    return fib_sum


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Sum_Fibs(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_fibs(1000), 1785)

    def test_2(self):
        self.assertEqual(sum_fibs(4000000), 4613732)

    def test_3(self):
        self.assertEqual(sum_fibs(4), 5)

    def test_4(self):
        self.assertEqual(sum_fibs(75024), 60696)

    def test_5(self):
        self.assertEqual(sum_fibs(75025), 135721)

    def test_6(self):
        self.assertEqual(sum_fibs(10), 10)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
