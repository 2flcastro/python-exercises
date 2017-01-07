# ----------------------------------
# Seek and Destroy
# ----------------------------------
# You will be provided with an initial array (first argument) followed by one or
# more arguments. Remove all elements from the initial array that are of the
# same value as these arguments.
# ----------------------------------

import unittest

def destroyer(arr):
    return arr



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Destroyer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(destroyer([1, 2, 3, 1, 2, 3], 2, 3), [1, 1])

    def test_2(self):
        self.assertEqual(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3), [1, 5, 1])

    def test_2(self):
        self.assertEqual(destroyer([3, 5, 1, 2, 2], 2, 3, 5), [1])

    def test_2(self):
        self.assertEqual(destroyer([2, 3, 2, 3], 2, 3)), [])

    def test_2(self):
        self.assertEqual(destroyer(["tree", "hamburger", 53], "tree", 53), ["hamburger"])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
