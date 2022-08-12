class Solution:
    @staticmethod
    def sign(a):
        if a > 0:
            return 1
        elif a < 0:
            return -1
        else:
            return 0

    def divide(self, dividend: int, divisor: int) -> int:
        s1 = self.sign(dividend)
        s2 = self.sign(divisor)
        if s1 == s2:
            sign_ = 1
        else:
            sign_ = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while divisor <= dividend:
            i = 1
            d = divisor

            while d + d <= dividend:
                i += i
                d += d
            res += i
            dividend -= d

        if sign_ == -1:
            t = res
            res -= t
            res -= t

        return max(min(res, 2 ** 31 - 1), -2 ** 31)