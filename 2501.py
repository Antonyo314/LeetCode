from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = -1
        nums_set = set(nums)
        for num in nums:
            t = 1
            temp_num = num
            while True:
                temp_num = temp_num ** 2
                if temp_num in nums_set:
                    t += 1
                else:
                    break
            if t >= 2:
                res = max(res, t)

        return res


Solution().longestSquareStreak(nums=[4, 3, 6, 16, 8, 2])
