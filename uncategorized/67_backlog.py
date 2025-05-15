'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''
# 待看別人的解法

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a) + int(b)
        answer = ''
        carry = 0

        for c in str(sum)[::-1] + '0':
            curr_num = int(c) + carry 
            carry = int(curr_num) // 2
            answer += str(int(curr_num) % 2)
        
        if answer[-1] == '0' and len(answer) > 1:
            return answer[-2::-1]
        else:
            return answer[::-1]
        
'''
Easy
Math
# String
# Bit Manipulation
# Simulation
'''