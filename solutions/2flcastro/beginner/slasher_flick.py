# ----------------------------------
# Slasher Flick
# ----------------------------------
# Return the remaining elements of a list after chopping off "n" elements
# from the head.
#
# The head means the beginning of the list, or the zeroth index.
# ----------------------------------

import unittest

# simple slice technique
def slasher(lst, amount):
    return lst[amount:]


# using for-loop index and list.pop()
def slasher_2(lst, amount):
    for i in range(len(lst)):
        if i < amount:
            lst.pop(0)

    return lst


# using a while-loop and list.pop() method
def slasher_3(lst, amount):
    counter = amount
    while counter > 0:
        # to prevent error from performing list.pop() on empty list
        if not len(lst):
            return lst
        lst.pop(0)
        counter -= 1

    return lst


# using while-loop until end of lst
def slasher_4(lst, amount):
    # placeholder slahsed list
    slashed_lst = []

    counter = amount
    while counter < len(lst):
        slashed_lst.append(lst[counter])
        counter += 1

    return slashed_lst



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Slasher(unittest.TestCase):
    def test_1(self):
        self.assertEqual(slasher([1, 2, 3], 2), [3])

    def test_2(self):
        self.assertEqual(slasher([1, 2, 3], 0), [1, 2, 3])

    def test_3(self):
        self.assertEqual(slasher([1, 2, 3], 9), [])

    def test_4(self):
        self.assertEqual(slasher([1, 2, 3], 4), [])

    def test_5(self):
        self.assertEqual(slasher(["burgers", "fries", "shake"], 1), ["fries", "shake"])

    def test_6(self):
        self.assertEqual(slasher([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5), ["cheese", 4])


class Test_Slasher_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(slasher_2([1, 2, 3], 2), [3])

    def test_2(self):
        self.assertEqual(slasher_2([1, 2, 3], 0), [1, 2, 3])

    def test_3(self):
        self.assertEqual(slasher_2([1, 2, 3], 9), [])

    def test_4(self):
        self.assertEqual(slasher_2([1, 2, 3], 4), [])

    def test_5(self):
        self.assertEqual(slasher_2(["burgers", "fries", "shake"], 1), ["fries", "shake"])

    def test_6(self):
        self.assertEqual(slasher_2([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5), ["cheese", 4])


class Test_Slasher_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(slasher_3([1, 2, 3], 2), [3])

    def test_2(self):
        self.assertEqual(slasher_3([1, 2, 3], 0), [1, 2, 3])

    def test_3(self):
        self.assertEqual(slasher_3([1, 2, 3], 9), [])

    def test_4(self):
        self.assertEqual(slasher_3([1, 2, 3], 4), [])

    def test_5(self):
        self.assertEqual(slasher_3(["burgers", "fries", "shake"], 1), ["fries", "shake"])

    def test_6(self):
        self.assertEqual(slasher_3([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5), ["cheese", 4])


class Test_Slasher_4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(slasher_4([1, 2, 3], 2), [3])

    def test_2(self):
        self.assertEqual(slasher_4([1, 2, 3], 0), [1, 2, 3])

    def test_3(self):
        self.assertEqual(slasher_4([1, 2, 3], 9), [])

    def test_4(self):
        self.assertEqual(slasher_4([1, 2, 3], 4), [])

    def test_5(self):
        self.assertEqual(slasher_4(["burgers", "fries", "shake"], 1), ["fries", "shake"])

    def test_6(self):
        self.assertEqual(slasher_4([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5), ["cheese", 4])

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
