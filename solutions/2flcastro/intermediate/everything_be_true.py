# ----------------------------------
# Everything Be True
# ----------------------------------
# Check if the property (second argument) is truthy on all elements in a
# collection (first argument).
#
# Remember you can access a dictionary's properties through [] notation.
# ----------------------------------

import unittest

# using a for-loop
def truth_check(collection, prop):
    for item in collection:
        if not prop in item or not item[prop]:
            return False
    return True


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Truth_Check(unittest.TestCase):
    def test_1(self):
        self.assertEqual(truth_check([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex"), True)

    def test_2(self):
        self.assertEqual(truth_check([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex"), False)

    def test_3(self):
        self.assertEqual(truth_check([{"user": "Tinky-Winky", "sex": "male", "age": 0}, {"user": "Dipsy", "sex": "male", "age": 3}, {"user": "Laa-Laa", "sex": "female", "age": 5}, {"user": "Po", "sex": "female", "age": 4}], "age"), False)

    def test_4(self):
        self.assertEqual(truth_check([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True}, {"name": "FastFoward", "onBoat": None}], "onBoat"), False)

    def test_5(self):
        self.assertEqual(truth_check([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True, "alias": "Repete"}, {"name": "FastFoward", "onBoat": True}], "onBoat"), True)

    def test_6(self):
        self.assertEqual(truth_check([{"single": "yes"}], "single"), True)

    def test_7(self):
        self.assertEqual(truth_check([{"single": ""}, {"single": "double"}], "single"), False)

    def test_8(self):
        self.assertEqual(truth_check([{"single": "double"}, {"single": None}], "single"), False)

    def test_9(self):
        self.assertEqual(truth_check([{"single": "double"}, {"single": None}], "single"), False)


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
