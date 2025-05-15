'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # me: hash table
    def middleNode(self, head: ListNode) -> ListNode:
        nodes = {}
        count = 0
        
        while head:
            nodes[count] = head
            head = head.next
            count += 1
        
        return nodes[count//2]
    
    # Two-Pointers
    # TC: O(N), SC(O1)
    # https://vocus.cc/article/6588e890fd89780001c3f462
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head          # fast 速率是 slow 的 2 倍，所以當 fast 跑到終點時的當下，slow 跑到終點的一半距離 (d = vt)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

'''
# Easy
# Linked List
# Two Pointers
'''