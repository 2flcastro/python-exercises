# ----------------------------------
# Smallest Commom Multiple
# ----------------------------------
# Find the smallest common multiple of the provided parameters that can be
# evenly divided by both, as well as by all sequential numbers in the range
# between these parameters.
#
# The range will be a list of two numbers that will not necessarily be in
# numerical order.
#
# e.g. for 1 and 3, find the lowest common multiple of both 1 and 3 that is
# evenly divisible by all numbers BETWEEN 1 and 3.
#
# Helpful Links:
# - https://www.mathsisfun.com/least-common-multiple.html
# - https://www.artofproblemsolving.com/wiki/index.php/Least_common_multiple
# ----------------------------------

import unittest

# Using a while loop to test multiples of the largest number in list,
# incrementing the largest value on itself until it reaches a value all numbers
# in the range can evenly divide into.
def smallest_common(lst):
    lst.sort()
    largest_num = lst[len(lst) - 1]
    scm = largest_num
    while True:
        for number in range(lst[0], largest_num + 1):
            if scm % number != 0:
                scm += largest_num
                break
        else:
            # break out of the while-loop if scm found
            break
    return scm



# There is another formula for find the SCM of a pair of numbers:
#   LCM(a, b) = a * b / GCD(a, b)
# You first need to find the GCD (greatest common divisor), which is done Using
# the Euclidean Algorithm (euclidean_gcd() function).
def smallest_common_2(lst):
    def euclidean_gcd(a, b):
        if b == 0:
            return a
        else:
            return euclidean_gcd(b, a%b)

    lst.sort()
    scm = lst[0]
    for i in range(lst[0] + 1, lst[len(lst) - 1] + 1):
        scm = scm * i / euclidean_gcd(scm, i)
    return scm


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Smallest_Common(unittest.TestCase):
    def test_1(self):
        self.assertEqual(smallest_common([1, 5]), 60)

    def test_2(self):
        self.assertEqual(smallest_common([5, 1]), 60)

    def test_3(self):
        self.assertEqual(smallest_common([1, 13]), 360360)

    def test_4(self):
        self.assertEqual(smallest_common([23, 18]), 6056820)


class Test_Smallest_Common_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(smallest_common_2([1, 5]), 60)

    def test_2(self):
        self.assertEqual(smallest_common_2([5, 1]), 60)

    def test_3(self):
        self.assertEqual(smallest_common_2([1, 13]), 360360)

    def test_4(self):
        self.assertEqual(smallest_common_2([23, 18]), 6056820)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
