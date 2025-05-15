'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

'''
# how to do recursion?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # me
    def reverseList(self, head: ListNode) ->ListNode:
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        dummy = curr = ListNode()
        while node_list:
            curr.next = node_list.pop()
            curr = curr.next
        curr.next = None
        return dummy.next
    
    # ***
    # Iterative Approach
    # TC: O(n), SC: O(1)
    # https://www.youtube.com/watch?v=FsZaXsvL64U&ab_channel=LeetCodeWithMonu
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

'''
Easy
# Linked List
# Recursion
'''