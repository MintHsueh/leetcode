'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

'''

class Solution:

    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = [i for i in range(0, len(nums)) if nums[i] == 0]
        zero_index.reverse()
        if len(zero_index) > 0:
            for i in zero_index:
                del nums[i]
                nums.append(0)


    def moveZeroes_twoPointers(self, nums) -> None:
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
    
    #***
    def moveZeroes_twoPointers_2(self, nums) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        

Solution().moveZeroes_twoPointers_2(nums = [0,1,0,3,12])

# https://medium.com/@urdreamliu/283-%E5%9C%96%E8%A7%A3-move-zeroes-4da4900f5aac
