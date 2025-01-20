class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])

        res = a
        d = c - b

        if d > a:
            res += b
            return res
        else:
            c -= d
            t = a - d

            if t == 0:
                return res + min(b, c)
            while True:
                b -= 1
                t -= 1
                if t == 0:
                    return res + min(b, c)
                c -= 1
                t -= 1
                if t == 0:
                    return res + min(b, c)


Solution().maximumScore(a=4, b=4, c=6)
