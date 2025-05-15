'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''


class Solution:
    def longestCommonPrefix_1(self, strs) -> str:
        strs.sort(key=len)
        result = ""
        i = 0
        while i < len(strs[0]):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return result
            result += char
            i += 1
        return result
    
    #***
    # Sorting a list of things is only O(n log n) if it is O(1) work to compare 2 things. 
    # For strings ordered lexographically, we start comparing the first character and keep going up to the end. 
    # In the worst case, all m characters are needed to do 1 comparisons.
    # Since the worst case cost of comparing two strings is m, then the worst case sorting here is O(nlogn * m), 
    # then there is the additional 2*m scan to compare the first and last. So the runtime for this solution is O(nlogn m + 2m).
    def longestCommonPrefix_2(self, strs) -> str:
        strs.sort() # 排序後，只需比較第一個 & 最後一個 elm   
        result = ""
        first, last = strs[0], strs[-1]     # 也可以不要sort, 只接取 first, last = min(strs), max(strs)
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result
    
print(Solution().longestCommonPrefix_2(strs = ["flower","flow","flight"]))


'''
Easy
# String
# Trie
'''