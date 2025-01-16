from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ind2pair = {}
        ind2diff = {}
        ind = 0
        for a, b in costs:
            ind2pair[ind] = [a, b]
            ind2diff[ind] = b - a
            ind += 1

        ind2diff = dict(sorted(ind2diff.items(), key=lambda item: item[1]))

        n = 0
        N = len(ind2pair) // 2
        res = 0
        for k in ind2diff.keys():
            if n < N:
                res += ind2pair[k][1]
                n += 1
            else:
                res += ind2pair[k][0]

        return res
