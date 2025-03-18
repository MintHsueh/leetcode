# 20. Valid Parentheses
# Eazy
# 2025/03/18

class Solution:
    # TC: O(n), sc: O(n)
    def isValid(self, s: str) -> bool:

        # 可省略
        if len(s) % 2:  # if len(s) % 2 > 0
            return False

        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
   
        for b in s:
            if b in brackets:
                stack.append(b)
            elif not stack or b != brackets[stack.pop()]: # 記得 if note stack, 否則可能 stack 沒東西 pop
                    return False
        
        return not stack 

        # return not stack 等同於:
            # return len(stack) == 0  或
            
            # if stack:
            #     return False
            # return True