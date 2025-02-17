

def getValueInDecimal(n,b):

	rv = 0 
	p = 1

	while(n>0):

		digit = n % 10

		n = n // 10 

		rv+= digit * p 

		p = p * b 



	return rv



