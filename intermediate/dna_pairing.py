# ----------------------------------
# DNA Pairing
# ----------------------------------
# The DNA strand is missing the pairing element. Take each character, get items
# pair, and return the results as a 2d list.
#
# Base pairs are a pair of AT or CG. Match the missing element to the provided
# character. Return the provided character as a the first element in each list.
#
# For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]].
#
# The character and its pair are paired up in a list, and all the lists are
# grouped into one encapsulating list.
# ----------------------------------

import unittest

def dna_pair(dna_strand):
    return pair_lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Dna_Pair(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dna_pairing("ATCGA"), [["A","T"],["T","A"],["C","G"],["G","C"],["A","T"]])

    def test_2(self):
        self.assertEqual(dna_pairing("TTGAG"), [["T","A"],["T","A"],["G","C"],["A","T"],["G","C"]])

    def test_3(self):
        self.assertEqual(dna_pairing("CTCTA"), [["C","G"],["T","A"],["C","G"],["T","A"],["A","T"]])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
