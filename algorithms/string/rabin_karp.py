def rabin_karp(pattern, text, d=256, q=101):
    """
    Rabin-Karp string matching algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text to search within.
        d (int): The number of characters in the input alphabet (default is 256 for ASCII).
        q (int): A prime number used for hashing (default is 101).

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    M = len(pattern)
    N = len(text)

    # Edge case handling
    if M == 0 or N == 0 or M > N:
        return []

    pattern_hash = 0  # Hash value for pattern
    text_hash = 0  # Hash value for text
    h = 1  # The value of d^(M-1) % q

    # Precompute the value of h (d^(M-1) % q)
    for i in range(M - 1):
        h = (h * d) % q

    # Calculate hash value of the pattern and first window of text
    for i in range(M):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    print(f"Initial pattern hash: {pattern_hash}, Initial text hash: {text_hash}")  # Debugging

    result = []

    # Slide the pattern over the text one by one
    for i in range(N - M + 1):
        print(f"Checking window '{text[i:i+M]}' at index {i}")  # Debugging

        # Check if hash values are equal
        if pattern_hash == text_hash:
            # If hash values match, do an actual comparison (to handle hash collisions)
            if text[i:i + M] == pattern:
                result.append(i)

        # Calculate the hash for the next window in the text
        if i < N - M:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + M])) % q
            if text_hash < 0:
                text_hash += q  # Ensure positive hash value

            print(f"Updated text hash at index {i+1}: {text_hash}")  # Debugging

    return result
