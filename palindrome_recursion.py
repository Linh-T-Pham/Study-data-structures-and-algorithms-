""" Write a function that takes a string as a parameter and returns 
    True if the string is a palindrome, 
    False otherwise. Remember that a string is a palindrome 
    if it is spelled the same both forward and backward. 
    For example: radar is a palindrome. 
    for bonus points palindromes can also be phrases, 
    but you need to remove the spaces and punctuation before checking. 
    for example: madam i’m adam is a palindrome. 
    Other fun palindromes include:

    >>> recursive_palin("kayak")
    True

    >>> recursive_palin("aibohphobia")
    True  

    >>> recursive_palin("able was i ere i saw elba")
    True

    >>> recursive_palin("kanakanak")
    True

    >>> recursive_palin("wassamassaw")
    True

    >>> recursive_palin("Go hang a salami; I’m a lasagna hog")
    True

"""


def recursive_palin(string):
    """ use recursion to solve this problem """
    # slice_string = string[::-1].lower()
    
    # if string == slice_string:
    #     return True
    # return False
    if len(string) <= 1:
        return True 
    
    if string[0] == string[len(string)-1]:
        return recursive_palin(string[1: len(string)-1])

    return False 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")
