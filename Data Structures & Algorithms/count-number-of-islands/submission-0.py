class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Recursive function keeps checking until out of bounds or hits water.
        def dfs(r, c):
            # If out of bounds or on water, return.
            if r < 0 or r  >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            # Turn to water.
            grid[r][c] = "0"

            # Check up, down, left, right.
            dfs(r - 1, c) # UP
            dfs(r + 1, c) # DOWN
            dfs(r, c - 1) # LEFT
            dfs(r, c + 1) # RIGHT

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands