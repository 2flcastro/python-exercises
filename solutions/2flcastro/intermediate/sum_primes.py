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

# using list comprehension with prime_check() as conditional
def sum_primes(num):
    def prime_check(number):
        for i in range(2, number):
            if number % i == 0 and number != i:
                return False
        return True

    primes_lst = range(2, num + 1)
    primes_lst = [number for number in primes_lst if prime_check(number)]
    return sum(primes_lst)


# using nested for-loops
def sum_primes_2(num):
    total = 0
    for number in range(2, num + 1):
        prime_check = True
        for i in range(2, number + 1):
            if number % i == 0 and i != number:
                prime_check = False
                break
        if prime_check:
            total += number
    return total


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Sum_Primes(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_primes(10), 17)

    def test_2(self):
        self.assertEqual(sum_primes(977), 73156)


class Test_Sum_Primes_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_primes_2(10), 17)

    def test_2(self):
        self.assertEqual(sum_primes_2(977), 73156)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
