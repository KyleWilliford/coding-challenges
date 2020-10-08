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
        i = 0
        j = 0
        for j in range(n):
            prev = matrix[i][j]
            matrix[j][n - 1], prev = prev, matrix[j][n - 1]
            matrix[n - 1][n - 1 - j], prev = prev, matrix[n - 1][n - 1 - j]
            matrix[n - 1][-j], prev = prev, matrix[n - 1][n - 1 - j]
            matrix[n - 1][-j], prev = prev, matrix[j][n - 1]

            print(matrix, '\n', prev)
            if i == 0:
                j_next = n - 1
            prev = matrix[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
[[7,4,1],[8,5,2],[9,6,3]]