# 98. Validate Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        return helper(root, float('-inf'), float('inf'))

'''
時間複雜度：
每個節點都會被遍歷一次，因此時間複雜度是 O(n)，其中 n 是樹中節點的數量。
空間複雜度：
最壞情況下，樹是線性的（比如每個節點只有一個子節點），遞迴深度是 O(n)。最好的情況下，樹是平衡的，遞迴深度是 O(log n)。因此，空間複雜度是 O(h)，其中 h 是樹的高度。
'''