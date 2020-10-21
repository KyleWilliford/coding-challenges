"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Runtime: 32 ms. Your runtime beats 79.29 % of python3 submissions.
        Memory Usage: 14.3 MB
        :param strs:
        :return:
        """
        if not strs:
            return ""
        i = 0
        prefix = []
        flag = True
        n = min([len(s) for s in strs])
        while i < n and flag:
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    flag = False
                    break
            if flag:
                prefix.append(strs[0][i])
            else:
                break
            i += 1
        return ''.join(prefix) if i > 0 else ''




sol = Solution()
strs = ["flower", "flow", "flight"]
assert sol.longestCommonPrefix(strs) == 'fl'
strs = ["flower", "flow"]
assert sol.longestCommonPrefix(strs) == 'flow'
