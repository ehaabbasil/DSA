class Solution:
    def baseNeg2(self, n: int) -> str:

        if n == 0:
            return "0"
        ans = ""
        while n!=0:
            ans = str(n%2)+ans
            print(f"ans: {ans}")
            n = (n-1) // -2
            print(f"n:{n}")
        return ans




solution = Solution()

print(solution.baseNeg2(2))