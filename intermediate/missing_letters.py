# ----------------------------------
# Missing Letters
# ----------------------------------
# Find the missing letter in the passed letter range and return it.
#
# If all letters are present in the range return None.
# ----------------------------------

import unittest

# using range(), chr(), and ord() built-in functions
def missing_letters(strg):
    return missing_letter


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Missing_Letters(unittest.TestCase):
    def test_1(self):
        self.assertEqual(missing_letters("abce"), "d")

    def test_2(self):
        self.assertEqual(missing_letters("abcdefghjklmno"), "i")

    def test_3(self):
        self.assertEqual(missing_letters("bcd"), None)

    def test_4(self):
        self.assertEqual(missing_letters("yz"), None)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
