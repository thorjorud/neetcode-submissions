from collections import deque

class Solution:
    '''
    Time: O(V + E)
    Space: O(V + E)
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for cor, pre in prerequisites:
            adj[pre].append(cor)
            indegree[cor] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return res if len(res) == numCourses else []

