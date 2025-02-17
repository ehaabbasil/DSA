arr=[]

nge = []
st = [] 


st.append(len(arr)-1)
nge[len(arr)-1] = -1

for i in range(10,2,-1):
	# pop answers pushes

	while(size(st)>0 and arr[i] >= st[-1]):
		st.pop()

	if size(st) == 0:
		nge[i]=-1
	else:
		nge[i]=st[-1]


	st.append(arr[i])


