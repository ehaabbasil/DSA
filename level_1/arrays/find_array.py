

n = 5
arr = [int(input(f"Enter value {i + 1}: ")) for i in range(n)]  # Populate array with integers
print("Array:", arr)

a = int(input("Enter number to find: "))  # Convert search input to integer
idx = -1  # Default index if number is not found

# Search for the number in the array
for i in range(len(arr)):
    if arr[i] == a:
        idx = i
        break  # Exit loop once the number is found

print("Index of the number:", idx)