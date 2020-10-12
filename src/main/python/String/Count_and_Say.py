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
import re


class Solution:
    def countAndSay_iterative(self, n: int) -> str:
        """
        iterative

        Runtime: 36 ms. Your runtime beats 60.75 % of python3 submissions.
        Memory Usage: 14.3 MB
        :param n:
        :return:
        """
        count = '1'
        for j in range(n-1):
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
            count = ''.join(say)

        return count

    def countAndSay_recursive(self, n: int) -> str:
        """
        recursive

        Runtime: 36 ms. Your runtime beats 60.75 % of python3 submissions.
        Memory Usage: 14.3 MB
        :param n:
        :return:
        """

        if n == 1:
            return '1'

        count = self.countAndSay_Recursive(n-1)
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

    def countAndSay_RErecursive(self, n: int) -> str:
        """
        Recursive Regular Expression
        https://leetcode-cn.com/problems/count-and-say/solution/duo-chong-fang-fa-qiu-jie-wai-guan-shu-lie-bu-fang/

        :param n:
        :return:
        """
        if n == 1:
            return '1'

        s = self.countAndSay_RE(n-1)
        p = r'(\d)\1*'
        pattern = re.compile(p)
        res = [_.group() for _ in pattern.finditer(s)]  # 提取结果
        return ''.join(str(len(c)) + c[0] for c in res)  # join 内部的 str(len(c)) + c[0] for c in res 是生成器类型

    def countAndSay_REiterative(self, n: int) -> str:
        """
        Iterative Regular Expression
        https://leetcode-cn.com/problems/count-and-say/solution/duo-chong-fang-fa-qiu-jie-wai-guan-shu-lie-bu-fang/

        :param n:
        :return:
        """
        res = '1'
        p = r'(\d)\1*'
        pattern = re.compile(p)
        for _ in range(n-1):
            res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)  # 替换
        return res






sol = Solution()
n = 6
assert sol.countAndSay_Iteration(2) == '11'
assert sol.countAndSay_Recursive(2) == '11'
assert sol.countAndSay_Iteration(6) == '312211'
assert sol.countAndSay_Recursive(6) == '312211'
assert sol.countAndSay_Iteration(10) == '13211311123113112211'
assert sol.countAndSay_Recursive(10) == '13211311123113112211'
assert sol.countAndSay_RE(6) == '312211'
assert sol.countAndSay_REInplace(6) == '312211'
