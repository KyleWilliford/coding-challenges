"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

String to Integer (atoi)
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character. Assume we are dealing with an environment that
could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of
the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Runtime: 36 ms, faster than 58.54% of Python3 online submissions for String to Integer (atoi).
        Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for String to Integer (atoi).
        :param s:
        :return:
        """
        result = []
        s = s.lstrip()
        if not s:
            return 0
        elif s[0] == '-':
            boundry = -pow(2, 31)
            result.append(s[0])
            s = s[1:]
        elif s[0] == "+":
            boundry = pow(2, 31) - 1
            s = s[1:]
        else:
            boundry = pow(2, 31) - 1

        if not s or not s[0].isdigit():
            return 0

        for c in s:
            if c.isdigit():
                result.append(c)
            else:
                break

        result = int(''.join(result))
        return result if abs(result) <= abs(boundry) else boundry


sol = Solution()
str_test = "42"
assert sol.myAtoi(str_test) == 42
str_test = "-42"
assert sol.myAtoi(str_test) == -42
s = "    -42"
assert sol.myAtoi(str_test) == -42
str_test = "4193 with words"
assert sol.myAtoi(str_test) == 4193
str_test = "words and 987"
assert sol.myAtoi(str_test) == 0
str_test = "-91283472332"
assert sol.myAtoi(str_test) == -2147483648
str_test = "-+12"
assert sol.myAtoi(str_test) == 0
str_test = ""
assert sol.myAtoi(str_test) == 0
str_test = "+12"
assert sol.myAtoi(str_test) == 12
str_test = "+"
assert sol.myAtoi(str_test) == 0