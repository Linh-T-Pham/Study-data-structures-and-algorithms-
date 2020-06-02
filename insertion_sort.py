# Write a function that takes in an array of integers and return
#a sorted version of that array. Use the insertion sort algorithm
# to sort the array. 



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            j = i  
            while j > 0 and nums[j] < nums[j - 1]:
                swap(j, j - 1, nums)
                j = j - 1
                
        return nums
    
    def swap(i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]