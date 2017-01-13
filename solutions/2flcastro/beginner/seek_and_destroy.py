# ----------------------------------
# Seek and Destroy
# ----------------------------------
# You will be provided with an initial list (first argument) followed by one or
# more arguments. Remove all elements from the initial list that are of the
# same value as these arguments.
# ----------------------------------

import unittest

# use list comprehension as a list "map"
def destroyer(lst, *args):
    for arg in args:
        # could also use "!=" instead of "is not"
        lst = [item for item in lst if item is not arg]
    return lst


# use list.count() and list.remove() methods
def destroyer_2(lst, *args):
    for arg in args:
        if lst.count(arg):
            for i in range(lst.count(arg)):
                lst.remove(arg)
    return lst


# create new "clean" list and keep a tab on "clean" state
def destroyer_3(lst, *args):
    clean_lst = []
    for item in lst:
        clean = True
        for arg in args:
            if item == arg:
                clean = False
        if clean:
            clean_lst.append(item)
    return clean_lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Destroyer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(destroyer([1, 2, 3, 1, 2, 3], 2, 3), [1, 1])

    def test_2(self):
        self.assertEqual(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3), [1, 5, 1])

    def test_3(self):
        self.assertEqual(destroyer([3, 5, 1, 2, 2], 2, 3, 5), [1])

    def test_4(self):
        self.assertEqual(destroyer([2, 3, 2, 3], 2, 3), [])

    def test_5(self):
        self.assertEqual(destroyer(["tree", "hamburger", 53], "tree", 53), ["hamburger"])


class Test_Destroyer_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(destroyer_2([1, 2, 3, 1, 2, 3], 2, 3), [1, 1])

    def test_2(self):
        self.assertEqual(destroyer_2([1, 2, 3, 5, 1, 2, 3], 2, 3), [1, 5, 1])

    def test_3(self):
        self.assertEqual(destroyer_2([3, 5, 1, 2, 2], 2, 3, 5), [1])

    def test_4(self):
        self.assertEqual(destroyer_2([2, 3, 2, 3], 2, 3), [])

    def test_5(self):
        self.assertEqual(destroyer_2(["tree", "hamburger", 53], "tree", 53), ["hamburger"])


class Test_Destroyer_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(destroyer_3([1, 2, 3, 1, 2, 3], 2, 3), [1, 1])

    def test_2(self):
        self.assertEqual(destroyer_3([1, 2, 3, 5, 1, 2, 3], 2, 3), [1, 5, 1])

    def test_3(self):
        self.assertEqual(destroyer_3([3, 5, 1, 2, 2], 2, 3, 5), [1])

    def test_4(self):
        self.assertEqual(destroyer_3([2, 3, 2, 3], 2, 3), [])

    def test_5(self):
        self.assertEqual(destroyer_3(["tree", "hamburger", 53], "tree", 53), ["hamburger"])

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
