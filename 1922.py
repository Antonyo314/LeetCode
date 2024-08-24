class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            n //= 2
            res = pow(20, n, 10 ** 9 + 7)
        else:
            n = (n - 1) // 2
            res = pow(20, n, 10 ** 9 + 7)

            res *= 5

        return res % (10 ** 9 + 7)

