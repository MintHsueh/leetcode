'''
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 
Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n * m)???
    # n is the number of nodes in the root tree.
    # m is the number of nodes in the subRoot tree.
    # In the worst case, the algorithm may need to compare each node in the root tree with the entire subRoot tree.

    # Space complexity: O(h)
    # h is the height of the call stack during the recursive traversal.
    # In the worst case, when the trees are skewed (completely unbalanced), the space complexity is O(n).
    # In the best case, when the trees are perfectly balanced, the space complexity is O(log(n)).

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSame(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            return r.val == s.val and isSame(r.left, s.left) and isSame(r.right, s.right)
        
        if root and subRoot:
            if isSame(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)