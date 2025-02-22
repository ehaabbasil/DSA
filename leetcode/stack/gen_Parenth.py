# Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]



def genParenth(n):

	stack = []
	res = []


	def backtrack(openN,closeN):

		if openN == n == closeN:
			res.append("".join(stack))

		elif openN < n:

			stack.append('(')
			backtrack(openN+1,closeN)
			stack.pop()

		elif openN > closeN:

			stack.append(')')
			backtrack(openN, closeN+1)
			stack.pop()

	backtrack(0,0)
	return res











print(genParenth(3))
print(genParenth(1))
