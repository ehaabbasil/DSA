def topKfrequest(n):

	# Using bucket sort but changing the count as ith for the list of pairs 
	# Basically using indices as the count
	# Values are unbounded 

	 # [100] occurs once - map to 1 
	 # [2] occurs twice - map to 2 
	 # [1] occurs three times 


	 # All values that occur n times, because input array is size n, if every value was exact same, hence our array will be bounded to n 
	 # Scan through in linear time 

	 count = {}

	 freq = [[] for i in range(len(nums)+1)]  # initializing empty array, size of input 

	 for n in nums:
	 	count[n] = 1 + count.get(n,0) # counting every value how many times it is occuring, .get to get value 

	 for n, c in count.items():  # going through each value we counted, for every k:v pair insert count as the index append the n , n appears c num times 
	 	freq[c].append(n)

	 res = [] 

	 # top k elements  - > descending order 

	 for i in range(len(feq)-1,0,-1):
	 	for n in freq[i]:
	 		res.append(n)
	 		# when will we stop, at some point res len will be k 

	 		if len(res) == k:
	 			return res 







