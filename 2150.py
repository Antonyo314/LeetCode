from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        return [num for num in nums if d[num] == 1 and num - 1 not in d and num + 1 not in d]


Solution().findLonely(nums=[1, 3, 5, 3])
