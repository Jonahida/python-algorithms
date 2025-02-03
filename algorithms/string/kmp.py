# algorithms/searching/kmp.py

def kmp(pattern, text):
    """
    Knuth-Morris-Pratt (KMP) string matching algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text to search within.

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    # Preprocess the pattern to create the "longest prefix which is also suffix" (LPS) array
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    result = []
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

