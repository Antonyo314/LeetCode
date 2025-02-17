from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        arr = sorted(list(set(nums)))
        arr = arr[1:]

        res = 0
        t = len(arr)
        for a in arr[::-1]:
            res += d[a] * t
            t -= 1

        return res


Solution().reductionOperations([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
