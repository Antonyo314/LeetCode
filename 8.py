class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0

        sign = 1

        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]

        res = ''

        for i in s:
            try:
                _ = int(i)
                res += i
            except:
                break

        if res == '':
            return 0

        res = int(res)
        res *= sign

        res = max(res, -2 ** 31)
        res = min(res, 2 ** 31 - 1)

        return res