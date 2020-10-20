# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                cnt += 1
                i += 1
            else:
                nums[i - cnt] = nums[i]
                i += 1

        while cnt > 0:
            nums[-cnt] = 0
            cnt -= 1

nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
assert nums == [1,3,12,0,0]

nums = [0, 1, 0]
sol.moveZeroes(nums)
assert nums == [1,0,0]

nums = [0, 0, 1]
sol.moveZeroes(nums)
assert nums == [1,0,0]