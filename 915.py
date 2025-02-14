from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l_max = {}

        max_ = -1
        for ind, num in enumerate(nums):
            max_ = max(max_, num)

            l_max[ind] = max_

        r_min = {}

        min_ = 10 ** 100

        for ind, num in enumerate(nums[::-1]):
            min_ = min(min_, num)
            r_min[ind] = min_

        # print(l_max)
        # print(r_min)

        for i in range(len(nums)):
            # print(i, len(nums) - i - 1)
            if l_max[i] <= r_min[len(nums) - i - 2]:
                return i + 1
        # return 100