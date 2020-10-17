'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # method 1
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        # print(nums)

        # method 2
        n = len(nums)
        if k == n:
            return
        if n % k == 0:
            i = 0
            cnt = 0
            prev = nums[i]
            while i < k:
                print(f'i = {i}')
                while cnt < n/k:
                    print(f'cnt = {cnt}')
                    curr = nums[(i + k) % n]
                    nums[(i + k) % n] = prev
                    print(f'i : {i}, should be in: {(i + k) % n}, nums: {nums}, prev, curr: {prev, curr}')
                    i = (i + k) % n
                    prev = curr
                    cnt += 1
                i += 1
                cnt = 0
                prev = nums[i]
        else:
            i = 0
            cnt = 0
            prev = nums[0]
            while cnt < n:
                print(cnt)
                curr = nums[(i+k) % n]
                nums[(i + k) % n] = prev
                print(f'i : {i}, should be in: {(i+k) % n}, nums: {nums}, prev, curr: {prev, curr}')
                i = (i+k) % n
                prev = curr
                cnt += 1
        print(nums)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    k = 4
    sol = Solution()
    sol.rotate(nums, k)