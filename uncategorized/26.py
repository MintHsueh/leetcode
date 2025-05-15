'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

'''

class Solution:
    # Sum of all elememnts
    # Time complexity: O(n)     # Python内置函数 sum() 用于计算数值型列表中所有元素的总和。 其时间复杂度为O(n)，因为需要遍历整个列表才能计算总和，其中n为列表的长度。
    # Space complexity: O(1)
    def missingNumber_1(self, nums) -> int:
        n = len(nums)
        zeroToN_sum = int((1 + n) * n / 2)  # zeroToN_sum = sum(range(0,n+1))   # ((1 + n) * n) // 2
        nums_sum = sum(nums)
        return zeroToN_sum - nums_sum
    
    # XOR Operation
    # Time complexity: O(n)
    # Space complexity: O(1)
    def missingNumber_2(self, nums) -> int:
        n = len(nums)
        result = 0
        for i in range(0, n+1):
            result ^= i
        for num in nums:
            result ^= num
        return result

'''
Easy
# Array
# Hash Table
# Math
# Binary Search
# Bit Manipulation
# Sorting
'''