# ----------------------------------
# Roman Numeral Converter
# ----------------------------------
# Convert the given number into a roman numeral.
#
# All roman numeral answers should be provided in upper-case.
#
# Help link for roman numerals refresher:
# http://www.mathsisfun.com/roman-numerals.html
# ----------------------------------

import unittest
import math

# using condensed dictionary to map numbers to roman numberals
def convert_to_roman(original_num):
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    nums = sorted(list(roman_numerals.keys()), reverse=True)
    roman_numeral = ''
    for num in nums:
        while original_num >= num:
            roman_numeral += roman_numerals[num]
            original_num -= num
    return roman_numeral


# using a dictionary that maps each number to its roman numeral conterpart
def convert_to_roman_2(original_num):
    roman_nums = {
        1000: "M",
        900: "CM",
        800: "DCCC",
        700: "DCC",
        600: "DC",
        500: "D",
        400: "CD",
        300: "CCC",
        200: "CC",
        100: "C",
        90: "XC",
        80: "LXXX",
        70: "LXX",
        60: "LX",
        50: "L",
        40: "XL",
        30: "XXX",
        20: "XX",
        10: "X",
        9: "IX",
        8: "VIII",
        7: "VII",
        6: "VI",
        5: "V",
        4: "IV",
        3: "III",
        2: "II",
        1: "I"
    }
    nums = list(roman_nums.keys())
    nums.sort()
    nums.reverse()
    roman_numeral = ''
    for num in nums:
        div = math.floor(original_num / num)
        if div:
            for i in range(div):
                roman_numeral += roman_nums[num]
            original_num = original_num % num
        if original_num == 0:
            break
    return roman_numeral



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Convert_To_Roman(unittest.TestCase):
    def test_1(self):
        self.assertEqual(convert_to_roman(2), "II")

    def test_2(self):
        self.assertEqual(convert_to_roman(3), "III")

    def test_3(self):
        self.assertEqual(convert_to_roman(4), "IV")

    def test_4(self):
        self.assertEqual(convert_to_roman(5), "V")

    def test_5(self):
        self.assertEqual(convert_to_roman(9), "IX")

    def test_6(self):
        self.assertEqual(convert_to_roman(12), "XII")

    def test_7(self):
        self.assertEqual(convert_to_roman(16), "XVI")

    def test_8(self):
        self.assertEqual(convert_to_roman(29), "XXIX")

    def test_9(self):
        self.assertEqual(convert_to_roman(44), "XLIV")

    def test_10(self):
        self.assertEqual(convert_to_roman(45), "XLV")

    def test_11(self):
        self.assertEqual(convert_to_roman(68), "LXVIII")

    def test_12(self):
        self.assertEqual(convert_to_roman(83), "LXXXIII")

    def test_13(self):
        self.assertEqual(convert_to_roman(97), "XCVII")

    def test_14(self):
        self.assertEqual(convert_to_roman(99), "XCIX")

    def test_15(self):
        self.assertEqual(convert_to_roman(500), "D")

    def test_16(self):
        self.assertEqual(convert_to_roman(501), "DI")

    def test_17(self):
        self.assertEqual(convert_to_roman(649), "DCXLIX")

    def test_18(self):
        self.assertEqual(convert_to_roman(798), "DCCXCVIII")

    def test_19(self):
        self.assertEqual(convert_to_roman(891), "DCCCXCI")

    def test_20(self):
        self.assertEqual(convert_to_roman(1000), "M")

    def test_21(self):
        self.assertEqual(convert_to_roman(1004), "MIV")

    def test_22(self):
        self.assertEqual(convert_to_roman(1006), "MVI")

    def test_23(self):
        self.assertEqual(convert_to_roman(1023), "MXXIII")

    def test_24(self):
        self.assertEqual(convert_to_roman(2014), "MMXIV")

    def test_25(self):
        self.assertEqual(convert_to_roman(3999), "MMMCMXCIX")


class Test_Convert_To_Roman_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(convert_to_roman_2(2), "II")

    def test_2(self):
        self.assertEqual(convert_to_roman_2(3), "III")

    def test_3(self):
        self.assertEqual(convert_to_roman_2(4), "IV")

    def test_4(self):
        self.assertEqual(convert_to_roman_2(5), "V")

    def test_5(self):
        self.assertEqual(convert_to_roman_2(9), "IX")

    def test_6(self):
        self.assertEqual(convert_to_roman_2(12), "XII")

    def test_7(self):
        self.assertEqual(convert_to_roman_2(16), "XVI")

    def test_8(self):
        self.assertEqual(convert_to_roman_2(29), "XXIX")

    def test_9(self):
        self.assertEqual(convert_to_roman_2(44), "XLIV")

    def test_10(self):
        self.assertEqual(convert_to_roman_2(45), "XLV")

    def test_11(self):
        self.assertEqual(convert_to_roman_2(68), "LXVIII")

    def test_12(self):
        self.assertEqual(convert_to_roman_2(83), "LXXXIII")

    def test_13(self):
        self.assertEqual(convert_to_roman_2(97), "XCVII")

    def test_14(self):
        self.assertEqual(convert_to_roman_2(99), "XCIX")

    def test_15(self):
        self.assertEqual(convert_to_roman_2(500), "D")

    def test_16(self):
        self.assertEqual(convert_to_roman_2(501), "DI")

    def test_17(self):
        self.assertEqual(convert_to_roman_2(649), "DCXLIX")

    def test_18(self):
        self.assertEqual(convert_to_roman_2(798), "DCCXCVIII")

    def test_19(self):
        self.assertEqual(convert_to_roman_2(891), "DCCCXCI")

    def test_20(self):
        self.assertEqual(convert_to_roman_2(1000), "M")

    def test_21(self):
        self.assertEqual(convert_to_roman_2(1004), "MIV")

    def test_22(self):
        self.assertEqual(convert_to_roman_2(1006), "MVI")

    def test_23(self):
        self.assertEqual(convert_to_roman_2(1023), "MXXIII")

    def test_24(self):
        self.assertEqual(convert_to_roman_2(2014), "MMXIV")

    def test_25(self):
        self.assertEqual(convert_to_roman_2(3999), "MMMCMXCIX")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
