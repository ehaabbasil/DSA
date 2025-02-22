# Longest Valid Parentheses

def longest_valid_parenth(s):
	# Approach 1
	left = 0 
	right = 0 
	maxP = 0

	for c in s:
		if c == '(':
			left+=1

		else:
			right+=1

		if left == right:
			maxP = max(maxP,left*2)

		elif right > left:
			left = 0 
			right = 0 
	left = 0 
	right = 0 

	for i in range(len(s)-1,-1,-1):

		if s[i]== '(':
			left+=1

		else:
			right+=1

		if left == right:
			maxP = max(maxP,left*2)

		elif left > right:
			left = 0 
			right = 0 
	return maxP



	# Approach 2 

	max_length = 0 
	stack = [-1]

	for i, ch in enumerate(s):
		if ch == '(':
			stack.append(i)
		else:
			stack.pop()

			if not stack:
				stack.append(i)
			else:
				current_length = i - stack[-1]# Calculate valid substring length
				max_length = max(max_length, current_length)
	return max_length














print(longest_valid_parenth('(()'))
print(longest_valid_parenth(')()())'))
print(longest_valid_parenth(''))