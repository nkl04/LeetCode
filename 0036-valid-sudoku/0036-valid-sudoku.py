class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    digit = ord(board[i][j]) - ord('1')
                    box_idx = (i//3) * 3 + (j//3)
                    if rows[i][digit] or cols[j][digit] or boxes[box_idx][digit]:
                        return False
                    rows[i][digit] = cols[j][digit] = boxes[box_idx][digit] = True
        return True
