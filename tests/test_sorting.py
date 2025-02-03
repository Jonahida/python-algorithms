# tests/test_sorting.py

import unittest
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.merge_sort import merge_sort

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        data = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        result = bubble_sort(data)
        self.assertEqual(result, expected)

    def test_quick_sort(self):
        data = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        result = quick_sort(data)
        self.assertEqual(result, expected)

    def test_merge_sort(self):
        data = [5, 2, 9, 1, 5, 6]
        expected = [1, 2, 5, 5, 6, 9]
        result = merge_sort(data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

