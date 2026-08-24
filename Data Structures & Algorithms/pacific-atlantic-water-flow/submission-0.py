class Solution:
    '''
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or heights[r][c] < prev_height:
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, visit, heights[r][c])

        # Runs through top and bottom rows.
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # Runs for Pacific top row.
            dfs(rows - 1, c, atl, heights[rows - 1][c]) # Runs for Atlantic bottom row.

        # Runs through left and right cols.
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # Runs for left Pacific col.
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # Runs for right Atlantic col.

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

