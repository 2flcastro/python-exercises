# ----------------------------------
# Finders Keepers
# ----------------------------------
# Create a function that looks through a list (first argument) and returns the
# first element in the list that passes a truth test (second argument).
# ----------------------------------

import unittest

def find_element(lst, test):
    return lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Find_Element(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_element([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0 ), 8)

    def test_2(self):
        self.assertEqual(find_element([1, 3, 5, 9], lambda num: num % 2 == 0), None)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
