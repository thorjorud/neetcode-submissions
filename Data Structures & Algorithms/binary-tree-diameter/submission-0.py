# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(h)
        - Depending on the height of the call stack.
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 # Holds max diameter found.

        def dfs(curr):
            nonlocal res # Allows us to modify res from within this function.

            if not curr: # If current branch points to None its height is 0.
                return 0

            left = dfs(curr.left) # Find left childs height.
            right = dfs(curr.right) # Find right childs height.

            res = max(res, left + right) # Updates total max height found.

            return 1 + max(left, right) # Returns taller side + 1 (to count for current Node) to parent.

        dfs(root)
        return res