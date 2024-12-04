from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for num in nums.copy():
            nums.append(int(str(num)[::-1]))

        return len(set(nums))


Solution().countDistinctIntegers(nums=[1, 13, 10, 12, 31])
