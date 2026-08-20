# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [True, 0]

            left = dfs(curr.left)
            right = dfs(curr.right)

            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            height = 1 + max(left[1], right[1])

            return [balanced, height]

        return dfs(root)[0]