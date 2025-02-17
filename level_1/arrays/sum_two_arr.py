# Input for array 1
n1 = int(input("Enter the size of the array (n1): "))  # Define n1
arr1 = [int(input(f"Enter value {i}: ")) for i in range(n1)]  # Populate arr1
print("Array 1:", arr1)

# Input for array 2
n2 = int(input("Enter Size n2: "))  # Define n2
arr2 = [int(input(f"Enter value {i}: ")) for i in range(n2)]  # Populate arr2
print("Array 2:", arr2)

# Determine the larger size
larger_size = max(n1, n2)  # Use max() to find the larger size
arr_sum = [0] * (larger_size + 1)  # Initialize arr_sum with zeros (size = larger_size + 1 for carry)
print("Larger size:", larger_size)
print("Initial arr_sum:", arr_sum)

# Initialize pointers and carry
i = n1 - 1  # Pointer for arr1
j = n2 - 1  # Pointer for arr2
k = larger_size  # Pointer for arr_sum
c = 0  # Carry

# Sum the arrays
while i >= 0 or j >= 0 or c != 0:
    d = c  # Start with the carry

    if i >= 0:
        d += arr1[i]  # Add element from arr1
        i -= 1

    if j >= 0:
        d += arr2[j]  # Add element from arr2
        j -= 1

    c = d // 10  # Update carry
    d = d % 10  # Update digit

    arr_sum[k] = d  # Store the result
    k -= 1

# Print the result
if c != 0:
    arr_sum[k] = c  # Store the final carry if it exists

# Remove leading zeros from arr_sum
while len(arr_sum) > 1 and arr_sum[0] == 0:
    arr_sum.pop(0)
 
print("Sum of arrays:", arr_sum)

