# algorithms/dynamic_programming/knapsack.py

def knapsack(weights, values, capacity):
    """
    Solve the 0/1 knapsack problem using dynamic programming.

    Args:
        weights (list of int): List of weights of the items.
        values (list of int): List of values of the items.
        capacity (int): The maximum capacity of the knapsack.

    Returns:
        int: The maximum value that can be obtained with the given capacity.
    """
    n = len(weights)
    # Create a DP table where dp[i][w] represents the maximum value for the first i items with weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If the weight of the current item is greater than the current capacity, don't include it
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum value is found at dp[n][capacity]
    return dp[n][capacity]

