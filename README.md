# Algorithms Repository

A repository showcasing popular algorithms used in software engineering, including sorting, searching, graph algorithms, dynamic programming, and more. Each algorithm is implemented in Python with explanations, example usage, and Big-O time/space complexity analysis.

---

## Table of Contents
- [Project Description](#project-description)
- [Algorithms](#algorithms)
  - [Sorting](#sorting)
  - [Searching](#searching)
  - [Graph Algorithms](#graph-algorithms)
  - [Dynamic Programming](#dynamic-programming)
  - [String Matching](#string-matching)
- [How to Run the Program](#how-to-run-the-program)
- [Testing](#testing)
- [License](#license)

---

## Project Description

This project demonstrates popular algorithms implemented in Python, providing a reference for understanding algorithm design and analysis. The repository includes algorithms from various domains such as sorting, searching, graph traversal, dynamic programming, and string matching. Each algorithm is accompanied by explanations, example usage, and time/space complexity analysis.

---

## Algorithms

### Sorting

This section includes sorting algorithms for organizing data.

1. **Bubble Sort**
   - **Description:** A comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent items, and swaps them if needed.
   - **Time Complexity:**
     - Worst-case: O(n²)
     - Best-case: O(n)
     - Average-case: O(n²)

2. **Merge Sort**
   - **Description:** A divide-and-conquer sorting algorithm that splits the array into sub-arrays, sorts them, and merges them back together.
   - **Time Complexity:**
     - Worst-case: O(n log n)
     - Best-case: O(n log n)
     - Average-case: O(n log n)

3. **Quick Sort**
   - **Description:** A divide-and-conquer algorithm that partitions the array around a pivot element and recursively sorts the sub-arrays.
   - **Time Complexity:**
     - Worst-case: O(n²)
     - Best-case: O(n log n)
     - Average-case: O(n log n)

---

### Searching

In this section, searching algorithms are used to find specific elements within data structures.

1. **Binary Search**
   - **Description:** A search algorithm that finds the position of a target value within a sorted array by repeatedly dividing the search interval in half.
   - **Time Complexity:**
     - Worst-case: O(log n)
     - Best-case: O(1)
     - Average-case: O(log n)

2. **Linear Search**
   - **Description:** A simple search algorithm that checks each element one by one until the target is found.
   - **Time Complexity:**
     - Worst-case: O(n)
     - Best-case: O(1)
     - Average-case: O(n)

3. **Rabin-Karp**
   - **Description:** A string-searching algorithm that uses hashing to find a pattern in a text.
   - **Time Complexity:**
     - Worst-case: O(n * m)
     - Best-case: O(n + m)

---

### Graph Algorithms

Graph traversal algorithms explore graphs or networks.

1. **Breadth-First Search (BFS)**
   - **Description:** A graph traversal algorithm that explores neighbors at the current depth level before moving on to nodes at the next depth level.
   - **Time Complexity:**
     - Worst-case: O(V + E), where V is the number of vertices and E is the number of edges.

2. **Depth-First Search (DFS)**
   - **Description:** A graph traversal algorithm that explores as far down a branch as possible before backtracking.
   - **Time Complexity:**
     - Worst-case: O(V + E), where V is the number of vertices and E is the number of edges.

---

### Dynamic Programming

Dynamic programming algorithms solve complex problems by breaking them down into simpler subproblems.

1. **Fibonacci**
   - **Description:** An algorithm to compute the nth Fibonacci number efficiently using dynamic programming.
   - **Time Complexity:**
     - Worst-case: O(n)

2. **Knapsack Problem**
   - **Description:** Solves the 0/1 knapsack problem using dynamic programming.
   - **Time Complexity:**
     - Worst-case: O(n * W), where n is the number of items and W is the maximum weight.

---

### String Matching

These algorithms are used to search for patterns in strings.

1. **KMP (Knuth-Morris-Pratt)**
   - **Description:** A string-searching algorithm that improves on brute force by avoiding re-checking characters that are already known to match.
   - **Time Complexity:**
     - Worst-case: O(n + m), where n is the length of the text and m is the length of the pattern.

---

## How to Run the Program

To run the program and explore the algorithms interactively, use the following command:

```bash
$ python3 main.py
```
You will be prompted with the following menu to select an algorithm to explore:

```bash
Select an algorithm to explore:
1. Quick Sort
2. Merge Sort
3. Binary Search
4. Linear Search
5. BFS (Graph Traversal)
6. DFS (Graph Traversal)
7. Fibonacci (Dynamic Programming)
8. Knapsack Problem (Dynamic Programming)
9. KMP String Matching
10. Rabin-Karp String Matching
11. Run Tests
0. Exit
Enter your choice:
```
Select the desired algorithm to see an example usage, its explanation, and time complexity analysis.

## Testing

This project includes a comprehensive set of unit tests to verify the correctness of each algorithm. The tests ensure that each algorithm works as expected across various scenarios, including common use cases, edge cases, and potential performance bottlenecks. Each algorithm is tested thoroughly to confirm its accuracy, correctness, and efficiency.

### Test Coverage

The tests cover the following aspects:

- **Edge Cases:** For example, when an array is empty, or when inputs are at their minimum or maximum values.
- **Typical Use Cases:** Standard scenarios where the algorithm is expected to work under normal conditions.
- **Boundary Conditions:** Testing limits like large input sizes to ensure that algorithms perform well under stress.
- **Correctness:** Verifying that the algorithm returns the expected results.
- **Efficiency:** Testing the performance of the algorithms to confirm they run within acceptable time and space limits.

### Running the Tests

To run all the unit tests in the project, execute the following command:

```bash
$ python3 -m unittest discover tests
```

This will automatically discover and execute all test cases defined in the tests directory.

You can also run individual tests by specifying the path to the test file, like so:

```bash
$ python3 -m unittest tests.test_sorting
$ python3 -m unittest tests.test_searching
$ python3 -m unittest tests.test_graph
$ python3 -m unittest tests.test_dynamic_programming
$ python3 -m unittest tests.test_string_matching
```

### Test Output
If all tests pass successfully, you should see an output like the following:

```bash
..........
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

If a test fails or encounters an error, you will see detailed error messages indicating which tests failed and why. These messages will help you identify issues with the algorithm or its implementation.

## License

This project is licensed under the MIT License.