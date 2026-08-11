from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Tracks nums seen in rows.
        cols = defaultdict(set) # Tracks nums seen in cols.
        box = defaultdict(set)  # Tracks nums seen in boxes. KEY: e.g. (1, 0)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_key = (r // 3, c // 3)
                # If we are on a non number move to next col or row.
                if val == ".":
                    continue
                else:
                    # If we've seen this number return False (Duplicate value found).
                    if val in rows[r] or val in cols[c] or val in box[box_key]:
                        return False
                    # Otherwise add to hashmap sets.
                    else:
                        rows[r].add(val)
                        cols[c].add(val)
                        box[box_key].add(val)
        return True
                

