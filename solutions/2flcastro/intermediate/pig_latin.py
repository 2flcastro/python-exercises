# ----------------------------------
# Pig Latin
# ----------------------------------
# Translate the provided string to pig latin.
#
# Pig Latin takes the first consonant (or consonant cluster) of an English word,
# moves it to the end of the word and suffixes an "ay".
#
# If a word begins with a vowel you just add "way" to the end.
#
# Input strings are guaranteed to be English words in all lowercase.
# ----------------------------------

import unittest

# using while-loop and str slice
def pig_latin(strg):
    vowels = ["a", "e", "i", "o", "u"]
    if strg[0] in vowels:
        return strg + "way"
    while not strg[0] in vowels:
        strg = strg[1:] + strg[0]
    return strg + "ay"


# using for-loop and if-elif-else
def pig_latin_2(strg):
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(strg)):
        if i == 0 and strg[0] in vowels:
            return strg + "way"
        elif strg[0] in vowels:
            return strg + "ay"
        else:
            strg = strg[1:] + strg[0]


# using if-else and while-loop
def pig_latin_3(strg):
    vowels = ["a", "e", "i", "o", "u"]
    if strg[0] in vowels:
        return strg + 'way'
    else:
        strg = list(strg)
        consonant_check = True
        while consonant_check:
            if not strg[0] in vowels:
                strg.append(strg.pop(0))
            else:
                consonant_check = False
        return ''.join(strg) + 'ay'


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


class Test_Pig_Latin_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pig_latin_2("california"), "aliforniacay")

    def test_2(self):
        self.assertEqual(pig_latin_2("paragraphs"), "aragraphspay")

    def test_3(self):
        self.assertEqual(pig_latin_2("glove"), "oveglay")

    def test_4(self):
        self.assertEqual(pig_latin_2("algorithm"), "algorithmway")

    def test_5(self):
        self.assertEqual(pig_latin_2("eight"), "eightway")


class Test_Pig_Latin_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pig_latin_3("california"), "aliforniacay")

    def test_2(self):
        self.assertEqual(pig_latin_3("paragraphs"), "aragraphspay")

    def test_3(self):
        self.assertEqual(pig_latin_3("glove"), "oveglay")

    def test_4(self):
        self.assertEqual(pig_latin_3("algorithm"), "algorithmway")

    def test_5(self):
        self.assertEqual(pig_latin_3("eight"), "eightway")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
