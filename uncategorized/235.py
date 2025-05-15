# 235. Lowest Common Ancestor of a Binary Search Tree

class Solution:
    # Time complexity: O(h)
    # h is the height of the tree.
    # In the worst case, when the tree is skewed (completely unbalanced), the time complexity is O(n), where n is the number of nodes in the tree.
    # Space complexity: O(1)
    # The algorithm uses only a constant amount of extra space.
    def lowestCommonAncestor(self, root, p, q):
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

