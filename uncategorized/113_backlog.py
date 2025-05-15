# 113. Path Sum II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 看別人做法
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        def helper(root, target, path):
            if not root:
                return

            if root.val == target and not (root.left or root.right):
                paths.append(path+[root.val])
                return

            helper(root.left, target-root.val, path+[root.val])
            helper(root.right, target-root.val, path+[root.val])
        
        paths = []
        helper(root, targetSum, [])
        return paths
