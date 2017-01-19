# ----------------------------------
# Boo Who
# ----------------------------------
# Check if a value is classified as a boolean primative. Return True or False.
#
# Boolean primatives are True and False.
# ----------------------------------

import unittest

def boo_who(boolean):
    return boolean


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Boo_Who(unittest.TestCase):
    def test_1(self):
        self.assertEqual(boo_who(True), True)

    def test_2(self):
        self.assertEqual(boo_who(False), True)

    def test_3(self):
        self.assertEqual(boo_who([1, 2, 3]), False)

    def test_4(self):
        self.assertEqual(boo_who([]), False)

    def test_5(self):
        self.assertEqual(boo_who({ "a": 1 }), False)

    def test_6(self):
        self.assertEqual(boo_who(1), False)

    def test_7(self):
        self.assertEqual(boo_who(None), False)

    def test_8(self):
        self.assertEqual(boo_who("a"), False)

    def test_9(self):
        self.assertEqual(boo_who("true"), False)

    def test_10(self):
        self.assertEqual(boo_who("false"), False)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
