from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = nums[0]
        min_ = nums[0]

        total_max = nums[0]

        for num in nums[1:]:
            min_t = min(min_ * num, max_ * num)
            max_t = max(min_ * num, max_ * num)
            max_ = max(num, max_t)
            min_ = min(num, min_t)

            total_max = max(total_max, max_)
        return total_max
