class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        min_ = 10 ** 10
        res = 0
        for i in range(len(nums) - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1

            while j < k:
                diff = target - (nums[i] + nums[j] + nums[k])
                if abs(diff) < min_:
                    min_ = abs(diff)
                    res = nums[i] + nums[j] + nums[k]
                if diff < 0:
                    k -= 1
                elif diff > 0:
                    j += 1

                else:
                    return target
        return res
