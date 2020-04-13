# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# [0,1,0,1]
# [1,0,0,1]

# [0,0,1,0,0,0,1,1,0] => 6
  #  -----------------  
  #  ----------------
  #  ---------------

# sum(arr[i:]) == len(arr[i:])/2

# equal = True
# max_length = 4

# ones = 2
# zeroes = 2
# https://leetcode.com/problems/contiguous-array/solution/

# https://fellowship.hackbrightacademy.com/materials/challenges/monkey/index.html

# [1,2,3,0]

# t   list of idx
# 0   [4] --> is i <= jump_length  --> No
# 1   [1, 4]  --> is 3-0 <= jump_length --> Yes


# 3, [1, 4, 0, 2, 3, 5]

#     [0, 7]  

# t   list of idx         diff in idx
# 0   [0, 3, 7]           [3, 4]    --> all of these <= jump length? --> No
# 1   [0, 1, 3, 7]        [1, 2, 4] --> all of these <= jump length? --> No
# 2   [0, 1, 3, 4, 7]     [1, 2, 1, 3]  --> all of these <= jump length? --> Yes

#     [0, 5]

# t   list of idx         diff in idx
# 0   [0, 4, 5]           [4, 1]    --> all of these <= jump length? --> No
# 1   [0, 1, 4, 5]        [1, 3, 1] --> No


def earliest_arrival(jump_length, stone_list):
    stone_idx_lst = [0, len(stone_list)+1]

    for t, item in enumerate(stone_list):
      stone_idx = stone_list.index(t) + 1
      stone_idx_lst.append(stone_idx)

      stone_idx_lst.sort()

      idx_diffs = [stone_idx_lst[i+1] - stone_idx_lst[i] for i, num in enumerate(stone_idx_lst[:-1])]
      print(f'idx diffs list: {idx_diffs}')

      all_lt_jump_length = all(num <= jump_length for num in idx_diffs)  # T/F

      if all_lt_jump_length == True:
        return t
      
print(earliest_arrival(3, [1, 2, 3, 0]))  # 1
print(earliest_arrival(2, [1, 2, 3, 0]))  # 2
print(earliest_arrival(3, [1, 4, 0, 2, 3, 5]))  # 2







# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# [0,1,0,1]
# [1,0,0,1]

# [0,0,1,0,0,0,1,1,0] => 6
  #  -----------------  
  #  ----------------
  #  ---------------

# sum(arr[i:]) == len(arr[i:])/2

# equal = True
# max_length = 4

# ones = 2
# zeroes = 2
# https://leetcode.com/problems/contiguous-array/solution/

# https://fellowship.hackbrightacademy.com/materials/challenges/monkey/index.html

# [1,2,3,0]

# t   list of idx
# 0   [4] --> is i <= jump_length  --> No
# 1   [1, 4]  --> is 3-0 <= jump_length --> Yes


# 3, [1, 4, 0, 2, 3, 5]

#     [0, 7]  

# t   list of idx         diff in idx
# 0   [0, 3, 7]           [3, 4]    --> all of these <= jump length? --> No
# 1   [0, 1, 3, 7]        [1, 2, 4] --> all of these <= jump length? --> No
# 2   [0, 1, 3, 4, 7]     [1, 2, 1, 3]  --> all of these <= jump length? --> Yes

#     [0, 5]

# t   list of idx         diff in idx
# 0   [0, 4, 5]           [4, 1]    --> all of these <= jump length? --> No
# 1   [0, 1, 4, 5]        [1, 3, 1] --> No


# def earliest_arrival(jump_length, stone_list):
#   # stone_idx_lst = [0, len(stone_list)+1]

#   for t, item in enumerate(stone_list):
#     if t not in stone_list:
#       continue

#     # stone_idx = stone_list.index(t) + 1
#     # stone_idx_lst.append(stone_idx)
#     # stone_idx_lst.sort()

#     stone_idx_lst = []

#     for i, num in enumerate(stone_list):
#       if num <= t:
#         stone_idx_lst.append(i)

#     # stone_idx_lst = [0, stone_idx)]

#     idx_diffs = [stone_idx_lst[i+1] - stone_idx_lst[i] for i, num in enumerate(stone_idx_lst[:-1])]
#     print(f'idx diffs list: {idx_diffs}')

#     all_lt_jump_length = all(num <= jump_length for num in idx_diffs)  # T/F

#     if all_lt_jump_length == True:
#       return t
      
# print(earliest_arrival(3, [1, 2, 3, 0]))  # 1
# print(earliest_arrival(2, [1, 2, 3, 0]))  # 2
# print(earliest_arrival(3, [1, 4, 0, 2, 3, 5]))  # 2
# print(earliest_arrival(5, [5, 2, 3, 8, 9, 99, 4, 0])) # 3