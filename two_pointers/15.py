# 15. 3Sum
# medium
# 2025/03/18

class Solution:
    # Two Pointer
    # TC: O(n^2) 
    # SC: O(n) Depends on language you use. In python, sorting algorithm use Timsort which uses O(n) space.
    def threeSum_3(self, nums):
        nums.sort()
        result = []

        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:  # 移動第一個指針時，若遇到重複數字則跳過
                continue

            m = l + 1
            r = len(nums) - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total < 0:
                    m += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m-1] and m < r:   # 移動第二個指針時，若遇到重複數字則跳過 (記得 m<k 否則 list index out of range)
                        m += 1
        return result


