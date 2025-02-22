# Remove outermost Parentheses


# ( () () ) ( () )

# "()()()"


# "(()())(())(()(()))"

# "()()()()(())"

def remove_out_parenth(s):
	balance = 0 

	res = [] 

	for char in s:
		if char == '(':
			if balance > 0:
				res.append(char)
			balance+=1
		else:
			balance-=1
			if balance>0:
				res.append(char)

	return "".join(res)
			







print(remove_out_parenth("(()())(())"))

print(remove_out_parenth("(()())(())(()(()))"))