# 11. Container With Most Water
# Medium
# 2025/03/18

class Solution:
    # Two Pointers
    # TC: O(n), SC: O(1)
    def maxArea(self, height):
        max_amount = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                max_amount = max(max_amount, (r - l) * height[l])
                l += 1
            else:
                max_amount = max(max_amount, (r - l) * height[r])
                r -= 1
        
        return max_amount
    
    
    