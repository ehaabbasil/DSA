# n = int(input("Enter n:"))
# arr = []


# for i in range(n):
# 	value = input(f"Enter value {i + 1}: ")  
# 	arr.append(value)

# print("Final array:", arr)  # Print the populated array



n = int(input("Enter n: "))  # Convert input to integer

# Use list comprehension to populate the array
arr = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

print("Final array:", arr)  # Print the populated array

max_val = arr[0]
min_val = arr[0]

for i in range(n):
	if arr[i] > max_val:
		max_val= arr[i]

	if arr[i] < min_val:
		min_val = arr[i]

span = max_val - min_val
print("Span",span)



