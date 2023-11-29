class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') % 2 != 0 or corridor.count('S') == 0:
            return 0

        res = []

        s = 0
        p = 0
        left_seats = False
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                if p != 0:
                    res.append(p)
                p = 0
                s += 1
            if s == 2:
                s = 0
                left_seats = True
            if s == 0 and corridor[i] == 'P' and left_seats:
                p += 1
        result = 1
        for i in res:
            result *= i + 1
            result %= 10 ** 9 + 7

        return result
