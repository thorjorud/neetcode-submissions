from collections import deque

class Solution:
    '''
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    '''
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        # Find all treasure chests and add them to the queue.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Directions for up, down, left, right
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited):
                        grid[nr][nc] = grid[r][c] + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc))