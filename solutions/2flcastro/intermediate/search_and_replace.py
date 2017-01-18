# ----------------------------------
# Search and Replace
# ----------------------------------
# Perform a search and replace on the sentence using the arguments provided
# and return the new sentence.
#
# First argument is the sentence to perform the search and replace on. Second
# argument is the word that you will be replacing. Third argument is what you
# will be replacing the second argument with.
#
# Note: preserve the case of the orgininal word you are replacing. For example,
# if you mean to replace the word "Book" with "dog", it should be replaced
# as dog.
# ----------------------------------

import unittest
import re

# using islower(), capitalize(), and replace() str methods and conditional expression
def replace(sentence, before, after):
    return sentence.replace(before, after.capitalize() if not before.islower() else after)


# using regular expressions and unicode check for capital letters
def replace_2(sentence, before, after):
    if ord(before[0]) > 64 and ord(before[0]) < 91:
        return re.sub(before, after.capitalize(), sentence)
    return re.sub(before, after, sentence)


# using while-loop and find()
def replace_3(sentence, before, after):
    while sentence.find(before) > -1:
        if not before.islower():
            after = after.capitalize()
        sentence = sentence.replace(before, after)
    return sentence


# splitting into list and iterating through it
def replace_4(sentence, before, after):
    sentence = sentence.split()
    for i, word in enumerate(sentence):
        if word == before and not word.islower():
            sentence.pop(i)
            sentence.insert(i, after.capitalize())
        elif word == before:
            sentence.pop(i)
            sentence.insert(i, after)
    return ' '.join(sentence)


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Replace(unittest.TestCase):
    def test_1(self):
        self.assertEqual(replace("Let us go to the store", "store", "mall"), "Let us go to the mall")

    def test_2(self):
        self.assertEqual(replace("He is Sleeping on the couch", "Sleeping", "sitting"), "He is Sitting on the couch")

    def test_3(self):
        self.assertEqual(replace("This has a spellngi error", "spellngi", "spelling"), "This has a spelling error")

    def test_4(self):
        self.assertEqual(replace("His name is Tom", "Tom", "john"), "His name is John")

    def test_5(self):
        self.assertEqual(replace("Let us get back to more Coding", "Coding", "algorithms"), "Let us get back to more Algorithms")


class Test_Replace_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(replace_2("Let us go to the store", "store", "mall"), "Let us go to the mall")

    def test_2(self):
        self.assertEqual(replace_2("He is Sleeping on the couch", "Sleeping", "sitting"), "He is Sitting on the couch")

    def test_3(self):
        self.assertEqual(replace_2("This has a spellngi error", "spellngi", "spelling"), "This has a spelling error")

    def test_4(self):
        self.assertEqual(replace_2("His name is Tom", "Tom", "john"), "His name is John")

    def test_5(self):
        self.assertEqual(replace_2("Let us get back to more Coding", "Coding", "algorithms"), "Let us get back to more Algorithms")


class Test_Replace_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(replace_3("Let us go to the store", "store", "mall"), "Let us go to the mall")

    def test_2(self):
        self.assertEqual(replace_3("He is Sleeping on the couch", "Sleeping", "sitting"), "He is Sitting on the couch")

    def test_3(self):
        self.assertEqual(replace_3("This has a spellngi error", "spellngi", "spelling"), "This has a spelling error")

    def test_4(self):
        self.assertEqual(replace_3("His name is Tom", "Tom", "john"), "His name is John")

    def test_5(self):
        self.assertEqual(replace_3("Let us get back to more Coding", "Coding", "algorithms"), "Let us get back to more Algorithms")


class Test_Replace_4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(replace_4("Let us go to the store", "store", "mall"), "Let us go to the mall")

    def test_2(self):
        self.assertEqual(replace_4("He is Sleeping on the couch", "Sleeping", "sitting"), "He is Sitting on the couch")

    def test_3(self):
        self.assertEqual(replace_4("This has a spellngi error", "spellngi", "spelling"), "This has a spelling error")

    def test_4(self):
        self.assertEqual(replace_4("His name is Tom", "Tom", "john"), "His name is John")

    def test_5(self):
        self.assertEqual(replace_4("Let us get back to more Coding", "Coding", "algorithms"), "Let us get back to more Algorithms")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
