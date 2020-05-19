
""" Implement a method to perform basic string compression using the counts 
    of repeated characters.

    If the "compressed" string would not become smaller than the original string, 
    your method should return the original string.


    input: 'aabcccccaaa'
            012345678910
    output: 'a2b1c5a3'
    
    input: 'lmaooo'
           'l1m1a1o3'
    
    output: 'llmaooo'
"""

def string_compression(string):

    current_letter = string[0] # assign the current current letter at index 0
    letter_count = 0 # count how many time the letter occurs 
    new_string_lst = []

    for idx, letter in enumerate(string):
        if letter == current_letter:
            letter_count += 1
        else:
            new_string_lst.append(current_letter)
            new_string_lst.append(str(letter_count))
            current_letter = string[idx]
            letter_count = 1

    new_string_lst.append(current_letter)
    new_string_lst.append(str(letter_count))
    new_string = "".join(new_string_lst)
    return new_string
    
    if len(new_string_lst) < len(string):
        return(string)
    return(new_string_lst)




    








    # current_letter = string[0]
    # letter_count = 0
    # new_string_lst= []
    # for idx, letter in enumerate(string):
    #     if letter == current_letter:
    #         letter_count += 1
    #     else:
    #         new_string_lst.append(current_letter)
    #         new_string_lst.append(str(letter_count))
    #         current_letter = string[idx]
    #         letter_count = 1

    # new_string_lst.append(current_letter)
    # new_string_lst.append(str(letter_count))

    # new_string = ''.join(new_string_lst)
    # # original_string_len = len(string)
    # # new_string_lst = len(new_string_lst)

    # if len(string) < len(new_string_lst):
    #     return string
    # return new_string






# def string_compression(string):

#     current_letter = string[0]
#     letter_counter = 0
#     new_string = ""

#     for idx, letter in enumerate(string):
#         if letter == current_letter:
#             letter_counter += 1
#         else:
#             new_string = new_string + current_letter + str(letter_counter)
#             current_letter = string[idx]
#             letter_counter = 1 

#     new_string = new_string + current_letter + str(letter_counter)

#     original_string_len = len(string)
#     new_string_len = len(new_string)

#     if original_string_len < new_string_len:
#         return string
#     return new_string
     



print(string_compression('aabcccccaaa'))
print(string_compression('llmaooo'))
print(string_compression('yoooooooab'))