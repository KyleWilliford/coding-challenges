import numpy as np
class Solution(object):
    def maxProfit(prices):
        # print("prices: ", prices)
        m = len(prices)
        if m == 1:
            return 0
        profits = np.zeros((m, m), int)
        for i in range(m-1):
            for j in range(i+1, m):
                if prices[j] > prices[i]:
                    profits[i, j] = prices[j] - prices[i]
        print("profits matrix\n", profits)

        max_profits = []
        for i in range(m-2, -1, -1):
            print(f'i = {i}, max_profits = {max_profits}')
            print('part of profits', profits[i, i+2:])
            print('part of max_profit', max_profits)
            if len(profits[i, i+2:]) >0:
                profit_i = profits[i, i+2:] + np.array(max_profits)
            else:
                profit_i = []
            print(f'profits[i, i + 1] = {profits[i, i + 1]}')
            profit_i = list(profit_i) + [profits[i, i + 1]]
            print(f'profit_i = {profit_i}')

            max_profits.append(np.max(profit_i))
            # print(profit_i)
            # max_profits[i+1] = np.max(profit_i)
            # max_profits = profits[i, i:].reverse()

        # for i in range(m-1):
        #     for j in range(i+1, m):
        #         if prices[j] > prices[i]:
        #             # print(f'i = {i}, j = {j}, m={m}')
        #             # print(prices[i], prices[j], prices[j+1:m])
        #             if j == m-1:
        #                 profits[i, j] = prices[j] - prices[i]
        #             else:
        #                 profits[i, j] = prices[j] - prices[i] + maxProfit(prices[j+1:m])
        # print("profits matrix\n", profits)
        return np.max(max_profits)


prices = [7, 1, 5, 3, 6, 4]
print(Solution.maxProfit(prices))


