# 150. Evaluate Reverse Polish Notation
# Medium
# 2025/03/21

class Solution:
    # stack
    # TC: O(N), SC: O(N)
    def evalRPN(self, tokens) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            elif t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                post = stack.pop()
                pre = stack.pop()
                stack.append(pre - post)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                post = stack.pop()
                pre = stack.pop()
                stack.append(int(pre / post)) # 6 // -132 = -1 not 0
        return stack[-1]

'''
Notes:
1. a // b: floor division, 無條件往下取整
    5 // 2 = 2	    # 2.5 向下取整是 2
    5 // -2 = 3	    # -2.5 向下取整是 -3
    -5 // 2 = 3	    # -2.5 向下取整是 -3
    6 // -132 = -1	# -0.045 向下取整是 -1

2. int(a/b): truncation, 截斷除法, 直接去掉小數點
    int(6 / -132) = 0
'''