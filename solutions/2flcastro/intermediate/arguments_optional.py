# ----------------------------------
# Arguments Optional
# ----------------------------------
# Create a function that sums up two arguments together. If only one argument is
# provided, then return a function that expects one argument and returns the
# sum.
#
# For example, add_together(2, 3) should return 5, and add_together(2) should
# return a function. Calling this returned function with a single argument will
# return the sum: add_together(2)(3) = 5
#
# If either argument is not a valid number, return None.
#
# Hint: Python closures and positional arguments might come in handy.
# ----------------------------------

import unittest

def add_together(num, *args):
    if not len(args) and type(num) == int:
        def add_to(arg):
            return num + arg if type(arg) == int else None
        # return closure add_to()
        return add_to

    return num + args[0] if len(args) and type(args[0]) == int else None


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Add_Together(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add_together(2, 3), 5)

    def test_2(self):
        self.assertEqual(add_together(2)(3), 5)

    def test_3(self):
        self.assertEqual(add_together("http://bit.ly/IqT6zt"), None)

    def test_4(self):
        self.assertEqual(add_together(2, "3"), None)

    def test_5(self):
        self.assertEqual(add_together(2)([3]), None)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
