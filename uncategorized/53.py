'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: 
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
which is more subtle.

'''

class Solution:
    
    def maxSubArray(self, nums) -> int:
        curr_max = glo_max = nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            glo_max = max(glo_max, curr_max)
        return glo_max
    
    # TC: O(n)
    # SC: O(1)
    def maxSubArray(self, nums) -> int:
        result = nums[0]
        curr_sum = 0
        
        for num in nums:
            curr_sum += num 
            curr_sum = max(curr_sum, num) 
            result = max(result, curr_sum) 
        
        return result
    
a = Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
print(a)

'''
Medium
# Array
# Dynamic Programming
'''