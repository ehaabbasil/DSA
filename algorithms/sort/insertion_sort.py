A = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(A)
j = 2

for j in range(n):

    key = A[j]
    i = j - 1 

    while i >= 0 and A[i] > key:

        A[i+1]=A[i]
        i = i - 1
    A[i+1]=key


print("Sorted array:", A)


