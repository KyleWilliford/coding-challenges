class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Runtime: 44 ms
        Memory Usage: 14.9 MB
        :param n:
        :return:
        """
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result