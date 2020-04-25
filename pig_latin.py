"""Write a function to turn a phrase into Pig Latin.

    Your function will be given a phrase (of one or more space-separated words). There will be no punctuation in it. You should turn this into the same phrase in Pig Latin.

    Rules
    If the word begins with a consonant (not a, e, i, o, u), move the first letter to the end and add ‘ay’

    If the word begins with a vowel, add ‘yay’ to the end

For example:

    >>> pig_latin('porcupines are cute')
    'orcupinespay areyay utecay'

    >>> pig_latin('give me an apple')
    'ivegay emay anyay appleyay'

We’ve included a file, piglatin.py, with a function pig_latin:

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """














if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")