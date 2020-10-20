"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
another 2D matrix and do the rotation.
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(int(n / 2)):
            for j in range(i, n - 1 - i):
                prev = matrix[i][j]
                cnt = 0
                while cnt < 4:
                    i_next = j
                    j_next = n - 1 - i
                    matrix[i_next][j_next], prev = prev, matrix[i_next][j_next]
                    i = i_next
                    j = j_next
                    cnt += 1
                # print(f'i, j = {i, j}')
                # for r in matrix:
                #     print(r)

        for r in matrix:
            print(r)


sol = Solution()
test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(test)
assert test == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

test = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sol.rotate(test)
assert test == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
