# ----------------------------------
# Steam Roller
# ----------------------------------
# Flatten a nested list. You must account for varying levels of nesting.
# ----------------------------------

import unittest

# Recursive Nested Function:
# Using the nested flatten() function and "flat" list as non-list tacker. Call
# flatten() recursively for each list until it's completely flat.
def steam_roll(lst):
    def flatten(lst):
        if type(lst) == list:
            for item in lst:
                flatten(item) if type(item) == list else flat.append(item)
    flat = []
    flatten(lst)
    return flat



# Long Way:
# Using a while-loop to "unnest" the elements in the list. Keep checking if the
# items in the list are lists and if so add their items to flat list, and do so
# until there are no more remaining lists.
def steam_roll_2(lst):
    flat_lst = []
    nested = True
    while nested:
        nested = False
        for element in lst:
            if type(element) == list:
                for nested_element in element:
                    if type(nested_element == list):
                        # must continue with while-loop since there are still nested lists
                        nested = True
                    flat_lst.append(nested_element)
            else:
                flat_lst.append(element)

        lst = flat_lst
        flat_lst = []
    return lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Steam_Roll(unittest.TestCase):
    def test_1(self):
        self.assertEqual(steam_roll([[["a"]], [["b"]]]), ["a", "b"])

    def test_2(self):
        self.assertEqual(steam_roll([1, [2], [3, [[4]]]]), [1, 2, 3, 4])

    def test_3(self):
        self.assertEqual(steam_roll([1, [], [3, [[4]]]]), [1, 3, 4])

    def test_4(self):
        self.assertEqual(steam_roll([1, {}, [3, [[4]]]]), [1, {}, 3, 4])


class Test_Steam_Roll_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(steam_roll_2([[["a"]], [["b"]]]), ["a", "b"])

    def test_2(self):
        self.assertEqual(steam_roll_2([1, [2], [3, [[4]]]]), [1, 2, 3, 4])

    def test_3(self):
        self.assertEqual(steam_roll_2([1, [], [3, [[4]]]]), [1, 3, 4])

    def test_4(self):
        self.assertEqual(steam_roll_2([1, {}, [3, [[4]]]]), [1, {}, 3, 4])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
