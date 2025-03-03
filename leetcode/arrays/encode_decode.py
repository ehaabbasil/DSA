# Encode and Decode String 

# Given a list of strings encode into single 

# LENGHT OF FOLLOWING WORD # String # COUNT NEXT LENGTH of CHAR  

#4#leet5#code 


# Time and Space : O(N)

def encode(self, strs):

	res = ""

	for s in strs:
		res+= str(len(s))+"#"+s


def decode(self, strs):
	res, i  = [], 0 

	while i < len(str):

		j = i 

		while str[j] != "#":

			j+=1 

		length = int(str[i:j])

		res.append(str[j + 1 : j + 1 + length])
		
	return res





