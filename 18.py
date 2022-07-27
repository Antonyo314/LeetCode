class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        d = dict()

        for i in range(len(nums)):
            d[nums[i]] = i

        res = set()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    temp_target = target - (nums[i] + nums[j] + nums[k])
                    if temp_target in d and d[temp_target] > k:
                        res.add((nums[i], nums[j], nums[k], temp_target))
        res = [list(i) for i in res]
        return res