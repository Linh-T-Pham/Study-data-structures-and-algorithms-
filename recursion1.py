                                                                                                                                                                                          """Write a function, lucasNumber(n), that takes in a number.
    The function should return the n-th number of the Lucas Sequence.
    The 0-th number of the Lucas Sequence is 2.
    The 1-st number of the Lucas Sequence is 1
    To generate the next number of the sequence, we add up the previous two numbers.

    For example, the sequence begins: 2, 1, 3, 4, 7, 11, ...

    Solve this recursively!


For example:

    >>> lucasNumber(0)
    2

    >>> lucasNumber(1)
    1

    >>> lucasNumber(2)
    3

    >>> lucasNumber(3) 
    4

    >>> lucasNumber(5)
    11

    >>> lucasNumber(9) 
    76

"""

def lucasNumber(n):

    if n == 0:
        return 2
    elif n == 1:
        return 1 


    return lucasNumber(n-1) + lucasNumber(n-2)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")