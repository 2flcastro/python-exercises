# ----------------------------------
# Reverse A String:
# ----------------------------------
# Reverse the provided string. Your result must be a string.
# Try to find alternative methods for the 'slice [::]' notation used on strings.
# ----------------------------------

import unittest

def reverseString(str):
    return str[::-1]


def reverseString_2(str):
    str = list(str)
    str.reverse()
    return ''.join(str)


def reverseString_3(str):
    reverseStr = []
    for letter in str:
        reverseStr.insert(0, letter)
    return ''.join(reverseStr)

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


class TestReverseString_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseString_2('hello'), 'olleh')

    def test_2(self):
        self.assertEqual(reverseString_2('Howdy'), 'ydwoH')

    def test_3(self):
        self.assertEqual(reverseString_2('Greetings from Earth'),
            'htraE morf sgniteerG')


class TestReverseString_3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseString_3('hello'), 'olleh')

    def test_2(self):
        self.assertEqual(reverseString_3('Howdy'), 'ydwoH')

    def test_3(self):
        self.assertEqual(reverseString_3('Greetings from Earth'),
            'htraE morf sgniteerG')

# ----------------------------------
# Run tests
# ----------------------------------
if __name__ == '__main__':
    unittest.main()
