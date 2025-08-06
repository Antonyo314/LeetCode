from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {nums[i]:i for i in range(len(nums))}

        for operation in operations:
            d[operation[1]] = d[operation[0]]
            del d[operation[0]]

        d = {v: k for k, v in d.items()}

        return [d[i] for i in range(len(nums))]


Solution().arrayChange([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]])
