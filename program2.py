def matches(message: str, key: str) -> bool:
    m, k = len(message), len(key)
    i, j = 0, 0
    star_index = -1
    match_index = 0

    while i < m:
        if j < k and (key[j] == message[i] or key[j] == '?'):
            # Characters match, or key has a '?'
            i += 1
            j += 1
        elif j < k and key[j] == '*':
            # Record the position of '*' and current match index
            star_index = j
            match_index = i
            j += 1  # Move past the '*'
        elif star_index != -1:
            # If there's a previous '*', backtrack
            j = star_index + 1  # Move to the next character after '*'
            match_index += 1  # Try to match more characters with '*'
            i = match_index  # Continue from the new match index
        else:
            return False  # No match, and no '*' to fall back on

    # Check if there are remaining '*' characters in the key
    while j < k and key[j] == '*':
        j += 1

    # Return True if both message and key are fully processed
    return j == k


# Testing the function with various cases
print(matches("aa", "a"))      # False
print(matches("aa", "*"))      # True
print(matches("cb", "?a"))     # False
print(matches("abc", "a*c"))   # True
print(matches("abc", "a?c"))   # True
print(matches("abc", "a*d"))   # False
print(matches("", "*"))        # True (Empty string matches '*')
print(matches("abc", "****"))  # True (Multiple '*' are treated as one)
