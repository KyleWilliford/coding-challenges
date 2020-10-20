"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""


class Solution:
    def isValidSudoku(self, board):
        """
        Runtime: 92 ms. Your runtime beats 90.40 % of python3 submissions.
        Memory Usage: 14.2 MB
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        # validate
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    k = (i // 3) * 3 + j // 3

                    if num in rows[i]:
                        return False
                    rows[i].add(num)

                    if num in columns[j]:
                        return False
                    columns[j].add(num)

                    if num in boxs[k]:
                        return False
                    boxs[k].add(num)

        return True


sol = Solution()

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
assert sol.isValidSudoku(board)

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
assert not sol.isValidSudoku(board)
