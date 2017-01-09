# ----------------------------------
# Falsy Bouncer
# ----------------------------------
# Remove all falsy values from a list.
#
# Falsy values include: False, 0, "", [], (), {}, None
# ----------------------------------

import unittest

def bouncer(lst):
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


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
