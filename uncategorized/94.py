'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# l3_node = TreeNode(val=3, left=None, right=None)
# l2_node = TreeNode(val=2, left=l3_node, right=None)
# root = TreeNode(val=1, left=None, right=l2_node)

class Solution:
    # iteration
    # TC: O(n), where n is the total number of nodes.
    # sc: O(n)
    def inorderTraversal_1(self, root: TreeNode):  
        result = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result
    
    # Recursion
    # TC: O(n), where n is the total number of nodes.
    # sc: O(n)
    def inorderTraversal(self, root):
        result = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result


# Depth-First Search:
# 1. PreOrder: root, left, right
# 2. InOrder: left, root, right
# 3. PostOrder: left, right, root

'''
Easy
# Stack
# Tree
# Depth-First Search
# Binary Tree
'''