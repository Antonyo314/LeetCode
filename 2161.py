from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        print(nums)
        a, b, c = [], [], []

        for num in nums:
            if num < pivot:
                a.append(num)
        for num in nums:
            if num == pivot:
                b.append(num)
        for num in nums:
            if num > pivot:
                c.append(num)

        return a + b + c


Solution().pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10)
