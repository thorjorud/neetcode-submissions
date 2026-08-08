class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # n = number of rows and cols since we have a n x n square.
        n = len(matrix)

        # Transpose (Turn rows into cols)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse() # Reverse the row.

