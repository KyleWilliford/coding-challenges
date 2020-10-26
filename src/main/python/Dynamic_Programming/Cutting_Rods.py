"""
Created by Jiehan Zhu at 10/21/20

https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum
obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""


def CutRobs(prices, n):
    """
    dynamic programming
    :param prices: List[int]
    :param n: int
    :return: int
    """
    best_price = {i: j for i, j in zip(range(n + 1), prices)}
    for i in range(1, n + 1):
        best_price[i] = max([best_price[j] + best_price[i - j] for j in range(i)])
    return best_price[n]


# test
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
n = 8
assert CutRobs(prices, n) == 22

prices = [0, 3, 5, 8, 9, 10, 17, 17, 20]
assert CutRobs(prices, n) == 24
