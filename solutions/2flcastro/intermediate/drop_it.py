# ----------------------------------
# Drop It
# ----------------------------------
# Drop the elements of a list (first argument), starting from the front, until
# the predicate (second argument) returns True.
#
# The second element is a function you will use to test the elements of the
# list to decide if you should drop it or not.
#
# Return the rest of the list, otherwise return an empty list.
# ----------------------------------

import unittest

# Using recursion with list slice
def drop_elements(lst, func):
    if len(lst):
        return lst if func(lst[0]) else drop_elements(lst[1:], func)
    else:
        return lst


# Using a while-loop and list.pop()
def drop_elements_2(lst, func):
    while len(lst):
        if func(lst[0]):
            return lst
        lst.pop(0)
    return lst


# Using for-loop and list slice
def drop_elements_3(lst, func):
    for i in range(len(lst)):
        if func(lst[i]):
            return lst[i:]
    else:
        return []


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Drop_Elements(unittest.TestCase):
    def test_1(self):
        self.assertEqual(drop_elements([1, 2, 3, 4], lambda n : n >= 3 ), [3, 4])

    def test_2(self):
        self.assertEqual(drop_elements([0, 1, 0, 1], lambda n: n == 1 ), [1, 0, 1])

    def test_3(self):
        self.assertEqual(drop_elements([1, 2, 3], lambda n: n > 0), [1, 2, 3])

    def test_4(self):
        self.assertEqual(drop_elements([1, 2, 3, 4], lambda n: n > 5), [])

    def test_5(self):
        self.assertEqual(drop_elements([1, 2, 3, 7, 4], lambda n: n > 3),  [7, 4])

    def test_6(self):
        self.assertEqual(drop_elements([1, 2, 3, 9, 2], lambda n: n > 2), [3, 9, 2])


class Test_Drop_Elements_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(drop_elements_2([1, 2, 3, 4], lambda n : n >= 3 ), [3, 4])

    def test_2(self):
        self.assertEqual(drop_elements_2([0, 1, 0, 1], lambda n: n == 1 ), [1, 0, 1])

    def test_3(self):
        self.assertEqual(drop_elements_2([1, 2, 3], lambda n: n > 0), [1, 2, 3])

    def test_4(self):
        self.assertEqual(drop_elements_2([1, 2, 3, 4], lambda n: n > 5), [])

    def test_5(self):
        self.assertEqual(drop_elements_2([1, 2, 3, 7, 4], lambda n: n > 3),  [7, 4])

    def test_6(self):
        self.assertEqual(drop_elements_2([1, 2, 3, 9, 2], lambda n: n > 2), [3, 9, 2])


class Test_Drop_Elements_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(drop_elements_3([1, 2, 3, 4], lambda n : n >= 3 ), [3, 4])

    def test_2(self):
        self.assertEqual(drop_elements_3([0, 1, 0, 1], lambda n: n == 1 ), [1, 0, 1])

    def test_3(self):
        self.assertEqual(drop_elements_3([1, 2, 3], lambda n: n > 0), [1, 2, 3])

    def test_4(self):
        self.assertEqual(drop_elements_3([1, 2, 3, 4], lambda n: n > 5), [])

    def test_5(self):
        self.assertEqual(drop_elements_3([1, 2, 3, 7, 4], lambda n: n > 3),  [7, 4])

    def test_6(self):
        self.assertEqual(drop_elements_3([1, 2, 3, 9, 2], lambda n: n > 2), [3, 9, 2])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
