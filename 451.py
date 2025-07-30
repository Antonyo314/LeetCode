class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

        res = ''

        for k in d.keys():
            res += k * d[k]
        return res


Solution().frequencySort("eerrrt")