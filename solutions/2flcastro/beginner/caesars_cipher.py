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
# ----------------------------------

import unittest
import re

# using regular expression with re.sub() method
def rot13_3(message):
    def replace_fx(match_letter):
        return chr(65 + (ord(match_letter.group(0)) - 65 - 13) % 26)
    return re.sub('[A-Z]', replace_fx, message)


# using regular expressions and nested if-else statements
def rot13_2(message):
    decoded_message = ''
    for letter in message:
        # unicode int representing letter
        letter_code = ord(letter)
        # check if letter is alphabetical
        if re.match('[A-Z]', letter):
            if letter_code - 13 < 65:
                replacement = chr(letter_code + 13)
            else:
                replacement = chr(letter_code - 13)
            decoded_message += replacement
        else:
            decoded_message += letter
    return decoded_message


# using if-else statements and calculating "displacement" of letter manually
def rot13(message):
    decoded_message = ''
    for letter in message:
        letter_code = ord(letter)
        # check if letter is between "A" and "Z" based on unicode integer
        if letter_code > 64 and letter_code < 91:
            # check if letter is displaced beyond the letter "A", if so, retoate back from "Z"
            if letter_code - 13 < 65:
                # find displacement from "Z"
                displacement = 65 - (letter_code - 13)
                decoded_message += chr(91 - displacement)
            else:
                decoded_message += chr(letter_code - 13)
        # if letter is non-alpha, don't convert
        else:
            decoded_message += letter
    return decoded_message


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


class Test_Rot13_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rot13_2("SERR PBQR PNZC"), "FREE CODE CAMP")

    def test_2(self):
        self.assertEqual(rot13_2("SERR CVMMN!"), "FREE PIZZA!")

    def test_3(self):
        self.assertEqual(rot13_2("SERR YBIR?"), "FREE LOVE?")

    def test_4(self):
        self.assertEqual(rot13_2("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."), "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.")


class Test_Rot13_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rot13_3("SERR PBQR PNZC"), "FREE CODE CAMP")

    def test_2(self):
        self.assertEqual(rot13_3("SERR CVMMN!"), "FREE PIZZA!")

    def test_3(self):
        self.assertEqual(rot13_3("SERR YBIR?"), "FREE LOVE?")

    def test_4(self):
        self.assertEqual(rot13_3("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."), "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
