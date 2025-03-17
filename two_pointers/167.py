# 167. Two Sum II - Input Array Is Sorted
# Medium
# 2025/03/17

class Solution:
    # Two Pointers
    # TC: O(n logn), SC: O(1)
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
    
    # Consider putting the first condition (if nums[l] + nums[r] == target: return (l + 1, r + 1)) to be the last,
    # since only once it will evaluate to True.
    # Also, there is exactly one solution, so you don't have to check l<r in the while loop - you can just do while True.
    def twoSum_improved(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while True:   
            if target > numbers[i] + numbers[j]:
                i += 1
            elif target < numbers[i] + numbers[j]:
                j -= 1
            else:
                return [i + 1, j + 1]    # you only get to this line once
