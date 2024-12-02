from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        max_d = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > max_d:
                max_d = nums[i + 1] - nums[i]

        return max_d

Solution().maximumGap([3,6,9,1])