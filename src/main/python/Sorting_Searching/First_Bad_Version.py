"""
Created by Jiehan Zhu at 10/18/20

https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/

First Bad Version3
You are a product manager and currently leading a team to develop a new product. Unfortunately,
the latest version of your product fails the quality check. Since each version is developed based on the previous
version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version, bad=4):
    return version >= bad

class Solution:
    def firstBadVersion(self, n):
        """
        Runtime: 20 ms, faster than 98.34% of Python3 online submissions for First Bad Version.
        Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for First Bad Version.
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if isBadVersion(n) and not isBadVersion(n-1):
            return n

        def searchRange(min, max):
            if isBadVersion(max) and not isBadVersion(max - 1):
                return max
            middle = (min + max) // 2
            if isBadVersion(middle):
                return searchRange(min, middle)
            else:
                return searchRange(middle+1, max)

        return searchRange(1, n)

sol = Solution()
assert sol.firstBadVersion(5) == 4
