# 429. N-ary Tree Level Order Traversal

from collections import deque
'''
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
'''
class Solution:
    # BFS
    # Time: O(N), where N <= 10^4 is number of nodes in the tree.
    # Extra Space (without counting output as space): O(N), this is the memory to store elements in the queue. At most, the queue will have 2 layers of the tree on it at any given time.
        # In the best case, each level has only 1 node.
        # In the worst case, for example in balanced tree, there is about N/2 nodes in the lowest level.

    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            temp = []   # result.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)   # result[-1].append(node.val)
                queue.extend(node.children)
            result.append(temp)         # delete
        
        return result
        