"""

This is to compute factorial in two ways 

1. iteratively 
2. recursively 

interestingly both have the same complexity of o(n) 

"""

def fact_iter(n):
    prod = 1

    for i in range(1,n+1):
        prod*=1
    return prod




def fact_recur(n):

    if n<=1:
        return 1

    else:
        return n*fact_recur(n-1)