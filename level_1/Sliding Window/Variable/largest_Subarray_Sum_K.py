 # Largest Subarray of Sum K 

 # This is an example for Variable sized Sliding Window Questions
 # Here there would not be a given K size but instead will be a condition example sum = 5 



def largestSubarray(arr, k):
	n = len(arr)

	i = 0 
	j = 0 
	mx = 0
	s = 0 
	while j < n:

		s += arr[j]

		if s > k:
			while s > k:
				s-=arr[i]
				i+=1
		elif s == k:
			mx = max(mx,j-i+1)

		j+=1  

	return mx 
		 

print(largestSubarray([4,1,1,1,2,3,5],5))