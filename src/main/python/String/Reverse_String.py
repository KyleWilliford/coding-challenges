"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory.
You may assume all the characters consist of printable ascii characters.
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s) / 2)):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


sol = Solution()
test = ["h", "e", "l", "l", "o"]
sol.reverseString(test)
assert test == ["o", "l", "l", "e", "h"]

test = ["H", "a", "n", "n", "a", "h"]
sol.reverseString(test)
assert test == ["h", "a", "n", "n", "a", "H"]
