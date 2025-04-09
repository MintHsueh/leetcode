# 3. Longest Substring Without Repeating Characters
# Medium
# 2025/04/06 不熟

class Solution:
    # 設計一個 Sliding Window (左 index 為left, 右index 為 right)，從左到右掃描
    # 記錄每個字元最後一次出現的位置、檢查當下這個字元以前是否出現過、更新窗的最大長度(right-left+1)。
    # 如果當下字元以前出現過，且上次出現的位置在目前的窗範圍裡 (index >= left)，就把 left 往右移到此字元上次出現的位置 + 1 
    # 如果當下字元以前出現過但不在窗裡，或以前沒有出現過，就維持 left 繼續擴展right，
    
    # TC: O(n), SC: O(m)
    # Where n is the length of the string and m is the total number of unique characters in the string.
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0    
        seen = {}  
        
        for right in range(len(s)):  
            if s[right] in seen and seen[s[right]] >= left: # 記得(seen[s[right]] >= left), 確認上一次見到 s[right] 的 index 是在 current window 裡
                left = seen[s[right]] + 1  
            
            seen[s[right]] = right  
            max_len = max(max_len, right - left + 1)   
        
        return max_len

    