"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
[−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        Runtime: 32 ms, faster than 14.21% of Python online submissions for Reverse Integer.
        Memory Usage: 13.5 MB, less than 5.55% of Python online submissions for Reverse Integer.

        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        ls = list(str(x))
        for i in range(int(len(ls) / 2)):
            ls[i], ls[-(i + 1)] = ls[-(i + 1)], ls[i]
        result = sign * int(''.join(ls))
        if -1 * pow(2, 31) <= result <= pow(2, 31) - 1:
            return result
        else:
            return 0

    def reverse_2(self, x):
        """
        Check before Overflow

        Runtime: 16 ms, faster than 92.12% of Python online submissions for Reverse Integer.
        Memory Usage: 13.6 MB, less than 5.04% of Python online submissions for Reverse Integer.
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        ls = list(str(x))
        n = len(ls)-1
        result = 0
        while n >= 0:
            i = ls.pop()
            result += int(i) * (10 ** n)
            n -= 1
            if result > pow(2, 31):
                return 0
        result *= sign
        return result

    def reverse_3(self, x):
        """
        Pop and Check before Overflow

        Runtime: 20 ms, faster than 75.80% of Python online submissions for Reverse Integer.
        Memory Usage: 13.3 MB, less than 15.39% of Python online submissions for Reverse Integer.
        :type x: int
        :rtype: int
        """
        y, result = abs(x), 0
        boundary = (1 << 31) - 1 if x > 0 else 1 << 31
        result = 0
        while y > 0:
            result = result * 10 + y % 10
            y //= 10
            if result > boundary:
                return 0
        return result if x > 0 else -result


sol = Solution()
x = -123
x = 1534236469
assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21
assert sol.reverse(0) == 0
assert sol.reverse_2(-123) == -321
assert sol.reverse_2(120) == 21
assert sol.reverse_2(0) == 0
