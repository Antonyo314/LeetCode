from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if i == 0 else 1 for i in nums]
        sum_ = 0

        ind2sum = {}
        ind2sum[0] = 0
        max_l = 0
        for i, n in enumerate(nums):
            sum_ += n
            if sum_ not in ind2sum:
                ind2sum[sum_] = i + 1
            else:
                max_l = max(max_l, i - ind2sum[sum_] + 1)

        return max_l
