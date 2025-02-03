# algorithms/searching/linear_search.py

def linear_search(arr, target):
    """
    Perform a linear search for a target value in an array.
    Returns the index of the target if found, otherwise returns -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # Target not found

