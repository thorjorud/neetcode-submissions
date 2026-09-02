class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # If cell is in bounds and on a 'O'.
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O'):
                return
            
            # Mark border region cell as a T.
            board[r][c] = 'T'

            # Call dfs() on adjacent cells.
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)

        # Loops through top and bottom rows.
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Loops through left and right cols.
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = "X"