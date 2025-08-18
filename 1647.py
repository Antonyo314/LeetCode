class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}

        for a in s:
            if a not in d:
                d[a] = 0
            d[a] += 1

        values = sorted(d.values(), reverse=True)
        res = 0
        for i in range(len(values) - 1):
            if values[i] <= values[i + 1] != 0:
                res += min(values[i + 1] - values[i] + 1, values[i + 1])

                values[i + 1] = max(values[i] - 1, 0)
        return res


Solution().minDeletions("bbcebab")
