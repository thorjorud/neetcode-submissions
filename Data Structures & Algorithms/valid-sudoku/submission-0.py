'''
    Time Complexity: O(1), We loop through 81 values each run.
    Space Complexity: O(1), We can store up to 243 strings max.

    If we were solving this for a grid of size (N x N) then we would have:
        Time: O(n^2), We would have to check n^2 values in our grid.
        Space: O(n^2), We could store up to n^2 values in our hash set.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create our set to keep track of seen values (or notebook!).
        seen = set()

        # We loop through every row, column and 3x3 box.
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                # Create our labels to add to our set (or notebook).
                row_label = f"row {r} has {val}"
                col_label = f"col {c} has {val}"
                box_label = f"box {r // 3}-{c // 3} has {val}"

                # If we've already seen a label then return False (our Sudoku would be ruined).
                if row_label in seen or col_label in seen or box_label in seen:
                    return False
                
                seen.add(row_label)
                seen.add(col_label)
                seen.add(box_label)
        
        return True