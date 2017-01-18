# ----------------------------------
# Pig Latin
# ----------------------------------
# Translate the provided string to Pig Latin.
#
# Pig Latin takes the first consonant (or consonant cluster) of an English word,
# moves it to the end of the word and suffixes an "ay".
#
# If a word begins with a vowel you just add "way" to the end.
#
# Input strings are guaranteed to be English words in all lowercase.
# ----------------------------------

import unittest

def pig_latin(strg):
    return strg


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Pig_Latin(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pig_latin("california"), "aliforniacay")

    def test_2(self):
        self.assertEqual(pig_latin("paragraphs"), "aragraphspay")

    def test_3(self):
        self.assertEqual(pig_latin("glove"), "oveglay")

    def test_4(self):
        self.assertEqual(pig_latin("algorithm"), "algorithmway")

    def test_5(self):
        self.assertEqual(pig_latin("eight"), "eightway")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
