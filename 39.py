class Solution:
    def combination_sum(self, result, solution, candidates, target):
        if target == 0:
            result.append(solution)
        else:
            for candidate in candidates:
                if candidate <= target:
                    self.combination_sum(result, solution + [candidate], candidates, target - candidate)
                    self.combination_sum(result, solution, candidates[1:], target)
                    break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = list()
        self.combination_sum(result, list(), candidates, target)
        return result