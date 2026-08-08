class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        Time Complexity: O(n * m)
        Space Complexity: O(1)
        '''
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False # Tracks if 0th row contains zeros.

        # Set up flags for where 0's should go in row/col headers.
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Mark the column header.
                    if r > 0:
                        matrix[r][0] = 0 # Mark the row header.
                    else:
                        row_zero = True # Top row has a zero!

        # Zero out the grid.
        # Skip the top row and left col since they hold our marks.
        for r in range(1, rows):
            for c in range(1, cols):
                # Check if row/col header are zero.
                # If they are set element to zero.
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # Check if col 0 was flagged.
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Check if row 0 was flagged.
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0