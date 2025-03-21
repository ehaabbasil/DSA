"""
1. Two Sum

Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List  # Import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [i, j]


    def twoSum2(self, nums: List[int], target: int) -> List[int]:

        pair_idx ={}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target-num]]
            pair_idx[num] = i


# Lets use a different  of empty map 
    def twoSum3(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]

            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[n] = i






# Instantiate the Solution class and call the method
solution = Solution()
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum2([3,2,4], 6))
print(solution.twoSum3([3,2,4], 6))


# better than O(1) solution 


