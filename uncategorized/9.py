'''
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_reversed = ""
        # for i in range(len(str(x))-1, -1, -1):
        #     x_reversed += str(x)[i]
        # return str(x) == x_reversed
    
        return str(x) == str(x)[::-1]
    
    # ***
    def isPalindrome_noStr(self, x: int) -> bool:
        x_copy = x
        x_reversed = 0
        while x_copy > 0:
            x_reversed = (x_reversed * 10) + (x_copy % 10)
            x_copy = x_copy // 10
        return x == x_reversed

a = Solution().isPalindrome(x = 121)
print(a)


'''
Easy
# MaTh
'''

