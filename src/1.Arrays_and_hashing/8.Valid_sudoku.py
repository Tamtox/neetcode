# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit 1-9 or '.'.

def calculateSection (row, col):
    result = 0
    if(row < 3):
        if(col < 3):
            result = 0
        elif(col < 6):
            result = 1
        else:
            result = 2
    elif (row < 6):
        if(col < 3):
            result = 3
        elif(col < 6):
            result = 4
        else:
            result = 5
    elif (row < 9):
        if(col < 3):
            result = 6
        elif(col < 6):
            result = 7
        else:
            result = 8
    return result

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = []
        cols = []
        sections = []
        for _ in range(length):
            rows.append(set())
            cols.append(set())
            sections.append(set())
        for i in range(length):
            row = board[i]
            for j in range(length):
                section = calculateSection(i, j)
                if row[j] == '.':
                    continue
                if(row[j] in rows[i]):
                    return False
                if(row[j] in cols[j]):
                    return False
                if(row[j] in sections[section]):
                    return False
                rows[i].add(row[j])
                cols[j].add(row[j])
                sections[section].add(row[j])
        return True