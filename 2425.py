from typing import List
from functools import reduce


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        b = 0 if len(nums1) % 2 == 0 else reduce(lambda x, y: x ^ y, nums2)
        a = 0 if len(nums2) % 2 == 0 else reduce(lambda x, y: x ^ y, nums1)
        return a ^ b


Solution().xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0])
