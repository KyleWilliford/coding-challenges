"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""
from collections import defaultdict
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashCnt = defaultdict(int)
        ind = 0
        for k in s:
            hashCnt[k] += 1
        for k, cnt in hashCnt.items():
            # print(k, cnt)
            if cnt == 1:
                return ind
            ind += 1
        return -1

    def firstUniqChar_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashCnt = defaultdict(int)
        hashInd = defaultdict(int)
        ind = 0
        for k in s:
            hashCnt[k] += 1
            hashInd[k] = ind
            ind += 1
        unq_ind = []
        for k, cnt in hashCnt.items():
            # print(key, cnt)
            if cnt == 1:
                unq_ind.append(hashInd[k])
        if not unq_ind:
            return -1
        else:
            return min(unq_ind)

    def firstUniqChar_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashCnt = collections.Counter(s)
        # print(hashCnt)
        for idx, ch in enumerate(s):
            # print(idx, ch)
            if hashCnt[ch] == 1:
                return idx
        return -1


sol = Solution()
s = "leetcode"
assert sol.firstUniqChar(s) == 0
assert sol.firstUniqChar_1(s) == 0
assert sol.firstUniqChar_2(s) == 0
s = "loveleetcode"
assert sol.firstUniqChar(s) == 2
assert sol.firstUniqChar_1(s) == 2
assert sol.firstUniqChar_2(s) == 2
