# ----------------------------------
# Falsy Bouncer
# ----------------------------------
# Remove all falsy values from a list.
#
# Falsy values include: False, 0, "", [], (), {}, None
# ----------------------------------

import unittest

def bouncer(lst):
    for i in lst:
        if i != True:
            lst.remove(i)
    return lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Bouncer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bouncer([7, "ate", "", False, 9]), [7, "ate", 9])

    def test_2(self):
        self.assertEqual(bouncer(["a", "b", "c"]), ["a", "b", "c"])

    def test_2(self):
        self.assertEqual(bouncer([False, None, 0, ""]), [])

    def test_2(self):
        self.assertEqual(bouncer([1, None, 2]), [1, 2])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
