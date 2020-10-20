"""
Create by Jiehan Zhu at 10/20/2020

https://leetcode.com/problems/word-break/
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = sorted(wordDict, key=len, reverse=True)
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    return True
        return False

# test
sol = Solution()
s = "leetcode"
wordDict = ["leet", "code"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol.wordBreak(s, wordDict)