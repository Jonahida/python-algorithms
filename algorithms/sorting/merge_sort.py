def merge_sort(arr):
    """
    Merge Sort Algorithm (Recursive version).

    This function implements the Merge Sort algorithm, which is a divide-and-conquer
    sorting algorithm. It recursively divides the input list into two halves, sorts
    each half, and then merges the two sorted halves into a single sorted list.

    Merge Sort is a stable, efficient sorting algorithm with a time complexity of
    O(n log n), making it a good choice for large datasets.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements of the input array.

    Example:
        >>> merge_sort([12, 11, 13, 5, 6, 7])
        [5, 6, 7, 11, 12, 13]
    """
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    This function combines two already sorted lists (`left` and `right`) into a
    single sorted list by comparing elements from each list and appending the smaller
    element to the result list.

    The time complexity of this merging step is O(n), where n is the total number of
    elements in the two lists combined.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A new list containing all the elements from `left` and `right`, sorted.

    Example:
        >>> merge([5, 12], [6, 11, 13])
        [5, 6, 11, 12, 13]
    """
    sorted_list = []
    i = j = 0

    # Merge the two lists while maintaining sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements from either list
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
