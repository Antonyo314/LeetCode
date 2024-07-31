class Solution:
    def longestPalindrome(self, s: str) -> int:

        d = dict()

        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1

        v = d.values()

        v1 = [i % 2 for i in v]
        v2 = [i - i % 2 for i in v]

        res = sum(v2)
        if 1 in v1:
            res += 1

        return res


Solution().longestPalindrome('a')
