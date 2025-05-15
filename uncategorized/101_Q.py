'''
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''
# 待看 iterative

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive
    # TC: O(n)
    def isSymmetric_recursive(self, root: TreeNode) -> bool:
        def isSame(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return isSame(l.left, r.right) and isSame(l.right, r.left)
        
        if not root:
            return True
        else:
            return isSame(root.left, root.right)    #為什麼要return?
    
    # # iterative?
    # def isSymmetric(self, root):
    #     queue = [(root, root)]
    #     while queue:
    #         l, r = queue.pop(0)
    #         if l is None and r is None:
    #             continue

    #         if l is None or r is None:
    #             return False
    #         if l.val == r.val:
    #             queue.append((l.left, r.right))
    #             queue.append((l.right, r.left))
    #         else:
    #             return False
    #     return True

'''
Easy
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
'''