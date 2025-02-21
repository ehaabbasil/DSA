# Evaluate Reverse Polish Notation 

# Time and Space: o(n)

# Tokens is array of strings 
# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6



def evalRPN(tokens):
	# write code here 
	stack = [] 

	for token in tokens:
		if token == "+":
			stack.append(stack.pop()+stack.pop())

		elif token == "-":
			a , b = stack.pop(), stack.pop()

			stack.append(b-a)


		elif token == "*":
			stack.append(stack.pop()*stack.pop())


		elif token == "/":
			a , b = stack.pop(), stack.pop()
			stack.append(int(b/a))

		else:
			stack.append(int(token))


	return stack[-1]













print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


