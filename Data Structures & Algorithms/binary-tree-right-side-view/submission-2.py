# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    '''
    Time: O(n)
        - Each node is append and popped once from the queue.
    Space: O(n)
        - The queue holds at most the max number of nodes present on any single level
        of the tree. In a full or complete binary tree, the bottom leaf level can hold
        up to [n / 2] nodes. The res array in the worst case can also take up to 
        the height of the tree h which is also bounded by O(n).
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            level_len = len(q)

            for i in range(level_len):

                node = q.popleft()

                if i == level_len - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res