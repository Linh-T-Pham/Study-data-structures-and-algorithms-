

""" Write a function, pow(base, exponent), that takes in two numbers.
The function should calculate the base raised to the exponent power.

Note: 
A negative exponent can be calculate by taking the reciprocal of the positive exponent.
That is, pow(2, -5) is equal to 1 / pow(2, 5)
Solve this recursively!


>>> pow(2, 0)    
1
>>> pow(2, 1)    
2
>>> pow(2, 5)    
32
>>> pow(3, 4)    
81
>>> pow(2, -5)   
0.03125

"""

def pow(base, exponent):

    if exponent == 0:
        return 1

    elif exponent == 1:
        return base 

    elif exponent >= 2:
        return base * pow(base, exponent-1)

    elif exponent < 0:
        return 1 / (base * pow(base, abs(exponent)-1))



    # elif exponent<0:
    #     return (1/base)*pow(base,exponent+1)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** AWESOME!. GO GO GO!\n")