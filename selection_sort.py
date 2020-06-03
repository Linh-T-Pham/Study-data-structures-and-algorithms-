""" a function which takes in an array of integers and returns 
    a sorted version of that array. Use the Selection Sort Algorithm
    to sort the array. 

    input = [8,5,2,9,5,6,3]
    output = [2,3,5,5,6,8,9]
"""
 
def selectionSort(array):
    # divide the arrays into 2 sublists which are sorted numbers and 
    # unsorted numbers 
    # keep track of the first number in the unsorted sublist 
    # at the beginning all the numbers are unsorted 
    current_index = 0 # index of the first number in unsorted sublist 
    while current_index < len(array)-1: # len(array-1) is the final index
        # in the entire array 
        smallest_index = current_index # first number in the unsorted sublist
        
        for i in range(current_index + 1, len(array)):
            if array[smallest_index] > array[i]:
                smallest_index = i 
        swap(current_index, smallest_index, array)
        current_index += 1
    return array
        
def swap(i,j, array):
    array[i], array[j] = array[j]



