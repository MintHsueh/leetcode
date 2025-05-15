'''
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
 
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

'''

# O(1) memory?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # me
    # TC: O(NlogN), SC: O(N)
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        node_lst = []
        while cur:
            node_lst.append(cur.val)
            cur = cur.next
        
        node_lst.sort()

        nxt = None
        while node_lst:
            cur = ListNode(node_lst.pop(), nxt)
            nxt = cur
        
        return cur
    
    # Extract and Fill
    # TC: O(NlogN), SC: O(N)
    def sortList(self, head: ListNode) -> ListNode:
        cur, arr = head, []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        arr.sort()

        cur, i = head, 0
        while cur:
            cur.val = arr[i]
            i += 1
            cur = cur.next
        
        return head
    

'''
Medium
# Linked List
# Two Pointers
# Divide and Conquer
# Sorting
# Merge Sort
'''