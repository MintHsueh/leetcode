# 567. Permutation in String
# Medium
# 2025/04/08 不熟

from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # key: 記錄 s1 每個字母的數量, 滑窗遍歷s2, 比對s2跟s1的字母數量
        
        # TC: O(m+n), m=len(s1), n=len(s2) 
        # SC: O(1) 兩個字典最多 26 個 key
        count = defaultdict(int)
        for s in s1:
            count[s] += 1
        
        l = 0
        for r in range(len(s2)):
            count[s2[r]] -= 1
            
            # 當字母在視窗中「超過應有的次數」或「不該出現」, 要不斷縮小左邊界，直到視窗內字母合法為止
            while count[s2[r]] < 0:
                count[s2[l]] += 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
                
        return False

'''
Notes:

解題思路: 
1. count 記錄 s1 每個字母出現的次數
2. 遍歷 s2, 用 sliding window 從 count 中扣掉對應字母的數量
3. 如果 count[char] < 0, 代表:
    - 該字母在視窗中「出現超過該有次數」，或
    - 根本不該出現 (s1 裡沒有)
    此時就要不斷縮小左邊界，直到視窗重新回到合法狀態 (count 回到符合 s1 的配對)

4. 當所有字母的 count 都沒有 < 0, 且視窗長度剛好等於 len(s1) → 成功找到 permutation!
    - count >= 0 代表目前視窗內沒有多餘或不該出現的字母, 視窗長度=len(s1) 代表每個字母都出現剛剛好
    - 此時 s1 所有字母的需求都被「剛好配對」, 也就是 count 中所有值都回到 0

''' 