# Goal: Find the number of pairs of elements in the array the sum of which is divisible by K
# Inputs:
#    a: array of positive integers
#    K: the divisor
# Outputs:
#    C: number of pairs of elements whose sum is divisible by K
# Example:
#    a = [1, 4, 5, 3]
#    K = 3
#    C = 2 … This is because of the pairs ({1, 5}, {4, 5})
from collections import defaultdict


def sum_divisible_1(a, k) -> int:
    """ brute force

    :param a: List[int]
    :param k: int
    :return: int, number of pairs of elements whose sum is divisible by K
    """
    n = len(a)
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % k == 0:
                cnt += 1
    return cnt


def sum_divisible_2(a, k) -> int:
    """ hash map

    :param a: List[int]
    :param k: int
    :return: int, number of pairs of elements whose sum is divisible by K
    """
    hash_cnt = defaultdict(int)
    for n in a:
        hash_cnt[n % k] += 1

    sum_cnt = hash_cnt[0] * (hash_cnt[0] - 1) // 2
    if k % 2 == 1:
        sum_cnt += hash_cnt[k // 2] * (hash_cnt[k // 2] - 1) // 2
    for n in range(1, (k - 1) // 2):
        sum_cnt += hash_cnt[n] * hash_cnt[k - n]

    return sum_cnt


a_test = [1, 4, 5, 3]
K_test = 3
assert sum_divisible_1(a_test, K_test) == 2
assert sum_divisible_2(a_test, K_test) == 2

a_test = [1, 4, 5, 3, 3]
K_test = 3
assert sum_divisible_1(a_test, K_test) == 3
assert sum_divisible_2(a_test, K_test) == 3
