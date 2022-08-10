class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        if len(nums) == 1:
            return True

        while i + nums[i] < len(nums) - 1:
            if nums[i] == 0:
                return False

            max_ = 0
            best_i = 0
            for j in range(1, nums[i] + 1):
                if i + j + nums[i + j] > max_:
                    max_ = i + j + nums[i + j]
                    best_i = i + j

            i = best_i

        return True

