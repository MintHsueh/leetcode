# 76. Minimum Window Substring
# Hard
# 2025/04/09 不熟

from collections import defaultdict
class Solution:
    # key: 用 sliding_window 記錄目前的字母頻率，當視窗內剛好包含 t 所有字母且數量符合，就縮小左邊找最短答案。
    
    # TC: O(n + m). n=len(S), m=len(t)
    # SC: O(1). 兩個 dict 最多都只會記錄 26 個小寫英文字母
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        
        window_count = defaultdict(int)
        min_len = float("inf") # len(s)
        result = ""
        matches = 0     # 視窗裡滿足需求的字母個數

        l = 0
        for r in range(len(s)):
            window_count[s[r]] += 1
            
            # 不可以寫 if window_count[s[r]] == t+count[s[r]]: 這樣會增加一堆值為 0 的 key, 後面要求字母種類數量 len(t_count) 會錯 (除非一開始不要用 defaultdict())
            # 或寫成 if s[r] in t_count and window_count[s[r]] == t_count[s[r]]: 
            if window_count[s[r]] == t_count.get(s[r], 0): 
                matches += 1
            
            while matches == len(t_count):  # 不要 len(set(t)), 時間會爆掉
                if r - l + 1 <= min_len:
                    min_len = r - l + 1
                    result = s[l:r+1]
                
                # 從左邊縮小視窗長杜
                if s[l] in t_count:
                    if window_count[s[l]] == t_count[s[l]]: # 記得加這行，否則如果只需要一個 B，但 window 裡現在有 2 個 B，會錯把 matches-1
                        matches -= 1
                    window_count[s[l]] -= 1
                l += 1
        
        return result


'''
Notes

解題思路: 
1. 記錄需求字母數量
    用 t_count 統計 t 裡每個字母需要幾個

2. 滑動視窗遍歷 s
    用 window_count 記錄目前視窗中有哪些字母 & 各出現幾次

3. 用 matches 來追蹤「幾個字母達成需求」
    每次當 window_count[c] == t_count[c] 就代表這個字母達標 → matches += 1

4. 當所有需求字母都達標時 (matches == len(t_count)) → 嘗試縮左邊找更短的視窗

5. 縮左邊時，若縮掉的是剛好達標的字母，要 matches -= 1

'''