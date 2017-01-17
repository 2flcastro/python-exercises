# ----------------------------------
# Roman Numeral Converter
# ----------------------------------
# Convert the given number into a Roman Numeral.
#
# All Roman Numeral answers should be provided in upper-case.
#
# Help link for Roman Numerals refresher:
# http://www.mathsisfun.com/roman-numerals.html
# ----------------------------------

import unittest

def convert_to_roman(original_num):
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


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
