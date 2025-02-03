def bubble_sort(arr):
    """
    Bubble Sort Algorithm.

    This function implements the Bubble Sort algorithm, which repeatedly steps
    through the list, compares adjacent elements, and swaps them if they are in
    the wrong order. The pass through the list is repeated until the list is sorted.

    Bubble Sort is a simple but inefficient sorting algorithm with a time complexity of
    O(n^2) in the worst case.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: The sorted list.

    Example:
        >>> bubble_sort([5, 2, 9, 1])
        [1, 2, 5, 9]
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
    return arr
