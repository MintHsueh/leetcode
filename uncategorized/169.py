'''
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

class Solution:

    # The time complexity of this approach is O(n) because it iterates through the array once to count the occurrences and then iterates through the hash map, 
    # which has a maximum size of the number of distinct elements in the array.
    def majorityElement(self, nums) -> int:
        element_count = {}
        for i in nums:
            if i in element_count:
                element_count[i] += 1
            else:
                element_count[i] = 1
        
        for key, value in element_count.items():
            if value > len(nums)/2:
                return key
            

    def majorityElement_2(self, nums) -> int:
        element_set = set(nums)
        for i in element_set:
            if nums.count(i) > len(nums)/2:
                return i


    #***
    # The time complexity of this approach is O(n log n) since sorting an array of size n takes O(n log n) time.
    def majorityElement_3(self, nums) -> int:     
        nums.sort()
        n = len(nums)
        return nums[n//2]


a = Solution().majorityElement_3(nums = [2,2,1,1,1,2,2])
print(a)