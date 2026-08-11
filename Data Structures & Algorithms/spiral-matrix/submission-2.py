class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = [] # Result Array.

        top, bottom = 0, len(matrix) - 1 # Tracks Rows.
        left, right = 0, len(matrix[0]) - 1 # Tracks Columns.

        while left <= right and top <= bottom:
            # Traverse top row.
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1 # Move top boundary down.

            # Traverse down the right column.
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1 # Move right boundary in one.

            # Checks if we still have valid rows and columns left.
            if not (left <= right and top <= bottom):
                break

            # Traverse along the bottom from right to left.
            for c in range(right, left - 1, - 1):
                res.append(matrix[bottom][c])
            bottom -= 1 # Move bottom boundary up by one.

            # Trave along the left column from bottom to top.
            for r in range(bottom, top - 1, - 1):
                res.append(matrix[r][left])
            left += 1 # Move left boundary in by one.

        return res

            
            
