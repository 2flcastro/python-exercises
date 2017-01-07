# ----------------------------------
# Confirm The Ending
# ----------------------------------
# Check if a string (first argument "str") ends with the given target string
# (second argument "traget").
# ----------------------------------

import unittest

def confirm_ending(str, target):
    return True



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


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
