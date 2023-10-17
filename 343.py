class Solution(object):
    def integerBreak(self, n):
        """
        intuition
        """

        b = n % 3
        a = n - b
        a //= 3

        if n == 3:
            return 2
        if n == 2:
            return 1
        if b == 1:
            return 3 ** (a - 1) * (b + 3)
        if b == 0:
            return 3 ** a
        return 3 ** a * b