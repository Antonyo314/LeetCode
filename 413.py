class Solution:
    def fact(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diffs = []
        for i in range(1, len(nums)):
            diffs.append(nums[i] - nums[i - 1])

        t = []

        k = 1
        if len(diffs) == 0:
            return 0
        prev = diffs[0]

        for i in range(1, len(diffs)):
            if diffs[i] != prev:
                t.append(k)
                k = 1
                prev = diffs[i]
            else:
                k += 1

        t.append(k)

        res = 0
        for i in t:
            if i >= 2:
                res += self.fact(i) / (self.fact(2) * self.fact(i - 2))

        return int(res)