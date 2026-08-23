from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        # Track amount of fresh fruits and add rotten fruit coords initially.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            # Loop through each number of rotten fruits at the moment.
            for i in range(len(q)):
                r, c = q.popleft() # Pop rotten fruit coords from queue.

                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or row == rows or col < 0 or col == cols:
                        continue
                    # If fresh fruit, rot it.
                    if grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append((row, col))
                    else:
                        continue
            time += 1

        return time if fresh == 0 else -1
