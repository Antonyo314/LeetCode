from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        max_r_d = {}
        max_r = height[-1]
        for i in range(len(height) - 1, 0, -1):
            max_r = max(max_r, height[i])
            max_r_d[i] = max_r

        new_height = height.copy()
        max_ = 0

        for i in range(1, len(new_height) - 1):
            max_ = max(max_, new_height[i - 1])
            new_height[i] = max(min(max_, max_r_d[i]), new_height[i])

        return sum([new_height[i] - height[i] for i in range(len(height))])
