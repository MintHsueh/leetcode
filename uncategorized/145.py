'''
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# iteration?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iteration: reversed(root-右-左) = 左-右-root
    # TC: O(n), where n is the total number of nodes.
    # sc: O(n)
    def postorderTraversal_ite(self, root: TreeNode):
        result, stack = [], []

        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            root = stack.pop()
            root = root.left

        return result[::-1]


    # Recursion
    # TC: O(n), where n is the total number of nodes.
    # sc: O(n)
    def postorderTraversal_rec(self, root: TreeNode):
        result = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        postorder(root)
        return result

'''
Easy
# Stack
# Tree
# Depth-First Search
# Binary Tree
'''