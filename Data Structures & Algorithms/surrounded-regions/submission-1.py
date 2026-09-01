class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O'):
                return

            board[r][c] = 'T'

            # Call the dfs for each direction.
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = dr + r, dc + c

                dfs(row, col)

        # Loops through top and bottom rows.
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Loops through left and right cols.
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
            