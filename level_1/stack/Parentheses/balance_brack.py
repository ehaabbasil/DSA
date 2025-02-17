

stack = []

sr1 = "[(a+b)+{(c+d)*(e/f)}]"
sr2 = "[(a+b)+{(c+d)*(e/f)]}"


for ch in sr2:

	if ch == '(' or ch == '{' or ch == '[':
		stack.append(ch)

	elif ch == ')':
		if len(stack)==0:
			print("False")
			exit()

		elif stack[-1] != '(':
			 print("False")  
			 exit()
		else:
			stack.pop()

	elif ch == '}':
		if len(stack)==0:
			print("False")
			exit()

		elif stack[-1] != '{':
			 print("False")  
			 exit()
		else:
			stack.pop()
		

	elif ch == ']':
		if len(stack)==0:
			print("False")
			exit()

		elif stack[-1] != '[':
			 print("False")  
			 exit()
		else:
			stack.pop()


if len(stack) == 0:
	print("True")
else:
	print("False")

