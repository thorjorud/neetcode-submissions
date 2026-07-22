# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n + m) 
            - Where n and m are the lengths of list1 and list2. We visit each node at most once.

            Space Complexity: O(1) 
            - We re-link existing nodes in-place without creating extra nodes or using recursive call stack space.
        """
        # Create a fake start node dummy (to keep track of the beginning of our new merged list).
        # Set tail to point to the head of dummy.
        dummy = ListNode()
        tail = dummy

        # Compare the heads of list1 and list2 while they both nodes.
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 # Connect tails arrow to list1's node.
                list1 = list1.next  # Step list1 forward to its next node.
            else:
                tail.next = list2 # Connect tails arrow to list2's node.
                list2 = list2.next # Step list2 forward to its next node.
            
            tail = tail.next # Move tail forward to the newly attached node.

        # 3. Attach whatever is left over from either list directly to the end
        tail.next = list1 if list1 else list2

        # 4. Return the head of the real list (skipping our dummy placeholder)
        return dummy.next

        """
        Brute Force Approach:
        Extract all node values from both linked lists into a standard Python list, sort 
        the list, and then build a brand new linked list using those sorted values.

        Steps:
            1. Traverse list1 and append every node's value to an array.
            2. Traverse list2 and append every node's value to the same array.
            3. Sort the array using Python's built-in sort (Timsort).
            4. Iterate through the sorted array and instantiate new ListNode objects to create the merged list.

        Complexity Analysis:
            - Time Complexity: O((n + m) log(n + m)) 
                - Collecting values takes O(n + m), but sorting an array of size (n + m) dominates the runtime.
            - Space Complexity: O(n + m) 
                - Requires extra memory to store the array of values and create (n + m) new ListNode objects.
        """