"""
Create by Jiehan Zhu at 10/19/2020

https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/

House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of
money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security
system connected and it will automatically contact the police if two adjacent houses were broken into on the same
night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Runtime: 28 ms. Your runtime beats 87.08 % of python3 submissions.
        Memory Usage: 14.2 MB
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        sum_1 = sum_2 = 0
        for num in nums:
            sum_1, sum_2 = max(sum_1, sum_2), sum_1 + num
        return max(sum_1, sum_2)


sol = Solution()
assert sol.rob([2, 1, 1, 2]) == 4
