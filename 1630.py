from typing import List


class Solution:
    @staticmethod
    def is_arithmetic_sequence(arr):
        arr.sort()

        t = arr[1] - arr[0]
        for i, j in zip(range(1, len(arr)), range(2, len(arr))):
            if arr[j] - arr[i] != t:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            res.append(self.is_arithmetic_sequence(nums[l[i]:r[i] + 1]))
        return res


Solution().checkArithmeticSubarrays(nums=[-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0], l=[5, 4, 3, 2, 4, 7, 6, 1, 7],
                                    r=[6, 5, 6, 3, 7, 10, 7, 4, 10]
                                    )
