# ----------------------------------
# Largest Numbers in List
# ----------------------------------
# Return a list consisting of the largest number from each provided sub-list.
# For simplicity, the provided list will contain exactly 4 sub-lists.
# ----------------------------------

import unittest

# using list comprehensions
def largest_of_four(lsts):
    return [max(lst) for lst in lsts]


# looping through each list and its numbers
def largest_of_four_2(lsts):
    largest_lst = []
    for lst in lsts:
        largest_num = lst[0]
        for number in lst:
            if number > largest_num:
                largest_num = number
        largest_lst.append(largest_num)
    return largest_lst



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Largest_Of_Four(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_of_four([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]), [27,5,39,1001])

    def test_2(self):
        self.assertEqual(largest_of_four([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]), [9, 35, 97, 1000000])


class Test_Largest_Of_Four_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_of_four_2([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]), [27,5,39,1001])

    def test_2(self):
        self.assertEqual(largest_of_four_2([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]), [9, 35, 97, 1000000])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
