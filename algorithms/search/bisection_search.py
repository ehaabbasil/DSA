
"""

One implementation of bisection search 

which is not optimal because it copies which costs more 
"""

def bisect_search1(L,e):

    if L == []:
        return False   # constant 

    elif len(L)==1:
        return L[0] == e  # constant 
    else:
        half = len(L)//2 # constant

        if L[half] > e:
            return bisect_search1(L[:half],e) # not constant
        else:
            return bisect_search1(L[half:],e)  # not constant 



def bisect_search2(L,e):
    def bisect_search_helper(L,e,low,high):

        if high == low:
            return L[low] == e # if they are the same cool, i have a list of 1 just check if it is the same
        mid = (high+low)//2    # if they are not the same, then find midpoint integer division by 2

        if L[mid] == e: # is the middle the element? 
            return True
        
        elif L[mid] > e:  # check if the thing in middle is bigger than e
             if low == mid: # nothing left to search, list of size 1 
                return False
            else:
                return bisect_search_helper(L,e,low,mid-1)   # check the lower to mid
        else:
            return bisect_search_helper(L,e, mid + 1, high)  # check the mid to high
        
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L,e,0,len(L)-1)

    

