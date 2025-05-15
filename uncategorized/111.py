# 111. Minimum Depth of Binary Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #***
    # BFS
    def minDepth_bfs(self, root:TreeNode):
        if not root:
            return 0
        
        depth = 1
        que = deque([root])

        while que:
            for i in range(len(que)):
                node = que.popleft()
                if not node:
                    continue
                if not node.left and not node.right:
                    return depth
                else:
                    que.append(node.left)
                    que.append(node.right)
            depth += 1
    
    # DFS
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
                    
        
        