"""

57645 / 10 = 4 

76 / 10 = 6 

7 / 10 = 7 


how many times 5 appears?

"""


def get_digit_frequency(n,d):

	rv = 0 
	print(n)
	print(d)
	while(n>0):
		digit = n % 10
		print(f"digit={digit}")
		n = n//10 
		print(f"n={n}")

		if digit == d:
			rv+=1
			

	return rv


print(get_digit_frequency(5255,5))





