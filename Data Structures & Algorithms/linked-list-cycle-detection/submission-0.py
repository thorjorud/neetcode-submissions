# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Time Complexity:
        - Brute Force (Hash Set): O(n) time, but uses O(n) extra space to store seen nodes.
        - Floyd's Algorithm (Two Pointers): O(n) time.
            * No cycle: 'fast' reaches the end in n / 2 steps -> O(n).
            * Has cycle: 'fast' gains 1 node on 'slow' each iteration, catching up in at most 'n' steps.

    Space Complexity:
        - Brute Force (Hash Set): O(n) space for the set.
        - Floyd's Algorithm (Two Pointers): O(1) space (only two pointers, regardless of list size).
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Start both pointers at the head of the linked list.
        slow, fast = head, head

        # Keep running as long as the fast runner hasn't  hit the end of the line.
        while fast and fast.next:
            slow = slow.next          # Slow runner moves 1 step forward
            fast = fast.next.next     # Fast runner moves 2 steps forward
            
            # Did the fast runner lap the slow runner?
            if slow == fast:
                return True # The met! That means there IS a cycle.

        # Fast runner hit the end safely. 
        return False        # No cycle exists.
