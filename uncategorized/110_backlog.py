'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: 

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive DFS
    # Time complexity: O(n), The algorithm performs a depth-first traversal of the binary tree, visiting each node once.
    # Space complexity: O(h), where h is the height of the binary tree
        # The space complexity is determined by the maximum height of the call stack during the recursive DFS traversal.
        # In the worst case, when the tree is skewed (completely unbalanced), the space complexity is O(n).
        # In the best case, when the tree is perfectly balanced, the space complexity is O(log(n)).
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1
        
        if not root:
            return True
        
        if abs(depth(root.left) - depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        else:
            return False
        
    # ***
    # 一旦發現高度相差超過1的情形,就讓測最大深度函式的最終回傳值變為-1, 最後只要看結果是否等於-1就知道該樹是否是高度平衡二元樹了
    def isBalanced_2(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            if left_depth != -1 and right_depth != -1 and abs(left_depth - right_depth) <= 1:
                return max((left_depth, right_depth)) + 1
            else:
                return -1
        
        return depth(root) != -1
    
'''
Easy
# Tree
# Depth-First Search
# Binary Tree
'''