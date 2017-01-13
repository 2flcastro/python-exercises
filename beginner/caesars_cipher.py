# ----------------------------------
# Caesars Cipher
# ----------------------------------
# One of the most simplest and most widely known "ciphers" is a "Caesar Cipher",
# also known as a "shift cipher". In a shift cipher the meaning of the letters
# are shifted by some amount.
#
# A common modern use is the ROT13 cipher, where the values of the letters argument
# shifted by 13 places. Thus "A" <=> "N", "B" <=> "O" and so on.
# https://en.wikipedia.org/wiki/ROT13
#
# Write a function that takes a ROT13 encoded string as input and returns a
# decoded string.
#
# All letters will be uppercase. Do not transform any non-alphabetic character
# (i.e. spaces, punctuations), but do pass them on.
#
# Tip: You might find the Python built-in functions chr() and ord() useful for
# this exercise:
# https://docs.python.org/3.4/library/functions.html
# ----------------------------------

import unittest

def rot13(strg):
    return decoded_strg



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Rot13(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rot13("SERR PBQR PNZC"), "FREE CODE CAMP")

    def test_2(self):
        self.assertEqual(rot13("SERR CVMMN!"), "FREE PIZZA!")

    def test_3(self):
        self.assertEqual(rot13("SERR YBIR?"), "FREE LOVE?")

    def test_4(self):
        self.assertEqual(rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."), "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
