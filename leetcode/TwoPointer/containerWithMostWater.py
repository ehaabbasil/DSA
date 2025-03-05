# Container With Most Water 

def containterWithMostWater(heights):

	# Linear Time Solution o(n)

	res = 0 

	l,r = 0, len(heights)-1

	while l < r:
		area = (r-l)*min(heights[l], heights[r])
		res = max(res,area)

		if heights[l] < heights[r]:
			l+=1 

		else:
			r--=1 

	return res 

	# Brute Force Solution o(N)^2 

	# res = 0 

	# for l in range(heights[l]):
	# 	for r in range(l+1, len[heights]):
	# 		area = (r-l) * min(heights[l],heights[r])
	# 		res = max(res,area)
	# return res 
