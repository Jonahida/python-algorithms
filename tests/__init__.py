# tests/test_string.py

import unittest
from algorithms.string.kmp import kmp
from algorithms.string.rabin_karp import rabin_karp

class TestStringAlgorithms(unittest.TestCase):

    def test_kmp(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABAB"
        expected = [0, 10, 15]
        result = kmp(pattern, text)
        self.assertEqual(result, expected)

    def test_rabin_karp(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABAB"
        expected = [0, 10, 15]
        result = rabin_karp(pattern, text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

