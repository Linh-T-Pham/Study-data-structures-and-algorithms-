"""
    Give 2 non-empty arrays of integers, finds the pair of numbers
    one from each array whose absolute difference is closet to zero and
    returns an array containing those 2 numbers, with the number form the fist
    array in the first position 

    >>> find_small_differnce([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    [28, 26]

       
"""

def find_small_differnce(array1, array2):
    # sort the array in place 
    array1.sort()
    array2.sort()

    index1 = 0
    index2 = 0 

    # Initialize the small_difference to an empty array
    smallest_difference_pair = []

    smallest = float('inf')
    current = float('inf')

    # Why I don't initize the largest to inf

    while index1 < len(array1) and index2 < len(array2):
        first_num = array1[index1]
        second_num = array2[index2]

        if first_num < second_num:
            current = second_num - first_num
            index1 += 1

        elif second_num < first_num:
            current = first_num - second_num
            index2 += 1

        else:
            
            return [first_num, second_num]

        if smallest > current:
            smallest = current
            smallest_difference_pair = [first_num, second_num]

    return smallest_difference_pair

























if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")