# Facorialize A Number
# --------------------------
# Return a factorial of the provided ineger.
# If the integer is represented with the letter "n", a
# factorial is the product of all positive integers less
# than or equal to n.
#
# Factorials are often represented with the notation "n!"
# Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# Note: you can return whatever variable you want from your
# function - no necessarily one named "num" - so long as it
# is your solution.
# -----------------------------------------------------------
import unittest

def factorialize(num):
    # your code here...
    return num



# ----------------------------------
# Unit Tests
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
