from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits
        digits = [1] + digits
        return digits


sol = Solution()
assert sol.plusOne([1,2,3]) == [1, 2, 4]
assert sol.plusOne([0]) == [1]
assert sol.plusOne([9]) == [1, 0]
