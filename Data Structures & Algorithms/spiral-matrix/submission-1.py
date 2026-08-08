class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        # Set up boundaries.
        top, bottom = 0, len(matrix) - 1 # Tracks rows.
        left, right = 0, len(matrix[0]) - 1 # Tracks columns.

        while left <= right and top <= bottom:
            # Walk across the top columns from left to right (inclusive).
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            # Shrink top down by 1.
            top += 1

            # Walk down from top to bottom (inclusive).
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            # Shrink right in by 1.
            right -= 1

            # If top and bottom boundaries haven't crossed.
            if top <= bottom:
                # Loop from bottom right col to bottom left col.
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                # Shrink bottom boundary by 1.
                bottom -= 1

            # Make sure left and right boundaries haven't crossed.
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                # Shrink the left boundary in by 1.
                left += 1

        return res
                