# ----------------------------------
# Sorted Union
# ----------------------------------
# Write a function that takes two or more lists and returns a new list of
# unique values in order of the original provided lists.
#
# In other words, all the values present from all lists should be included in
# original order, but with no duplicates in their final form.
#
# The unique numbers should be sorted by their original order, but the final
# list should not be sorted in numerical order.
# ----------------------------------

import unittest

# using for-loop and list comprehension
def unite_unique(lst, *args):
    unique_lst = []
    lsts = [lst] + list(args)
    for lst in lsts:
        unique_lst.extend([item for item in lst if not item in unique_lst])
    return unique_lst
    [item for item in lst for lst in lsts]


# using nested for-looops
def unite_unique_2(lst, *args):
    unique_lst = []
    lsts = [lst]
    # pull all arguments into a single 2d list
    for arg in args:
        lsts.append(arg)
    for lst in lsts:
        for item in lst:
            if not item in unique_lst:
                unique_lst.append(item)
    return unique_lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Unite_Union(unittest.TestCase):
    def test_1(self):
        self.assertEqual(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]), [1, 3, 2, 5, 4])

    def test_2(self):
        self.assertEqual(unite_unique([1, 3, 2], [1, [5]], [2, [4]]), [1, 3, 2, [5], [4]])

    def test_3(self):
        self.assertEqual(unite_unique([1, 2, 3], [5, 2, 1]), [1, 2, 3, 5])

    def test_4(self):
        self.assertEqual(unite_unique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]), [1, 2, 3, 5, 4, 6, 7, 8])


class Test_Unite_Union_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(unite_unique_2([1, 3, 2], [5, 2, 1, 4], [2, 1]), [1, 3, 2, 5, 4])

    def test_2(self):
        self.assertEqual(unite_unique_2([1, 3, 2], [1, [5]], [2, [4]]), [1, 3, 2, [5], [4]])

    def test_3(self):
        self.assertEqual(unite_unique_2([1, 2, 3], [5, 2, 1]), [1, 2, 3, 5])

    def test_4(self):
        self.assertEqual(unite_unique_2([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]), [1, 2, 3, 5, 4, 6, 7, 8])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
