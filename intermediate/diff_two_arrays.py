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

def diff_lst(lst1, lst2):
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


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
