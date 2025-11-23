def find_first_repeating_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

if __name__ == "__main__":
    s = "abddbacc"
    print(find_first_repeating_char(s))
