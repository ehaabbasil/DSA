 

def getValue(n,b1,b2):

	dec = getValueInDecimal(n,b1)
	dn = any_base_to_decimal(dec,b2)

	return dn

 

def getValueInDecimal(n,b):

	rv = 0 
	p = 1

	while(n>0):

		digit = n % 10

		n = n // 10 

		rv+= digit * p   

		p = p * b 



	return rv

def any_base_to_decimal(n,d):


	rv = 0 
	p = 1

	while (n>0):

		digit = n % d 

		n = n // d # diving by the base 

		rv += digit * p

		p = p * 10


	return rv 

print(getValue(172,8,2))