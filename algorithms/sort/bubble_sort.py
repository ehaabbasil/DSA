"""

Bubble Sort : 

"""

def bubble_sort_first(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] =L[j+1], L[j]
                print(f"Bubble Sort: {L}")
    return L

def bubble_sort(L):
    swap = False

    while not swap:
        print("Bubble Sort: " + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1]>L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L



test_list = [1,3,5,7,2,6,25,18,13]

bubble_sort(test_list)
print(test_list)

test_list = [50,20,10,60,40,30]

print(test_list)
bubble_sort_first(test_list)


