'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 

Example 2:
Input: root = [1,null,2]
Output: 2
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''
# SC?

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    # Time complexity: O(n). n is the total number of nodes in the binary tree.
    # ??Space complexity: O(h). h is the height of the binary tree. but in the worst case, it can be as large as O(n)
    def maxDepth_DFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # BFS
    # Time complexity: O(n). n is the total number of nodes in the binary tree.
    # Space complexity: O(w). w is the maximum width of the tree (worst-case O(n)).
    def maxDepth_BFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return depth
        





'''
Easy
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
'''