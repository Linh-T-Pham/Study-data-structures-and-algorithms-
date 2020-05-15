# Problem 1 *****************


"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple : 1
    berry : 2
    cherry : 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello : 1
    hey : 1
    hi : 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi : 1
    hi : 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""
    new_dict = {}
    """split will change a phrase to a list"""
    new_phrase = phrase.split()
    for word in new_phrase:
        """ At the key new_dict[word] if word is not in the dict, add word to the dict.
        If the key already exits, increment the word by 1 """
        new_dict[word] = new_dict.get(word, 0) + 1


    """Create a sorted list of all keys in new_dict"""
    for key in sorted(list(new_dict.keys())):
        print(key,":",new_dict[key])
    


# word_count("berry cherry cherry cherry berry apple")
# word_count("hey hi hello")
# word_count("hi Hi hi")
# world_count("linh Linh")


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")