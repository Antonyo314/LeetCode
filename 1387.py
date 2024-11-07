from functools import lru_cache


class Solution:
    @staticmethod
    @lru_cache(maxsize=None)
    def power(x):
        k = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            k += 1
        return k

    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}
        for i in range(lo, hi + 1):
            d[i] = self.power(i)
        sorted_keys = sorted(d, key=d.get)

        return sorted_keys[k - 1]
