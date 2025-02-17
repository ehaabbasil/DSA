
# Duplicate Brackets

stack = []
sr1 = "((a+b)+(c+d))" # false
sr2 = "(a+b)+((c+d))" # true

# for c in sr2:
# 	if c == ')':

# 		if stack[-1] == "(": #duplicate exists
# 			print("True")
# 			exit()
# 		else:
# 			while stack[-1] != '(':
# 				stack.pop()
# 			stack.pop()   
# 	else: 
# 		stack.append(c)
# print("False")


for c in sr1:
	if c == ')':

		if stack[-1]=="(":
			print("True")
			exit()
		else:
			while stack[-1] != '(':
				stack.pop()
			stack.pop()
	else:
		stack.append(c)
print("False")








































