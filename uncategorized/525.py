'''
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

'''

class Solution:
    # Brute force
    # Time Limit Exceeded
    # TC: O(n^2)
    def findMaxLength_1(self, nums) -> int:
        result = 0
        for i in range(0, len(nums)-1):
            curr_sum = 0
            if nums[i] == 0:
                curr_sum -= 1
            else:
                curr_sum += 1

            for j in range(i+1, len(nums)):
                if nums[j] == 0:
                    curr_sum -= 1
                else:
                    curr_sum += 1
                
                if curr_sum == 0:
                    result = max(result, j-i+1)
        
        return result
    
    #***
    # Prefix Sum
    # TC: O(n)
    # sc: O(n)
    # https://hackmd.io/@Hungen/HysFuRadi
    def findMaxLength_2(self, nums) -> int:
        pref_sums = {0:-1}  # {1跟0的數量差: index}
        pref_sum = 0        
        result = 0

        for i in range(len(nums)):
            # if nums[i] == 0:
            #     pref_sum -= 1
            # else:
            #     pref_sum += 1
            pref_sum += 1 if nums[i] == 1 else -1
            
            # sum[0:j] - sum[0:i] = sum[i+1:j]
            if pref_sum in pref_sums:
                result = max(result, i-pref_sums[pref_sum])
            else:
                pref_sums[pref_sum] = i
        
        return result


'''
Medium
# Array
# Hash Table
# Prefix Sum
'''