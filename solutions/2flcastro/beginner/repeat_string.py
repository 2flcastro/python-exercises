# ----------------------------------
# Repeat a String Repeat a String
# ----------------------------------
# Repeat a given string (first argument, "str") "num" times (second argumet).
# Return an empty string if "num" is not a positive number.
#
# Try to use something other than the "*" operator!
# ----------------------------------

import unittest

def repeat_string(str, num):
    return str



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Repeat_String(unittest.TestCase):
    def test_1(self):
        self.assertEqual(repeat_string("*", 3), "***")

    def test_2(self):
        self.assertEqual(repeat_string("abc", 3), "abcabcabc")

    def test_3(self):
        self.assertEqual(repeat_string("abc", 4), "abcabcabcabc")

    def test_4(self):
        self.assertEqual(repeat_string("abc", 1), "abc")

    def test_5(self):
        self.assertEqual(repeat_string("*", 8), "********")

    def test_6(self):
        self.assertEqual(repeat_string("abc", -2), "")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
