class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        temp_d = dict()

        for i in range(len(nums)):
            temp_d[nums[i]] = i

        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in temp_d and temp_d[target] > j:
                    res.add((nums[i], nums[j], -(nums[i] + nums[j])))
        res = [list(i) for i in res]
        return res