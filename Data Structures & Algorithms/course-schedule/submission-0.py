class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build map of what each course requires.
        pre_map = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # 0 = unvisited, 1 = currently visiting, 2 = safe
        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False # Found a cycle.
            if visited[course] == 2: 
                return True # Already checked this path, safe.

            visited[course] = 1 # Mark as visiting.

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False

            visited[course] = 2 # Mark as completely safe
            return True
        
        # Check every course in case the graph has seperate pieces.
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True