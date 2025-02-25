# Sliding Maximum Window 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position               



def maxSlidingWindow(nums,k):
	n = len(nums)
	st = [] 
	nge = [0]*n

	st.append(n-1)
	nge[n-1] = n

	for i in range(n-2,-1,-1):

		while st and nums[i]>=nums[st[-1]]:
			st.pop()

		if not st:
			nge[i] = n


		else:

			nge[i] = st[-1]
		st.append(i)


	res = [] 
	j = 0 

	for i in range(n-k+1):

		if j < i :
			j = i 

		while nge[j] < i+k:
			j = nge[j]

		res.append(nums[j])

	return res



















print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

