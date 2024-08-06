class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if k == 0:

            d_ = {}

            for n in nums:
                if n not in d_:
                    d_[n] = 0
                d_[n] += 1

            return len([k for k in d_ if d_[k] >= 2])

        nums = set(nums)
        res = 0
        for n in nums:
            if n + k in nums:
                res += 1
