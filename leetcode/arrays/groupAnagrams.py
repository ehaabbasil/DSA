def groupAnagrams(s):

	# O(m*n) solution


	res = defaultdict(list) # mapping char count of each string to list of anagrams 

	for s in strs:
		count = [0]*26 # lower case a - z 26 char 

		for c in s:
			count[ord(c)- ord("a")]+=1  # lower case z - a will be 25. a lower case b = 81-80 -> mapped to 1

		res[tuple(count)].append(s)

	return res.values()