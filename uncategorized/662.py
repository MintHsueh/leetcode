# 662. Maximum Width of Binary Tree

# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree_tuple(self, root: TreeNode) -> int:
        q = deque([(root, 0)])
        w = 1
        while q:
            _, start = q[0]
            for i in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx*2))
                if node.right:
                    q.append((node.right, idx*2+1))
            w = max(w, idx-start+1)
        return w
    
    # 改 val
    def widthOfBinaryTree_val(self, root: TreeNode) -> int:
        q = deque([root])
        root.val = 0
        w = 0

        while q:
            w = max(w, q[-1].val - q[0].val + 1)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    node.left.val = node.val * 2 
                    q.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 1
                    q.append(node.right)
        
        return w