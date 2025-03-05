# Maximum Sum of Distinct Subarrays

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # Time and Space O(N) O(K)
        res = 0 
        prevIdx = {}
        l = 0 

        cur_sum = 0 

        for r in range(len(nums)):
            cur_sum+= nums[r]

            i = prevIdx.get(nums[r],-1)

            while  l <= i or r - l + 1 >k:
                cur_sum -= nums[l]
                l+=1
            
            if r - l + 1 == k:
                res = max(res,cur_sum)
            prevIdx[nums[r]] = r 

        return res
            