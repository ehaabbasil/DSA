"""

This is an example of logarithmic complexity, converting integer to string

"""


def intToStr(i):
    
    digits = '012345789'

    if i == 0:
        return '0'
    
    res = ''

    while i > 0:
        res = digits[i%10] + res
        )
        i = i//10
       
    return res



print(intToStr(50))