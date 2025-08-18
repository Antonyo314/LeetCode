from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [num for num in nums if num > 0]
        b = [num for num in nums if num < 0]

        res = []

        for i in range(len(a)):
            res.append(a[i])
            res.append(b[i])
        return res


Solution().rearrangeArray(nums=[3, 1, -2, -5, 2, -4])
