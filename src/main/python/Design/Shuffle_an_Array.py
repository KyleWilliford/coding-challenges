"""
Create by Jiehan Zhu at 10/19/2020

Shuffle an Array
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from typing import List
import random


class Solution:
    """
    Runtime: 264 ms. Your runtime beats 95.02 % of python3 submissions.
    Memory Usage: 19.4 MB
    """
    def __init__(self, nums: List[int]):
        self.input = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.input.copy()

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        Runtime: 264 ms
        Memory Usage: 19.4 MB
        """
        nums = self.input.copy()
        random.shuffle(nums)
        return nums

    def shuffle1(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        use pop and insert
        Runtime: 268 ms, faster than 93.47% of Python3 online submissions for Shuffle an Array.
        Memory Usage: 19.4 MB, less than 14.01% of Python3 online submissions for Shuffle an Array.
        """
        nums = self.input.copy()
        n = len(self.input)
        for i in range(n - 1):
            new_inx = random.randrange(n - i)
            nums.append(nums.pop(new_inx))
        return nums

    def shuffle2(self) -> List[int]:
        """
        Returns a random shuffling of the array.

        Fisher-Yates Algorithm from https://leetcode.com/problems/shuffle-an-array/solution/
        Runtime: 292 ms, faster than 82.92% of Python3 online submissions for Shuffle an Array.
        Memory Usage: 19.4 MB, less than 14.01% of Python3 online submissions for Shuffle an Array.
        """
        nums = self.input.copy()
        n = len(self.input)
        for i in range(n - 1):
            swap_to = random.randrange(i, n)
            nums[i], nums[swap_to] = nums[swap_to], nums[i]
        return nums

# Your Solution object will be instantiated and called as such:
obj = Solution(list(range(1, 10)))
param_1 = obj.reset()
param_2 = obj.shuffle1()