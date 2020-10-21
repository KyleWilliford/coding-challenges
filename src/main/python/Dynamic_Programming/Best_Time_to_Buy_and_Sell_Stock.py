"""
Created by Jiehan Zhu at 10/18/20

https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i. If you were
only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an
algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one.
"""
from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        """
        brute force
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0
        max_profit = 0
        n = len(prices)
        for buy in range(n - 1):
            for sell in range(buy + 1, n):
                max_profit = max(prices[sell] - prices[buy], max_profit)
        return max_profit

    def maxProfit_dp2(self, prices: List[int]) -> int:
        """
        dynamic programing speed up replace min and max function with check condition

        Runtime: 56 ms. Your runtime beats 94.58 % of python3 submissions.
        Memory Usage: 14.9 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p - min_price > max_profit:
                max_profit = p - min_price
            if p < min_price:
                min_price = p
        return max_profit

    def maxProfit_dp(self, prices: List[int]) -> int:
        """
        dynamic programing

        Runtime: 64 ms, faster than 66.70% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 14.9 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices[1:]:
            max_profit = max(max_profit, p-min_price)
            min_price = min(min_price, p)
        return max_profit


sol = Solution()
assert sol.maxProfit_1([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit_1([7, 6, 4, 3, 1]) == 0
assert sol.maxProfit_dp([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit_dp([7, 6, 4, 3, 1]) == 0
assert sol.maxProfit_dp([1, 2]) == 1
assert sol.maxProfit_dp([3, 5, 1, 2]) == 2
