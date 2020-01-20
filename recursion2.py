"""Write a function, reverseString(str), that takes in a string.
The function should return the string with it's characters in reverse order.
Solve this recursively!

Examples:

>>> reverseString("")            
''
>>> reverseString("c")          
'c'

>>> reverseString("internet")    
'tenretni'

>>> reverseString("friends")     
'sdneirf'

"""

def reverseString(Str):
    
    if Str == "":
        return Str

    return reverseString(Str[1:]) + Str[0]









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Awesome!. GO GO GO!\n")