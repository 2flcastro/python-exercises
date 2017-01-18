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

# using list comprehension
def dna_pairing(dna_strand):
    pairs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    pair_lst = list(dna_strand)
    pair_lst = [[strand, pairs[strand]] for strand in pair_lst]
    return pair_lst


# using forl-loop
def dna_pairing_2(dna_strand):
    pairs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    pair_lst = []
    for element in dna_strand:
        pair_lst.append([element, pairs[element]])
    return pair_lst


# using two lists and index
def dna_pairing_3(dna_strand):
    pair_1 = ["A", "T", "C", "G"]
    pair_2 = ["T", "A", "G", "C"]
    pair_lst = []
    for i, strand in enumerate(dna_strand):
        index = pair_1.index(strand)
        pair_lst.append([pair_1[index], pair_2[index]])
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


class Test_Dna_Pair_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dna_pairing_2("ATCGA"), [["A","T"],["T","A"],["C","G"],["G","C"],["A","T"]])

    def test_2(self):
        self.assertEqual(dna_pairing_2("TTGAG"), [["T","A"],["T","A"],["G","C"],["A","T"],["G","C"]])

    def test_3(self):
        self.assertEqual(dna_pairing_2("CTCTA"), [["C","G"],["T","A"],["C","G"],["T","A"],["A","T"]])


class Test_Dna_Pair_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dna_pairing_3("ATCGA"), [["A","T"],["T","A"],["C","G"],["G","C"],["A","T"]])

    def test_2(self):
        self.assertEqual(dna_pairing_3("TTGAG"), [["T","A"],["T","A"],["G","C"],["A","T"],["G","C"]])

    def test_3(self):
        self.assertEqual(dna_pairing_3("CTCTA"), [["C","G"],["T","A"],["C","G"],["T","A"],["A","T"]])

# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
