# algorithms/graph/bfs.py

from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (node): The starting node for BFS.

    Returns:
        list: List of nodes visited in BFS order.
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

