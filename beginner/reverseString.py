# ----------------------------------
# Reverse A String:
# ----------------------------------
# Reverse the provided string. Your result must be a string.
# Try to find alternative methods for the 'slice [::]' notation used on strings.
# ----------------------------------

import unittest

def reverseString(str):
    # your code goes here...
    return str[::-1]

def reverseString2(str):
    new_str = ""
    index = len(str) -1
    while index >= 0:
        new_str += str[index]
        index -= 1
    return new_str

# ----------------------------------
# Unit Tests
# ----------------------------------
class TestReverseString(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseString('hello'), 'olleh')

    def test_2(self):
        self.assertEqual(reverseString('Howdy'), 'ydwoH')

    def test_3(self):
        self.assertEqual(reverseString('Greetings from Earth'),
            'htraE morf sgniteerG')


class TestReverseString2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseString2('hello'), 'olleh')

    def test_2(self):
        self.assertEqual(reverseString2('Howdy'), 'ydwoH')


# ----------------------------------

# Run tests
# ----------------------------------
if __name__ == '__main__':
    unittest.main()
