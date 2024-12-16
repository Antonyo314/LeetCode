class Solution:
    def minSteps(self, s: str, t: str) -> int:

        chars = list(set(s).union(set(t)))

        d_s = {}
        d_t = {}

        for i in chars:
            d_s[i] = 0
            d_t[i] = 0

        for i in s:
            d_s[i] += 1

        for i in t:
            d_t[i] += 1

        res = 0

        for i in chars:
            res += abs(d_t[i] - d_s[i])

        return res


Solution().minSteps(s = "night", t = "thing")
