def matches(message: str, key: str) -> bool:
    m, k = len(message), len(key)
    i, j = 0, 0
    star_index = -1
    match_index = 0

    while i < m:
        if j < k and (key[j] == message[i] or key[j] == '?'):
            # Characters match or key has a '?'
            i += 1
            j += 1
        elif j < k and key[j] == '*':
            # Record the position of '*'
            star_index = j
            match_index = i
            j += 1  # Move past the '*'
        elif star_index != -1:
            # If there's a previous '*', try matching more characters
            j = star_index + 1  # Move to the next character after '*'
            match_index += 1  # Increase the match position in the message
            i = match_index  # Reset i to match the new position
        else:
            return False  # No match and no '*' to fall back on

    # Check if there are remaining '*' in the key
    while j < k and key[j] == '*':
        j += 1

    return j == k  # Both the key and message should be completely processed

# Testing the function with example cases
print(matches("aa", "a"))    # False
print(matches("aa", "*"))    # True
print(matches("cb", "?a"))   # False
print(matches("abc", "a*c")) # True
print(matches("abc", "a?c")) # True
print(matches("abc", "a*d")) # False
