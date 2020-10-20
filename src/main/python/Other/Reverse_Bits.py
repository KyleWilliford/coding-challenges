"""
Create by Jiehan Zhu at 10/19/2020

https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/

Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
Follow up:
If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits_1(self, n: int) -> int:
        """
        Runtime: 28 ms. Your runtime beats 84.46 % of python3 submissions.
        Memory Usage: 14.1 MB
        :param n:
        :return:
        """
        return int(format(n, '032b')[::-1], 2)
