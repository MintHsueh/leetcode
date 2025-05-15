# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: The time complexity for this approach is (O(n)), where (n) is the number of elements in the array. This is because we are visiting each element once while constructing the BST.
    # Space complexity: The space complexity is (O(n)) as well. This is because, in the worst-case scenario, we could end up with a recursive call stack depth of (n) during the creation of the BST.
    def sortedArrayToBST(self, nums) :
        if len(nums) == 0:  # if not nums:
            return 
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root