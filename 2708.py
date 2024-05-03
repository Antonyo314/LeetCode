from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        positives = [n for n in nums if n > 0]
        negatives = [n for n in nums if n < 0]

        if len(positives) + len(negatives) == 0:
            return 0
        elif len(positives) + len(negatives) == 1:
            if len(positives) == 1:
                return positives[0]
            else:
                return 0
        res = 1
        for i in positives:
            res *= i

        for i in negatives:
            res *= i

        if len(negatives) % 2 != 0:
            res /= max(negatives)

        return int(res)
