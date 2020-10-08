"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

Given two arrays, write a function to compute their intersection.
- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
    the memory at once?
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        both = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    both.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    nums2.remove(i)
                    both.append(i)
        return both
