# ( ) valid 
# ) ( invalid , unclosed 
# [] {} valid 
# ([)) invalid 

# o(n) and o(n)

class Solution:
	def isValid(self, s: str) -> bool:
		stack = [] 
		closeToOpen = { ")":"(","]":"[", "}":"{"}


		for c in s:
			if c in closeToOpen:
				
				if stack and stack[-1] == closeToOpen[c]: # make sure stack is not empty and matching opening 
 
					stack.pop()

				else: 
					return False
			else:
				stack.append(c)

		return True if not stack else False






