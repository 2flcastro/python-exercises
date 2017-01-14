# ----------------------------------
# Chunky Monkey
# ----------------------------------
# Write a function that splits a list (first argument) into groups the length
# of "size" (second argument) and returns them as a two dimensional list.
# ----------------------------------

import unittest
import math

# using temporary chunk
def chunky_monkey(lst, size):
    chunks = []
    temp_chunk = []
    for item in lst:
        if len(temp_chunk) == size:
            chunks.append(temp_chunk)
            temp_chunk = []
            temp_chunk.append(item)
        else:
            temp_chunk.append(item)
    chunks.append(temp_chunk)
    return chunks


# using list slices
def chunky_monkey_2(lst, size):
    chunks = []
    num_chunks = math.floor(len(lst) / size)
    for i in range(num_chunks):
        chunks.append(lst[i * size:i * size + size])
    if len(lst) % size:
        chunks.append(lst[num_chunks * size:])
    return chunks


# ----------------------------------
# Unit Tests
# ----------------------------------
class Test_Chunk_Array_Groups(unittest.TestCase):
    def test_1(self):
        self.assertEqual(chunky_monkey(["a", "b", "c", "d"], 2), [["a", "b"], ["c", "d"]])

    def test_2(self):
        self.assertEqual(chunky_monkey([0, 1, 2, 3, 4, 5], 3), [[0, 1, 2], [3, 4, 5]])

    def test_3(self):
        self.assertEqual(chunky_monkey([0, 1, 2, 3, 4, 5], 2), [[0, 1], [2, 3], [4, 5]])

    def test_4(self):
        self.assertEqual(chunky_monkey([0, 1, 2, 3, 4, 5], 4), [[0, 1, 2, 3], [4, 5]])

    def test_5(self):
        self.assertEqual(chunky_monkey([0, 1, 2, 3, 4, 5, 6], 3), [[0, 1, 2], [3, 4, 5], [6]])

    def test_6(self):
        self.assertEqual(chunky_monkey([0, 1, 2, 3, 4, 5, 6, 7, 8], 4), [[0, 1, 2, 3], [4, 5, 6, 7], [8]])

    def test_7(self):
        self.assertEqual(chunky_monkey([0, 1, 2, 3, 4, 5, 6, 7, 8], 2), [[0, 1], [2, 3], [4, 5], [6, 7], [8]])


class Test_Chunk_Array_Groups_2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(chunky_monkey_2(["a", "b", "c", "d"], 2), [["a", "b"], ["c", "d"]])

    def test_2(self):
        self.assertEqual(chunky_monkey_2([0, 1, 2, 3, 4, 5], 3), [[0, 1, 2], [3, 4, 5]])

    def test_3(self):
        self.assertEqual(chunky_monkey_2([0, 1, 2, 3, 4, 5], 2), [[0, 1], [2, 3], [4, 5]])

    def test_4(self):
        self.assertEqual(chunky_monkey_2([0, 1, 2, 3, 4, 5], 4), [[0, 1, 2, 3], [4, 5]])

    def test_5(self):
        self.assertEqual(chunky_monkey_2([0, 1, 2, 3, 4, 5, 6], 3), [[0, 1, 2], [3, 4, 5], [6]])

    def test_6(self):
        self.assertEqual(chunky_monkey_2([0, 1, 2, 3, 4, 5, 6, 7, 8], 4), [[0, 1, 2, 3], [4, 5, 6, 7], [8]])

    def test_7(self):
        self.assertEqual(chunky_monkey_2([0, 1, 2, 3, 4, 5, 6, 7, 8], 2), [[0, 1], [2, 3], [4, 5], [6, 7], [8]])


# ----------------------------------
# Run Tests
# ----------------------------------
if __name__ == "__main__":
    unittest.main()
