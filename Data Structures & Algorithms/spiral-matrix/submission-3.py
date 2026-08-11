class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = [] # Holds our result.

        top, bottom = 0, len(matrix) - 1  # Tracks rows.
        left, right = 0, len(matrix[0]) - 1 # Tracks columns.

        # If we still have rows and cols left.
        while top <= bottom and left <= right:
            # Traverse along the top row.
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1 # Move top boundary in by 1.

            # Traverse down the right col.
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1 # Move right boundary in by one.

            # Emergency Check! Do we still have rows and cols left to check?
            if not (top <= bottom and left <= right):
                break
            
            # Traverse down the bottom row from right to left.
            for c in range(right, left - 1, - 1):
                res.append(matrix[bottom][c])
            bottom -= 1 # Move bottom boundary up one.

            # Traverse up the left column rows from bottom to top.
            for r in range(bottom, top - 1, - 1):
                res.append(matrix[r][left])
            left += 1 # Move left boundary in by one.

        return res

            
