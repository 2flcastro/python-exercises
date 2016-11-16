# Unit Tests: Reverse A String
# --------------------------------
import sys
sys.path.append(sys.path[0] + '/../../beginner')

import unittest
from reverseString import reverseString

# Unit Tests
class TestReverseString(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseString('hello'), 'olleh')

    def test_2(self):
        self.assertEqual(reverseString('Howdy'), 'ydwoH')

    def test_3(self):
        self.assertEqual(reverseString('Greetings from Earth'),
            'htraE morf sgniteerG')

#Run tests
if __name__ == '__main__':
    unittest.main()
