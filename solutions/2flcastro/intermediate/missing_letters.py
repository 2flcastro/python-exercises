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
    for i in range(len(strg) - 1):
        if ord(strg[i]) + 1 != ord(strg[i + 1]):
            return chr(ord(strg[i]) + 1)
    return None


# using starting_point as reference
def missing_letters_2(strg):
    starting_point = ord(strg[0])
    for letter in strg:
        if starting_point != ord(letter):
            return chr(starting_point)
        starting_point += 1
    return None


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


class Test_Missing_Letters_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(missing_letters_2("abce"), "d")

    def test_2(self):
        self.assertEqual(missing_letters_2("abcdefghjklmno"), "i")

    def test_3(self):
        self.assertEqual(missing_letters_2("bcd"), None)

    def test_4(self):
        self.assertEqual(missing_letters_2("yz"), None)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
