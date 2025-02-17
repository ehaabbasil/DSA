class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        rv = 0 
        p = 1 
        s = 0

        while(n>0):
            digit = n % k 
            n = n // k 

            rv += digit * p
            p = p * 10 
        
        while(rv>0):
            d = rv % 10
            rv = rv//10
            s += d
        return s