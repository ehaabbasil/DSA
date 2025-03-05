# Longest Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time and Space: O(n*26) o(n) rounded off 
        count = {} # hashmap to count the occurances of each character
        res = 0 # longest substring we can create 

        l = 0 # left pointer 
        # optimization maxF

        for r in range(len(s)):
            count[s[r]]= 1 + count.get(s[r],0) # update the count in hashmap by one with its previous but if not exist return - 
            # maxF = max(maxF, count[s[r]])
            # while (r-l+1) - maxF > k: 
            while (r-l+1) - max(count.values()) > k: # while window is not valid, tell us how many replacements can be done in window but rep is greater than k then shift left pointer
                count[s[l]] -=1 # decrement the value of the left as we are going out og the window
                l += 1  # shift the pointer 

            res = max(res, r-l+1)
        return res 

