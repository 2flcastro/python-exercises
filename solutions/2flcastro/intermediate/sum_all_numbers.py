# ----------------------------------
# Sum all Numbers in a Range
# ----------------------------------
# You will recieve a list of two numbers. Return the sum of those two numbers
# and all the numbers between them.
#
# The lowsest number will not always come firt.
# ----------------------------------

import unittest

# using built-in functions min(), max(), range(), sum()
def sum_all(lst):
    lst = list(range(min(lst), max(lst) + 1 ))
    return sum(lst)


# using range() and sort()
def sum_all_2(lst):
    lst.sort()
    total = 0
    for i in range(lst[0], lst[1] + 1):
        total += i
    return total


# using while-loop and min(), max()
def sum_all_3(lst):
    total = 0
    counter = max(lst)
    while counter >= min(lst):
        total += counter
        counter -= 1
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


class Test_Sum_All_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_all_2([1, 4]), 10)

    def test_2(self):
        self.assertEqual(sum_all_2([4, 1]), 10)

    def test_3(self):
        self.assertEqual(sum_all_2([5, 10]), 45)

    def test_4(self):
        self.assertEqual(sum_all_2([10, 5]), 45)


class Test_Sum_All_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_all_3([1, 4]), 10)

    def test_2(self):
        self.assertEqual(sum_all_3([4, 1]), 10)

    def test_3(self):
        self.assertEqual(sum_all_3([5, 10]), 45)

    def test_4(self):
        self.assertEqual(sum_all_3([10, 5]), 45)

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
