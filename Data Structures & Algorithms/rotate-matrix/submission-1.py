class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose: Swap elements diagonally.
        for r in range(n):
            # Start at (r + 1) so we only hit the upper triangle where c > r.
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row.
        for r in range(n):
            matrix[r].reverse()







