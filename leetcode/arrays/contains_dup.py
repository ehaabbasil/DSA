

# Time : O(n)
# Space : O(n)


hashSet = set()

for n in nums:
	if n in hashSet:
		return True
	hashSet.add(n)
return False