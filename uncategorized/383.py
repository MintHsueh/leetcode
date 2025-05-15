'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''

class Solution:
    # time complexity: O(n)
    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:
        ran_count = {}
        mag_count = {}

        for letter in ransomNote:
            if letter in ran_count:
                ran_count[letter] += 1
            else:
                ran_count[letter] = 1
        
        for letter in magazine:
            if letter in mag_count:
                mag_count[letter] += 1
            else:
                mag_count[letter] = 1
        
        for key, value in ran_count.items():
            if key not in mag_count:
                return False
            elif key in mag_count and value > mag_count[key]:   # elif value > mag_count[key]:
                return False
        return True
    

    def canConstruct_1_improved(self, ransomNote, magazine):
        chars = {}
        for char in magazine:
            if char not in chars: chars[char] = 1
            else: chars[char] += 1

        for char in ransomNote:
            if char in chars and chars[char] > 0: chars[char] -= 1
            else: return False
        
        return True
    

    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        ran_set = set(ransomNote)
        for letter in ran_set:
            if letter not in magazine:
                return False
            elif ransomNote.count(letter) > magazine.count(letter):
                return False
        return True


    #***
    # time complexity: O(n)     # The outer loop has O(1) complexity as there can be max 26 lowercase letters. So its complexity will be O(n).
    def canConstruct_2_improved(self, ransomNote: str, magazine: str) -> bool:
        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True


'''
Easy
# Hash Table
# String
# Counting
'''