
def getsum(b,n1,n2):

	rv = 0
	p = 1
	c = 0

	while(n1>0 or n2>0 or c>0):

		d1 = n1 % 10     
		d2 = n2 % 10 

		n1 = n1 // 10 
		n2 = n2 // 10 


		d = d1 + d2 + c 

		c = d // b
		d = d % b


		rv += d * p 
		p = p * 10 


	return rv



print(getsum(8,236,754))
