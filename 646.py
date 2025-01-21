from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[0])

        res = 0
        while len(pairs) > 0:
            a = min([pair[1] for pair in pairs])
            res += 1
            pairs = [pair for pair in pairs if pair[0] > a]

        return res


Solution().findLongestChain(pairs = [[1,2],[7,8],[4,5]])