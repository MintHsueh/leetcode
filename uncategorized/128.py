# 128. Longest Consecutive Sequence

class Solution:
    # TC: O(nk), k is the longest lenght
    def longestConsecutive(self, nums) -> int:
        max_length = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + 1 in nums:
                    length += 1
                    num += 1
                max_length = max(max_length, length)
        
        return max_length

    # TC: O(n log n)
    def longestConsecutive_sort(self, nums) -> int:
        if not nums:
            return 0

        nums.sort()
        max_length, length = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                length += 1
            else:
                max_length = max(length, max_length) 
                length = 1

        max_length = max(length, max_length) 
        return max_length