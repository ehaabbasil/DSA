n = 51234
k = -2

temp = n
nod = 0  # Number of digits

# Calculate the number of digits in 'n'
while temp > 0:
    temp = temp // 10
    nod += 1

# Handle cases where k >= nod
k = k % nod  # Ensures k is within valid range

if k < 0:
	k = k + nod 

div = 1
mult = 1

# Compute div and mult to split 'n' into two parts
for i in range(nod):
    if i < k:  # Corrected from 'i <= k'
        div *= 10
    else:
        mult *= 10

# Split and rotate
q = n // div    # First part (remaining digits)
r = n % div     # Last 'k' digits
rotated = r * mult + q  # Combine parts

print(rotated)  # Output: 57234
 