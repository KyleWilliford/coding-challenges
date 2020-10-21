"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/

Count Primes
Count the number of prime numbers less than a non-negative number, n.
"""
from math import sqrt


def countPrimes_bruteForce(n: int) -> int:
    """
    Brute Force solution

    Runtime: 7144 ms
    Memory Usage: 18.2 MB
    :param n:
    :return:
    """
    # def isPrime(k: int) -> bool:
    #     for i in range()
    if n <= 2:
        return 0
    cnt = 1
    prime = [2]
    i = 2
    while i < n:
        iPrimeFlag = True
        for p in prime:
            if i % p == 0:
                iPrimeFlag = False
                break
            if p > int(sqrt(i)):
                break
        if iPrimeFlag:
            prime.append(i)
            cnt += 1
        i += 1
    # print(prime)
    return cnt


def countPrimes_math(n: int) -> int:
    """
    Runtime: 1140 ms
    Memory Usage: 183.3 MB
    :param n:
    :return:
    """
    def isPrime(i: int) -> bool:
        for k in range(2, int(sqrt(i)) + 1):
            if i % k == 0:
                return False
        return True

    if n <= 2:
        return 0
    nums = set(range(2, n))
    for i in range(2, int(sqrt(n)) + 1):
        if isPrime(i):
            j = pow(i, 2)
            while j < n:
                nums.discard(j)
                j += i
        i += 1
    # print(nums)
    return len(nums)


def countPrimes_math2(n: int) -> int:
    p = [1] * n
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            p[i * i: n * i] = [0] * ((n - 1 - i * i) // i + 1)
    return max(0, sum(p) - 2)


assert countPrimes_bruteForce(10) == 4
assert countPrimes_math(10) == 4
assert countPrimes_math2(10) == 4
