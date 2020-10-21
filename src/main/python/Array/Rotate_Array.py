"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


class Solution(object):
    def rotate_1(self, nums: List[int], k: int) -> None:
        """ method 1: Brute Force
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # speed up the rotation
        k %= len(nums)

        i = 0
        while i < k:
            nums.insert(0, nums.pop())
            i += 1
        print(nums)

    def rotate_2(self, nums: List[int], k: int) -> None:
        """ method 2: Using Cyclic Replacements
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # method 2
        n = len(nums)
        k %= len(nums)

        i_start = 0
        cnt = 0
        while cnt < n:
            i, prev_num = i_start, nums[i_start]
            while True:
                i_next = (i + k) % n
                nums[i_next], prev_num = prev_num, nums[i_next]
                i = i_next
                cnt += 1

                if i_start == i:
                    break

            i_start += 1
        print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    k = 4
    sol = Solution()
    sol.rotate_1(nums, k)
    nums = [1, 2, 3, 4, 5, 6]
    k = 4
    sol.rotate_2(nums, k)
