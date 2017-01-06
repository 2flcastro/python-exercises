# ----------------------------------
# Largest Numbers in Arrays
# ----------------------------------
# Return an array consisting of the largest number from each provided sub-array.
# For simplicity, the provided array will contain exactly 4 sub-arrays.
# ----------------------------------
import unittest

def largest_of_four(arrs):
    return largest_arr



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Largest_Of_Four(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_of_four([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]), [27,5,39,1001])

    def test_2(self):
        self.assertEqual(largest_of_four([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]), [9, 35, 97, 1000000])

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
