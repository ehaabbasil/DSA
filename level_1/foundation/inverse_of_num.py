
n = 21453


inverse = 0 
original_place= 1


while(n!=0): # till number is not 0 
	original_digit = n % 10
	inverted_digit= original_place
	inverted_place = original_digit

	# make change changes 
	inverse = inverse + inverted_digit * pow(10, inverted_place - 1)

	n = n // 10 

	original_place+=1


print(inverse) 