# Next Greater Element 1 



# nums 1 = [4,1,2]
# nums 2 = [1,3,4,2]

# output = [-1, 3, -1]

def next_greater_element(nums1,nums2):



	idxNums1 = {n:i for i,n in enumerate(nums1)}
	nge = [-1]*len(nums1)

	stack = []
	
	for i in range(len(nums2)):
		cur = nums2[i]
		while stack and cur > stack[-1]:
			val = stack.pop()
			index = idxNums1[val]
			nge[index] = cur 

		if cur in idxNums1:
			stack.append(cur)

	return nge 


print(next_greater_element([4,1,2],[1,3,4,2]))

print(next_greater_element([2,4],[1,2,3,4]))

