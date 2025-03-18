# Longest Substring With all unique Characters 


def longest_Substring_With_All_Unique_Char(arr, k):
    i = 0
    hmap = {}
    mx = 0
    for j in range(len(arr)):
        char = arr[j]
        hmap[char] = hmap.get(char, 0) + 1  # Fix 1: Correctly track character counts
        
        # Shrink window if unique characters exceed the window
        while len(hmap) < j - i + 1:
            left_char = arr[i]
            hmap[left_char] -= 1
            if hmap[left_char] == 0:
                del hmap[left_char]
            i += 1
        
        # Update max length if current window has exactly K unique chars
        if len(hmap) == j - i + 1 :
            mx = max(mx, j - i + 1)
    
    return mx

print(longest_Substring_With_All_Unique_Char("aabacbebebe", 3))  


def longest_unique_substring(s):
    i = 0
    char_map = {}
    max_length = 0
    for j in range(len(s)):
        if s[j] in char_map:
            # Ensure i doesn't move leftward (e.g., consider "abba")
            i = max(i, char_map[s[j]] + 1)
        char_map[s[j]] = j
        max_length = max(max_length, j - i + 1)
    return max_length

print(longest_unique_substring("aabacbebebe"))  # Output: 4