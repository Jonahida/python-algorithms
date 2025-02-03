# tests/test_searching.py

import unittest
from algorithms.searching.binary_search import binary_search
from algorithms.searching.linear_search import linear_search

class TestSearching(unittest.TestCase):

    def test_binary_search(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 7
        expected = 6  # Index of 7
        result = binary_search(data, target)
        self.assertEqual(result, expected)

    def test_linear_search(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 7
        expected = 6  # Index of 7
        result = linear_search(data, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

