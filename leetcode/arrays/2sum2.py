class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers)-1
        curSum = 0 


        while l < r:
            curSum = numbers[l]+numbers[r]

            if target == curSum:
                return [l+1,r+1]
            
            elif curSum<target:
                l+=1

            elif curSum>target:
                r-=1


