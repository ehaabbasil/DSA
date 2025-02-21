


def nge_to_right(arr):

	stack=[]
	nge = [0]*len(arr)

	stack.append(len(arr)-1)
	nge[len(arr)-1] = -1 

	for i in range(len(arr)-2,-1,-1):

		while stack and arr[i]>=stack[-1]:
			stack.pop()

		if not stack:
			nge[i]= -1

		else:
			nge[i] = stack[-1]

		stack.append(arr[i])

	return nge








arr = [2,5,9,3,1,12,6,8,7]
print(nge_to_right(arr))