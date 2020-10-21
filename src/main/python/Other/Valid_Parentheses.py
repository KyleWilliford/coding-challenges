"""
Create by Jiehan Zhu at 10/19/2020

https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/

Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Runtime: 24 ms. Your runtime beats 94.53 % of python3 submissions.
        Memory Usage: 14.1 MB
        :param s:
        :return:
        """
        stack = []
        hash_map = {'}': '{', ')': '(', ']': '['}
        for c in s:
            if c not in hash_map:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack.pop() != hash_map[c]:
                return False
        return not stack


sol = Solution()
assert sol.isValid("()")
assert sol.isValid("()[]{}")
assert sol.isValid("{[]}")
assert not sol.isValid("(]")
assert not sol.isValid("([)]")
assert not sol.isValid("(")
