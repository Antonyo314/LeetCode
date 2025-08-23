class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        l = []
        t = 0
        for i in s:
            l.append(t)
            if i == '1':
                t += 1
        r = []
        t = 0
        for i in s[::-1]:
            r.append(t)
            if i == '0':
                t += 1
        r = r[::-1]
        res = len(s)
        for i in range(len(s)):
            res = min(res, l[i] + r[i])

        return res


Solution().minFlipsMonoIncr(s="00110")
