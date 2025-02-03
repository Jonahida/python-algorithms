import sys
import unittest
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.searching.binary_search import binary_search
from algorithms.searching.linear_search import linear_search
from algorithms.graph.bfs import bfs
from algorithms.graph.dfs import dfs
from algorithms.dynamic_programming.fibonacci import fibonacci
from algorithms.dynamic_programming.knapsack import knapsack
from algorithms.string.kmp import kmp
from algorithms.string.rabin_karp import rabin_karp
from tests import test_sorting, test_searching, test_graph, test_dynamic_programming, test_string

def print_menu():
    print("\nSelect an algorithm to explore:")
    print("1. Quick Sort")
    print("2. Merge Sort")
    print("3. Bubble Sort")  # Add Bubble Sort option
    print("4. Binary Search")
    print("5. Linear Search")
    print("6. BFS (Graph Traversal)")
    print("7. DFS (Graph Traversal)")
    print("8. Fibonacci (Dynamic Programming)")
    print("9. Knapsack Problem (Dynamic Programming)")
    print("10. KMP String Matching")
    print("11. Rabin-Karp String Matching")
    print("12. Run Tests")
    print("0. Exit")


def algorithm_details(choice):
    if choice == '1':
        print("\nQuick Sort: A divide-and-conquer algorithm that picks an element as a pivot and partitions the array into two sub-arrays according to whether they are less than or greater than the pivot. It recursively sorts the sub-arrays.")
        quick_sort_example()
    elif choice == '2':
        print("\nMerge Sort: A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves.")
        merge_sort_example()
    elif choice == '3':
        print("\nBubble Sort: A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.")
        bubble_sort_example()  # Add Bubble Sort example
    elif choice == '4':
        print("\nBinary Search: A fast search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.")
        binary_search_example()
    elif choice == '5':
        print("\nLinear Search: A simple search algorithm that checks every element of the array to find a target value.")
        linear_search_example()
    elif choice == '6':
        print("\nBFS (Breadth-First Search): A graph traversal algorithm that explores all nodes at the present depth level before moving on to the nodes at the next depth level.")
        bfs_example()
    elif choice == '7':
        print("\nDFS (Depth-First Search): A graph traversal algorithm that explores as far as possible along each branch before backtracking.")
        dfs_example()
    elif choice == '8':
        print("\nFibonacci: A classic problem in dynamic programming that calculates the nth Fibonacci number.")
        fibonacci_example()
    elif choice == '9':
        print("\nKnapsack Problem: A dynamic programming problem where you try to fill a knapsack with items of given weights and values to maximize the value without exceeding the weight limit.")
        knapsack_example()
    elif choice == '10':
        print("\nKMP (Knuth-Morris-Pratt): A linear time string matching algorithm that searches for occurrences of a pattern within a text string.")
        kmp_example()
    elif choice == '11':
        print("\nRabin-Karp: A string matching algorithm that uses hashing to find an exact match of a pattern within a text string.")
        rabin_karp_example()
    elif choice == '12':
        print("\nRunning tests...")
        run_tests()
    else:
        print("\nInvalid choice. Please try again.")

def quick_sort_example():
    """
    Demonstrates the Quick Sort algorithm with an example.

    This function provides a predefined example to illustrate Quick Sort
    and then allows the user to input their own list of numbers for sorting.

    Steps:
    1. Displays an example of Quick Sort in action.
    2. Prompts the user to enter a list of numbers.
    3. Sorts the list using Quick Sort and prints the result.

    Example:
        Input:  [34, 7, 23, 32, 5, 62]
        Output: [5, 7, 23, 32, 34, 62]
    """
    print("\nExample of Quick Sort:")
    example_arr = [34, 7, 23, 32, 5, 62]
    print(f"Input: {example_arr}")
    print(f"Sorted Output: {quick_sort(example_arr)}\n")

    arr = list(map(int, input("Enter numbers separated by spaces to sort: ").split()))
    print(f"Original array: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")


def merge_sort_example():
    """
    Demonstrates the Merge Sort algorithm with an example.

    This function first provides a predefined example to illustrate Merge Sort.
    Then, it allows the user to input their own list of numbers for sorting.

    Steps:
    1. Displays an example of Merge Sort in action.
    2. Prompts the user to enter a list of numbers.
    3. Sorts the list using Merge Sort and prints the result.

    Example:
        Input:  [38, 27, 43, 3, 9, 82, 10]
        Output: [3, 9, 10, 27, 38, 43, 82]
    """
    print("\nExample of Merge Sort:")
    example_arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Input: {example_arr}")
    print(f"Sorted Output: {merge_sort(example_arr)}\n")

    arr = list(map(int, input("Enter numbers separated by spaces to sort: ").split()))
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")


def bubble_sort_example():
    """
    Demonstrates the Bubble Sort algorithm with an example.

    This function first provides a predefined example to illustrate Bubble Sort.
    Then, it allows the user to input their own list of numbers for sorting.

    Steps:
    1. Displays an example of Bubble Sort in action.
    2. Prompts the user to enter a list of numbers.
    3. Sorts the list using Bubble Sort and prints the result.

    Example:
        Input:  [64, 34, 25, 12, 22, 11, 90]
        Output: [11, 12, 22, 25, 34, 64, 90]
    """
    print("\nExample of Bubble Sort:")
    example_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Input: {example_arr}")
    print(f"Sorted Output: {bubble_sort(example_arr)}\n")

    arr = list(map(int, input("Enter numbers separated by spaces to sort: ").split()))
    print(f"Original array: {arr}")
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")


def binary_search_example():
    """
    Demonstrates the Binary Search algorithm with an example.

    This function first provides a predefined example to illustrate Binary Search.
    Then, it allows the user to input their own sorted list of numbers and a target value.

    Steps:
    1. Displays an example of Binary Search in action.
    2. Prompts the user to enter a sorted list of numbers.
    3. Asks the user for a target value to search for.
    4. Uses Binary Search to locate the target and prints the result.

    Example:
        Input Array: [10, 20, 30, 40, 50]
        Target: 30
        Output: Found target 30 at index 2
    """
    print("\nExample of Binary Search:")
    example_arr = [10, 20, 30, 40, 50]
    example_target = 30
    print(f"Array: {example_arr}, Target: {example_target}")
    example_result = binary_search(example_arr, example_target)
    print(f"Found target {example_target} at index {example_result}" if example_result != -1 else "Target not found.")

    arr = list(map(int, input("\nEnter a sorted array of numbers separated by spaces: ").split()))
    target = int(input("Enter the target value to search for: "))
    print(f"Array: {arr}")
    result = binary_search(arr, target)
    print(f"Found target {target} at index {result}" if result != -1 else "Target not found.")


def linear_search_example():
    """
    Demonstrates the Linear Search algorithm with an example.

    This function first provides a predefined example to illustrate Linear Search.
    Then, it allows the user to input their own list of numbers and a target value.

    Steps:
    1. Displays an example of Linear Search in action.
    2. Prompts the user to enter a list of numbers.
    3. Asks the user for a target value to search for.
    4. Uses Linear Search to locate the target and prints the result.

    Example:
        Input Array: [3, 1, 4, 1, 5, 9]
        Target: 4
        Output: Found target 4 at index 2
    """
    print("\nExample of Linear Search:")
    example_arr = [3, 1, 4, 1, 5, 9]
    example_target = 4
    print(f"Array: {example_arr}, Target: {example_target}")
    example_result = linear_search(example_arr, example_target)
    print(f"Found target {example_target} at index {example_result}" if example_result != -1 else "Target not found.")

    arr = list(map(int, input("\nEnter numbers separated by spaces to search: ").split()))
    target = int(input("Enter the target value to search for: "))
    print(f"Array: {arr}")
    result = linear_search(arr, target)
    print(f"Found target {target} at index {result}" if result != -1 else "Target not found.")


def bfs_example():
    """
    Demonstrates the Breadth-First Search (BFS) algorithm.

    This function first provides a predefined example graph for BFS.
    Then, it allows the user to input their own graph as an adjacency list and a starting node.

    Example:
        Graph:
        A -> B, C
        B -> D, E
        C -> F
        D -> []
        E -> []
        F -> []
        Start Node: A
        Output: A -> B -> C -> D -> E -> F
    """
    print("\nExample of BFS Traversal:")
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    example_start = 'A'
    print(f"Graph: {example_graph}, Start Node: {example_start}")
    bfs(example_graph, example_start)

    graph = {}
    n = int(input("\nEnter number of nodes in the graph: "))
    print("Enter the adjacency list for each node:")
    for _ in range(n):
        node = input("Node: ")
        neighbors = input(f"Neighbors of {node}: ").split()
        graph[node] = neighbors
    start_node = input("Enter the start node for BFS: ")

    if start_node not in graph:
        print(f"Error: Node {start_node} is not present in the graph.")
        return

    print("Graph:", graph)
    bfs(graph, start_node)


def dfs_example():
    """
    Demonstrates the Depth-First Search (DFS) algorithm.

    This function first provides a predefined example graph for DFS.
    Then, it allows the user to input their own graph as an adjacency list and a starting node.

    Example:
        Graph:
        A -> B, C
        B -> D, E
        C -> F
        D -> []
        E -> []
        F -> []
        Start Node: A
        Output: A -> B -> D -> E -> C -> F
    """
    print("\nExample of DFS Traversal:")
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    example_start = 'A'
    print(f"Graph: {example_graph}, Start Node: {example_start}")
    dfs(example_graph, example_start)

    graph = {}
    n = int(input("\nEnter number of nodes in the graph: "))
    print("Enter the adjacency list for each node:")
    for _ in range(n):
        node = input("Node: ")
        neighbors = input(f"Neighbors of {node}: ").split()
        graph[node] = neighbors
    start_node = input("Enter the start node for DFS: ")

    print("Graph:", graph)
    dfs(graph, start_node)


def fibonacci_example():
    """
    Demonstrates the Fibonacci sequence using Dynamic Programming.

    This function first provides a predefined example.
    Then, it allows the user to enter their own number.

    Example:
        Input: 6
        Output: Fibonacci of 6 is: 8
    """
    print("\nExample of Fibonacci Calculation:")
    example_n = 6
    print(f"Fibonacci of {example_n} is: {fibonacci(example_n)}")

    n = int(input("\nEnter the number to find its Fibonacci value: "))
    print(f"Fibonacci of {n} is: {fibonacci(n)}")


def knapsack_example():
    """
    Demonstrates the 0/1 Knapsack problem using Dynamic Programming.

    The user is prompted to enter item values, weights, and the knapsack weight limit.

    Example:
        Items:
        Values: [60, 100, 120]
        Weights: [10, 20, 30]
        Max Weight: 50
        Output: Maximum value in Knapsack: 220
    """
    print("\nExample of Knapsack Problem:")
    example_values = [60, 100, 120]
    example_weights = [10, 20, 30]
    example_capacity = 50
    print(f"Values: {example_values}, Weights: {example_weights}, Capacity: {example_capacity}")
    print(f"Maximum value in Knapsack: {knapsack(example_weights, example_values, example_capacity)}")

    n = int(input("\nEnter the number of items: "))
    values = []
    weights = []
    for i in range(n):
        value = int(input(f"Enter value for item {i + 1}: "))
        weight = int(input(f"Enter weight for item {i + 1}: "))
        values.append(value)
        weights.append(weight)
    W = int(input("Enter the maximum weight the knapsack can carry: "))
    print(f"Maximum value in Knapsack: {knapsack(weights, values, W)}")


def kmp_example():
    """
    Demonstrates the KMP (Knuth-Morris-Pratt) string matching algorithm.

    The user is prompted to enter a text and a pattern to search.

    Example:
        Text: "ababcababcabc"
        Pattern: "abc"
        Output: Pattern found at index: [2, 6, 10]
    """
    text = input("Enter the text string: ")
    pattern = input("Enter the pattern to search for: ")
    print(f"Pattern found at index: {kmp(text, pattern)}")



def rabin_karp_example():
    """
    Demonstrates the Rabin-Karp string matching algorithm.

    The user is prompted to enter a text and a pattern to search.

    Example:
        Text: "ababcababcabc"
        Pattern: "abc"
        Output: Pattern found at index: [2, 6, 10]
    """
    text = input("Enter the text string: ")
    pattern = input("Enter the pattern to search for: ")
    print(f"Pattern found at index: {rabin_karp(pattern, text)}")



# Define explanation functions
def explain_quick_sort():
    print("\nQuick Sort: A divide-and-conquer algorithm that picks an element as a pivot and partitions the array into two sub-arrays according to whether they are less than or greater than the pivot. It recursively sorts the sub-arrays.")
    quick_sort_example()

def explain_merge_sort():
    print("\nMerge Sort: A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves.")
    merge_sort_example()

def explain_bubble_sort():
    print("\nBubble Sort: A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.")
    bubble_sort_example()

def explain_binary_search():
    print("\nBinary Search: A fast search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.")
    binary_search_example()

def explain_linear_search():
    print("\nLinear Search: A simple search algorithm that checks every element of the array to find a target value.")
    linear_search_example()

def explain_bfs():
    print("\nBFS (Breadth-First Search): A graph traversal algorithm that explores all nodes at the present depth level before moving on to the nodes at the next depth level.")
    bfs_example()

def explain_dfs():
    print("\nDFS (Depth-First Search): A graph traversal algorithm that explores as far as possible along each branch before backtracking.")
    dfs_example()

def explain_fibonacci():
    print("\nFibonacci: A classic problem in dynamic programming that calculates the nth Fibonacci number.")
    fibonacci_example()

def explain_knapsack():
    print("\nKnapsack Problem: A dynamic programming problem where you try to fill a knapsack with items of given weights and values to maximize the value without exceeding the weight limit.")
    knapsack_example()

def explain_kmp():
    print("\nKMP (Knuth-Morris-Pratt): A linear time string matching algorithm that searches for occurrences of a pattern within a text string.")
    kmp_example()

def explain_rabin_karp():
    print("\nRabin-Karp: A string matching algorithm that uses hashing to find an exact match of a pattern within a text string.")
    rabin_karp_example()

# Map choices to explanation functions
algorithm_explanations = {
    '1': explain_quick_sort,
    '2': explain_merge_sort,
    '3': explain_bubble_sort,
    '4': explain_binary_search,
    '5': explain_linear_search,
    '6': explain_bfs,
    '7': explain_dfs,
    '8': explain_fibonacci,
    '9': explain_knapsack,
    '10': explain_kmp,
    '11': explain_rabin_karp,
    '12': lambda: print("\nRunning tests...") or run_tests()
}

def run_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromModule(test_sorting))
    suite.addTest(loader.loadTestsFromModule(test_searching))
    suite.addTest(loader.loadTestsFromModule(test_graph))
    suite.addTest(loader.loadTestsFromModule(test_dynamic_programming))
    suite.addTest(loader.loadTestsFromModule(test_string))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting...")
            sys.exit()
        algorithm_explanations.get(choice, lambda: print("\nInvalid choice. Please try again."))()

if __name__ == "__main__":
    main()
