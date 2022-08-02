
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        i = 0
        j = len(nums) - 1
        while j - i > 1:
            t = i + (j - i) // 2
            if nums[t] >= target:
                j = t
            elif nums[t] <= target:
                i = t
        print(i, j)
        if nums[i] == target:
            return i
        else:
            return j

