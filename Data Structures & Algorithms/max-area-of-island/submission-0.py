class Solution:
    '''
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # If grid is empty.
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return (1 + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area
        
