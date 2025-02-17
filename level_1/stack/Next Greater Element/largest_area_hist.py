
rb[] # nse index on the right 

lb[] #nse index on the left 
arr[]

st[]
st.append(len(arr)-1)
rb[len(arr)-1] = len(arr)

for i in range(len(arr),2,-1):

	while st and arr[i] < st[-1]:
		st.pop()


	if not st:
		rb[i] == len(arr)

	else:
		rb[i] = st[-1]


	st.push(i)



st[]
st.append(0)
lb[0] = -1

for i in range(len(arr)):

	while st and arr[i] < st[-1]:
		st.pop()


	if not st:
		lb[i] == -1

	else:
		lb[i] = st[-1]


	st.push(i)


maxArea = 0 

for i in range(len(arr)): 
	width = rb[i] - lb[i] -1
	area = arr[i] * width 
	 if area > maxArea:
	 	maxArea = area 






