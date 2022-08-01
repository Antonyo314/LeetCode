class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        i = 0
        j = len(nums) - 1

        while j - i > 1:
            t = i + (j - i) // 2
            if nums[t] > target:
                j = t
            else:
                i = t
        if nums[i] == target:
            k = i
        elif nums[j] == target:
            k = j
        else:
            return [-1, -1]
        i = k
        j = k

        while nums[max(i - 1, 0)] == target or nums[min(j + 1, len(nums) - 1)] == target:
            if i > 0 and nums[i - 1] == target:
                i -= 1
            elif j < len(nums) - 1 and nums[j + 1] == target:
                j += 1
            else:
                return [i, j]
        return [i, j]

