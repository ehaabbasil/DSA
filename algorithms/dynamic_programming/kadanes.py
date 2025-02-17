"""
Kadane's Algorithm 

Solves Maximum Contiguous Subarray Problem
//
Pseudo :

        M -> 0 ,  S -> 0

        for i to n do 
            S -> max(s + A[i], 0) here 0 is used to reset 
            M - > max(M,S)
        end for
        
        
         kadane algorithm
         space: 0(1) time: O(n)

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -10000
        cur_sum = 0

        for i in nums:

            cur_sum = max(cur_sum + i, i)
            max_sum = max(cur_sum, max_sum)
        
        return max_sum

        
            
            
        