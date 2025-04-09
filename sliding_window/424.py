# 424. Longest Repeating Character Replacement
# Medium
# 2025/04/07 不熟

from collections import defaultdict

class Solution:
    # key: 視窗長度 - 最常出現的字母數量 ≤ k; 若超過 k, 就要把 left 向右縮小
    
    # TC: O(n), SC: O(m)
    # Where n is the length of the string and m is the total number of unique characters in the string.
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        count = defaultdict(int)    # 記錄每個字母出現的次數
        max_freq = 0                # 出現最多的字母次數

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if right - left + 1 - max_freq > k: # 如果目前這個視窗需要替換的字母超過 k，就縮小視窗
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

'''
Notes

關於沒有即時更新正確的 max_freq 問題：

有時候視窗縮小後 (left-1), max_freq 對應的字母數量已經減少了 (e.g. 最大頻率的 3 個 A 變為 2 個 A)
但如果接下來加入的是別的字母, 且這個字母出現次數還沒超過原本的 max_freq (這次迭代出現 B, 而目前 B 的數量 < 3)
那 max_freq 就不會被更新，依舊是「暫時過時」的值 (max_freq 則會依舊保持 3 而非正確地更新成 2)

但! 沒有每次都正確 max_freq 沒關係
因為視窗長度不變 (left 往右移一個, right 也往右前進一個)
不管是高估 max_freq, 或是正確的更新 max_freq 成更小的數字
right - left + 1 - max_freq > k 都成立
因此就算下次迭代依舊出現不合法的情況，儘管 max_freq 被高估，還是會照樣縮小視窗

這時候你可能會想說: 那如果 max_freq 變大了, 但沒被正確更新, 這條不等式可能就不成立了!
但是! 若 max_freq 要變大, 他就一定會正確更新成更大的, 因為:
如果有某個字母開始出現得比之前還多 (真的超過目前的 max_freq)
我們有用 max() 去比較, 它會自動把 max_freq 更新成正確值，這時候合情合理視窗就可以擴大

換句煥說:
若最高頻率的字母出現了, 一定就會正確更新 max_freq, 視窗長度能正確增加
否則若出現其他字母, max_freq 雖然被高估，但頂多就等於上一次的 max_freq
而上一次較大的 max_freq 都能滿足 right - left + 1 - max_freq > k
就代表真正更小的 max_freq 也能滿足這條式子
所以遇到不合法的情況, 即使 max_freq 被高估, 還是會乖乖縮小視窗

結論:
1. 如果當出現一個字母數量 > 目前的 max_freq, 那它一定會讓 max_freq 被更新 (因為 max())
2. 而其他情況出現不重要字母時, 高估 max_freq 沒關係, 不管 max_freq 維持一樣或更小, 都會縮短視窗
3. 所以沒準確更新 max_freq 沒關係，重點是我們永遠不會「錯過更新 max_freq 成更大的時候」

(卡超久嗚嗚)
'''