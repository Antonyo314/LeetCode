class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        t = nums[0]
        i = 1
        res_len = 1
        while i < len(nums) and nums[i] != '_':
            if nums[i] == t:
                del nums[i]
                nums.append('_')
            else:
                t = nums[i]
                i += 1
                res_len += 1

        return i
