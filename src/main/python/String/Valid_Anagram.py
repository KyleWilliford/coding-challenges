"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

Given two strings s and t , write a function to determine if t is an anagram of s.
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from collections import defaultdict, Counter


class Solution(object):
    def isAnagram_1(self, s, t):
        """
        Use two Counter/Hash table

        Runtime: 40 ms, faster than 87.88% of Python3 online submissions for Valid Anagram.
        Memory Usage: 14.4 MB, less than 26.70% of Python3 online submissions for Valid Anagram.
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash = Counter(s)
        t_hash = Counter(t)
        return s_hash == t_hash

    def isAnagram_2(self, s, t):
        """
        Use one hash table.

        Runtime: 52 ms, faster than 52.65% of Python3 online submissions for Valid Anagram.
        Memory Usage: 14.3 MB, less than 26.70% of Python3 online submissions for Valid Anagram.
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash = Counter(s)
        for c in t:
            if c in s_hash:
                s_hash[c] -= 1
            else:
                return False
        for c, cnt in s_hash.items():
            if cnt != 0:
                return False
        return True


sol = Solution()
s = "anagram"
t = "nagaram"
assert sol.isAnagram_1(s, t)
assert sol.isAnagram_2(s, t)

s = "rat"
t = "car"
assert not sol.isAnagram_1(s, t)
assert not sol.isAnagram_2(s, t)