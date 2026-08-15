class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, bottom = 0, len(matrix) - 1 # Tracks rows.
        left, right = 0, len(matrix[0]) - 1 # Tracks columns.

        res = []

        while top <= bottom and left <= right:
            # Loop across top row.
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # Loop down right column.
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # Middle check to make sure boundaries are still correct.
            if not (top <= bottom and left <= right):
                break

            # Loop across bottom row from right to left.
            for c in range(right, left - 1, - 1):
                res.append(matrix[bottom][c])
            bottom -= 1

            # Loop across left col from bottom up.
            for r in range(bottom, top - 1, - 1):
                res.append(matrix[r][left])
            left += 1

        return res
            

        


            
