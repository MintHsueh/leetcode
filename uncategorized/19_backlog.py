'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?

'''
# how to do Two Pointers?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC: O(N), SC: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        if count - n == 0:
            return head.next

        curr = head
        for i in range(count-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
    
        # i = 1
        # while curr and curr.next:
        #     if i == count - n:
        #         curr.next = curr.next.next
        #         return head
        #     curr = curr.next
        #     i += 1
      
        
'''
Medium
# Linked List
# Two Pointers
'''