class Solution:
    '''
    Time: O(m * n)
    Space: O(m * n)
    '''
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # If we are out of bounds.
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O'):
                return

            board[r][c] = 'T' # Mark 'O' as safe if it connects to a border 'O'.

            # Call all four neighbors.
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

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

        # Turn border 'T's back to 'O's and inner 'O' to 'X's.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        