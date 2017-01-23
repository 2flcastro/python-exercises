# ----------------------------------
# Finders Keepers
# ----------------------------------
# Create a function that looks through a list (first argument) and returns the
# first element in the list that passes a truth test (second argument).
# ----------------------------------

import unittest

# using recursion with each call slicing off first element of list
def find_element(lst, test):
    if len(lst):
        return lst[0] if test(lst[0]) else find_element(lst[1:], test)


# using list comprehension as filter and returning first (True) element
def find_element_2(lst, test):
    lst = [element for element in lst if test(element)]
    return lst[0] if len(lst) else None


# for-loop with if statement that executes test
def find_element_3(lst, test):
    for element in lst:
        if test(element):
            return element


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Find_Element(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_element([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0 ), 8)

    def test_2(self):
        self.assertEqual(find_element([1, 3, 5, 9], lambda num: num % 2 == 0), None)


class Test_Find_Element_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_element_2([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0 ), 8)

    def test_2(self):
        self.assertEqual(find_element_2([1, 3, 5, 9], lambda num: num % 2 == 0), None)


class Test_Find_Element_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_element_3([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0 ), 8)

    def test_2(self):
        self.assertEqual(find_element_3([1, 3, 5, 9], lambda num: num % 2 == 0), None)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
