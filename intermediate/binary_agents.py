# ----------------------------------
# Binary Agents
# ----------------------------------
# Return an English translated sentence of the passed binary string.
#
# The binary string will be space seperated.
#
# Hint: use the built-it Python functions chr(), ord(), int()
# ----------------------------------

import unittest

def binary_agent(sentence):
    return sentence


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Binary_Agents(unittest.TestCase):
    def test_1(self):
        self.assertEqual(binary_agent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"), "Aren't bonfires fun!?")

    def test_2(self):
        self.assertEqual(binary_agent(("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001"), "I love FreeCodeCamp!")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
