'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

'''

class Solution:
    def searchRange(self, nums, target):
        first, last = 0, len(nums)-1
        while first <= last:
            if nums[first] == target and nums[last] == target:
                return [first, last]
            
            elif nums[first] == target and nums[last] != target:
                last -= 1
            
            elif nums[first] != target and nums[last] == target:
                first += 1

            else:
                mid = (first + last) // 2
                if nums[mid] < target:
                    first = mid + 1
                elif nums[mid] > target:
                    last = mid - 1
                else:
                    first += 1
                    last -= 1
            
        return [-1, -1]

a = Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
print(a)