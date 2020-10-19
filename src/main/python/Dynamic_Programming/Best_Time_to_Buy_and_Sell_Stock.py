"""
Created by Jiehan Zhu at 10/18/20

https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max = float('-inf')
        profit = float('-inf')
        for i in range(1, len(prices)):
            if prices[i] = prices[i-1] > 0:


            if p - sell > 0:
                profit += p-sell
                sell = p
        return profit


sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 5