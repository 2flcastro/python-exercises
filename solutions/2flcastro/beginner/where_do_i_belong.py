# ----------------------------------
# Where do I Belong
# ----------------------------------
# Return the lowest index at which a value (second argument) should be inserted
# into an list (first argument) once it has been sorted. The returned value
# should be a number.
#
# For example, get_index([1,2,3,4], 1.5) should return "1" because it i
# greater than 1 (index 0) and less than 2 (index 1).
#
# Likewise, get_index([20,3,5], 19) should return "2" because once the list has
# been sorted it will look like [3, 5, 20] and 19 is less than 20 (index 2)
# and greater than 5 (index 1).
# ----------------------------------

import unittest

# use list.append(), list.sort(), and list.index() methods
def get_index(lst, num):
    lst.append(num)
    lst.sort()
    return lst.index(num)


# using for-loop to get index
def get_index_2(lst, num):
    lst.append(num)
    lst.sort()
    for i in range(len(lst)):
        if lst[i] == num:
            return i


# not adding new num to lst
def get_index_3(lst, num):
    lst.sort()
    for i, item in enumerate(lst):
        if item >= num:
            return i
    # if num is the largest item on list, return last index
    return len(lst)



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Get_Index(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_index([10, 20, 30, 40, 50], 35), 3)

    def test_2(self):
        self.assertEqual(get_index([10, 20, 30, 40, 50], 30), 2)

    def test_3(self):
        self.assertEqual(get_index([40, 60], 50), 1)

    def test_4(self):
        self.assertEqual(get_index([3, 10, 5], 3), 0)

    def test_5(self):
        self.assertEqual(get_index([5, 3, 20, 3], 5), 2)

    def test_6(self):
        self.assertEqual(get_index([2, 20, 10], 19), 2)

    def test_7(self):
        self.assertEqual(get_index([2, 5, 10], 15), 3)


class Test_Get_Index_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_index_2([10, 20, 30, 40, 50], 35), 3)

    def test_2(self):
        self.assertEqual(get_index_2([10, 20, 30, 40, 50], 30), 2)

    def test_3(self):
        self.assertEqual(get_index_2([40, 60], 50), 1)

    def test_4(self):
        self.assertEqual(get_index_2([3, 10, 5], 3), 0)

    def test_5(self):
        self.assertEqual(get_index_2([5, 3, 20, 3], 5), 2)

    def test_6(self):
        self.assertEqual(get_index_2([2, 20, 10], 19), 2)

    def test_7(self):
        self.assertEqual(get_index_2([2, 5, 10], 15), 3)


class Test_Get_Index_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_index_3([10, 20, 30, 40, 50], 35), 3)

    def test_2(self):
        self.assertEqual(get_index_3([10, 20, 30, 40, 50], 30), 2)

    def test_3(self):
        self.assertEqual(get_index_3([40, 60], 50), 1)

    def test_4(self):
        self.assertEqual(get_index_3([3, 10, 5], 3), 0)

    def test_5(self):
        self.assertEqual(get_index_3([5, 3, 20, 3], 5), 2)

    def test_6(self):
        self.assertEqual(get_index_3([2, 20, 10], 19), 2)

    def test_7(self):
        self.assertEqual(get_index_3([2, 5, 10], 15), 3)

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
