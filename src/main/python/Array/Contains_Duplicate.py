"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every
element is distinct.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_unq = list(set(nums))
        return not len(nums) == len(nums_unq)