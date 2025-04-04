# 33. Search in Rotated Sorted Array (Compare with 153)
# Medium
# 2025/04/04 不熟

class Solution:
    # python's list.index()
    # TC: O(n), SC: O(1)
    def search(self, nums, target) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
    
    # ***
    # binary search
    # TC: O(log⁡n), SC: O(1)
    def search_2(self, nums, target) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] < nums[r]:               # right side is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:                               # left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
                 
