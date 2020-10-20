"""
Create by Jiehan Zhu at 10/19/2020

https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Runtime: 24 ms.Your runtime beats 93.97 % of python3 submissions.
        Memory Usage: 14.2 MB
        :param numRows:
        :return:
        """
        if numRows <= 1:
            return [[1]][:numRows]
        result = [[1]]
        for i in range(numRows - 1):
            new_row = []
            for j in range(1, i + 1):
                new_row.append(result[-1][j - 1] + result[-1][j])
            result.append([1] + new_row + [1])
        return result

    def generate_2(self, numRows: int) -> List[List[int]]:
        """
        math solution
        Runtime: 28 ms. Your runtime beats 79.95 % of python3 submissions.
        Memory Usage: 14 MB
        :param numRows:
        :return:
        """
        result = []
        for i in range(numRows):
            result.append([BinomialCoefficient(i, j) for j in range(i+1)])
        return result


def BinomialCoefficient(n: int, k: int) -> int:
    """
    n! / k!(n−k)!
    :param n:
    :param k:
    :return:
    """
    if not 0 <= k <= n:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result *= (n - i + 1)
        result //= i
    return result


sol = Solution()
assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert sol.generate_2(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


assert BinomialCoefficient(6, 2) == 15
assert BinomialCoefficient(7, 3) == 35
