# ----------------------------------
# Chunky Monkey
# ----------------------------------
# Write a function that splits an array (first argument) into groups the length
# of "size" (second argument) and returns them as a two dimensional array.
# ----------------------------------

import unittest

def chunk_array_groups(arr, size):
    # create final chunk list
    chunk_array = []
    # create placeholder list
    temp_chunk = []
    for item in arr:
        if len(temp_chunk) == size:
            chunk_array.append(temp_chunk)
            temp_chunk = []
            temp_chunk.append(item)
        else:
            temp_chunk.append(item)
    chunk_array.append(temp_chunk)
    return chunk_array



# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Chunk_Array_Groups(unittest.TestCase):
    def test_1(self):
        self.assertEqual(chunk_array_groups(["a", "b", "c", "d"], 2), [["a", "b"], ["c", "d"]])

    def test_2(self):
        self.assertEqual(chunk_array_groups([0, 1, 2, 3, 4, 5], 3), [[0, 1, 2], [3, 4, 5]])

    def test_3(self):
        self.assertEqual(chunk_array_groups([0, 1, 2, 3, 4, 5], 2), [[0, 1], [2, 3], [4, 5]])

    def test_4(self):
        self.assertEqual(chunk_array_groups([0, 1, 2, 3, 4, 5], 4), [[0, 1, 2, 3], [4, 5]])

    def test_5(self):
        self.assertEqual(chunk_array_groups([0, 1, 2, 3, 4, 5, 6], 3), [[0, 1, 2], [3, 4, 5], [6]])

    def test_6(self):
        self.assertEqual(chunk_array_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4), [[0, 1, 2, 3], [4, 5, 6, 7], [8]])

    def test_7(self):
        self.assertEqual(chunk_array_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2), [[0, 1], [2, 3], [4, 5], [6, 7], [8]])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
