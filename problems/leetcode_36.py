from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
        # setting the rows, cols, and squares to a dict of sets 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9) :
            for c in range(9):
                # skipping the . characters
                if board[r][c] == '.':
                    continue

                # if the number exists in the given row or col or squares then return False
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True

        
