# 102. Binary Tree Level Order Traversal

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
            
        result = []
        layer = [root]
        
        while layer:
            layer_val = []
            next_layer = []
            for node in layer:
                layer_val.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            result.append(layer_val)
            layer = next_layer
        
        return result


    def levelOrder_deque(self, root: TreeNode):
        # from collections import deque
        result = []
        layer = deque([root])

        while layer:
            temp = []
            for i in range(len(layer)):
                node = layer.popleft()
                if node:
                    temp.append(node.val)
                    layer.extend([node.left, node.right])   # layer.append(node.left) /n layer.append(node.right)
            if temp:
                result.append(temp)
        
        return result