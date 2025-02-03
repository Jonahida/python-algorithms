# algorithms/graph/dfs.py

def dfs(graph, start):
    """
    Perform Depth-First Search (DFS) on a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (node): The starting node for DFS.

    Returns:
        list: List of nodes visited in DFS order.
    """
    visited = set()
    result = []

    def dfs_helper(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)

    dfs_helper(start)
    return result

