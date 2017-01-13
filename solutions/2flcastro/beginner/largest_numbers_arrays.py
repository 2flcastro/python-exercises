# ----------------------------------
# Largest Numbers in List
# ----------------------------------
# Return a list consisting of the largest number from each provided sub-list.
# For simplicity, the provided list will contain exactly 4 sub-lists.
# ----------------------------------

import unittest

def largest_of_four(arrs):
    largest_arr = []
    for arr in arrs:
        largest_num = arr[0]
        for number in arr:
            if number > largest_num:
                largest_num = number
        largest_arr.append(largest_num)
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
