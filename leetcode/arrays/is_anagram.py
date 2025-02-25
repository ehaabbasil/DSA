s = "anagram"
"aaangrm"
t = "nagram"

# iterate through all the keys 

# Time and Space complexity 
# O(S+T)
# O(S+T)

if len(s) != len(t):
	return False
countS, countT = {}

for i in range(len(s)):
	countS[s[i]] = 1 + countS.get(s[i],0)
	counT[t[i]] = 1 + countT.get(t[i],0)

for c in countS:
	if countS[c] != countT.get(c,0):
		return False:
return True  




 

