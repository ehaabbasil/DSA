  """

PSUEDO CODE 

    IF x < 0 or x end in 0 or x is not equal to 0 :
        return False 

    reversedHalf = 0 

    while x > reversedHalf:
        add last digit of x to reversedHalf
        remove last digit from x 

    after loop check if x is equal to number reversed or x is equal to reversednumber divided by 10
    for odd

    O log 10 
 



"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x%10==0 and x != 0):
            return False

        revertedHalf = 0 

        while (x>revertedHalf):
            revertedHalf = revertedHalf * 10 + x % 10
            x//=10

        return x == revertedHalf or x == revertedHalf // 10
        



