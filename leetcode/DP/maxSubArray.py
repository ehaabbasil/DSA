class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # kadane algorithm
        # space: 0(1) time: O(n)

        
        max_sum = -10000
        cur_sum = 0

        for i in nums:

            cur_sum = max(cur_sum+i, i)
            max_sum = max(cur_sum, max_sum)
        
        return max_sum

        