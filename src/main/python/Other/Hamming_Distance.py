"""
Create by Jiehan Zhu at 10/19/2020

Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.
"""


class Solution:
    def hammingDistance_1(self, x: int, y: int) -> int:
        """
        Runtime: 32 ms. Your runtime beats 50.24 % of python3 submissions.
        Memory Usage: 14 MB
        :param x:
        :param y:
        :return:
        """
        dist = 0
        while x > 0 or y > 0:
            # print(f'x, y, dist, x & y  = {x, y, dist, (x % 2) & (y % 2)}')
            dist += (x % 2) != (y % 2)
            x >>= 1
            y >>= 1
        return dist

    def hammingDistance_2(self, x: int, y: int) -> int:
        """
        Runtime: 28 ms. Your runtime beats 77.32 % of python3 submissions.
        Memory Usage: 14.1 MB
        :param x:
        :param y:
        :return:
        """
        x_byte = (format(x, '032b'))
        y_byte = (format(y, '032b'))
        dist = sum([x_byte[i] != y_byte[i] for i in range(32)])
        return dist

    def hammingDistance_3(self, x: int, y: int) -> int:
        """
        Runtime: 20 ms. Your runtime beats 98.53 % of python3 submissions.
        Memory Usage: 14 MB
        :param x:
        :param y:
        :return:
        """
        return bin(x ^ y).count('1')



sol = Solution()
assert sol.hammingDistance_1(1, 4) == 2
assert sol.hammingDistance_2(1, 4) == 2
assert sol.hammingDistance_3(1, 4) == 2
