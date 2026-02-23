
def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters.
    """
    char_map = {} # Stores character -> last seen index
    start = 0
    max_length = 0
    longest_substr = "" # Optional: just to visualize
    
    for end in range(len(s)):
        char = s[end]
        
        # If the character is repeated AND it is within the current window
        if char in char_map and char_map[char] >= start:
            # Move the start pointer to the right of the previous occurrence
            start = char_map[char] + 1
            
        # Update the last seen index of the character
        char_map[char] = end
        
        # Update max length
        current_len = end - start + 1
        if current_len > max_length:
            max_length = current_len
            longest_substr = s[start : end + 1]
            
    return max_length, longest_substr

# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3) # Tricky case!
    ]
    
    print(f"{'Input String':<20} | {'Expected':<10} | {'Result':<10} | {'Ex. Substr':<15} | {'Status'}")
    print("-" * 80)
    
    for s, expected in test_cases:
        length, substring = length_of_longest_substring(s)
        status = "PASSED" if length == expected else "FAILED"
        print(f"'{s:<18}' | {str(expected):<10} | {str(length):<10} | {substring:<15} | {status}")
