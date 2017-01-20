# ----------------------------------
# Spinal Tap Case
# ----------------------------------
# Convert a string to spinal case.
#
# Spinal case is all-lower-case-words-joined-by-dashes
#
# Python RegEx: https://docs.python.org/3/library/re.html#module-re
# ----------------------------------

import unittest

def spinal_case(sentence):
    return sentence


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Spinal_Case(unittest.TestCase):
    def test_1(self):
        self.assertEqual(spinal_case("This Is Spinal Tap"), "this-is-spinal-tap")

    def test_2(self):
        self.assertEqual(spinal_case("thisIsSpinalTap"), "this-is-spinal-tap")

    def test_3(self):
        self.assertEqual(spinal_case("The_Andy_Griffith_Show"), "the-andy-griffith-show")

    def test_4(self):
        self.assertEqual(spinal_case("Teletubbies say Eh-oh"), "teletubbies-say-eh-oh")

    def test_5(self):
        self.assertEqual(spinal_case("AllThe-small Things"), "all-the-small-things")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
