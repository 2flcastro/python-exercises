# ----------------------------------
# Sum All Prime
# ----------------------------------
# Sum all the prime numbers up to and including the provided number. A prime
# number is defined as a number greater than one and having only two divisors,
# one and itself. For example, 2 is a prime number beacuse it is only divisible
# by 1 and 2.
#
# The provided number may not be a prime.
# ----------------------------------

import unittest

def sum_primes(num):
    return total


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Sum_Primes(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_primes(10), 17)

    def test_2(self):
        self.assertEqual(sum_primes(977), 73156)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
