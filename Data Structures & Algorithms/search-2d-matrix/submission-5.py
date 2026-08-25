class Solution:
    '''
    Time: O(log(n * m))
    Space: O(1)
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // cols
            col = mid % cols

            curr_num = matrix[row][col]

            if curr_num == target:
                return True
            elif curr_num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False