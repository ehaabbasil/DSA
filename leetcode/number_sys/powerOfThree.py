class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        rv = 0 
        p = 1

        while(n>0):
            digit = n % 3
            if digit == 2:
                return False
            n//= 3
        return True
            
             
            