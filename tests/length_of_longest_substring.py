def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    seen = set()
    left = 0
    ans = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        ans = max(ans, right - left + 1)
    return ans

if __name__ == "__main__":
    s = "abcabcbb"
    print(length_of_longest_substring(s))