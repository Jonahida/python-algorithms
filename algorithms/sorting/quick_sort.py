def quick_sort(arr):
    """
    Quick Sort Algorithm (Recursive version).

    This function implements the Quick Sort algorithm, which is a divide-and-conquer
    algorithm. It selects a pivot element and partitions the array into three sub-arrays:
    one with elements less than the pivot, one with elements equal to the pivot, and one
    with elements greater than the pivot. It then recursively sorts the sub-arrays and
    combines them to form a sorted array.

    The time complexity of Quick Sort is O(n log n) on average, but it can degrade to O(n^2)
    in the worst case (when the pivot is poorly chosen).

    Parameters:
    arr (list): A list of elements to be sorted.

    Returns:
    list: A new sorted list that contains the same elements as the input array.

    Example:
    >>> quick_sort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)  # New array returned, not modifying `arr` in-place
