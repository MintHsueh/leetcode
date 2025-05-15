'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# SC??
# The space complexity of the method is O(h), where h is the height of the binary tree. 
# This is because the method uses recursive calls, and the maximum number of function calls on the call stack is equal to the height of the binary tree. 
# In the worst case, the binary tree is skewed, and the height is equal to the number of nodes in the tree, making the space complexity O(n). 
# However, in a balanced binary tree, the height is log(n), making the space complexity O(log(n)).

class Solution:
    # recursive DFS
    # TC: O(n)
    # SC: O(N) Recursive stack space?
    def invertTree_recursive(self, root:TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        else:
            return
        
    def invertTree_recursive_2(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    # iterative DFS
    # TC: O(n)
    # SC: O(N)
    def invertTree_iterative(self, root:TreeNode) -> TreeNode:
        if not root:
            return
        
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


'''
Easy
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
'''