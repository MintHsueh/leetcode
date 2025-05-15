'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

class Solution:

    # The time complexity of this approach is O(n log n), where n is the length of the array.
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def containsDuplicate_2(self, nums) -> bool:
        num_count = {}
        for i in nums:
            if i in num_count:
                num_count[i] += 1
                if num_count[i] == 2:
                    return True
            else:
                num_count[i] = 1
        return False
    
    def containsDuplicate_3(self, nums) -> bool:
        num_count = {}
        for i in nums:
            if i in num_count:
                return True
            else:
                num_count[i] = 1
        return False
    
    #***
    # The time complexity of this approach is O(n), where n is the length of the array.
    # 改用 list.append 會超時
    def containsDuplicate_4(self, nums) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
    
    # Time Limit Exceeded
    def containsDuplicate_5(self, nums) -> bool:
        nums_noDuplicate = sorted(list(set(nums)), key=nums.index)
        if nums_noDuplicate == nums:
            return False
        else:
            return True

a= Solution().containsDuplicate_3(nums = [1,1,1,3,3,4,3,2,4,2])
print(a)


'''
Easy

# Array
# Hash Table
# Sorting

'''