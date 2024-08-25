class Solution:
    @staticmethod
    def lin_combination(satisfaction):
        res = 0
        for i in range(len(satisfaction)):
            res += (i + 1) * satisfaction[i]
        return res

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        max_ = -1_000_000

        while len(satisfaction) > 0:
            t = self.lin_combination(satisfaction)
            if t > max_:
                max_ = t
            satisfaction = satisfaction[1:]

        return max(max_, 0)