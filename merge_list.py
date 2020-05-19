"""
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 15, 19, 20]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 15, 19, 20]
print(merge_lists(my_list, alices_list))

0 <= i < len(array1)
0 <= j < len(array2)
"""

def merge_lists(my_list, alices_list):
    
    result_array = []
    i = 0
    j = 0
    
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] < alices_list[j]:
            result_array.append(my_list[i])
            i += 1
        elif my_list[i] > alices_list[j]:
            result_array.append(alices_list[j])
            j += 1
        else:
            result_array.append(my_list[i])
            result_array.append(alices_list[j])
            i += 1
            j += 1
    
#     if len(my_list) < len(alices_list):
#         remaining_nums = alices_list[len(my_list):]
#         result_array.extend(remaining_nums)
#     else:
#         remaining_nums = my_list[len(alices_list):]
#         result_array.extend(remaining_nums)
        
    if i < len(my_list):
        result_array.extend(my_list[i:])
        
    if j < len(alices_list):
        result_array.extend(alices_list[j:])
    return result_array 
            
            

my_list     = [3, 4, 6, 10, 11, 15, 20, 21]
#i=0,1,2,3,4,5,6
alices_list = [1, 5, 8, 12, 14, 15, 19]
#j=0,1,2,3,4,5,6,7
# result = 1, 3, 4, 5,6,8,10,11,12,14,15,15,19

print(merge_lists(my_list, alices_list))