class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        res = 0

        while i + nums[i] < len(nums) - 1:
            max_ = 0
            best_i = 0
            for j in range(1, nums[i] + 1):
                if i + j + nums[i + j] > max_:
                    max_ = i + j + nums[i + j]
                    best_i = i + j
            i = best_i
            res += 1
        return res + 1