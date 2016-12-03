# Find the Longest Word in a String
# --------------------------------------
# Return the length of the longest word in the provided sentence.
#
# Your response should be a number.
# --------------------------------------
import unittest


def find_longest_word(str):
    return len(str)


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



# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == '__main__':
    unittest.main()
