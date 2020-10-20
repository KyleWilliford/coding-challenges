"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of
haystack. Clarification: What should we return when needle is an empty string? This is a great question to ask during
an interview. For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to
C's strstr() and Java's indexOf().

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Double pointer

        Runtime: 36 ms
        Memory Usage: 14.3 MB
        :param haystack: str
        :param needle: str
        :return: int
        """
        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            j = 0
            while j < m:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == m:
                return i
        return -1

    def strStr_2(self, haystack: str, needle: str) -> int:
        """
        Directly check the list

        Runtime: 28 ms Your runtime beats 84.47 % of python3 submissions.
        Memory Usage: 14.4 MB
        :param haystack: str
        :param needle: str
        :return: int
        """
        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i: i + m] == needle:
                return i
        return -1


sol = Solution()
haystack = "hello"
needle = "ll"
assert sol.strStr(haystack, needle) == 2
haystack = "aaaaa"
needle = "bba"
assert sol.strStr(haystack, needle) == -1
haystack = ""
needle = ""
assert sol.strStr(haystack, needle) == 0
haystack = "a"
needle = "a"
assert sol.strStr(haystack, needle) == 0
haystack = "mississippi"
needle = "issip"
assert sol.strStr(haystack, needle) == 4
