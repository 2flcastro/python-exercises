# ----------------------------------
# Wherefore Art Thou / Whats in A Name
# ----------------------------------
# Make a function that looks through a list of dictionaries (first argument)
# and returns a list of all dictionaries that have matching property and value
# pairs (second argument). Each property and value pair of the original source
# dictionary has to be present in the dictionary from the collection if it is
# to be included in the returned list.
#
# For example, if the first argument of the function is:
#
#   [{"first": "Romeo", "last": "Montague"}, {"first": "Mercutio", "last": None},
#       {"first": "Tybalt", "last": "Capulet"}]
#
# and the second argument is:
#
#   {"last": "Capulet"}
#
# then you must return the third object from the list (first argument), because
# it contains the property and its value (second argument).
# ----------------------------------

import unittest

# using built-in filter function
def whats_in_a_name(collection, source):
    def collection_filter(item):
        for key in source:
            if (not key in item) or (item[key] != source[key]):
                return False
        return True
    return list(filter(collection_filter, collection))


# using nested for-loops
def whats_in_a_name_2(collection, source):
    match_lst = []
    for item in collection:
        match = True
        for key in source:
            if not key in item or (item[key] != source[key]):
                match = False
                break
        if match:
            match_lst.append(item)
    return match_lst


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Whats_In_A_Name(unittest.TestCase):
    def test_1(self):
        self.assertEqual(whats_in_a_name([{ "first": "Romeo", "last": "Montague" }, { "first": "Mercutio", "last": None }, { "first": "Tybalt", "last": "Capulet" }], { "last": "Capulet" }), [{ "first": "Tybalt", "last": "Capulet" }])

    def test_2(self):
        self.assertEqual(whats_in_a_name([{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }], { "a": 1 }), [{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }])

    def test_3(self):
        self.assertEqual(whats_in_a_name([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "b": 2 }), [{ "a": 1, "b": 2 }, { "a": 1, "b": 2, "c": 2 }])

    def test_4(self):
        self.assertEqual(whats_in_a_name([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "c": 2 }), [{ "a": 1, "b": 2, "c": 2 }])


class Test_Whats_In_A_Name_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(whats_in_a_name_2([{ "first": "Romeo", "last": "Montague" }, { "first": "Mercutio", "last": None }, { "first": "Tybalt", "last": "Capulet" }], { "last": "Capulet" }), [{ "first": "Tybalt", "last": "Capulet" }])

    def test_2(self):
        self.assertEqual(whats_in_a_name_2([{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }], { "a": 1 }), [{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }])

    def test_3(self):
        self.assertEqual(whats_in_a_name_2([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "b": 2 }), [{ "a": 1, "b": 2 }, { "a": 1, "b": 2, "c": 2 }])

    def test_4(self):
        self.assertEqual(whats_in_a_name_2([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "c": 2 }), [{ "a": 1, "b": 2, "c": 2 }])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
