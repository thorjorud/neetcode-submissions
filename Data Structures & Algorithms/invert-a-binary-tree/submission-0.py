# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(h)
            - Where h is the height of the tree corresponding to the max
            depth of the call stack (which is O(n) in the worst case for a skewed
            tree or O(log n) for a balanced tree).
        '''

        # If the node dosen't exist, stop recursion.
        if not root:
            return None

        # Swap the left and right children.
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree
        self.invertTree(root.left)

        # Recursively invert the right subtree
        self.invertTree(root.right)

        # Return the root of the inverted tree.
        return root

        '''
        Brute Force Approach: Use an iterative BFS approach.
            Time Complexity: O(n)
            Space Complexity: O(n)
        '''