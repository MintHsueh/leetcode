'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''

class Solution:
    # TC: O(n)
    # SC: ??
    def subarraySum(self, nums, k: int) -> int:
        prevSum_count = {0:1}
        prevSum = 0
        result = 0

        for num in nums:
            prevSum += num
            if prevSum - k in prevSum_count:
                result += prevSum_count[prevSum - k]

            if prevSum in prevSum_count:
                prevSum_count[prevSum] += 1
            else:
                prevSum_count[prevSum] = 1
        
        return result
    

    def subarraySum_improved(self, nums, k: int) -> int:
        prevSum_count = {0:1}
        prevSum = 0
        result = 0

        for num in nums:
            prevSum += num
            result += prevSum_count.get(prevSum - k, 0)   # dic.get(key, num) means if key exist return dic[key] ow. return num 
            prevSum_count[prevSum] = prevSum_count.get(prevSum, 0) + 1
            
        return result

'''
Medium
# Array
# Hash Table
# Prefix Sum : https://leetcode.jp/leetcode-560-subarray-sum-equals-k-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/
'''