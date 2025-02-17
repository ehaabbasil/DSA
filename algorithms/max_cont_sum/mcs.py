

# Maximum Contiguous Subarray Sum
from typing import List

def mcs(nums: List[int]) -> int:

    m = nums[0]

    for i in range(len(nums)):

        s = 0

        for j in range(i, len(nums)):
            s =s + nums[j]
            m = max(m,s)

    return m


print(mcs(nums=[-2,1,-3,4,-1,2,1,-5,4]))
print(mcs(nums=[1]))
print(mcs(nums=[5,4,-1,7,8]))

# Kadane's Algorithm done in o(n) time and o(1) space


    def maxSubArray(self, nums: List[int]) -> int:

        # kadane algorithm
        # space: 0(1) time: O(n)

        
        max_sum = -10000
        cur_sum = 0

        for i in nums:

            cur_sum = max(cur_sum+i, i)
            max_sum = max(cur_sum, max_sum)
        
        return max_sum

        
            
            
        