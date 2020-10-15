"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

Power of Three
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
from numpy import base_repr
import re

def isPowerOfThree_recursive(n: int) -> bool:
    """
    Runtime: 56 ms, faster than 99.25% of Python3 online submissions for Power of Three.
    Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Power of Three.
    :param n:
    :return:
    """
    if n < 3:
        return n == 1
    if n % 3 != 0:
        return False
    return isPowerOfThree_recursive(int(n / 3))


assert isPowerOfThree_recursive(1)
assert isPowerOfThree_recursive(27)
assert not isPowerOfThree_recursive(8)


def isPowerOfThree_interactive(n: int) -> bool:
    """
    Runtime: 64 ms, faster than 94.89% of Python3 online submissions for Power of Three.
    Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Power of Three.
    :param n:
    :return:
    """
    while n >= 3:
        if n % 3 != 0:
            return False
        n /= 3
    return n == 1


assert isPowerOfThree_interactive(1)
assert isPowerOfThree_interactive(27)
assert not isPowerOfThree_interactive(8)


def isPowerOfThree(n: int) -> bool:
    """
    Base conversion

    Runtime: 208 ms, faster than 5.30% of Python3 online submissions for Power of Three.
    Memory Usage: 30.2 MB, less than 100.00% of Python3 online submissions for Power of Three.
    :param n:
    :return:
    """
    if n < 3:
        return n == 1
    nBase3 = base_repr(n, 3)
    return bool(re.match(r'^10*$', nBase3))


assert isPowerOfThree(1)
assert isPowerOfThree(27)
assert not isPowerOfThree(6)


def isPowerOfThree(n: int) -> bool:
    """
    Integer Limitations

    Runtime: 112 ms, faster than 22.58% of Python3 online submissions for Power of Three.
    Memory Usage: 30.3 MB, less than 100.00% of Python3 online submissions for Power of Three.
    :param n:
    :return:
    """
    return n > 0 and pow(3, 19) % n == 0


assert isPowerOfThree(1)
assert isPowerOfThree(27)
assert not isPowerOfThree(6)

