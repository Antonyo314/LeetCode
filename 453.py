from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)


Solution().minMoves([1,10**10])
