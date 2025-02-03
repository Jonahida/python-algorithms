# tests/test_dynamic_programming.py

import unittest
from algorithms.dynamic_programming.knapsack import knapsack
from algorithms.dynamic_programming.fibonacci import fibonacci

class TestDynamicProgramming(unittest.TestCase):

    def test_knapsack(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 5
        expected = 7  # The maximum value that can be obtained
        result = knapsack(weights, values, capacity)
        self.assertEqual(result, expected)

    def test_fibonacci(self):
        n = 6
        expected = 8  # Fibonacci of 6 is 8
        result = fibonacci(n)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

