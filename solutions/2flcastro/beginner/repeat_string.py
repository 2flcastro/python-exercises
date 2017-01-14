# ----------------------------------
# Repeat a String Repeat a String
# ----------------------------------
# Repeat a given string (first argument, "str") "num" times (second argumet).
# Return an empty string if "num" is not a positive number.
#
# Try to use something other than the "*" operator!
# ----------------------------------

import unittest

# using "*" operator
def repeat_string(strg, num):
    return strg * num


# using recursion
def repeat_string_2(strg, num):
    if num == 1:
        return strg
    if num >= 0:
        return strg + repeat_string_2(strg, num - 1)
    else:
        return ""


# using while-loop to concatenate
def repeat_string_3(strg, num):
    repeated_strg = ""
    while num > 0:
        repeated_strg += strg
        num -= 1
    return repeated_strg


# using a for-loop to concatenate
def repeat_string_4(strg, num):
    repeated_strg = ""
    for i in range(num):
        repeated_strg += strg
    return repeated_strg



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


class Test_Repeat_String_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(repeat_string_2("*", 3), "***")

    def test_2(self):
        self.assertEqual(repeat_string_2("abc", 3), "abcabcabc")

    def test_3(self):
        self.assertEqual(repeat_string_2("abc", 4), "abcabcabcabc")

    def test_4(self):
        self.assertEqual(repeat_string_2("abc", 1), "abc")

    def test_5(self):
        self.assertEqual(repeat_string_2("*", 8), "********")

    def test_6(self):
        self.assertEqual(repeat_string_2("abc", -2), "")


class Test_Repeat_String_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(repeat_string_3("*", 3), "***")

    def test_2(self):
        self.assertEqual(repeat_string_3("abc", 3), "abcabcabc")

    def test_3(self):
        self.assertEqual(repeat_string_3("abc", 4), "abcabcabcabc")

    def test_4(self):
        self.assertEqual(repeat_string_3("abc", 1), "abc")

    def test_5(self):
        self.assertEqual(repeat_string_3("*", 8), "********")

    def test_6(self):
        self.assertEqual(repeat_string_3("abc", -2), "")


class Test_Repeat_String_4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(repeat_string_4("*", 3), "***")

    def test_2(self):
        self.assertEqual(repeat_string_4("abc", 3), "abcabcabc")

    def test_3(self):
        self.assertEqual(repeat_string_4("abc", 4), "abcabcabcabc")

    def test_4(self):
        self.assertEqual(repeat_string_4("abc", 1), "abc")

    def test_5(self):
        self.assertEqual(repeat_string_4("*", 8), "********")

    def test_6(self):
        self.assertEqual(repeat_string_4("abc", -2), "")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
