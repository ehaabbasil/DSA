
# There is a special discount for items in the shop. 
#If you buy the ith item, then you will receive a discount 

#equivalent to prices[j] where 
#j is the minimum index 

#such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, 
#considering the special discount.


# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 


# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]

# Approach Next Smallest Element to the right 
def finalPrices(prices):
    nse = [0] * len(prices)
    stack = []
    stack.append(0)

    for i in range(1, len(prices)):  
        while stack and prices[i] <= prices[stack[-1]]:
            pos = stack[-1]
            nse[pos] = prices[stack[-1]] - prices[i]
            stack.pop()
        
        stack.append(i)

    while stack:
        pos = stack.pop()
        nse[pos] = prices[pos]  # Fix incorrect variable reference

    return nse

# Test cases
print(finalPrices([1, 2, 3, 4, 5]))  # Expected: [1, 2, 3, 4, 5]
print(finalPrices([8, 4, 6, 2, 3]))  # Expected: [4, 2, 4, 2, 3]
