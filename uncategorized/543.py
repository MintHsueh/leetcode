'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n), where n is the number of nodes in the binary tree. The algorithm visits each node once.
    # Space complexity: O(h), where h is the height of the binary tree. This represents the maximum depth of the recursive call stack. In the worst case, the space complexity is O(n) for a skewed tree, and in the best case, it is O(log n) for a balanced tree.
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def depth(root):
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            self.result = max(self.result, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
    
        self.result = 0
        depth(root)
        return self.result

'''
Easy
# Tree
# Depth-First Search
# Binary Tree
'''