"""
Linear Search on unsorted list 

"""
# order o(n)


def linear_search(L,e):
    found = False
    
    for i in range(len(L)):
        if e == L[i]:
            found = True  # speed doesnt impact the worst case
             
    return found

print(linear_search([1,4,5,6], 5))


# If sorted list 

def linear_search_sorted(L,e):
    for i in range(len(l)):
        if l[i] == e:
            return True
        if l[i]>e:
            return False
    return False


# isSubset  quadratic

def isSubset(L1,L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True 
                break
        if not matched:
            return False
    return True

L1 = [1, 6]
L2 = [1, 2, 3, 4, 5]
print(isSubset(L1, L2))  # Expected output: False


