class Solution:

    def f_2(self, n):
        res = 0
        k = 1
        while 2 ** k <= n:
            i = 1
            while i * 2 ** k <= n:
                res += k
                i += 2
            k += 1
        return res

    def f_5(self, n):
        res = 0
        k = 1
        while 5 ** k <= n:
            i = 1
            while i * 5 ** k <= n:
                res += k
                i += 1
                if i % 5 == 0:
                    i += 1
            k += 1
        return res

    def trailingZeroes(self, n: int) -> int:

        return min(self.f_2(n), self.f_5(n))


print(Solution().trailingZeroes(5))
