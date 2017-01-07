# ----------------------------------
# Slasher Flick
# ----------------------------------
# Return the remaining elements of a list after chopping off "n" elements
# from the head.
#
# The head means the beginning of the list, or the zeroth index.
# ----------------------------------

import unittest

def slasher(lst, amount):
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


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
