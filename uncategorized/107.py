# 107. Binary Tree Level Order Traversal II

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        result = []
        queue = deque([root])

        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if temp:
                result.append(temp)
        
        return result[::-1]