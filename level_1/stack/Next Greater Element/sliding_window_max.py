class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        if n == 0 or k == 0:
            return []
        stack = [] 
        nge = [0]*n

        stack.append(n-1)
        nge[n-1]=n

        for i in range(n-2,-1,-1):
    
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()

            if not stack:
                nge[i]=n
            else:
                nge[i]=stack[-1]

            stack.append(i)

        res = []
        j = 0 
        for i in range(n-k+1):
            if(j<i):
                j=i

            while(nge[j]<i+k):
                j = nge[j]
            res.append(nums[j])
        return res
