'''
From https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Author: Jiehan Zhu
'''

import numpy as np
class Solution(object):
    def maxProfit_2(self, prices):
        ''' Approach 2: Peak Valley Approach '''
        m = len(prices)
        if m == 1:
            return 0
        peak = prices[0]
        valley = prices[0]
        max_profit = 0
        i = 0
        while i < m-1:
            while i < m-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < m-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
            print(f'At time {i}, peak = {peak}, Valley = {valley}, incremental profit = {peak - valley}')
        return max_profit


    def maxProfit_3(self, prices):
        ''' Approach 3: Simple One Pass '''
        # print("prices: ", prices)
        m = len(prices)
        if m == 1:
            return 0
        max_profit = 0
        for i in range(1, m):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                print(f'At time {i}, buy at {prices[i-1]}, sell at {prices[i]}, incremental profit = {prices[i] - prices[i-1]}')
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices = [1, 7, 2, 3, 6, 7, 6, 7]
print(prices)
print(Solution.maxProfit_2(prices))
print(Solution.maxProfit_3(prices))


