class Solution:
    '''
    Time: O(n^2)
    Space: O(n^2)
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = board[r][c]

                row_lab = f"row {r} has val {val}"
                col_lab = f"col {c} has val {val}"
                box_lab = f"box {r // 3}-{c // 3} has val {val}"

                if row_lab in seen or col_lab in seen or box_lab in seen:
                    return False
                
                seen.add(row_lab)
                seen.add(col_lab)
                seen.add(box_lab)
        
        return True
