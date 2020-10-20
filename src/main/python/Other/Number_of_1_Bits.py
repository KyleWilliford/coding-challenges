"""
Create by Jiehan Zhu at 10/19/2020

Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a
signed integer type. It should not affect your implementation, as the integer's internal binary representation is the
same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above, the
input represents the signed integer. -3.

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight_1(self, n: int) -> int:
        """
        Runtime: 32 ms. Your runtime beats 58.56 % of python3 submissions.
        Memory Usage: 14.1 MB
        :param n:
        :return:
        """
        cnt = 0
        while n > 0:
            cnt += n % 2
            n //= 2
        return cnt

    def hammingWeight_2(self, n: int) -> int:
        """
        Runtime: 24 ms. Your runtime beats 94.40 % of python3 submissions.
        Memory Usage: 14.2 MB
        :param n:
        :return:
        """
        cnt = 0
        while n > 0:
            cnt += n % 2
            n >>= 1
        return cnt

    def hammingWeight_3(self, n: int) -> int:
        """
        Runtime: 28 ms
        Memory Usage: 14.1 MB
        :param n:
        :return:
        """
        cnt = 0
        while n > 0:
            cnt += n & 1
            n >>= 1
        return cnt


sol = Solution()
sol.hammingWeight_1(9)
