# Check for Palindromes
# --------------------------
# Return True if the given string is a palindrome. Otherwise, return False.
#
# A palindrome is a word or sentence that's spelled the same way both forward
# and backward, ignoring punctuation, case, and spelling.
#
# Note: You'll need to remove all non-alphanumeric characters (punctuation,
# spaces, and symbols) and turn everything lower case in order to check for
# palindromes.
#
# We'll pass strings with varying formats, such as "racecar", "RaceCar", and
# "race CAR" among others.
#
# We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2",
# and "2_A3*3#A2".
# ----------------------------------------------------
import unittest

def palindrome(str):
    return True



# ----------------------------------
# Unit Tests
# ----------------------------------
class TestPalindrome(unittest.TestCase):
    def Test_1(self):
        self.assertEqual(palindrome('eye'), True)

    def Test_2(self):
        self.assertEqual(palindrome('_eye'), True)

    def Test_3(self):
        self.assertEqual(palindrome('race car'), True)

    def Test_4(self):
        self.assertEqual(palindrome('not a palindrome'), False)

    def Test_5(self):
        self.assertEqual(palindrome('A man, a plan, a canal. Panama'), True)

    def Test_6(self):
        self.assertEqual(palindrome('never odd or even'), True)

    def Test_7(self):
        self.assertEqual(palindrome('nope'), False)

    def Test_8(self):
        self.assertEqual(palindrome('almostomla'), False)

    def Test_9(self):
        self.assertEqual(palindrome('My age is 0, 0 si ega ym.'), True)

    def Test_10(self):
        self.assertEqual(palindrome('1 eye for of 1 eye'), False)

    def Test_11(self):
        self.assertEqual(palindrome('0_0 (: /-\ :) 0-0'), True)

    def Test_12(self):
        self.assertEqual(palindrome('five|\_/|four'), False)


# Run Tests
if __name__ == "__main__":
    unittest.main()
