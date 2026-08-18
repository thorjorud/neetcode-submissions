"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Stores original nodes to their new copy.
        old_to_copy = {None : None}

        curr = head
        # Create copies of original nodes and map them to their original.
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        # Wire up random and next to the copy nodes we made.
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        # Return head of copy list.
        return old_to_copy[head]