class Solution:
    @staticmethod
    def mult(a, b):
        res = 1
        for i in range(a, b + 1):
            res *= i
        return res

    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        m, n = min(m, n), max(m, n)

        return int(self.mult(m + 1, m + n) / self.mult(1, n))
