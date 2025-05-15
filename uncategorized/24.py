'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC: O(N), SC: O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode()
        cur.next = head

        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            c = cur.next.next.next
            cur.next = b
            cur.next.next = a
            cur.next.next.next = c
            cur = cur.next.next

        return dummy.next

'''
Medium
# Linked List
# Recursion
'''