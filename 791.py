class Solution:
    def customSortString(self, order: str, str_: str) -> str:
        d = {}

        for s in str_:
            if s not in d:
                d[s] = 0
            d[s] += 1

        res = ''
        for s in order:
            if s in d:
                res += s * d[s]

        for s in set(d.keys()).difference(set(order)):
            res += s * d[s]
        return res

Solution().customSortString('bcafg', 'abcd')