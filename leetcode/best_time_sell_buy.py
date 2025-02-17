# MEM O(1)
# Time = O(N)

# only have to scan array one time 


def maxProfit(self, prices: List[int]) ->int:
	l,r = 0, 1 # left = buying, right = selling 
	maxP = 0 

	while r < len(prices):
		# profitable
		if prices[l] < prices[r]:
			profit  = prices[r] - prices[l]
			maxP = max(maxP, profit)
		else:
			l = r
		r+=1    
	return maxP



