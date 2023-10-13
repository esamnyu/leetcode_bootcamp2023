def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # A hash map to store the last index of each character
    max_length = 0  # The maximum length of substring found so far
    start = 0  # The start index of the current substring
    
    for end, char in enumerate(s):  # end is the end index of the current substring
        # If the character is already in the hash map, update the start index
        if char in char_index:
            start = max(start, char_index[char] + 1)
        # Update the hash map with the new index of the character
        char_index[char] = end
        # Update the maximum length if a longer substring is found
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Usage
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3
