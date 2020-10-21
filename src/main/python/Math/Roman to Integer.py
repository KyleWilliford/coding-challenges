"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/

Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Runtime: 40 ms. Your runtime beats 92.51 % of python3 submissions.
        Memory Usage: 14.1 MB
        :param s:
        :return:
        """
        valueMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = 0
        iPrior = 0
        for j in range(len(s) - 1, -1, -1):
            r = s[j]
            i = valueMap[r]
            if i < iPrior:
                n -= i
            else:
                n += i
            # print(f'r, i, iPrior, n = {r, i, iPrior, n}')
            iPrior = i
        return n


s = "III"
sol = Solution()
assert sol.romanToInt("IV") == 4
assert sol.romanToInt("IX") == 9
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
