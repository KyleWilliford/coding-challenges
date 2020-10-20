"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointers

        Runtime: 44 ms. Your runtime beats 80.99 % of python3 submissions.
        Memory Usage: 15.2 MB
        :param s: str
        :return: int
        """
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        n = len(s)
        if n == 1:
            return True
        for i in range(int((n + 1) / 2)):
            if s[i] != s[-(i + 1)]:
                return False
        return True


sol = Solution()
s = "A man, a plan, a canal: Panama"
assert sol.isPalindrome(s) == True
s = "race a car"
assert sol.isPalindrome(s) == False
s = "0P"
assert sol.isPalindrome(s) == False
s = "a"
assert sol.isPalindrome(s) == True
