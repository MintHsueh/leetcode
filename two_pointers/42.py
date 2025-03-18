# 42. Trapping Rain Water
# Hard
# 2025/03/18 不熟

class Solution:
    # Two Pointer
    # TC: O(n), SC: O(1)
    def trap(self, height) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water = 0

        # 比較左右兩邊最長的bar，較短的那邊移動指針
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += r_max - height[r]
        
        return water