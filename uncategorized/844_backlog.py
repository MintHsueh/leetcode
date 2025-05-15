'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 
Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?

'''

# class Solution:
#     # Time complexity: O(n^2)
#     def backspace(self, strig):
#         strig_list = list(strig)
#         while "#" in strig_list:    # i in list → O(n)
#             if strig_list[0] == "#":
#                 strig_list.remove("#")
#             else:
#                 strig_list.pop(strig_list.index("#")-1) # list.pop(index) → O(n)
#                 strig_list.remove("#")  # list.remove() → O(n)
#         return strig_list
    
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         return self.backspace(s) == self.backspace(t)


class Solution:
    # Time complexity: O(n^2)
    def backspaceCompare(self, s: str, t: str) -> bool:
    
        def backspace(strig):
            strig_list = list(strig)
            while "#" in strig_list:    # i in list → O(n)
                if strig_list[0] == "#":
                    strig_list.remove("#")
                else:
                    strig_list.pop(strig_list.index("#")-1) # list.pop(index) → O(n)
                    strig_list.remove("#")  # list.remove() → O(n)
            return strig_list
        
        return backspace(s) == backspace(t)
    

    #***
    # stack
    # Time complexity: O(n) // Both strings are traversed once, where n is the total length of the strings s and t.
    # Space complexity: O(n) // In the worst case, if there are no backspaces, the entire string might be stored in the stack.
    def backspaceCompare_2(self, s: str, t: str) -> bool:

        def backspace(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return backspace(s) == backspace(t)
    
print(Solution().backspaceCompare(s = "ab#c", t = "ad#c"))

# Two Pointers?


'''
Easy
# Two Pointers
# String
# Stack
# Simulation
'''