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

def replace(sentence, before, after):
    return sentence


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


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
