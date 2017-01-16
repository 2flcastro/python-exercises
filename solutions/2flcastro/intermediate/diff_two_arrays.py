# ----------------------------------
# Diff Two Arrays
# ----------------------------------
# Compare two lists and return a new list with any items only found in one of
# the two given lists, but not both. In other words, return the symmetric
# difference of the two lists.
#
# Note: sometimes your solution might return a list with the right items, but in
# a different order. Adjust your code to fit the order of the unit tests, or
# modify the unit test themselves if needed.
# ----------------------------------

import unittest

# using list comprehension as a filter
def diff_lst(lst1, lst2):
    sym_diff = lst1 + lst2
    return [item for item in sym_diff if (not item in lst1) or (not item in lst2)]


# using two sets of for-loops
def diff_lst_2(lst1, lst2):
    sym_diff = []
    for item in lst1:
        if not item in lst2:
            sym_diff.append(item)
    for item in lst2:
        if not item in lst1:
            sym_diff.append(item)
    return sym_diff


# using a for-loop with offset tracker
def diff_lst_3(lst1, lst2):
    sym_diff = lst1 + lst2
    offset = 0
    for i in range(len(sym_diff)):
        if (sym_diff[i - offset] in lst1) and (sym_diff[i - offset] in lst2):
            sym_diff.pop(i - offset)
            offset += 1
    return sym_diff



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Diff_Lst(unittest.TestCase):
    def test_1(self):
        self. assertEqual(diff_lst(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool"])

    def test_2(self):
        self. assertEqual(diff_lst(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool", "diorite"])

    def test_3(self):
        self. assertEqual(diff_lst([1, 2, 3, 5], [1, 2, 3, 4, 5]), [4])

    def test_4(self):
        self. assertEqual(diff_lst([1, "calf", 3, "piglet"], [1, "calf", 3, 4]), ["piglet", 4])

    def test_5(self):
        self. assertEqual(diff_lst([], ["snuffleupagus", "cookie monster", "elmo"]), ["snuffleupagus", "cookie monster", "elmo"])

    def test_6(self):
        self. assertEqual(diff_lst([1, "calf", 3, "piglet"], [7, "filly"]), [1, "calf", 3, "piglet", 7, "filly"])


class Test_Diff_Lst_2(unittest.TestCase):
    def test_1(self):
        self. assertEqual(diff_lst_2(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool"])

    def test_2(self):
        self. assertEqual(diff_lst_2(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool", "diorite"])

    def test_3(self):
        self. assertEqual(diff_lst_2([1, 2, 3, 5], [1, 2, 3, 4, 5]), [4])

    def test_4(self):
        self. assertEqual(diff_lst_2([1, "calf", 3, "piglet"], [1, "calf", 3, 4]), ["piglet", 4])

    def test_5(self):
        self. assertEqual(diff_lst_2([], ["snuffleupagus", "cookie monster", "elmo"]), ["snuffleupagus", "cookie monster", "elmo"])

    def test_6(self):
        self. assertEqual(diff_lst_2([1, "calf", 3, "piglet"], [7, "filly"]), [1, "calf", 3, "piglet", 7, "filly"])


class Test_Diff_Lst_3(unittest.TestCase):
    def test_1(self):
        self. assertEqual(diff_lst_3(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool"])

    def test_2(self):
        self. assertEqual(diff_lst_3(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]), ["pink wool", "diorite"])

    def test_3(self):
        self. assertEqual(diff_lst_3([1, 2, 3, 5], [1, 2, 3, 4, 5]), [4])

    def test_4(self):
        self. assertEqual(diff_lst_3([1, "calf", 3, "piglet"], [1, "calf", 3, 4]), ["piglet", 4])

    def test_5(self):
        self. assertEqual(diff_lst_3([], ["snuffleupagus", "cookie monster", "elmo"]), ["snuffleupagus", "cookie monster", "elmo"])

    def test_6(self):
        self. assertEqual(diff_lst_3([1, "calf", 3, "piglet"], [7, "filly"]), [1, "calf", 3, "piglet", 7, "filly"])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
