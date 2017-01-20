# ----------------------------------
# Spinal Tap Case
# ----------------------------------
# Convert a string to spinal case.
#
# Spinal case is all-lower-case-words-joined-by-dashes
# ----------------------------------

import unittest
import re

# using two rounds of regex
def spinal_case(sentence):
    sentence = re.sub('[[a-z](?=[A-Z])', lambda match: match.group(0) + "-", sentence)
    sentence = re.sub('[_\s]|[\s+]', '-', sentence)
    return sentence.lower()


# using regular expressions with callback function
def spinal_case_2(sentence):
    def replacement(match):
        if re.match('[a-z]', match.group(0)):
            return match.group(0) + "-"
        else:
            return "-"
    sentence = re.sub('[a-z](?=[A-Z])|[\s_]', replacement, sentence)
    return sentence.lower()


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Spinal_Case(unittest.TestCase):
    def test_1(self):
        self.assertEqual(spinal_case("This Is Spinal Tap"), "this-is-spinal-tap")

    def test_2(self):
        self.assertEqual(spinal_case("thisIsSpinalTap"), "this-is-spinal-tap")

    def test_3(self):
        self.assertEqual(spinal_case("The_Andy_Griffith_Show"), "the-andy-griffith-show")

    def test_4(self):
        self.assertEqual(spinal_case("Teletubbies say Eh-oh"), "teletubbies-say-eh-oh")

    def test_5(self):
        self.assertEqual(spinal_case("AllThe-small Things"), "all-the-small-things")


class Test_Spinal_Case_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(spinal_case_2("This Is Spinal Tap"), "this-is-spinal-tap")

    def test_2(self):
        self.assertEqual(spinal_case_2("thisIsSpinalTap"), "this-is-spinal-tap")

    def test_3(self):
        self.assertEqual(spinal_case_2("The_Andy_Griffith_Show"), "the-andy-griffith-show")

    def test_4(self):
        self.assertEqual(spinal_case_2("Teletubbies say Eh-oh"), "teletubbies-say-eh-oh")

    def test_5(self):
        self.assertEqual(spinal_case_2("AllThe-small Things"), "all-the-small-things")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
