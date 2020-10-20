"""
Create by Jiehan Zhu at 10/19/2020

https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

Constraints:
1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    def maxSubArray_bf(self, nums: List[int]) -> int:
        """
        brute force
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_sum = 0
        for i in range(n):
            sum = 0
            for j in range(i + 1, n):
                sum += nums[j]
                max_sum = max(sum, max_sum)
        return max_sum

    def maxSubArray_dp(self, nums: List[int]) -> int:
        """
        Runtime: 60 ms. Your runtime beats 92.73 % of python3 submissions.
        Memory Usage: 14.9 MB
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]

        start = 0
        max_sum = float('-inf')
        cum_sum = start
        for n in nums:
            cum_sum += n
            if cum_sum - start > max_sum:
                max_sum = cum_sum - start
            if cum_sum < start:
                start = cum_sum
        return max_sum

sol = Solution()
assert sol.maxSubArray_bf([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert sol.maxSubArray_bf([1]) == 1
assert sol.maxSubArray_dp([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert sol.maxSubArray_dp([1]) == 1
assert sol.maxSubArray_dp([-1, -2]) == -1
assert sol.maxSubArray_dp([1, 2]) == 3
