"""
Create by Jiehan Zhu at 10/19/2020

Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
from typing import List


class Solution:
    def missingNumber_1(self, nums: List[int]) -> int:
        """
        Runtime: 128 ms. Your runtime beats 85.39 % of python3 submissions.
        Memory Usage: 15.2 MB
        :param nums:
        :return:
        """
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumber_2(self, nums: List[int]) -> int:
        """
        Runtime: 128 ms. Your runtime beats 85.39 % of python3 submissions.
        Memory Usage: 15.1 MB
        :param nums:
        :return:
        """
        n = len(nums)
        return ((1 + n) * n // 2) - sum(nums)
