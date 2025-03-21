# 1. Two Sum
# Easy
# 2025/03/17

class Solution:
    # Hash Map
    # TC: O(n), SC: O(n)
    def twoSum(self, nums, target):
        numMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                return [numMap[target - nums[i]], i]
            numMap[nums[i]] = i


