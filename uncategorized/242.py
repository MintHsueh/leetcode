'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''

class Solution:

    # this approach has a time complexity of O(n log n) due to the sorting operation, where n is the length of the strings.
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # The time complexity of this solution is O(n), where n is the total number of characters in both strings.
    def isAnagram_2(self, s: str, t: str) -> bool:
        def helper(word):
            count = {}
            for i in word:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            return count
        
        return helper(s) == helper(t)   # 兩個字典成分一樣就相同,順序不一樣沒關係
        

# Easy
        
# Hash Table
# String
# Sorting