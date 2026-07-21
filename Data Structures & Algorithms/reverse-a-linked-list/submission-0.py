# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    '''
    Brute Force Approach: We could first create a copy of the linked list 
    using a stack. Then iterate through the linked list again rewriting the
    nodes from the end of the stack.
        - Time Complexity: O(n)
        - Space Complexity: O(n)
    '''