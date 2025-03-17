# 238. Product of Array Except Self
# Medium
# 2025/03/16

class Solution:
    # ***
    # Prefix & Suffix
    # TC: O(n), SC: O(1) since the output array is excluded from space analysis.
    def productExceptSelf_1(self, nums):
        n = len(nums)
        result = [1] * n
        prefix, suffix = 1, 1
        
        for i in range(n-1):
            prefix *= nums[i]
            result[i+1] = prefix
        
        for i in range(n-1, 0, -1):
            suffix *= nums[i]
            result[i-1] *= suffix
        
        return result
    
    # Brute Force
    # TC: O(n^2), SC: O(1) since the output array is excluded from space analysis.
    def productExceptSelf_2(self, nums):
        result = []
        n = len(nums)
        for i in range(n):
            p = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    p *= nums[j]
            result.append(p)   
        return result 