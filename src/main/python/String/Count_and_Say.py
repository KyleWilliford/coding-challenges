"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/

Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in
other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        """

        Runtime: 36 ms. Your runtime beats 60.75 % of python3 submissions.
        Memory Usage: 14.3 MB
        :param n:
        :return:
        """
        def transferToSay(count):
            say = []
            cnt = 1
            key = count[0]
            for i in range(1, len(count)):
                if count[i] == key:
                    cnt += 1
                else:
                    say.append(str(cnt))
                    say.append(key)
                    cnt = 1
                    key = count[i]
                # print(key, cnt)
            say.append(str(cnt))
            say.append(key)
            return ''.join(say)

        count = '1'
        for j in range(n-1):
            count = transferToSay(count)

        return count

    def countAndSay_2(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            v = ''
            for digit, group in itertools.groupby(ans):
                count = len(list(group))
                v += (str(count) + digit)
            ans = v
        return ans


sol = Solution()
n = 2
sol.countAndSay(n)
sol.countAndSay_2(n)
