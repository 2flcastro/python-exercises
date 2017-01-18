# ----------------------------------
# Mutations
# ----------------------------------
# Return true if the string in the first element of the list contains all of
# the letters of the string in the second element of the list.
#
# For example, ["hello", "Hello"] should return True because of the letter in
# the second string are present in the first, ignoring case.
#
# The arguments ["hello", "hey"] should return False because the string "hello"
# does not contain a "y".
#
# Lastly, ["Alien", "line"] should return True because all of the letters in
# "line" are present in "Alien".
# ----------------------------------

import unittest

def mutations(lst):
    return True


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Mutations(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mutations(["hello", "hey"]), False)

    def test_2(self):
        self.assertEqual(mutations(["hello", "Hello"]), True)

    def test_3(self):
        self.assertEqual(mutations(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]), True)

    def test_4(self):
        self.assertEqual(mutations(["Mary", "Army"]), True)

    def test_5(self):
        self.assertEqual(mutations(["Mary", "Aarmy"]), True)

    def test_6(self):
        self.assertEqual(mutations(["Alien", "line"]), True)

    def test_7(self):
        self.assertEqual(mutations(["floor", "for"]), True)

    def test_8(self):
        self.assertEqual(mutations(["hello", "neo"]), False)

    def test_9(self):
        self.assertEqual(mutations(["voodoo", "no"]), False)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
