"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    '''
    Time Complexity: O(V + E)
        - V = number of vertices (or nodes).
        - E = number of edges (lines connecting nodes).
    Space Complexity: O(V)
        - Our dfs() stores a copy of each node. 
        - The call stack can grow up to the size of the number of nodes.
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_copy = {} # Maps original node to new copy node.

        def dfs(curr):
            if not curr:
                return None

            if curr in old_to_copy:
                return old_to_copy[curr]

            copy = Node(curr.val)
            old_to_copy[curr] = copy
            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        
        return dfs(node)