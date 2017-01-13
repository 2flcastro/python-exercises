# ----------------------------------
# Confirm The Ending
# ----------------------------------
# Check if a string (first argument "str") ends with the given target string
# (second argument "traget").
# ----------------------------------

import unittest

# using endswith() list method
def confirm_ending(strg, target):
    return strg.endswith(target)


# using list slice
def confirm_ending_2(strg, target):
    return strg[len(strg) - len(target):] == target


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Confirm_Ending(unittest.TestCase):
    def test_1(self):
        self.assertEqual(confirm_ending("Bastian", "n"), True)

    def test_2(self):
        self.assertEqual(confirm_ending("Connor", "n"), False)

    def test_3(self):
        self.assertEqual(confirm_ending("Walking on water and developing software from a specification are easy if both are frozen", "specification"), False)

    def test_4(self):
        self.assertEqual(confirm_ending("He has to give me a new name", "name"), True)

    def test_5(self):
        self.assertEqual(confirm_ending("Open sesame", "same"), True)

    def test_6(self):
        self.assertEqual(confirm_ending("Open sesame", "pen"), False)

    def test_7(self):
        self.assertEqual(confirm_ending("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain"), False)


class Test_Confirm_Ending_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(confirm_ending_2("Bastian", "n"), True)

    def test_2(self):
        self.assertEqual(confirm_ending_2("Connor", "n"), False)

    def test_3(self):
        self.assertEqual(confirm_ending_2("Walking on water and developing software from a specification are easy if both are frozen", "specification"), False)

    def test_4(self):
        self.assertEqual(confirm_ending_2("He has to give me a new name", "name"), True)

    def test_5(self):
        self.assertEqual(confirm_ending_2("Open sesame", "same"), True)

    def test_6(self):
        self.assertEqual(confirm_ending_2("Open sesame", "pen"), False)

    def test_7(self):
        self.assertEqual(confirm_ending_2("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain"), False)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
