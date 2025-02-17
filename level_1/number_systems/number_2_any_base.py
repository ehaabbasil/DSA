

"""


(634) base 10 converted to (1172) base 8


"""
def number_to_any_base(n,d):


	rv = 0 
	p = 1

	while (n>0):

		digit = n % d 

		n = n // d # diving by the base 

		rv += digit * p

		p = p * 10


	return rv 


print(number_to_any_base(634,8))
print(number_to_any_base(2,2))