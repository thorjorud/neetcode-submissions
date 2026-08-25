# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Time: O(n)
        - For each node we do the 4 constant operations.
    Space: O(1)
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            nxt = curr.next # Keep track of rest of list.
            curr.next = prev # Re-wire curr backward to prev.

            # Move ahead prev and curr.
            prev = curr
            curr = nxt

        return prev # Return new head.