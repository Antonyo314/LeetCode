class Solution:
    def combination_sum(self, d, result, solution, candidates, candidates_full, target):
        if target == 0:
            result.append(tuple(solution))
        else:
            for candidate in candidates:
                if candidate <= target:
                    self.combination_sum(d, result, solution + [candidate], candidates[1:], candidates_full,
                                         target - candidate)
                    self.combination_sum(d, result, solution, candidates_full[d[candidates[0]] + 1:], candidates_full,
                                         target)
                    break

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = list()
        d = dict()
        for ind, i in enumerate(candidates):
            d[i] = ind
        self.combination_sum(d, result, list(), candidates, candidates, target)
        return result