"""
Created by Jiehan Zhu at 10/18/20

https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dynamic programming
        Runtime: 32 ms
        Memory Usage: 14.1 MB
        :param n:
        :return:
        """
        if n <= 2:
            return n
        fn_1, fn_2 = 1, 2
        for _ in range(3, n+1):
            fn_1, fn_2 = fn_2, fn_1 + fn_2
        return fn_2


sol = Solution()
assert sol.climbStairs(3) == 3
assert sol.climbStairs(10) == 89
