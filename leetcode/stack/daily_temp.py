# Daily Temperatures 

def dailyTemperatures(temp):

	stack = [] 
	nge = [0]*len(temp)
	stack.append(0)

	for i in range(len(temp)):
		while stack and temp[i]>temp[stack[-1]]:

			idx = stack[-1]
			nge[idx] = i - stack[-1]
			stack.pop()
		stack.append(i)
	return nge




print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))

