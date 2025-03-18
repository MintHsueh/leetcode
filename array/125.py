# 125. Valid Palindrome
# Easy
# 2025/03/17

class Solution:
    # Reverse String
    # TC: O(n), SC: O(n)
    def isPalindrome(self, s: str) -> bool:
        s_tran = ("".join(filter(str.isalnum, s))).lower()
        return s_tran == s_tran[::-1]
    
    def isPalindrome_2(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
    
    # ***
    def isPalindrome_2(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1]

'''
Notes:

1. String 字元/Case 調整大小寫
    .upper() ：全數變成大寫
    .lower() ：全數變成小寫
    .title() ：單字字首大寫
    .capitalize() ：字首變成大寫
    .swapcase() ：大小寫轉換

2. str.isalnum()
    isalnum() 方法檢測字串是否由字母和數字組成 return true or false

3. 其他字串處理
    https://ithelp.ithome.com.tw/m/articles/10269203 

'''