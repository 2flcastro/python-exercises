# ----------------------------------
# Convert HTML Entities
# ----------------------------------
# Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a
# string to their corresponding HTML entities.
#
# Useful Links:
# - HTML Entities: https://dev.w3.org/html5/html-author/charref
# - Python RegEx: https://docs.python.org/3/library/re.html#module-re
# ----------------------------------

import unittest
import re

# using regular expressions
def html_converter(sentence):
    html_chars = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;"
    }

    def substitute(match):
        return html_chars[match.group(0)]

    return re.sub('[&<>"\']', substitute, sentence)


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Html_Converter(unittest.TestCase):
    def test_1(self):
        self.assertEqual(html_converter("Dolce & Gabbana"), "Dolce &amp; Gabbana")

    def test_2(self):
        self.assertEqual(html_converter("Hamburgers < Pizza < Tacos"), "Hamburgers &lt; Pizza &lt; Tacos")

    def test_3(self):
        self.assertEqual(html_converter("Sixty > twelve"), "Sixty &gt; twelve")

    def test_4(self):
        self.assertEqual(html_converter('Stuff in "quotation marks"'), "Stuff in &quot;quotation marks&quot;")

    def test_5(self):
        self.assertEqual(html_converter("Shindler's List"), "Shindler&apos;s List")

    def test_6(self):
        self.assertEqual(html_converter("<>"), "&lt;&gt;")

    def test_7(self):
        self.assertEqual(html_converter("abc"), "abc")


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
