# ----------------------------------
# Truncate a String
# ----------------------------------
# Truncate a string (first argument) if it is longer than the given maximum
# string length (second argument). Return the truncated string with a "..."
# ending.
#
# Note that inserting the three dots to the end will to their string length.
#
# However, if the given maximum string length "num" is less than or equal to 3,
# then the addition of the three dots does does not add to the string length in
# determining the truncated string.
# ----------------------------------

import unittest

def truncate_string(strg, num):
    return strg



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Truncate_String(unittest.TestCase):
    def test_1(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", 11), "A-tisket...")

    def test_2(self):
        self.assertEqual(truncate_string("Peter Piper picked a peck of pickled peppers", 14), "Peter Piper...")

    def test_3(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket")), "A-tisket a-tasket A green and yellow basket")

    def test_4(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket") + 2) , "A-tisket a-tasket A green and yellow basket")

    def test_5(self):
        self.assertEqual(truncate_string("A-", 1), "A...")

    def test_6(self):
        self.assertEqual(truncate_string("Absolutely Longer", 2), "Ab...")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
