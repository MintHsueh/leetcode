'''
136. Single Number

'''

class Solution:
    def singleNumber(self, nums) -> int:
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        for key, value in num_count.items():
            if value == 1:
                return 
    
    # to long        
    def singleNumber_2(self, nums) -> int:
        num_set = set(nums)
        for num in num_set:
            if nums.count(num) == 1:
                return num
    
    # ***
    # Use Xor/Bit Manipulation: Xor of any two num gives the difference of bit as 1 and same bit as 0.
    # e.g. 0^a=a,a^a=0, 0^a^b^c^b^a=c 
    # Time: O(n), Space: O(1)
    def singleNumber_XOR(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result 

'''
Easy
# Array
# Bit Manipulation
'''