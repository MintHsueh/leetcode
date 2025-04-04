# 153. Find Minimum in Rotated Sorted Array (Compare with 33)
# Medium
# 2025/04/04 不熟

class Solution:
    # TC: O(logN), SC: O(1)
    def findMin(self, nums) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
