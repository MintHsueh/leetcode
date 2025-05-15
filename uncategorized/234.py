'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # me: stack
    # TC: O(N), SC: O(N)
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        while head:
            if head.val != stack.pop():
                return False
            head = head.next
        return True

        # # list
        # left, right = 0, len(stack)-1
        # while left < right:
        #     if stack[left] != stack[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True 

class Solution:
    # Two pointers
    # TC: O(N), SC: O(1)
    def reverseList(self, head: ListNode) ->ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverseList(slow)    # 原本的 head 改變了

        # print('head:', head)
        # print('rev:', rev)

        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True

        
        

'''
Easy
# Linked List
# Two Pointers
# Stack
# Recursion
'''