# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Time Complexity: O(m + n)
    Space Complexity: O(m + n) or O(1)
        - O(1) if we dont count the linkedlist we made as auxiliary space.
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10 # Finds number that carrys over to next column.
            new_val = total % 10 # Finds number that stays in column and gets attached.

            curr.next = ListNode(new_val)
            
            # Advance pointers.
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


