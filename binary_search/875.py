# 875. Koko Eating Bananas
# Medium
# 2025/04/03

import math
class Solution:
    # TC: O(n*logm), SC: O(1)
    # Where n is the length of piles and m is the maximum number of bananas in a pile.
    def minEatingSpeed(self, piles, h: int) -> int:
        l = 1             # l 為最小速度, 起始設為 1 
        r = max(piles)    # r 為最大速度
        
        while l < r:
            m = (l + r) // 2
            time = 0
            for n in piles:
                time += math.ceil(n / m)
            if time <= h:   # 在速度 m 之下, 可吃完所有香蕉, 更新 r
                r = m
            else:           # 在速度 m 之下，吃不完所有香蕉, 更新 l
                l = m + 1
        
        return l

'''
Notes: python 各種取整

import math

1. 向上取整: math.ceil()
    math.ceil(-0.5) -> 0
    math.ceil(0.3) -> 1

2. 向下取整: math.floor() & "//"
    (-3) // 2 -> -2  # math.floor(-1.5) -> -2        
    3 // 2 -> 1      # math.floor(1.5) -> 1           

3. 向0取整: int()
    int(-0.5) = 0
    int(0.5) = 0

4. 四舍五入: round() ps.但當小數末尾為 5: , 末尾前一位為基數則進位，為偶數則捨棄
    round(-2.5) -> -2
    round(-1.5) -> -2
    round(-0.5) -> 0
    round(0.5) -> 0
    round(1.5) -> 2
    round(2.5) -> 2

'''