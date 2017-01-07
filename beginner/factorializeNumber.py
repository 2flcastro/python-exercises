# ----------------------------------
# Facorialize A Number
# ----------------------------------
# Return a factorial of the provided ineger.
# If the integer is represented with the letter "n", a
# factorial is the product of all positive integers less
# than or equal to n.
#
# Factorials are often represented with the notation "n!"
# Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# Note: you can return whatever variable you want from your
# function - not necessarily one named "num" - so long as it
# is your solution.
# ----------------------------------

import unittest

# using recursion
def factorialize(num):
    factorial = 1
    if num == 1 or num == 0:
        return 1
    return num * factorialize(num - 1)

# using range()
def factorialize_2(num):
    factorial = 1
    for i in range(num):
        factorial = factorial * (i + 1);
    return factorial

# using while loop
def factorialize_3(num):
    factorial = 1
    while num > 0:
        factorial *= num;
        num -= 1
    return factorial



# ----------------------------------
# Unit Tests
# ----------------------------------
class TestFactorializeNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorialize(5), 120)

    def test_2(self):
        self.assertEqual(factorialize(10), 3628800)

    def test_3(self):
        self.assertEqual(factorialize(20), 2432902008176640000)

    def test_4(self):
        self.assertEqual(factorialize(0), 1)


class TestFactorializeNumber_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorialize_2(5), 120)

    def test_2(self):
        self.assertEqual(factorialize_2(10), 3628800)

    def test_3(self):
        self.assertEqual(factorialize_2(20), 2432902008176640000)

    def test_4(self):
        self.assertEqual(factorialize_2(0), 1)


class TestFactorializeNumber_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorialize_3(5), 120)

    def test_2(self):
        self.assertEqual(factorialize_3(10), 3628800)

    def test_3(self):
        self.assertEqual(factorialize_3(20), 2432902008176640000)

    def test_4(self):
        self.assertEqual(factorialize_3(0), 1)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == '__main__':
    unittest.main()
