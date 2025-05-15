'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # me
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        k = k % count

        if k == 0:
            return head

        cur = head
        for i in range(count-k-1):
            cur = cur.next
            
        res_head = cur.next
        cur.next = None

        cur = res_head
        while cur.next:
            cur = cur.next   
        
        cur.next = head
        
        return res_head
    
    #***
    # TC: O(N), SC: O(1)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        cur = head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
        
        cur.next = head # circle
        k = k % count

        cur = head
        for i in range(count-k-1):
            cur = cur.next
            
        res_head = cur.next
        cur.next = None
        
        return res_head


'''
Medium
# Linked List
# Two Pointers
'''
            
      