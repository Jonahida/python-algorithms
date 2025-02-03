# tests/test_graph.py

import unittest
from algorithms.graph.bfs import bfs
from algorithms.graph.dfs import dfs

class TestGraph(unittest.TestCase):

    def test_bfs(self):
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        }
        start_node = 0
        expected = [0, 1, 2, 3, 4]
        result = bfs(graph, start_node)
        self.assertEqual(result, expected)

    def test_dfs(self):
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        }
        start_node = 0
        expected = [0, 1, 3, 4, 2]
        result = dfs(graph, start_node)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

