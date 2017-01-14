# ----------------------------------
# Title Case a Sentence
# ----------------------------------
# Return the provided string with the first letter of each word capitalized.
# Make sure the rest of the words are in lower case.
#
# For the purposes of this exercise, you should also capitalize connecting words
# like  "the" or "of".
# ----------------------------------

import unittest

# using list comprehension and list.capitalize()
def title_case(sentence):
    words = sentence.split()
    words = [word.lower().capitalize() for word in words]
    return ' '.join(words)


# using for-loop and str.capitalize()
def title_case_2(sentence):
    words = sentence.split()
    for i, word in enumerate(words):
        word = word.lower()
        words[i] = word.capitalize()
    sentence = ' '.join(words)
    return sentence



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Title_Case(unittest.TestCase):
    def test_1(self):
        self.assertEqual(title_case("I'm a little tea pot"), "I'm A Little Tea Pot")

    def test_2(self):
        self.assertEqual(title_case("sHoRt AnD sToUt"), "Short And Stout")

    def test_3(self):
        self.assertEqual(title_case("HERE IS MY HANDLE HERE IS MY SPOUT"), "Here Is My Handle Here Is My Spout")


class Test_Title_Case_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(title_case_2("I'm a little tea pot"), "I'm A Little Tea Pot")

    def test_2(self):
        self.assertEqual(title_case_2("sHoRt AnD sToUt"), "Short And Stout")

    def test_3(self):
        self.assertEqual(title_case_2("HERE IS MY HANDLE HERE IS MY SPOUT"), "Here Is My Handle Here Is My Spout")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
