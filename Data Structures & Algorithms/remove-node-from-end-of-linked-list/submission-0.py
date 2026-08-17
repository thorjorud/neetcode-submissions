# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Time Complexity: O(n)
        - Each pointer only hits each node up to one time.
    Space Complexity: O(1)
        - We only use basic pointer variables.
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right ahead n steps.
        for _ in range(n):
            right = right.next

        # Slide both pointers ahead one by one to keep the gap until right hits None.
        while right:
            left = left.next
            right = right.next

        # Unlinks the target node.
        left.next = left.next.next

        return dummy.next