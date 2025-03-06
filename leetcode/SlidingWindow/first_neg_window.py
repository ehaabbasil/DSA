from collections import deque

def firstNegativeNumber(nums, k):
    l = 0
    q = deque()
    res = []
    
    for r in range(len(nums)):
        # Add current element's index to deque if it's negative
        if nums[r] < 0:
            q.append(r)
        
        # When the window reaches size k
        if r >= k - 1:
            # Remove indices from the front that are out of the current window
            while q and q[0] < l:
                q.popleft()
            
            # Append the first negative in the current window or 0 if none exist
            if q:
                res.append(nums[q[0]])
            else:
                res.append(0)
            
            # Move the left pointer to slide the window
            l += 1
    
    return res

# Test the function with the sample input
print(firstNegativeNumber([12, -1, -7, 8, -15, 30, 16, 28], 3))  # Output: [-1, -1, -7, -15, -15, 0]