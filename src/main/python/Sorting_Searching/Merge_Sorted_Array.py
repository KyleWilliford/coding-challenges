"""
Created by Jiehan Zhu at 10/18/20

https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
"""
from typing import List


class Solution:
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Brute force
        Runtime: 36 ms. Your runtime beats 73.16 % of python3 submissions.
        Memory Usage: 14.1 MB
        """
        if n == 0:
            pass

        i = j = 0
        k = 0
        while i < m + k and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i + 1:m + k + 1] = nums1[i:m + k]
                nums1[i] = nums2[j]
                k += 1
                j += 1
                i += 1

        if j < n:
            nums1[i:] = nums2[j:]

    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        start the the tail to reduce number of move

        Runtime: 36 ms. Your runtime beats 73.16 % of python3 submissions.
        Memory Usage: 14.2 MB
        """
        if n == 0:
            pass
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[: j + 1]




sol = Solution()

nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
sol.merge_1(nums1, m, nums2, n)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1, m, nums2, n = [2, 0], 1, [1], 1
sol.merge_1(nums1, m, nums2, n)
assert nums1 == [1, 2]

nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
sol.merge_2(nums1, m, nums2, n)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1, m, nums2, n = [2, 0], 1, [1], 1
sol.merge_2(nums1, m, nums2, n)
assert nums1 == [1, 2]
