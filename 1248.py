class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num % 2 for num in nums]

        sum_ = sum(nums)
        b = sum_
        d = {}

        for i in range(0, sum_ + 1):
            d[i] = 0
        d[sum_] = 1
        for num in nums:
            b -= num
            d[b] += 1

        res = 0
        for r_value in d.keys():
            if r_value >= k:
                res += d[r_value] * d[r_value - k]
        return res
