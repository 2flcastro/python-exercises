# ----------------------------------
# Steam Roller
# ----------------------------------
# Flatten a nested list. You must account for varying levels of nesting.
# ----------------------------------

import unittest

def steam_roll(lst):
    return lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Steam_Roll(unittest.TestCase):
    def test_1(self):
        self.assertEqual(steam_roll([[["a"]], [["b"]]]), ["a", "b"])

    def test_2(self):
        self.assertEqual(steam_roll([1, [2], [3, [[4]]]]), [1, 2, 3, 4])

    def test_3(self):
        self.assertEqual(steam_roll([1, [], [3, [[4]]]]), [1, 3, 4])

    def test_4(self):
        self.assertEqual(steam_roll([1, {}, [3, [[4]]]]), [1, {}, 3, 4])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
