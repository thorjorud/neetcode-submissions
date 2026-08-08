class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        '''
        rows, cols = len(matrix), len(matrix[0])
        row_0 = False # Keeps track if row 0 has zeros.

        # Mark headers
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Set column header to 0.
                    # If we are on a row greater then 0.
                    if r > 0:
                        matrix[r][0] = 0 # Set row header to 0.
                    # Ir row 0 has a zero, then set row_0 to True!
                    else: 
                        row_0 = True

        # Change the inner grid. 
        # Start from col and row 1 so we dont change our headers.
        for r in range(1, rows):
            for c in range(1, cols):
                # If current elements header is 0
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0 # Set current element to 0.
                
        # Change first column if needed.
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
            
        # Change first row if needed.
        if row_0:
            for c in range(cols):
                matrix[0][c] = 0




        