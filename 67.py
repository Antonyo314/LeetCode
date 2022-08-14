class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_ = max(len(a), len(b))

        a = '0' * (max_ - len(a)) + a
        b = '0' * (max_ - len(b)) + b
        a = a[::-1]
        b = b[::-1]
        remainder = 0

        res = []
        for i in range(len(a)):
            x = int(a[i])
            y = int(b[i])

            t = x + y + remainder
            if t <= 1:
                res.append(t)
                remainder = 0

            elif t == 2:
                res.append(0)
                remainder = 1
            else:
                res.append(1)
                remainder = 1

        if remainder == 1:
            res.append(1)
        res = res[::-1]
        res = [str(i) for i in res]
        res = ''.join(res)
        return res