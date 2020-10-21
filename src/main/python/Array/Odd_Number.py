"""
Given a non-empty array of integers nums, every element appears even number of times except for one that that appears
oss number of times. Find that single one.
Follow up: Could you think of two way to solve this problem? Could you use set to solve this?
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""
from collections import defaultdict


def find_odd_1(nums):
    """
    Use a Hash map to track the count.

    :param nums: List[int
    :return: int
    """
    hash_cnt = defaultdict(int)
    for n in nums:
        hash_cnt[n] += 1
    for n in hash_cnt.keys():
        if hash_cnt[n] % 2 == 1:
            return n


def find_odd_2(nums):
    """
    Add and remove from set.

    :param nums: List[int
    :return: int
    """
    set_nums = set()
    for n in nums:
        if n in set_nums:
            set_nums.remove(n)
        else:
            set_nums.add(n)
    return set_nums.pop()


nums_test = [4, 1, 2, 1, 2, 2, 2, 4, 4]
assert find_odd_1(nums_test) == 4
assert find_odd_2(nums_test) == 4
