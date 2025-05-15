# 103. Binary Tree Zigzag Level Order Traversal

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        queue = deque([root])

        n = 1
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.extend([node.left, node.right])

            if temp and n % 2 != 0:
                result.append(temp)
            if temp and n % 2 == 0:
                result.append(temp[::-1])
            n += 1

        return result
