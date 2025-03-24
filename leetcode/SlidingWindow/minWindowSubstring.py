class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        countT = {}  # Fixed counts of characters in t
        window = {}  # Current counts in the sliding window
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)  # Track progress toward matching all characters
        res, resLen = [-1, -1], float('inf')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1  # Expand window to the right
            
            # Update `have` if current character's count is exactly matched
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # Shrink window from the left while all characters are matched
            while have == need:
                # Update result if a smaller valid window is found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Remove leftmost character from the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1  # Break the loop if a required character is now missing
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""