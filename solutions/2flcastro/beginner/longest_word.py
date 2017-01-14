# ----------------------------------
# Find the Longest Word in a String
# ----------------------------------
# Return the length of the longest word in the provided sentence.
#
# Your response should be a number.
# ----------------------------------

import unittest

# using list comprehension and max() built-in function
def find_longest_word(strg):
    words = strg.split()
    return max([len(word) for word in words])


# using split() and a for-loop
def find_longest_word_2(strg):
    sentence = strg.split()
    longest_word =  len(strg[0])
    for word in sentence:
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Find_Longest_Word(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_longest_word('The quick brown fox jumped over the lazy dog'), 6)

    def test_2(self):
        self.assertEqual(find_longest_word('May the force be with you'), 5)

    def test_3(self):
        self.assertEqual(find_longest_word('Google do a barrel roll'), 6)

    def test_4(self):
        self.assertEqual(find_longest_word('What is the average airspeed velocity of an unladen swallow'), 8)

    def test_5(self):
        self.assertEqual(find_longest_word('What if we try a super-long word such as otorhinolaryngology'), 19)


class Test_Find_Longest_Word_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_longest_word_2('The quick brown fox jumped over the lazy dog'), 6)

    def test_2(self):
        self.assertEqual(find_longest_word_2('May the force be with you'), 5)

    def test_3(self):
        self.assertEqual(find_longest_word_2('Google do a barrel roll'), 6)

    def test_4(self):
        self.assertEqual(find_longest_word_2('What is the average airspeed velocity of an unladen swallow'), 8)

    def test_5(self):
        self.assertEqual(find_longest_word_2('What if we try a super-long word such as otorhinolaryngology'), 19)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == '__main__':
    unittest.main()
