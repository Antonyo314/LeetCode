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
        sign_ = self.sign(dividend * divisor)
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

        return max(min(res * sign_, 2 ** 31 - 1), -2 ** 31)

