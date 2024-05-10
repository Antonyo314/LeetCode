from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        sum1 = nums[0]
        sum2 = sum(nums[1:])
        if sum1 >= sum2:
            res += 1
        for i in range(1, len(nums) - 1):
            sum1 += nums[i]
            sum2 -= nums[i]
            if sum1 >= sum2:
                res += 1
        return res

Solution().waysToSplitArray([2,3,1,0])
