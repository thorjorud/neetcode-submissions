# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        # Offset fast by one to make sure we find the correct middle node.
        slow, fast = head, head.next

        # When fast hits the end, slow will be at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the 2nd half of the list.

        # First node of 2nd half.
        second = slow.next
        # Cuts off the first half of the list.
        slow.next = None
        # Stores the head of our reversed list.
        prev = None

        while second:
            tmp = second.next # Saves rest of list.
            second.next = prev # Reverse the pointer to point back to prev.
            prev = second      # Move prev forward to the current node.
            second = tmp # Move second forward to the saved next node.

        # Merge/Zipper the two halves together.
        first = head    # Start of the first half
        second = prev   # Start of the reversed second half.

        while second:
            # Save the rest of the halves.
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            # Move both pointers forward.
            first = tmp1
            second = tmp2

        '''
        Brute Force Approach: We can save all the nodes in an array. We
        then can use a two pointer approach to reorder the nodes. We then
        point the last element to None to ensure no cycle exists.
            - Time Complexity: O(n)
            - Space Complexity: O(n)
                * O(n) since we need to allocate an array to store the nodes.
        '''

