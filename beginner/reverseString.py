# Reverse A String:
# --------------------
# Reverse the provided string. Your result must be a string.
# Try to find alternative methods for the 'slice [::]' notation used on strings.
# ----------------------------------
import unittest

def reverseString(str):
    # your code goes here...
    return str[::-1]



# ----------------------------------
# Unit Tests
class TestReverseString(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseString('hello'), 'olleh')

    def test_2(self):
        self.assertEqual(reverseString('Howdy'), 'ydwoH')

    def test_3(self):
        self.assertEqual(reverseString('Greetings from Earth'),
            'htraE morf sgniteerG')

# Run tests
if __name__ == '__main__':
    unittest.main()
>>>>>>> 637c1d90f6ee657b7ba3459a22b2eba6bdbf4fdf
