"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""
from typing import List
from collections import defaultdict

class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        """Dictionary solution
        Time complexity : O(n * 1) = O(n)
        Space complexity : O(n)
        """
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i

    def singleNumber_2(self, nums: List[int]) -> int:
        """Math solution
        Time complexity : O(n + n) = O(n)
        Space complexity : O(n + n) = O(n)
        """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_3(self, nums: List[int]) -> int:
        """Bit Manipulation: https://leetcode.com/problems/single-number/solution/
        """
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    sol = Solution()
    print(sol.singleNumber_1(nums))
    print(sol.singleNumber_2(nums))
    print(sol.singleNumber_3(nums))
