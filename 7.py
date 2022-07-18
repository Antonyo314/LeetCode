class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1

        if sign == -1:
            x = str(x)[1:]
        else:
            x = str(x)

        x = int(x[::-1])

        x *= sign

        if not -2 ** 31 <= x < 2 ** 31:
            return 0
        else:
            return x