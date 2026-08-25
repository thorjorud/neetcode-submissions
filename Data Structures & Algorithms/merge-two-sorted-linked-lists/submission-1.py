# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Time: O(n + m)
        - n is the # of nodes in list1.
        - m is the # of nodes in list2.
    Space: O(1)
        - We create one dummy node.
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Helps us keep track of head of merged list.
        builder = dummy # Helps us build re-wire the new list.

        while list1 and list2:
            if list1.val < list2.val:
                builder.next = list1 # Wire list1.val to builder.

                # Move both ahead by one.
                list1 = list1.next
                builder = builder.next
            else:
                builder.next = list2

                # Move both ahead by one.
                list2 = list2.next
                builder = builder.next
        
        if list1:
            builder.next = list1
        else:
            builder.next = list2

        return dummy.next