# ----------------------------------
# Falsy Bouncer
# ----------------------------------
# Remove all falsy values from a list.
#
# Falsy values include: False, 0, "", [], (), {}, None
# ----------------------------------

import unittest

# using a comprehension to create a list "filter"
def bouncer(lst):
    lst = [item for item in lst if item]
    return lst


# create a new list and add "truthy" elements to it
def bouncer_2(lst):
    clean_lst = []
    for item in lst:
        if item:
            clean_lst.append(item)
    return clean_lst


# use for-loop and index offset
def bouncer_3(lst):
    # need to keep track of index offset
    index_offset = 0
    for i in range(len(lst)):
        if not lst[i - index_offset]:
            lst.pop(i - index_offset)
            index_offset += 1
    return lst



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Bouncer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bouncer([7, "ate", "", False, 9]), [7, "ate", 9])

    def test_2(self):
        self.assertEqual(bouncer(["a", "b", "c"]), ["a", "b", "c"])

    def test_3(self):
        self.assertEqual(bouncer([False, None, 0, ""]), [])

    def test_4(self):
        self.assertEqual(bouncer([1, None, 2]), [1, 2])

    def test_5(self):
        self.assertEqual(bouncer([[], {}, (), set(), "Empty Data Structures"]), ["Empty Data Structures"])


class Test_Bouncer_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bouncer_2([7, "ate", "", False, 9]), [7, "ate", 9])

    def test_2(self):
        self.assertEqual(bouncer_2(["a", "b", "c"]), ["a", "b", "c"])

    def test_3(self):
        self.assertEqual(bouncer_2([False, None, 0, ""]), [])

    def test_4(self):
        self.assertEqual(bouncer_2([1, None, 2]), [1, 2])

    def test_5(self):
        self.assertEqual(bouncer_2([[], {}, (), set(), "Empty Data Structures"]), ["Empty Data Structures"])


class Test_Bouncer_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bouncer_3([7, "ate", "", False, 9]), [7, "ate", 9])

    def test_2(self):
        self.assertEqual(bouncer_3(["a", "b", "c"]), ["a", "b", "c"])

    def test_3(self):
        self.assertEqual(bouncer_3([False, None, 0, ""]), [])

    def test_4(self):
        self.assertEqual(bouncer_3([1, None, 2]), [1, 2])

    def test_5(self):
        self.assertEqual(bouncer_3([[], {}, (), set(), "Empty Data Structures"]), ["Empty Data Structures"])

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
