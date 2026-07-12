class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Time Complexity: O(log(m * n))
        Space Complexity: O(1)
        '''
        # Check if the matrix is empty. 
        if not matrix or not matrix[0]:
            return False
        
        # Number of rows.
        m = len(matrix)
        # Number of columns.
        n = len(matrix[0])

        # Initialize our binary search pointers
        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert our 'mid' index into 2D (row, col) coordinates.
            row = mid // n
            col = mid % n

            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                # If mid is too small look in the right half.
                left = mid + 1
            else:
                # If mid is too high look at the left half.
                right = mid - 1

        # If we never return after the loop.
        return False

        '''
        Brute Force Approach: The most straightforward approach would be to use
        two nested loops and do a linear search through every element in the matrix.
        This would require us to completely ignore that the rows are sorted.
        This solution would be very slow if our input matrix was very large.
            Time Complexity: O(m * n)
            Space Complexity: O(1)
        '''

